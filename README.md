# docs-osascript

Local, scriptable mirrors of Apple’s archived AppleScript documentation.

## Contents

- `data/` – source artifacts for each mirrored collection (TOC JSON, raw HTML, downloaded assets).
- `build/` – cleaned Markdown output with the same directory structure as Apple’s site plus copied assets.
- `scripts/` – automation utilities for fetching, converting, validating, and syncing documentation sets.
- `PLAN.md` – running log of progress, open questions, and next actions.

Current mirrored sets:

1. **AppleScript Overview** (`data/applescript-overview`, `build/applescript-overview`)
2. **AppleScript Language Guide** (`data/applescript-language-guide`, `build/applescript-language-guide`)

## Usage

Each script accepts explicit inputs so new doc sets can be mirrored without editing code. Typical workflow:

```bash
# 1. Generate TOC artifacts (hierarchy + page list)
python3 scripts/inventory_toc.py \
  --book-json data/<collection>/book.json \
  --base-url https://developer.apple.com/library/archive/documentation/.../<collection>/ \
  --output-dir data/<collection>

# 2. Download HTML chapters
python3 scripts/download_html.py \
  --pages-file data/<collection>/html_pages.txt \
  --base-url https://developer.apple.com/library/archive/documentation/.../<collection>/ \
  --output-dir data/<collection>/html

# 3. Convert HTML to Markdown while cleaning nav chrome
python3 scripts/convert_html_to_md.py \
  --html-dir data/<collection>/html \
  --output-dir build/<collection>

# 4. Normalize internal links (across all mirrored collections)
python3 scripts/normalize_markdown_links.py \
  --markdown-dir build \
  --pages-file data/applescript-overview/html_pages.txt \
  --pages-file data/applescript-language-guide/html_pages.txt \
  --pages-file data/mac-automation-scripting-guide/html_pages.txt \
  --pages-file data/jxa-release-notes/html_pages.txt

# 5. Mirror referenced images/assets and copy them into the Markdown tree
python3 scripts/download_assets.py \
  --html-dir data/<collection>/html \
  --base-url https://developer.apple.com/library/archive/documentation/.../<collection>/ \
  --asset-dir data/<collection>/assets

python3 scripts/sync_assets.py \
  --assets-dir data/<collection>/assets \
  --markdown-dir build/<collection>
```

## Validation

Use the text comparison helper to confirm Markdown content matches the HTML source:

```bash
python3 scripts/validate_markdown.py \
  --html-dir data/<collection>/html \
  --markdown-dir build/<collection>
```

For scriptable doc sets with large index tables (e.g., AppleScript Language Guide), expect structural diffs due to the extensive cross-reference entries; manual inspection has confirmed the data is preserved.

## Notes

- All local assets live alongside the Markdown files, so the `.md` files render the same images offline.
- The folder hierarchy mirrors Apple’s original layout, which keeps relative links intact and makes it easy to cross-reference with archived URLs.
- `PLAN.md` tracks remaining work; update it when new doc sets are mirrored or follow-up items are closed.
- After regenerating Markdown, rerun `python3 scripts/normalize_markdown_links.py --markdown-dir build --pages-file ...` (include every collection `html_pages.txt`) so cross-collection anchors stay valid.
- Regenerate MkDocs navigation with `python3 scripts/generate_mkdocs_nav.py` before `mkdocs build` whenever new collections are added.
- Export plain text + JSONL datasets with `python3 scripts/export_dataset.py --collections <collection>` (defaults to all collections) — see `docs/dataset-packaging.md` for details; treat `dataset/` as build output and package separately for releases (see the release checklist there).
- Fetch standalone resources (PDFs, ZIPs, etc.) with `python3 scripts/download_file.py --url <source> --output data/<collection>/assets/<filename>`.
- Dataset export planning lives in `docs/dataset-packaging.md`; follow it when producing plain text or JSONL corpora.
- Manual cleanups / pending decisions are tracked in `docs/manual-followups.md`.
