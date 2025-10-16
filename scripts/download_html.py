#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import urljoin
from urllib.request import urlopen


def fetch(url: str) -> bytes:
    with urlopen(url) as response:
        return response.read()


def main(pages_file: Path, base_url: str, output_dir: Path) -> None:
    pages = [line.strip() for line in pages_file.read_text().splitlines() if line.strip()]

    output_dir.mkdir(parents=True, exist_ok=True)

    for rel_path in pages:
        url_path = rel_path
        url = urljoin(base_url, url_path)
        try:
            data = fetch(url)
        except HTTPError as exc:
            if exc.code == 404 and rel_path.endswith(".html"):
                alt_path = rel_path[:-5]
                url = urljoin(base_url, alt_path)
                data = fetch(url)
                url_path = alt_path
            else:
                raise
        storage_rel = rel_path if rel_path.endswith(".html") else f"{rel_path}.html"
        dest = output_dir / storage_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        print(f"Fetched {url_path} -> {storage_rel} ({len(data)} bytes)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download HTML files listed in a TOC")
    parser.add_argument("--pages-file", required=True, type=Path)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    main(args.pages_file, args.base_url, args.output_dir)
