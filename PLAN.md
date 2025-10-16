# AppleScript Docs Archive Plan

## Snapshot (updated: 2025-10-16)
- **Current focus**
  - Finish mirroring priority collections (Mac Automation Scripting Guide, JXA release notes, Script Editor User Guide).
  - Stand up the change-detection framework that keeps mirrors fresh.
  - Prepare for a public-facing catalog and LLM-ready datasets.
- **Next actions**
  1. Execute issue #2 (MkDocs + Material scaffold) — capture navigation/search requirements and wire the site shell to `build/`.
  2. Outline dataset packaging (plain text + JSONL export strategy) once the catalog scaffold exists.
  3. Mirror the Script Editor User Guide to round out the core collections.
- **Blockers / decisions pending**
  - Determine how to handle large WWDC video assets (link-out vs. local copy).
  - Decide on the storage/export format for man-page captures (plain text vs. Markdown).
  
## Objectives
- Mirror AppleScript documentation (Overview, Language Guide, and future sets) as local Markdown.
- Keep the original Apple TOC layout intact within each collection for reliable cross-linking.
- Maintain reproducible scripts to refresh sources and note gaps for manual cleanup (assets, PDFs, etc.).
- Track active work in GitHub Issues with consistent labels (`to-do`, `in-progress`, `blocked`, `done`).
- Measure success by: (a) mirror coverage (% of `apple-official-docs.md` done), (b) freshness (monitoring jobs produce actionable reports), (c) catalog usability (GitHub Pages site loads with working navigation/search), and (d) dataset readiness (plain text/JSONL exports available for local LLMs).

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
- 2025-10-15: Added `monitor/manifest.json` and `scripts/check_updates.py` to seed the change-detection pipeline.
- 2025-10-15: Mirrored the Mac Automation Scripting Guide (`data/mac-automation-scripting-guide/`, `build/mac-automation-scripting-guide/`) and enhanced conversion/validation to handle complex code listings.
- 2025-10-16: Defined monitoring thresholds/cadence (weekly Monday 09:00 UTC checks), noted WWDC video helper script approach (download on demand), and captured initial report in `reports/update-status-YYYYMMDD.md`.
- 2025-10-16: Added pytest coverage for inline code + definition list conversions, mirrored the JXA release notes, archived the Session 306 PDF, and linked to a curated WWDC resources note (note injection now automated during conversion with matching validator suppression).
- 2025-10-16: Scoped MkDocs + Material scaffold (issue #2); MKDocs nav will surface each mirrored collection landing page plus a custom index, powered by `build/` as `docs_dir`.
- 2025-10-16: Built `scripts/generate_mkdocs_nav.py` to auto-generate the MkDocs navigation from `toc_hierarchy.json` and pull in extra Markdown (e.g., WWDC resources); remaining MkDocs warnings stem from Apple anchors targeting external docs.
- 2025-10-16: Preserved Apple `//apple_ref` anchors during conversion and expanded link normalization to rewrite cross-collection references; internal links now resolve across mirrored sets.
- 2025-10-16: Converted unresolved cross-collection anchors to page-level links and rewrote unknown relative paths to the Apple archive domain; MkDocs now builds without warnings.

## Task Board

| Status | Task |
| --- | --- |
| ✅ | Inventory the table of contents and normalize target URLs (Overview & Language Guide). |
| ✅ | Automate page retrieval & HTML→Markdown conversion with reusable scripts. |
| ✅ | Keep Markdown outputs aligned with original Apple doc paths per collection. |
| ✅ | Post-process Markdown (handle external assets, review remaining HTML links) and spot-check formatting. |
| ⬜️ | Document any gaps or manual follow-ups required. |
| ✅ | Mirror the Mac Automation Scripting Guide collection (see `apple-official-docs.md`). |
| ✅ | Mirror JavaScript for Automation release notes + WWDC resources. |
| ⬜️ | Capture Script Editor User Guide for offline use. |
| ⬜️ | Implement change detection (`monitor/manifest.json` + `scripts/check_updates.py`). |
| ⬜️ | Publish GitHub Pages catalog sourced from `build/`. |
| ⬜️ | Generate LLM-ready datasets (plain text + JSONL chunks, optional embeddings). |

## Open Questions
- Which additional AppleScript doc sets (e.g., Apple Events Programming Guide) should be pulled next?
- Should PDFs/assets be stored alongside each doc or centralized under `assets/`?
- Do we want to capture linked non-AppleScript materials that live outside the mirrored paths?
- Where should large binary artifacts (WWDC video, high-res PDFs) live if mirrored locally?
- How aggressively should we reconcile legacy Apple anchor fragments in MkDocs (ignore vs. rewrite vs. custom redirect pages)?

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
- **Metrics**: Track mirror coverage, freshness, catalog usability, and dataset readiness in the Snapshot or relevant issues so progress stays visible.
- **Catalog tooling**: MkDocs + Material theme will power the GitHub Pages site; capture structural notes in repo issues/docs as the scaffold progresses.
- **Monitoring cadence**: Run `python3 scripts/check_updates.py --manifest monitor/manifest.json --save --report reports/update-status-YYYYMMDD.md` every Monday at 09:00 UTC (and before major releases). Exit code `3` (changed) ⇒ re-run the mirror pipeline; exit code `2` (error) ⇒ investigate (HTTP issue, network outage).
  - The WWDC Session 306 pointer and supporting note are generated automatically when converting the JXA release notes set.
- **MkDocs navigation**: Regenerate `mkdocs.yml` via `python3 scripts/generate_mkdocs_nav.py` to sync nav with mirrored TOCs; rerun `mkdocs build` to spot anchor/backlink warnings that need triage.
- **MkDocs scaffold (issue #2)**: Use `build/` as `docs_dir`, create a lightweight `index.md` landing page, and expose each collection via its primary landing Markdown (`AppleScriptX.md`, `ASLR_intro.md`, `index.md`, `Articles/Introduction.md`). Future enhancements: richer nav hierarchy, search tuning, theme customization.
- **Link normalization**: After regenerating Markdown, run `python3 scripts/normalize_markdown_links.py --markdown-dir build --pages-file …` so cross-collection links drop missing anchors and off-repo references point to `https://developer.apple.com/library/archive/`.

## Next Up
1. Execute issue #1 (mirror JXA release notes + WWDC resources) with tests, pipeline run, and monitoring update.
2. Draft the MkDocs/Material catalog structure (navigation + search expectations) before wiring up GitHub Pages.
3. Outline dataset packaging (plain text + JSONL export strategy) once the catalog scaffold exists.
