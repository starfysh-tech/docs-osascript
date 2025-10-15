#!/usr/bin/env python3
from __future__ import annotations

import argparse
import posixpath
from pathlib import Path
from typing import Dict, Set
from urllib.parse import urljoin
from urllib.request import urlopen

from urllib.parse import urljoin, urlparse
from urllib.request import urlopen

from bs4 import BeautifulSoup


def collect_assets(html_dir: Path) -> Dict[Path, Set[str]]:
    mapping: Dict[Path, Set[str]] = {}
    for html_path in sorted(html_dir.rglob("*.html")):
        soup = BeautifulSoup(html_path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
        sources = {img.get("src") for img in soup.find_all("img") if img.get("src")}
        if sources:
            mapping[html_path] = sources
    return mapping


def resolve_asset_path(page_rel: str, src: str) -> str:
    page_dir = posixpath.dirname(page_rel)
    joined = posixpath.join(page_dir, src)
    normalized = posixpath.normpath(joined)
    while normalized.startswith("../"):
        normalized = normalized[3:]
    return normalized.lstrip("./")


def fetch(url: str) -> bytes:
    with urlopen(url) as response:
        return response.read()


def main(html_dir: Path, base_url: str, asset_dir: Path) -> None:
    asset_dir.mkdir(parents=True, exist_ok=True)
    collected = collect_assets(html_dir)
    downloaded = 0
    skipped = 0
    for html_path, sources in collected.items():
        page_rel = html_path.relative_to(html_dir).as_posix()
        page_url = urljoin(base_url, page_rel)
        for src in sources:
            if src.startswith(("http://", "https://")):
                parsed = urlparse(src)
                asset_rel = posixpath.join("external", parsed.netloc, parsed.path.lstrip("/"))
                asset_url = src
            else:
                asset_rel = resolve_asset_path(page_rel, src)
                if not asset_rel:
                    continue
                asset_url = urljoin(page_url, src)
            dest = asset_dir / asset_rel
            if dest.exists():
                skipped += 1
                continue
            dest.parent.mkdir(parents=True, exist_ok=True)
            data = fetch(asset_url)
            dest.write_bytes(data)
            downloaded += 1
            print(f"Fetched {asset_rel} ({len(data)} bytes)")
    print(f"Downloaded {downloaded} new asset(s); skipped {skipped} existing.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download assets referenced by HTML files.")
    parser.add_argument("--html-dir", required=True, type=Path)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--asset-dir", required=True, type=Path)
    args = parser.parse_args()
    main(args.html_dir, args.base_url, args.asset_dir)
