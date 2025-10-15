# Repository Guidelines

## Project Structure & Module Organization
- `scripts/`: Python utilities to fetch `book.json`, download HTML, convert to Markdown, sync assets, and validate outputs.
- `data/<collection>/`: Source artifacts for each mirrored doc set (`book.json`, `toc_hierarchy.json`, raw HTML, and downloaded assets).
- `build/<collection>/`: Generated Markdown and colocated assets mirroring Apple’s original folder hierarchy.
- `PLAN.md`: Running project log; update when milestones shift.

## Build, Test, and Development Commands
- `python3 scripts/inventory_toc.py --book-json data/<collection>/book.json --base-url <url> --output-dir data/<collection>` – parse the table of contents and emit link manifests.
- `python3 scripts/download_html.py --pages-file data/<collection>/html_pages.txt --base-url <url> --output-dir data/<collection>/html` – mirror chapter HTML.
- `python3 scripts/convert_html_to_md.py --html-dir data/<collection>/html --output-dir build/<collection>` – render cleaned Markdown.
- `python3 scripts/normalize_markdown_links.py --pages-file data/<collection>/html_pages.txt --markdown-dir build/<collection>` – rewrite intra-site links to `.md`.
- `python3 scripts/download_assets.py ... && python3 scripts/sync_assets.py ...` – capture images and place them beside Markdown.
- `python3 scripts/validate_markdown.py --html-dir data/<collection>/html --markdown-dir build/<collection>` – compare Markdown text to the HTML source.

## Coding Style & Naming Conventions
- Python scripts follow PEP 8 defaults: 4-space indentation, snake_case functions, UPPER_SNAKE constants.
- Prefer pathlib over os.path, argparse for CLIs, and explicit encoding (`utf-8`).
- New collections should use hyphenated folder names matching Apple’s doc root (e.g., `applescript-language-guide`).

## Testing Guidelines
- Use `scripts/validate_markdown.py` as the primary regression check; all newly generated Markdown must pass without unexpected diffs (table-heavy pages may require manual review notes).
- When adding new parsing logic, craft small sample HTML fixtures under `data/tmp/` and run the script locally before mirroring live docs.

## Commit & Pull Request Guidelines
- Commit messages follow short imperative titles (e.g., “Add AppleScript doc mirrors and tooling”) with optional details separated by blank lines.
- For PRs, include: summary of mirrored collections or scripts touched, verification commands run (`validate_markdown`, etc.), and highlight any manual follow-up needed (assets, external links).
- Link related issues when available; attach before/after snippets or directory listings if structure changes.
