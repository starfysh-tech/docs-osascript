#!/usr/bin/env python3
from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup
import markdown


def iter_html_files(html_root: Path) -> Iterable[Path]:
    for path in sorted(html_root.rglob("*.html")):
        if path.is_file():
            yield path


WWDC_NOTE_TEXT = "See also WWDC 2014 Session 306 resources for the companion PDF and streaming video referenced by this release."

SKIP_LINES = {
    "Next",
    "Previous",
    "PDF",
    "Companion File",
    WWDC_NOTE_TEXT,
}


def canonicalize_text(text: str) -> str:
    result: list[str] = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line in SKIP_LINES:
            continue
        if line in {"*", "|"}:
            continue
        if line[0].isdigit():
            parts = line.split(".", 1)
            if len(parts) == 2 and parts[0].isdigit():
                line = parts[1].strip()
        stripped = line.lstrip()
        if stripped.startswith(('* ', '- ', '• ')):
            line = stripped[2:].strip()
        if line.lower().startswith("image:"):
            continue
        if line.startswith("|"):
            segments = [seg.strip() for seg in line.split("|") if seg.strip()]
            result.extend(" ".join(seg.split()) for seg in segments if seg)
            continue
        if "|" in line:
            segments = [seg.strip() for seg in line.split("|") if seg.strip()]
            result.extend(" ".join(seg.split()) for seg in segments if seg)
            continue
        result.append(" ".join(line.split()))
    flattened = " ".join(result)
    flattened = (
        flattened.replace(" )", ")")
        .replace("( ", "(")
        .replace(" : ", " ")
        .replace(" .", ".")
        .replace(" ,", ",")
        .replace(" ;", ";")
        .replace(" ?", "?")
        .replace(" !", "!")
    )
    flattened = flattened.replace(":", "")
    flattened = flattened.replace("`", "")
    return " ".join(flattened.split())


def article_text(html_path: Path) -> str:
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8", errors="ignore"), "html.parser")
    article = soup.find("article", id="contents")
    if not article:
        article = soup.find("article", class_="chapter")
    if not article:
        article = soup.find("article")
    if not article:
        raise RuntimeError(f"Could not locate article#contents in {html_path}")
    for selector in [
        "#next_previous",
        ".pageNavigationLinks",
        "#pediaWindow",
        ".jumpNav",
        ".feedback",
    ]:
        for el in article.select(selector):
            el.decompose()
    return canonicalize_text(article.get_text(separator="\n"))


def markdown_text(md_path: Path) -> str:
    html = markdown.markdown(md_path.read_text(encoding="utf-8"), extensions=["tables"])
    soup = BeautifulSoup(html, "html.parser")
    text = canonicalize_text(soup.get_text(separator="\n"))
    if WWDC_NOTE_TEXT in text:
        text = text.replace(WWDC_NOTE_TEXT, "")
    return " ".join(text.split())


def diff_text(html_txt: str, md_txt: str, context: int = 3) -> str | None:
    if html_txt == md_txt:
        return None
    diff = difflib.unified_diff(
        html_txt.splitlines(),
        md_txt.splitlines(),
        fromfile="html",
        tofile="markdown",
        n=context,
    )
    return "\n".join(diff)


def main(html_dir: Path, markdown_dir: Path, limit: int) -> int:
    failures = 0
    for html_path in iter_html_files(html_dir):
        rel = html_path.relative_to(html_dir)
        md_path = markdown_dir / rel.with_suffix(".md")
        if not md_path.exists():
            print(f"[MISSING] No Markdown counterpart for {rel}", file=sys.stderr)
            failures += 1
            continue
        html_txt = article_text(html_path)
        md_txt = markdown_text(md_path)
        diff = diff_text(html_txt, md_txt)
        if diff:
            failures += 1
            print(f"=== DIFF: {rel} ===")
            if limit and len(diff.splitlines()) > limit:
                snippet = "\n".join(diff.splitlines()[:limit])
                print(snippet)
                print("... (diff truncated)")
            else:
                print(diff)
            print()
    if failures:
        print(f"{failures} file(s) differ.", file=sys.stderr)
        return 1
    print("All Markdown files match the HTML text content.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Markdown mirrors HTML content.")
    parser.add_argument("--html-dir", required=True, type=Path)
    parser.add_argument("--markdown-dir", required=True, type=Path)
    parser.add_argument("--diff-lines", type=int, default=80, help="Max diff lines to display per file (0 for full).")
    args = parser.parse_args()
    raise SystemExit(main(args.html_dir, args.markdown_dir, args.diff_lines))
