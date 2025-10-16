#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as dt
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Optional

import markdown
from bs4 import BeautifulSoup


DATASET_TIMESTAMP_FMT = "%Y-%m-%dT%H:%M:%SZ"


@dataclass(frozen=True)
class ManifestEntry:
    url: str
    sha256: Optional[str]
    etag: Optional[str]
    last_modified: Optional[str]


def load_manifest(manifest_path: Path) -> Dict[str, ManifestEntry]:
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    mapping: Dict[str, ManifestEntry] = {}
    for collection in data.get("collections", []):
        for source in collection.get("sources", []):
            path = source.get("output")
            if not path:
                continue
            mapping[path] = ManifestEntry(
                url=source.get("url", ""),
                sha256=source.get("sha256"),
                etag=source.get("etag"),
                last_modified=source.get("last_modified"),
            )
    return mapping


def iter_markdown_files(build_dir: Path, collection: str) -> Iterator[Path]:
    root = build_dir / collection
    if not root.exists():
        raise FileNotFoundError(f"Collection '{collection}' not found in {build_dir}")
    yield from sorted(root.rglob("*.md"))


def markdown_to_plain_text(markdown_source: str) -> str:
    html = markdown.markdown(
        markdown_source,
        extensions=["tables", "fenced_code"],
    )
    soup = BeautifulSoup(html, "html.parser")

    # Preserve code fences with indentation.
    for pre in soup.find_all("pre"):
        code = pre.find("code")
        if code:
            code.replace_with(code.get_text())

    lines: List[str] = []
    for raw_line in soup.get_text("\n").splitlines():
        line = raw_line.rstrip()
        if not line:
            if lines and lines[-1] == "":
                continue
            lines.append("")
            continue
        lines.append(line)
    return "\n".join(lines).strip() + "\n"


def extract_title(markdown_source: str) -> Optional[str]:
    for raw_line in markdown_source.splitlines():
        line = raw_line.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    return None


def build_record(
    collection: str,
    rel_path: Path,
    body: Optional[str],
    manifest_entry: Optional[ManifestEntry],
    *,
    binary: bool = False,
) -> Dict[str, Optional[str]]:
    record: Dict[str, Optional[str]] = {
        "collection": collection,
        "path": rel_path.as_posix(),
        "title": extract_title(body) if body else None,
        "body": body,
        "binary": binary,
    }
    if manifest_entry:
        record.update(
            {
                "source_url": manifest_entry.url,
                "sha256": manifest_entry.sha256,
                "etag": manifest_entry.etag,
                "last_modified": manifest_entry.last_modified,
            }
        )
    else:
        record.update(
            {
                "source_url": None,
                "sha256": None,
                "etag": None,
                "last_modified": None,
            }
        )
    return record


def write_plain_text(
    plain_dir: Path,
    collection: str,
    rel_path: Path,
    content: str,
    metadata: Dict[str, Optional[str]],
) -> None:
    dest = plain_dir / collection / rel_path.with_suffix(".txt")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content, encoding="utf-8")

    sidecar = dest.with_suffix(".meta.json")
    sidecar.write_text(json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def export_collection(
    collection: str,
    build_dir: Path,
    plain_dir: Path,
    jsonl_dir: Path,
    manifest_map: Dict[str, ManifestEntry],
) -> Dict[str, int]:
    jsonl_path = jsonl_dir / f"{collection}.jsonl"
    jsonl_path.parent.mkdir(parents=True, exist_ok=True)
    exported = 0

    with jsonl_path.open("w", encoding="utf-8") as jsonl_file:
        for md_path in iter_markdown_files(build_dir, collection):
            markdown_source = md_path.read_text(encoding="utf-8")
            rel_path = md_path.relative_to(build_dir / collection)
            manifest_key = f"{build_dir.name}/{collection}/{rel_path.as_posix()}"
            manifest_entry = manifest_map.get(manifest_key)

            record = build_record(collection, rel_path, markdown_source, manifest_entry)
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")

            plain_text = markdown_to_plain_text(markdown_source)
            write_plain_text(plain_dir, collection, rel_path, plain_text, record)

            exported += 1

        # add binary artifacts tracked in manifest (e.g., PDFs)
        for output_path, entry in manifest_map.items():
            if not output_path.endswith(('.pdf', '.zip')):
                continue
            parts = Path(output_path)
            if parts.parts[1] != collection:
                continue
            rel = Path(*parts.parts[2:])
            record = build_record(collection, rel, None, entry, binary=True)
            jsonl_file.write(json.dumps(record, ensure_ascii=False) + "\n")
            exported += 1

    return {"documents": exported}


def generate_dataset_manifest(
    manifest_path: Path,
    summary: Dict[str, Dict[str, int]],
    command: str,
) -> None:
    dataset_manifest = {
        "generated": dt.datetime.utcnow().strftime(DATASET_TIMESTAMP_FMT),
        "command": command,
        "collections": summary,
    }
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(dataset_manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export mirrored Markdown to plain text and JSONL datasets.")
    parser.add_argument(
        "--collections",
        nargs="+",
        help="Specific collections to export (defaults to all directories under build/).",
    )
    parser.add_argument("--build-dir", type=Path, default=Path("build"), help="Directory containing Markdown collections.")
    parser.add_argument("--plain-dir", type=Path, default=Path("dataset/plain"), help="Destination for plain text exports.")
    parser.add_argument("--jsonl-dir", type=Path, default=Path("dataset/jsonl"), help="Destination directory for JSONL files.")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("monitor/manifest.json"),
        help="Path to monitoring manifest for URL/hash metadata.",
    )
    parser.add_argument(
        "--dataset-manifest",
        type=Path,
        default=Path("dataset/manifest.json"),
        help="Path to write dataset manifest summary.",
    )
    return parser.parse_args(argv)


def auto_discover_collections(build_dir: Path) -> List[str]:
    return sorted(
        entry.name
        for entry in build_dir.iterdir()
        if entry.is_dir()
    )


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = parse_args(argv)
    collections = args.collections or auto_discover_collections(args.build_dir)
    if not collections:
        raise SystemExit("No collections found to export.")

    manifest_map = load_manifest(args.manifest) if args.manifest.exists() else {}
    summary: Dict[str, Dict[str, int]] = {}
    for collection in collections:
        stats = export_collection(
            collection,
            args.build_dir,
            args.plain_dir,
            args.jsonl_dir,
            manifest_map,
        )
        summary[collection] = stats
        print(f"Exported {stats['documents']} document(s) from {collection}")

    command = " ".join(["python3", "scripts/export_dataset.py"] + (collections or []))
    generate_dataset_manifest(args.dataset_manifest, summary, command)
    print(f"Dataset manifest written to {args.dataset_manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
