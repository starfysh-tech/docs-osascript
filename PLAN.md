# AppleScript Docs Archive Plan

## Snapshot (updated: 2025-10-15)
- **Current focus**: Mirror the Mac Automation Scripting Guide and design the automated change-detection framework.
- **Next actions**
  1. Draft the extraction workflow for the Mac Automation Scripting Guide (TOC source, assets, validation expectations).
  2. Outline the monitoring manifest schema (`monitor/manifest.json`) and `scripts/check_updates.py`.
  3. Sketch the GitHub Pages catalog structure (collections listing, per-page routing, search).
- **Blockers / decisions pending**: Determine how to handle large WWDC video assets (link-out vs. local copy) and agree on the storage format for man-page exports.

## Objectives
- Mirror AppleScript documentation (Overview, Language Guide, and future sets) as local Markdown.
- Keep the original Apple TOC layout intact within each collection for reliable cross-linking.
- Maintain reproducible scripts to refresh sources and note gaps for manual cleanup (assets, PDFs, etc.).
- Track active work in GitHub Issues with consistent labels (`to-do`, `in-progress`, `blocked`, `done`).

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
| ⬜️ | Implement change detection (`monitor/manifest.json` + `scripts/check_updates.py`). |
| ⬜️ | Publish GitHub Pages catalog sourced from `build/`. |
| ⬜️ | Generate LLM-ready datasets (plain text + JSONL chunks, optional embeddings). |

## Open Questions
- Which additional AppleScript doc sets (e.g., Apple Events Programming Guide) should be pulled next?
- Should PDFs/assets be stored alongside each doc or centralized under `assets/`?
- Do we want to capture linked non-AppleScript materials that live outside the mirrored paths?
- What cadence should the monitoring job run (weekly vs. monthly)?
- Where should large binary artifacts (WWDC video, high-res PDFs) live if mirrored locally?

## Backlog Reference
- `apple-official-docs.md` enumerates all official Apple automation resources. Highlight near-term targets:
  1. **Mac Automation Scripting Guide** – conceptual + how-to content for scripting terminology.
  2. **JavaScript for Automation (JXA) Release Notes & WWDC 2014 resources** – provide parity for JavaScript automation workflows.
  3. **Script Editor User Guide** – support documentation for the tooling used in most walkthroughs.
- Remaining sections cover AppleScript references already mirrored; treat the rest as sequential backlog until all links are archived locally.

## Workflow Notes
- **Issues**: Create one GitHub Issue per work item and label it (`to-do`, `in-progress`, `blocked`, `done`). Reference the issue number in commits/PRs.
- **Snapshot**: Update the Snapshot section at the top of this file at the beginning or end of each work session.
- **Reports**: Store monitoring results under `reports/` (e.g., `reports/update-status-YYYYMMDD.md`) once `scripts/check_updates.py` is in place.

## Next Up
1. Draft the extraction workflow for the Mac Automation Scripting Guide and open a GitHub Issue enumerating subtasks.
2. Triage `apple-official-docs.md`: note which resources are HTML, PDF, or video and capture that in their respective Issues.
3. Define the verification checklist for current collections and the upcoming change-detection pipeline (record in an Issue or this plan).
