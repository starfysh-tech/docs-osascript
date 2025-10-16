from __future__ import annotations

import json
from pathlib import Path

from scripts.export_dataset import main as export_main


def test_export_dataset_creates_plain_text_and_jsonl(tmp_path: Path, monkeypatch) -> None:
    build_dir = tmp_path / "build"
    collection_dir = build_dir / "sample"
    markdown_dir = collection_dir / "docs"
    markdown_dir.mkdir(parents=True)

    md_path = markdown_dir / "Example.md"
    md_path.write_text("# Example\n\nBody text.\n\n```\ncode\n```", encoding="utf-8")

    manifest = {
        "version": 1,
        "collections": [
            {
                "id": "sample",
                "sources": [
                    {
                        "id": "Example",
                        "path": "Example.md",
                        "url": "https://example.test/Example",
                        "type": "html",
                        "output": "build/sample/docs/Example.md",
                        "sha256": "abc123",
                        "etag": "etag",
                        "last_modified": "Wed, 01 Jan 2025 00:00:00 GMT",
                    },
                    {
                        "id": "ExamplePDF",
                        "path": "Example.pdf",
                        "url": "https://example.test/Example.pdf",
                        "type": "pdf",
                        "output": "build/sample/docs/Example.pdf",
                        "sha256": "deadbeef",
                        "etag": None,
                        "last_modified": None,
                    },
                ],
            }
        ],
    }
    manifest_path = tmp_path / "monitor" / "manifest.json"
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    plain_dir = tmp_path / "dataset" / "plain"
    jsonl_dir = tmp_path / "dataset" / "jsonl"
    dataset_manifest = tmp_path / "dataset" / "manifest.json"

    args = [
        "--collections",
        "sample",
        "--build-dir",
        str(build_dir),
        "--plain-dir",
        str(plain_dir),
        "--jsonl-dir",
        str(jsonl_dir),
        "--manifest",
        str(manifest_path),
        "--dataset-manifest",
        str(dataset_manifest),
    ]

    export_main(args)

    plain_text = (plain_dir / "sample" / "docs" / "Example.txt").read_text(encoding="utf-8")
    assert "Example" in plain_text
    assert "code" in plain_text

    sidecar = (plain_dir / "sample" / "docs" / "Example.meta.json").read_text(encoding="utf-8")
    metadata = json.loads(sidecar)
    assert metadata["collection"] == "sample"
    assert metadata["source_url"] == "https://example.test/Example"

    jsonl_file = jsonl_dir / "sample.jsonl"
    records = [json.loads(line) for line in jsonl_file.read_text(encoding="utf-8").splitlines()]
    assert any(r["path"] == "docs/Example.md" and r["binary"] is False for r in records)
    assert any(r["path"] == "docs/Example.pdf" and r["binary"] is True for r in records)

    dataset_meta = json.loads(dataset_manifest.read_text(encoding="utf-8"))
    assert dataset_meta["collections"]["sample"]["documents"] == 2
