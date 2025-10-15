# Repository Guidelines

## Project Structure & Module Organization
- `scripts/` — Python CLIs for TOC harvesting, HTML mirroring, Markdown conversion, asset syncing, and validation.
- `data/<collection>/` — Source inputs (e.g., `book.json`, `toc_hierarchy.json`, downloaded HTML, and raw assets). Treat folders as read-only archives of Apple’s originals.
- `build/<collection>/` — Generated Markdown plus colocated assets, preserving Apple’s directory hierarchy to keep links functional offline.
- `PLAN.md` — Rolling roadmap and decision log; update after every meaningful milestone.
- `apple-official-docs.md` — Backlog of official Apple automation resources to mirror next.

## Build, Test, and Development Commands
- TOC harvest: `python3 scripts/inventory_toc.py --book-json data/<collection>/book.json --base-url <url> --output-dir data/<collection>`.
- HTML mirror: `python3 scripts/download_html.py --pages-file data/<collection>/html_pages.txt --base-url <url> --output-dir data/<collection>/html`.
- Markdown render: `python3 scripts/convert_html_to_md.py --html-dir data/<collection>/html --output-dir build/<collection>`.
- Link rewrite: `python3 scripts/normalize_markdown_links.py --pages-file data/<collection>/html_pages.txt --markdown-dir build/<collection>`.
- Asset sync: run `download_assets.py` followed by `sync_assets.py` with matching arguments to copy images beside Markdown.
- Verification: `python3 scripts/validate_markdown.py --html-dir data/<collection>/html --markdown-dir build/<collection>`.

## Coding Style & Naming Conventions
- Follow PEP 8: 4-space indentation, snake_case functions, UPPER_SNAKE constants. Prefer `pathlib.Path` and `argparse` over ad-hoc utilities.
- Collection folders should reuse Apple’s slug (e.g., `applescript-language-guide`, `mac-automation-scripting-guide`) to simplify cross-linking.
- Keep scripts single-purpose and composable; expose arguments rather than hard-coding paths.

## Testing Guidelines
- `validate_markdown.py` is the primary regression test; diffs must be reviewed and either resolved or annotated in `PLAN.md`.
- When altering parsing rules, create minimal HTML fixtures under `data/tmp/` and run the full pipeline before touching live URLs.
- For large table-heavy pages, document any acceptable discrepancies (e.g., index tables) in the PR description.

## Commit & Pull Request Guidelines
- Commits use short, imperative subjects (“Mirror Mac Automation guide introduction”) and include details when context aids review.
- Each PR should summarize new collections or script changes, list commands executed (mirror + validate), and note outstanding follow-ups (missing assets, manual checks).
- Link backlog items from `apple-official-docs.md` or issues whenever applicable; attach representative directory listings or sample diffs to aid reviewers.

## Agent Workflow Tips
- Check `PLAN.md` before starting work to avoid conflicting mirror efforts.
- Preserve the original Apple path casing; many cross-links are case-sensitive.
- If a resource is a PDF or video rather than HTML, note it in the PR and store it under `data/<collection>/assets/` for later processing.
- Always refresh the Snapshot in `PLAN.md` and update GitHub Issue statuses when starting or finishing a work session.
- After noteworthy chats or milestones, append an entry to `blog/journal.md` that captures both the discussion highlights and resulting action—the blog acts as our narrative log for future posts.
