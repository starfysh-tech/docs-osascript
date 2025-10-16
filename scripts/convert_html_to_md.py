#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup, Tag
from markdownify import MarkdownConverter


class DocsMarkdownConverter(MarkdownConverter):
    """Custom converter with consistent heading and list styles."""

    def convert_code(self, el, text, parent_tags):  # type: ignore[override]
        ticks = "`"
        if "`" in text:
            return f"`` {text} ``"
        return f"{ticks}{text}{ticks}"


def make_converter() -> DocsMarkdownConverter:
    return DocsMarkdownConverter(heading_style="ATX", bullets="*")


def iter_html_files(directory: Path) -> Iterable[Path]:
    for path in sorted(directory.rglob("*.html")):
        if path.is_file():
            yield path


def clean_article(soup: BeautifulSoup, article: Tag) -> None:
    for selector in [
        ".pageNavigationLinks",
        "#pediaWindow",
        ".jumpNav",
        ".feedback",
        "#next_previous",
    ]:
        for el in article.select(selector):
            el.decompose()

    # Convert note/important boxes into proper blockquotes
    for box in article.select("div.importantbox, div.notebox"):
        blockquote = soup.new_tag("blockquote")
        # Prefer <aside> contents if present
        aside = box.find("aside")
        source = aside if aside else box
        for child in list(source.contents):
            blockquote.append(child.extract())
        for aside in blockquote.find_all("aside"):
            aside.unwrap()
        box.replace_with(blockquote)

    # Convert .note blocks (common in Mac Automation docs)
    for note in article.select("div.note"):
        blockquote = soup.new_tag("blockquote")
        aside = note.find("aside")
        source = aside if aside else note
        title = source.find(class_="aside-title")
        if title:
            strong = soup.new_tag("strong")
            strong.string = title.get_text(strip=True)
            blockquote.append(strong)
            title.decompose()
        for child in list(source.contents):
            blockquote.append(child.extract())
        note.replace_with(blockquote)

    # Remove anchor placeholders with no visible text and no href
    for anchor in list(article.find_all("a")):
        if anchor.get("href"):
            continue
        if anchor.get("name") and not anchor.get_text(strip=True):
            anchor.decompose()
            continue
        if not anchor.get_text(strip=True):
            anchor.unwrap()


def convert_file(html_path: Path, converter: DocsMarkdownConverter, html_root: Path, output_root: Path) -> Path:
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article", id="contents")
    if not article:
        article = soup.find("article", class_="chapter")
    if not article:
        article = soup.find("article")
    if not article:
        raise RuntimeError(f"Could not locate main article content in {html_path}")

    clean_article(soup, article)

    markdown = converter.convert_soup(article)
    markdown = markdown.replace("| * ", "| ")
    markdown = markdown.replace(" * |", " |")
    markdown = markdown.replace(". * ", ". ")
    markdown = markdown.replace("\xa0", " ").strip() + "\n"

    relative = html_path.relative_to(html_root)
    md_path = output_root / relative.with_suffix(".md")
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(markdown, encoding="utf-8")
    return md_path


def main(html_dir: Path, output_dir: Path) -> None:
    converter = make_converter()
    output_dir.mkdir(parents=True, exist_ok=True)

    outputs = []
    for html_path in iter_html_files(html_dir):
        md_path = convert_file(html_path, converter, html_dir, output_dir)
        outputs.append(md_path)
        print(f"Converted {html_path.relative_to(html_dir)} -> {md_path.relative_to(output_dir)}")

    print(f"Generated {len(outputs)} Markdown files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert downloaded HTML docs to Markdown")
    parser.add_argument("--html-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    main(args.html_dir, args.output_dir)
