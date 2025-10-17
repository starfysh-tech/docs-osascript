#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

WWDC_NOTE = (
    "> **See also:** [WWDC 2014 Session 306 resources](../WWDC-2014-session.md) "
    "for the companion PDF and streaming video referenced by this release.\n\n"
)


class DocsMarkdownConverter(MarkdownConverter):
    """Custom converter with consistent heading and list styles."""

    def convert_code(self, el, text, convert_as_inline=False, parent_tags=None, **kwargs):  # type: ignore[override]
        parent = el.parent
        if parent and parent.name == "pre":
            return text
        ticks = "`"
        if "`" in text:
            return f"`` {text} ``"
        return f"{ticks}{text}{ticks}"

    def convert_dl(self, el, text, convert_as_inline=False, parent_tags=None, **kwargs):  # type: ignore[override]
        context = set(parent_tags or [])
        result: list[str] = []
        current_term: str | None = None

        def extract_term(node: Tag) -> str | None:
            def collect_text(current: Tag) -> list[str]:
                parts: list[str] = []
                for child in current.children:
                    if isinstance(child, NavigableString):
                        text = str(child)
                        if text.strip():
                            parts.append(text)
                        else:
                            parts.append(" ")
                        continue
                    if not isinstance(child, Tag):
                        continue
                    if child.name == "a" and not child.get("href"):
                        continue
                    if child.name in {"td", "tr"}:
                        parts.extend(collect_text(child))
                        continue
                    rendered = self.process_tag(child, parent_tags=set(context)).strip()
                    if rendered:
                        parts.append(rendered)
                return parts

            collected = collect_text(node)
            term_txt = " ".join(" ".join(collected).split())
            if term_txt:
                return term_txt
            for candidate in node.find_all(("code", "em", "strong", "span", "a"), recursive=True):
                if candidate.name == "a" and not candidate.get("href"):
                    continue
                term_txt = self.process_tag(candidate, parent_tags=set(context)).strip()
                if term_txt:
                    return term_txt
            return None

        for child in el.find_all(["tr", "dt", "dd"], recursive=True):
            if not isinstance(child, Tag):
                continue
            if child.find_parent("dl") is not el:
                continue
            if child.name in {"tr", "dt"}:
                term = extract_term(child)
                if term:
                    current_term = term.replace("\n", " ").strip(" :")
            elif child.name == "dd":
                term = current_term
                first_tag = next((c for c in child.children if isinstance(c, Tag)), None)
                if first_tag and first_tag.name == "em" and first_tag.get_text(strip=True).endswith(":"):
                    term = self.process_tag(first_tag, parent_tags=set(context)).strip()
                    first_tag.decompose()
                if not term:
                    continue
                clean_term = term.replace("\n", " ").strip(" :")
                definition = self.process_tag(child, parent_tags=set(context)).strip()
                definition = definition.lstrip(": ").strip()
                definition = " ".join(definition.split())
                if clean_term and definition:
                    result.append(f"{clean_term}\n:   {definition}\n\n")
                    current_term = None
        return "".join(result)

    def convert_a(self, el, text, parent_tags):  # type: ignore[override]
        href = el.get("href")
        if not href:
            anchor = el.get("name") or el.get("id")
            if anchor:
                anchor_markup = f'<a id="{anchor}"></a>'
                return f"{anchor_markup}{text}" if text else anchor_markup
        return super().convert_a(el, text, parent_tags)

    def process_text(self, el, parent_tags=None):  # type: ignore[override]
        if isinstance(el, NavigableString):
            text = str(el)
            text = text.replace("\\", "\\\\")
            tags = set(parent_tags or [])
            if "td" in tags or "th" in tags:
                text = text.replace("|", "\\|")
            text = text.replace("<", "&lt;").replace(">", "&gt;")
            el = NavigableString(text)
        return super().process_text(el, parent_tags=parent_tags)


def make_converter() -> DocsMarkdownConverter:
    return DocsMarkdownConverter(heading_style="ATX", bullets="*")


def iter_html_files(directory: Path) -> Iterable[Path]:
    for path in sorted(directory.rglob("*.html")):
        if path.is_file():
            yield path


ANCHOR_PLACEHOLDER_PREFIX = "@@ANCHOR@@"


def find_main_content(soup: BeautifulSoup) -> Tag:
    article = soup.find("article", id="contents")
    if article:
        return article
    article = soup.find("article", class_="chapter")
    if article:
        return article
    article = soup.find("article")
    if article:
        return article

    support_container = soup.select_one("#article-section .book-content")
    if support_container:
        support_body = support_container.find(
            "body",
            class_=lambda value: value and "apd-topic" in value.split(),
        )
        if support_body and support_body.parent and support_body.parent.name not in {"html", "[document]"}:
            return support_body
        return support_container

    support_bodies = soup.find_all("body", class_=lambda value: value and "apd-topic" in value.split())
    for candidate in support_bodies:
        if candidate.parent and candidate.parent.name not in {"html", "[document]"}:
            return candidate

    raise RuntimeError("Could not locate main article content.")


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
        name = anchor.get("name")
        text = anchor.get_text(strip=True)
        if name and name.startswith("//apple_ref"):
            continue
        if name and not text:
            anchor.decompose()
            continue
        if not anchor.get_text(strip=True):
            anchor.unwrap()

    for sample in article.select("div.codesample"):
        snippets = [pre.get_text().rstrip("\n") for pre in sample.select("pre")]
        snippets = [snippet for snippet in snippets if snippet]
        if not snippets:
            continue
        code_text = "\n".join(snippets)
        new_pre = soup.new_tag("pre")
        code_tag = soup.new_tag("code")
        code_tag.string = code_text
        new_pre.append(code_tag)
        sample.replace_with(new_pre)

    for pre in list(article.find_all("pre")):
        for br in pre.find_all("br"):
            br.replace_with("\n")
        parts: list[str] = []
        for node in pre.children:
            if isinstance(node, NavigableString):
                parts.append(str(node))
            else:
                parts.append(node.get_text())
        text_builder: list[str] = []
        for part in parts:
            if not text_builder:
                text_builder.append(part)
                continue
            if part == "\n":
                text_builder.append(part)
                continue
            if not text_builder[-1].endswith((" ", "\n")) and not part.startswith((" ", "\n", ".", ",", ")")):
                text_builder.append(" ")
            text_builder.append(part)
        text = "".join(text_builder)
        new_pre = soup.new_tag("pre")
        code_tag = soup.new_tag("code")
        code_tag.string = text
        new_pre.append(code_tag)
        pre.replace_with(new_pre)

    for empty_code in list(article.find_all("code")):
        if not empty_code.get_text(strip=True):
            empty_code.decompose()

    for sup in list(article.find_all("sup")):
        sup.replace_with(f"^{sup.get_text(strip=True)}")

    for icon in article.select("figure.topicIcon"):
        icon.decompose()

    for universal in article.select("div.LinkUniversal"):
        universal.name = "p"
        universal.attrs.pop("class", None)
        link = universal.find("a")
        if link and (not link.previous_sibling or link.previous_sibling.string is None):
            link.insert_before(soup.new_string(" "))

    for em in article.select("em.variableText"):
        prev = em.previous_sibling
        needs_space = True
        if prev is None:
            needs_space = True
        elif isinstance(prev, NavigableString):
            if prev.endswith((" ", "\n")):
                needs_space = False
        elif prev.name == "br":
            needs_space = False
        if needs_space:
            em.insert_before(soup.new_string(" "))

def inject_special_note(markdown: str) -> str:
    if WWDC_NOTE in markdown:
        return markdown
    if not markdown.startswith("# "):
        return markdown
    first_newline = markdown.find("\n")
    if first_newline == -1:
        return markdown + "\n" + WWDC_NOTE
    head = markdown[: first_newline + 1]
    tail = markdown[first_newline + 1 :].lstrip("\n")
    return f"{head}\n{WWDC_NOTE}{tail}\n"


def convert_file(
    html_path: Path,
    converter: DocsMarkdownConverter,
    html_root: Path,
    output_root: Path,
    *,
    extra_intro_note: bool = False,
) -> Path:
    html = html_path.read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(html, "html.parser")
    try:
        article = find_main_content(soup)
    except RuntimeError as exc:
        raise RuntimeError(f"Could not locate main article content in {html_path}") from exc
    clean_article(soup, article)

    markdown = converter.convert_soup(article)
    markdown = markdown.replace("| * ", "| ")
    markdown = markdown.replace(" * |", " |")
    markdown = markdown.replace(". * ", ". ")
    markdown = markdown.replace("\xa0", " ").strip() + "\n"

    relative = html_path.relative_to(html_root)
    md_path = output_root / relative.with_suffix(".md")
    if extra_intro_note and relative.as_posix() == "Articles/Introduction.html":
        markdown = inject_special_note(markdown)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(markdown, encoding="utf-8")
    return md_path


def main(html_dir: Path, output_dir: Path) -> None:
    converter = make_converter()
    output_dir.mkdir(parents=True, exist_ok=True)

    extra_intro_note = html_dir.parent.name == "jxa-release-notes"

    outputs = []
    for html_path in iter_html_files(html_dir):
        md_path = convert_file(
            html_path,
            converter,
            html_dir,
            output_dir,
            extra_intro_note=extra_intro_note,
        )
        outputs.append(md_path)
        print(f"Converted {html_path.relative_to(html_dir)} -> {md_path.relative_to(output_dir)}")

    if extra_intro_note:
        note_path = output_dir / "WWDC-2014-session.md"
        note_path.write_text(
            "# WWDC 2014 Session 306 Resources\n\n"
            "Apple’s JXA release notes reference WWDC Session 306 (“JavaScript for Automation”). "
            "We archive the session PDF locally and link out to the streaming video.\n\n"
            "* [Session 306 PDF](./306_javascript_for_automation.pdf)\n"
            "* [Streaming video on developer.apple.com](https://developer.apple.com/videos/play/wwdc2014/306/)\n",
            encoding="utf-8",
        )

    print(f"Generated {len(outputs)} Markdown files.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert downloaded HTML docs to Markdown")
    parser.add_argument("--html-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    main(args.html_dir, args.output_dir)
