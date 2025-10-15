#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlopen


def fetch(url: str) -> bytes:
    with urlopen(url) as response:
        return response.read()


def main(pages_file: Path, base_url: str, output_dir: Path) -> None:
    pages = [line.strip() for line in pages_file.read_text().splitlines() if line.strip()]

    output_dir.mkdir(parents=True, exist_ok=True)

    for rel_path in pages:
        url = urljoin(base_url, rel_path)
        dest = output_dir / rel_path
        dest.parent.mkdir(parents=True, exist_ok=True)

        data = fetch(url)
        dest.write_bytes(data)
        print(f"Fetched {rel_path} ({len(data)} bytes)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download HTML files listed in a TOC")
    parser.add_argument("--pages-file", required=True, type=Path)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    main(args.pages_file, args.base_url, args.output_dir)
