#!/usr/bin/env python3
"""Check remote documentation sources for changes.

This script reads `monitor/manifest.json`, performs conditional HTTP
requests against each listed source, and reports whether the upstream
content changed. Optionally, it can persist updated metadata (etag,
last-modified, sha256) back into the manifest and emit a Markdown report.

Usage examples:

    python3 scripts/check_updates.py --manifest monitor/manifest.json \
        --report reports/update-status-$(date +%Y%m%d).md --save

The default mode is read-only/dry-run, which simply prints a summary to
stdout without touching the manifest.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, List
from urllib import error, request


UTC = dt.timezone.utc


def load_manifest(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_manifest(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def iso_now() -> str:
    return dt.datetime.now(tz=UTC).isoformat(timespec="seconds")


def build_request(src: Dict[str, Any]) -> request.Request:
    headers = {
        "User-Agent": "docs-osascript-monitor/1.0"
    }
    if src.get("etag"):
        headers["If-None-Match"] = src["etag"]
    if src.get("last_modified"):
        headers["If-Modified-Since"] = src["last_modified"]
    return request.Request(src["url"], headers=headers, method="GET")


def sha256_digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def check_source(src: Dict[str, Any], timeout: float) -> Dict[str, Any]:
    """Return a result dict describing the outcome for the source."""

    req = build_request(src)
    now = iso_now()

    try:
        with request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            digest = sha256_digest(body)
            etag = resp.headers.get("ETag")
            last_mod = resp.headers.get("Last-Modified")

            previous_digest = src.get("sha256")
            changed = previous_digest is None or digest != previous_digest

            src.update(
                {
                    "sha256": digest,
                    "etag": etag or src.get("etag"),
                    "last_modified": last_mod or src.get("last_modified"),
                    "last_checked": now,
                }
            )

            return {
                "id": src.get("id"),
                "url": src["url"],
                "status": "changed" if changed else "unchanged",
                "http_status": resp.status,
                "message": "content updated" if changed else "no change",
            }

    except error.HTTPError as exc:
        if exc.code == 304:  # Not Modified
            src["last_checked"] = now
            return {
                "id": src.get("id"),
                "url": src["url"],
                "status": "unchanged",
                "http_status": 304,
                "message": "not modified",
            }
        return {
            "id": src.get("id"),
            "url": src["url"],
            "status": "error",
            "http_status": exc.code,
            "message": str(exc),
        }
    except Exception as exc:  # pylint: disable=broad-except
        return {
            "id": src.get("id"),
            "url": src["url"],
            "status": "error",
            "http_status": None,
            "message": repr(exc),
        }


def collect_sources(manifest: Dict[str, Any]) -> List[Dict[str, Any]]:
    sources: List[Dict[str, Any]] = []
    for collection in manifest.get("collections", []):
        for src in collection.get("sources", []):
            # annotate back reference so reports can group by collection
            src.setdefault("collection_id", collection.get("id"))
            sources.append(src)
    return sources


def render_report(results: List[Dict[str, Any]], manifest_path: Path) -> str:
    lines = [
        f"# Update Report — {iso_now()}",
        "",
        f"Manifest: `{manifest_path}`",
        "",
    ]
    summary = {
        "changed": 0,
        "unchanged": 0,
        "error": 0,
    }
    for res in results:
        summary[res["status"]] = summary.get(res["status"], 0) + 1
    lines.append(
        "Summary: "
        + ", ".join(
            f"{key}={value}" for key, value in summary.items() if value
        )
    )
    lines.append("")
    for res in results:
        lines.append(
            f"- **{res['status']}** — {res['url']}"
            f" (status={res['http_status']}, message={res['message']})"
        )
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest",
        default="monitor/manifest.json",
        type=Path,
        help="Path to manifest JSON file",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=10.0,
        help="HTTP request timeout in seconds",
    )
    parser.add_argument(
        "--report",
        type=Path,
        help="Optional path to write a Markdown-formatted report",
    )
    parser.add_argument(
        "--save",
        action="store_true",
        help="Persist updated metadata back to the manifest",
    )
    return parser.parse_args(argv)


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    manifest = load_manifest(args.manifest)
    manifest["generated"] = iso_now()

    sources = collect_sources(manifest)
    if not sources:
        print("No sources found in manifest", file=sys.stderr)
        return 1

    results = [
        check_source(src, timeout=args.timeout)
        for src in sources
    ]

    changed = [r for r in results if r["status"] == "changed"]
    errors = [r for r in results if r["status"] == "error"]

    for res in results:
        print(
            f"[{res['status']}] {res['url']}"
            f" (status={res['http_status']}, message={res['message']})"
        )

    if args.save:
        save_manifest(args.manifest, manifest)

    if args.report:
        report_text = render_report(results, args.manifest)
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report_text, encoding="utf-8")

    if errors:
        return 2
    if changed:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
