from __future__ import annotations

import subprocess
from pathlib import Path
import shutil

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

COLLECTIONS = {
    "applescript-overview": [],
    "applescript-language-guide": ["Index/index_of_book.html"],
    "mac-automation-scripting-guide": [],
    "jxa-release-notes": [],
    "script-editor-user-guide": [],
    "apple-events-programming-guide": [],
    "applescript-scripting-additions-guide": [],
    "introduction-to-scripting": [],
}


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=REPO_ROOT, check=True)


def test_mkdocs_build() -> None:
    if shutil.which("mkdocs") is None:
        pytest.skip("mkdocs command not found in PATH")
    run(["mkdocs", "build"])


def test_site_links() -> None:
    run(["python3", "scripts/validate_site_links.py"])


def test_validate_collections() -> None:
    for collection, skips in COLLECTIONS.items():
        html_dir = REPO_ROOT / "data" / collection / "html"
        if not html_dir.exists():
            continue
        markdown_dir = REPO_ROOT / "build" / collection
        cmd = [
            "python3",
            "scripts/validate_markdown.py",
            "--html-dir",
            str(html_dir),
            "--markdown-dir",
            str(markdown_dir),
            "--diff-lines",
            "0",
        ]
        for skip in skips:
            cmd.extend(["--skip", skip])
        run(cmd)
