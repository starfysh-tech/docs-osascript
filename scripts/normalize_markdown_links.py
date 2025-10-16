#!/usr/bin/env python3
from __future__ import annotations

import argparse
import posixpath
import re
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

LINK_RE = re.compile(r"(?P<prefix>!?\[[^\]]*\])\((?P<url>[^)\s]+)\)")

COLLECTION_ALIASES = {
    "applescript-overview": ["AppleScriptX"],
    "applescript-language-guide": ["AppleScriptLangGuide"],
    "mac-automation-scripting-guide": ["MacAutomationScriptingGuide"],
    "jxa-release-notes": [
        "RN-JavaScriptForAutomation",
        "InterapplicationCommunication/RN-JavaScriptForAutomation",
    ],
}


def load_html_mapping(pages_files: Iterable[Path]) -> Dict[str, str]:
    mapping: Dict[str, str] = {}
    for pages_file in pages_files:
        html_pages = [
            line.strip()
            for line in pages_file.read_text().splitlines()
            if line.strip()
        ]
        collection = pages_file.parent.name
        aliases = COLLECTION_ALIASES.get(collection, [])
        for page in html_pages:
            stem, _ = posixpath.splitext(page)
            target_md = posixpath.join(collection, stem + ".md")
            variants = {
                page,
                posixpath.join(collection, page),
            }
            if "/" not in page:
                variants.add(posixpath.join(stem, page))
            for alias in aliases:
                variants.add(posixpath.join(alias, page))
            for variant in variants:
                mapping.setdefault(variant, target_md)
    return mapping


def normalize_path(base_dir: str, target: str) -> Tuple[str, str]:
    """Return normalized absolute-like path within build root and anchor."""
    path_part, _, anchor = target.partition("#")
    if not path_part:
        return "", anchor

    combined = posixpath.join(base_dir or ".", path_part)
    normalized = posixpath.normpath(combined)
    return normalized, anchor


def rewrite_links(md_path: Path, mapping: Dict[str, str], markdown_root: Path) -> bool:
    rel_path = md_path.relative_to(markdown_root).as_posix()
    base_dir = posixpath.dirname(rel_path)
    original = md_path.read_text(encoding="utf-8")
    updated = original

    def repl(match: re.Match) -> str:
        prefix = match.group("prefix")
        url = match.group("url")

        lower = url.lower()
        if lower.startswith(("http://", "https://", "mailto:", "javascript:")):
            return match.group(0)

        normalized, anchor = normalize_path(base_dir, url)
        if not normalized:
            return match.group(0)

        if normalized in mapping:
            target_md = mapping[normalized]
            rel_target = posixpath.relpath(target_md, base_dir or ".")
            if anchor:
                rel_target = f"{rel_target}#{anchor}"
            return f"{prefix}({rel_target})"

        return match.group(0)

    updated = LINK_RE.sub(repl, updated)

    if updated != original:
        md_path.write_text(updated, encoding="utf-8")
        return True
    return False


def main(pages_files: List[Path], markdown_dir: Path) -> None:
    mapping = load_html_mapping(pages_files)
    touched = 0
    for md_file in sorted(markdown_dir.rglob("*.md")):
        if rewrite_links(md_file, mapping, markdown_dir):
            touched += 1
    print(f"Rewrote links in {touched} Markdown files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Normalize local Markdown links to .md targets")
    parser.add_argument(
        "--pages-file",
        action="append",
        required=True,
        type=Path,
        help="Path(s) to html_pages.txt files used for building the link mapping.",
    )
    parser.add_argument("--markdown-dir", required=True, type=Path)
    args = parser.parse_args()
    main(args.pages_file, args.markdown_dir)
