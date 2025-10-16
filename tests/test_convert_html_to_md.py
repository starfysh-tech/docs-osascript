from pathlib import Path

from scripts.convert_html_to_md import convert_file, main, make_converter
from scripts.normalize_markdown_links import main as normalize_links_main


def write_html(tmp_path: Path, name: str, body: str) -> Path:
    html_root = tmp_path / "html"
    html_root.mkdir(parents=True, exist_ok=True)
    html_path = html_root / f"{name}.html"
    html_path.write_text(
        f"<!DOCTYPE html><html><body><article id='contents'>{body}</article></body></html>",
        encoding="utf-8",
    )
    return html_path


def run_conversion(
    tmp_path: Path,
    html_path: Path,
    *,
    html_root: Path | None = None,
    extra_intro_note: bool = False,
) -> str:
    output_dir = tmp_path / "md"
    root = html_root if html_root else html_path.parent
    md_path = convert_file(
        html_path,
        make_converter(),
        root,
        output_dir,
        extra_intro_note=extra_intro_note,
    )
    return md_path.read_text(encoding="utf-8")


def test_inline_code_preserves_backticks(tmp_path) -> None:
    html_path = write_html(
        tmp_path,
        "inline-code",
        "<p>Inline <code>console.log</code> example and <code>tick`escape</code> sample.</p>",
    )

    markdown = run_conversion(tmp_path, html_path)

    assert "`console.log`" in markdown
    assert "`` tick`escape ``" in markdown


def test_definition_list_renders_expected_markdown(tmp_path) -> None:
    html_path = write_html(
        tmp_path,
        "definition-list",
        "<dl><dt>Automation</dt><dd><p>Runs JavaScript for Automation applets.</p></dd><dt>Library</dt><dd><p>References shared script libraries.</p></dd></dl>",
    )

    markdown = run_conversion(tmp_path, html_path)

    assert "Automation\n:   Runs JavaScript for Automation applets." in markdown
    assert "Library\n:   References shared script libraries." in markdown


def test_codesample_blocks_render_as_code_fences(tmp_path) -> None:
    html_path = write_html(
        tmp_path,
        "codesample",
        "<div class='codesample clear'><table><tr><td scope='row'><pre>Application('Mail')</pre></td></tr></table></div>",
    )

    markdown = run_conversion(tmp_path, html_path)

    assert "```" in markdown
    assert "| --- |" not in markdown
    assert "Application('Mail')" in markdown


def test_intro_page_gets_wwdc_note_when_enabled(tmp_path) -> None:
    html_root = tmp_path / "html"
    article_dir = html_root / "Articles"
    article_dir.mkdir(parents=True, exist_ok=True)
    html_path = article_dir / "Introduction.html"
    html_path.write_text(
        "<!DOCTYPE html><html><body><article id='contents'><h1>Intro</h1><p>Body</p></article></body></html>",
        encoding="utf-8",
    )

    markdown = run_conversion(
        tmp_path,
        html_path,
        html_root=html_root,
        extra_intro_note=True,
    )

    assert "WWDC 2014 Session 306 resources" in markdown


def test_main_creates_wwdc_note_for_jxa(tmp_path) -> None:
    root = tmp_path / "jxa-release-notes"
    html_dir = root / "html" / "Articles"
    html_dir.mkdir(parents=True, exist_ok=True)
    html_path = html_dir / "Introduction.html"
    html_path.write_text(
        "<!DOCTYPE html><html><body><article id='contents'><h1>Intro</h1></article></body></html>",
        encoding="utf-8",
    )

    output_dir = tmp_path / "build"
    main(html_dir.parent, output_dir)

    note_path = output_dir / "WWDC-2014-session.md"
    assert note_path.exists()
    content = note_path.read_text(encoding="utf-8")
    assert "Session 306 PDF" in content


def test_apple_ref_anchors_preserved(tmp_path) -> None:
    html_path = write_html(
        tmp_path,
        "anchors",
        "<a name='//apple_ref/doc/uid/test'></a><h2>Section</h2>",
    )

    markdown = run_conversion(tmp_path, html_path)

    assert '<a id="//apple_ref/doc/uid/test"></a>' in markdown


def test_cross_collection_links_rewrite(tmp_path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    overview = data_root / "foo"
    overview.mkdir(parents=True)
    (overview / "html_pages.txt").write_text("Doc.html\n", encoding="utf-8")

    lang = data_root / "bar"
    lang.mkdir(parents=True)
    (lang / "html_pages.txt").write_text("Sub/Ref.html\n", encoding="utf-8")

    build_dir = tmp_path / "build"
    (build_dir / "foo").mkdir(parents=True)
    (build_dir / "foo" / "Doc.md").write_text("# Doc\n", encoding="utf-8")

    target_dir = build_dir / "bar" / "Sub"
    target_dir.mkdir(parents=True, exist_ok=True)
    md_path = target_dir / "Ref.md"
    md_path.write_text(
        "See [Doc](../../foo/Doc.html#//apple_ref/doc/uid/test).",
        encoding="utf-8",
    )

    normalize_links_main([overview / "html_pages.txt", lang / "html_pages.txt"], build_dir)

    updated = md_path.read_text(encoding="utf-8")
    assert "../../foo/Doc.md#//apple_ref/doc/uid/test" in updated
