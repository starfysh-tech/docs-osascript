# AppleScript Docs Archive Plan

## Objectives
- Mirror AppleScript documentation (Overview, Language Guide, and future sets) as local Markdown.
- Keep the original Apple TOC layout intact within each collection for reliable cross-linking.
- Maintain reproducible scripts to refresh sources and note gaps for manual cleanup (assets, PDFs, etc.).

## Progress Log
- 2024-10-15: Confirmed `url-to-md` runs in this environment by exporting the landing page to `test.md`.
- 2024-10-15: Downloaded `AppleScript Overview` book.json, parsed the table of contents, and generated TOC artifacts.
- 2024-10-15: Trialed `url-to-md` conversion (default vs `--clean-content`) on `Concepts/ScriptingOnOSX.html` to gauge output quality.
- 2024-10-15: Implemented custom BeautifulSoup + markdownify pipeline (`scripts/download_html.py`, `scripts/convert_html_to_md.py`) to fetch all HTML chapters and render cleaned Markdown.
- 2024-10-15: Refactored scripts to accept configurable inputs and reorganized outputs under `data/` and `build/` per collection.
- 2024-10-15: Regenerated the AppleScript Overview set under `data/applescript-overview/` and `build/applescript-overview/`.
- 2024-10-15: Mirrored the AppleScript Language Guide set into `data/applescript-language-guide/` and `build/applescript-language-guide/`.
- 2024-10-15: Added asset downloader/sync helpers and captured all referenced images locally for both collections.
- 2024-10-15: Ran formatting sanity checks (H1 presence, image availability, non-breaking space scan) across Markdown outputs.
- 2024-10-15: Built `scripts/validate_markdown.py` and verified AppleScript Overview matches source HTML exactly; Language Guide diffs limited to dense tables (manually inspected).
- 2024-10-15: Imported `apple-official-docs.md` as the authoritative backlog of Apple automation docs to mirror.

## Task Board

| Status | Task |
| --- | --- |
| ✅ | Inventory the table of contents and normalize target URLs (Overview & Language Guide). |
| ✅ | Automate page retrieval & HTML→Markdown conversion with reusable scripts. |
| ✅ | Keep Markdown outputs aligned with original Apple doc paths per collection. |
| ✅ | Post-process Markdown (handle external assets, review remaining HTML links) and spot-check formatting. |
| ⬜️ | Document any gaps or manual follow-ups required. |
| ⬜️ | Mirror the Mac Automation Scripting Guide collection (see `apple-official-docs.md`). |
| ⬜️ | Mirror JavaScript for Automation release notes + WWDC resources. |
| ⬜️ | Capture Script Editor User Guide for offline use. |

## Open Questions
- Which additional AppleScript doc sets (e.g., Apple Events Programming Guide) should be pulled next?
- Should PDFs/assets be stored alongside each doc or centralized under `assets/`?
- Do we want to capture linked non-AppleScript materials that live outside the mirrored paths?

## Backlog Reference
- `apple-official-docs.md` enumerates all official Apple automation resources. Highlight near-term targets:
  1. **Mac Automation Scripting Guide** – conceptual + how-to content for scripting terminology.
  2. **JavaScript for Automation (JXA) Release Notes & WWDC 2014 resources** – provide parity for JavaScript automation workflows.
  3. **Script Editor User Guide** – support documentation for the tooling used in most walkthroughs.
- Remaining sections cover AppleScript references already mirrored; treat the rest as sequential backlog until all links are archived locally.

## Next Up
1. Draft extraction plan for Mac Automation Scripting Guide (TOC source, assets, expected HTML patterns).
2. Run backlog triage: mark which `apple-official-docs.md` entries require custom handling (videos, PDFs) vs. HTML scraping.
3. Create verification checklist (lint/spot-check) for both current and upcoming collections.
