#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple
from urllib.parse import urljoin


def load_book_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def normalize_entry(entry: Dict[str, Any], base_url: str) -> Dict[str, Any]:
    href = entry.get("href", "")
    page_path, anchor = split_href(href)
    normalized: Dict[str, Any] = {
        "title": entry.get("title", "").strip(),
        "href": href,
        "url": urljoin(base_url, href),
        "page": page_path,
        "anchor": anchor,
    }

    sections = entry.get("sections") or []
    children = [normalize_entry(child, base_url) for child in sections]
    if children:
        normalized["children"] = children
    return normalized


def split_href(href: str) -> Tuple[Optional[str], Optional[str]]:
    if not href:
        return None, None
    if "#" in href:
        page, fragment = href.split("#", 1)
        return page or None, fragment or None
    return href, None


def collect_pages(entries: Iterable[Dict[str, Any]]) -> List[str]:
    seen: Set[str] = set()

    def walk(node: Dict[str, Any]) -> None:
        page = node.get("page")
        if page:
            if page not in seen:
                seen.add(page)
        for child in node.get("children", []):
            walk(child)

    for entry in entries:
        walk(entry)

    return sorted(seen)


def main(book_json: Path, base_url: str, output_dir: Path) -> None:
    book_data = load_book_json(book_json)
    sections = book_data.get("sections") or []
    normalized_sections = [normalize_entry(section, base_url) for section in sections]

    toc_hierarchy_json = output_dir / "toc_hierarchy.json"
    toc_pages_txt = output_dir / "html_pages.txt"

    output_dir.mkdir(parents=True, exist_ok=True)

    toc_hierarchy_json.write_text(
        json.dumps(normalized_sections, indent=2, ensure_ascii=True),
        encoding="utf-8",
    )

    pages = collect_pages(normalized_sections)
    toc_pages_txt.write_text("\n".join(pages) + "\n", encoding="utf-8")

    print(f"Wrote {toc_hierarchy_json}")
    print(f"Wrote {toc_pages_txt} ({len(pages)} unique HTML files)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalize Apple document TOC")
    parser.add_argument("--book-json", required=True, type=Path)
    parser.add_argument("--base-url", required=True)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    main(args.book_json, args.base_url, args.output_dir)
