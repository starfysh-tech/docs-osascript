#!/usr/bin/env python3
"""Validate key links in the generated MkDocs site."""
from __future__ import annotations

import argparse
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup


def collect_local_links(index_html: Path) -> list[str]:
    soup = BeautifulSoup(index_html.read_text(encoding="utf-8"), "html.parser")
    links: list[str] = []
    for link in soup.find_all("a", href=True):
        href = link["href"].strip()
        if not href:
            continue
        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc:
            # external link
            continue
        if href.startswith("#"):
            continue
        links.append(href)
    return links


def resolve_path(site_dir: Path, href: str) -> Path:
    candidate = site_dir / href
    if candidate.exists():
        return candidate
    # MkDocs outputs .html; if href points to .md, convert
    if href.endswith(".md"):
        html_candidate = site_dir / href.replace(".md", ".html")
        if html_candidate.exists():
            return html_candidate
    # handle directory-style links from MkDocs nav (foo/ -> foo/index.html)
    if href.endswith("/"):
        html_candidate = site_dir / href / "index.html"
        if html_candidate.exists():
            return html_candidate
    # for PDF metadata-only links ensure file exists
    if href.endswith(".pdf"):
        return site_dir / href
    return candidate


def validate_site(site_dir: Path) -> int:
    index_html = site_dir / "index.html"
    if not index_html.exists():
        raise SystemExit("Missing site/index.html. Did you run mkdocs build?")

    failures: list[str] = []
    for href in sorted(set(collect_local_links(index_html))):
        target = resolve_path(site_dir, href)
        if not target.exists():
            failures.append(href)

    if failures:
        print("Broken links detected on index page:")
        for href in failures:
            print(f" - {href}")
        return 1
    print("All index page links resolve within the built site.")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    args = parser.parse_args()
    return validate_site(args.site_dir)


if __name__ == "__main__":
    raise SystemExit(main())
