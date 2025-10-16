from __future__ import annotations

from pathlib import Path

from scripts.download_file import compute_sha256, main as download_main


def test_download_file_from_local_uri(tmp_path: Path) -> None:
    source = tmp_path / "source.bin"
    source.write_bytes(b"hello world")
    dest = tmp_path / "dest.bin"

    url = source.resolve().as_uri()
    expected = compute_sha256(b"hello world")

    download_main(url, dest, expected_sha256=expected)

    assert dest.read_bytes() == b"hello world"
