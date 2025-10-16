# Repository Guidelines

## Project Structure & Module Organization
- `scripts/` — Python CLIs for TOC harvesting, HTML mirroring, Markdown conversion, asset syncing, and validation.
- `data/<collection>/` — Source inputs (e.g., `book.json`, `toc_hierarchy.json`, downloaded HTML, and raw assets). Treat folders as read-only archives of Apple’s originals.
- `build/<collection>/` — Generated Markdown plus colocated assets, preserving Apple’s directory hierarchy to keep links functional offline.
- `PLAN.md` — Rolling roadmap and decision log; update after every meaningful milestone.
- `apple-official-docs.md` — Backlog of official Apple automation resources to mirror next.

## Build, Test, and Development Commands
- After regenerating Markdown, run `python3 scripts/normalize_markdown_links.py --markdown-dir build --pages-file ...` (include all collection `html_pages.txt`) to keep cross-collection links and anchors accurate.
- Regenerate the MkDocs navigation whenever new build output is introduced via `python3 scripts/generate_mkdocs_nav.py` before running `mkdocs build`.
- Produce datasets from mirrored content with `python3 scripts/export_dataset.py --collections <slug>` (omit `--collections` to export everything); treat the outputs as build artifacts and package them separately if distributing.
- Fetch archived binaries with `python3 scripts/download_file.py --url <source> --output data/<collection>/assets/<filename>`.

- TOC harvest: `python3 scripts/inventory_toc.py --book-json data/<collection>/book.json --base-url <url> --output-dir data/<collection>`.
- HTML mirror: `python3 scripts/download_html.py --pages-file data/<collection>/html_pages.txt --base-url <url> --output-dir data/<collection>/html`.
- Markdown render: `python3 scripts/convert_html_to_md.py --html-dir data/<collection>/html --output-dir build/<collection>`.
- Link rewrite: `python3 scripts/normalize_markdown_links.py --markdown-dir build --pages-file data/applescript-overview/html_pages.txt --pages-file data/applescript-language-guide/html_pages.txt --pages-file data/mac-automation-scripting-guide/html_pages.txt --pages-file data/jxa-release-notes/html_pages.txt`.
- Asset sync: run `download_assets.py` followed by `sync_assets.py` with matching arguments to copy images beside Markdown.
- Standalone resource fetch: `python3 scripts/download_file.py --url <source> --output data/<collection>/assets/<name>`.
- Verification: `python3 scripts/validate_markdown.py --html-dir data/<collection>/html --markdown-dir build/<collection>`.
- Monitoring dry-run: `python3 scripts/check_updates.py --manifest monitor/manifest.json` (add `--save --report reports/update-status-<date>.md` when ready).
- Weekly monitoring check (Monday 09:00 UTC): `python3 scripts/check_updates.py --manifest monitor/manifest.json --save --report reports/update-status-YYYYMMDD.md`. Review the report: `changed` ⇒ re-run the mirror pipeline soon; `error` ⇒ investigate (HTTP issue, network outage, redirect).

## Coding Style & Naming Conventions
- Follow PEP 8: 4-space indentation, snake_case functions, UPPER_SNAKE constants. Prefer `pathlib.Path` and `argparse` over ad-hoc utilities.
- Collection folders should reuse Apple’s slug (e.g., `applescript-language-guide`, `mac-automation-scripting-guide`) to simplify cross-linking.
- Keep scripts single-purpose and composable; expose arguments rather than hard-coding paths.

## Testing Guidelines (TDD-friendly)
- Treat tests as the first-class steering wheel:
  - Before changing a script, sketch the expected outcome and encode it in a focused test (see below) so failures drive implementation work.
  - Keep fixtures minimal (`data/tmp/<case>/…`) and commit them when they capture edge cases we want to guard forever.
- Test command sequence after any pipeline change:
  1. Unit-style: run the targeted script-specific test (for example, `python3 tests/test_convert_html_to_md.py` once added) to confirm the edge case is covered.
  2. Integration: run the full sequence (`inventory_toc.py`, `download_html.py`, `convert_html_to_md.py`, `normalize_markdown_links.py`, `download_assets.py`, `sync_assets.py`, `validate_markdown.py`) against a minimal fixture collection before touching real data.
  3. Regression: execute `python3 scripts/validate_markdown.py --html-dir data/<collection>/html --markdown-dir build/<collection>` on the actual target collection and review diffs (resolve or document in `PLAN.md`).
- For large table-heavy pages or dynamic content, document acceptable deviations in PR descriptions and add TODO tests/fixtures so we revisit them.

## Commit & Pull Request Guidelines
- Commits use short, imperative subjects (“Mirror Mac Automation guide introduction”) and include details when context aids review.
- Each PR should summarize new collections or script changes, list commands executed (mirror + validate), and note outstanding follow-ups (missing assets, manual checks).
- Link backlog items from `apple-official-docs.md` or issues whenever applicable; attach representative directory listings or sample diffs to aid reviewers.

## Schedule & Monitoring
- Run `scripts/check_updates.py` every Monday 09:00 UTC (or before major releases) with `--save --report`. Store reports under `reports/` using `update-status-YYYYMMDD.md`.
- Treat exit code `3` (changed) as a blocking task: re-run the relevant mirror pipeline within 24 hours.
- Treat exit code `2` (error) as a follow-up: inspect the URL, retry with network access, or note in PLAN.md if Apple removes the page.

## Agent Workflow Tips
- Check `PLAN.md` before starting work to avoid conflicting mirror efforts.
- Preserve the original Apple path casing; many cross-links are case-sensitive.
- If a resource is a PDF or video rather than HTML, note it in the PR and store it under `data/<collection>/assets/` for later processing.
- Always refresh the Snapshot in `PLAN.md` and update GitHub Issue statuses when starting or finishing a work session.
- After noteworthy chats or milestones, append an entry to `blog/journal.md` that captures both the discussion highlights and resulting action—the blog acts as our narrative log for future posts.
