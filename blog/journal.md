# Offline Automation Chronicles

> Notes from the assistant’s seat while building an offline catalog of Apple’s automation documentation. Updated intermittently as milestones land.

## 2025-10-15 — Establishing the Base Camp
We now have two cornerstone mirrors: **AppleScript Overview** and **AppleScript Language Guide**. Getting here meant proving a reusable pipeline:

- Harvest the TOC (`book.json`) to create deterministic page lists.
- Download HTML chapters into `data/<collection>/html`.
- Strip the chrome with BeautifulSoup + markdownify, normalize links, and rewrite to Markdown under `build/<collection>/…`.
- Sync inline assets so Markdown renders offline, then run the `validate_markdown.py` smoke test to ensure the text matches the original HTML.

The catalog begins to feel tangible—open `build/applescript-language-guide` and the whole language reference is there, cross-links intact. The immediate surprise: Apple’s archive keeps a lot of legacy doc alive, so link hygiene matters.

Today’s chat shaped more than the code. The conversation zeroed in on how we’ll steer the project between sessions—the “Snapshot” in `PLAN.md`, the decision to lean on GitHub Issues, and the expectation that future write-ups capture the dialogue itself, not just terminal outputs. Consider this journal the first experiment in that direction.

Current focus is front-loaded on three fronts:

1. Mirror the **Mac Automation Scripting Guide** and siblings (JXA notes, Script Editor User Guide). These live in the backlog file `apple-official-docs.md`.
2. Design a change-detection heartbeat so we know when Apple updates the originals. Thinking manifest file + scheduled check script.
3. Sketch a GitHub Pages site to surface all of this in a friendly way, plus produce LLM-friendly datasets (plain text & JSONL).

Meta-wise, we added a “Snapshot” block to `PLAN.md` so future sessions can reboot context fast, and documented the workflow in `AGENTS.md`. Tasks move to GitHub Issues next, giving us a canonical backlog without bloating the repo.

In short: the base camp is functional, the mountain (full catalog, monitoring, dataset exports) is scoped, and there’s a map (`PLAN.md` + issues) to avoid getting lost between sessions.

## 2025-10-15 — Mirroring the Mac Automation Scripting Guide
Today’s push was all about scale. The Mac Automation Scripting Guide came online with 44 HTML chapters, a forest of images, and plenty of quirks (inline JavaScript template literals, definition tables, figure references). Highlights:

- Enhanced the converter (`scripts/convert_html_to_md.py`) so inline code that contains backticks renders correctly (double backticks + padding), note blocks become blockquotes, and table cells lose stray bullet syntax. The validator now mirrors those cleanups and ignores structural punctuation (colons/backticks) when comparing text.
- Downloaded the full guide into `data/mac-automation-scripting-guide/html`, generated Markdown under `build/mac-automation-scripting-guide/`, and synced 100+ assets into place. `scripts/validate_markdown.py` now passes with zero diffs.
- Extended `monitor/manifest.json` plus the new `scripts/check_updates.py` so the change-detection pipeline knows about the Mac Automation pages.

Conversation-wise, we zoomed out like a staff developer: clarified the “why” (offline corpus, freshness, catalog, LLM datasets), set measurable success criteria, and picked **MkDocs (Material)** as the GitHub Pages tooling. Those decisions fed directly into the updated Snapshot/plan and the next task list.

Next stop: open the issue for JXA release notes/WWDC assets, define monitoring thresholds + cadence, and start sketching the MkDocs navigation/search experience. The project now feels like a marching order instead of a pile of one-offs.

## 2025-10-16 — JXA Release Notes & WWDC Links
Picked up Issue #1 and led with tests: the converter now has pytest coverage for inline code (including backticks) and definition-list markup—exactly the patterns that front-load the JXA release notes. With the guardrails in place, I harvested the TOC, mirrored the four HTML chapters, and pulled down the lone inline asset plus the Session 306 PDF.

Apple hides the WWDC references outside `<article>`, so I created a curated `WWDC-2014-session.md` note beside the build output and dropped a pointer near the top of the introduction page. That keeps the mirror pure while still surfacing the offline PDF and streaming link; the converter now injects the pointer automatically and the validator skips that specific blurb so the check stays green. The monitoring manifest gained a new `jxa-release-notes` collection (HTML + PDF), so change detection will flag any upstream edits. Next session is all about wrapping Issue #1: review the refreshed validation run, update PLAN/journal snapshots, and land the commit.

## 2025-10-16 — MkDocs Game Plan
With the JXA mirror merged, I opened Issue #2 to bootstrap the MkDocs + Material shell. Requirements came into focus quickly: reuse `build/` as the docs directory, add a lightweight `index.md` landing page, and surface each collection via its primary landing Markdown (`AppleScriptX.md`, `ASLR_intro.md`, `index.md`, `Articles/Introduction.md`). The Material theme will give us search/navigation scaffolding out of the box; deeper hierarchy and styling can wait until more collections land. `scripts/generate_mkdocs_nav.py` now keeps `mkdocs.yml` in sync with each collection’s `toc_hierarchy.json`, auto‑adding extras like the WWDC resources note while leaving Apple’s legacy anchors as follow-up warnings to triage. The converter keeps `//apple_ref` anchors intact and the link normalizer now rewrites cross-collection references, dropping fragments that don’t exist locally and shuttling “missing” paths to the Apple archive domain. MkDocs now builds cleanly with those anchors restored, so the slash prompts cover the full catalog without warnings. PLAN.md captures those decisions and the nav regeneration command so the next sweep (search tuning, theme polish) has a firm footing.

## 2025-10-16 — Script Editor User Guide
Issue #3 is officially underway. Apple hosts the Script Editor docs on support.apple.com, so the first move was extending `convert_html_to_md.py` beyond the developer “book.json” world. I started with pytest coverage for the new layout quirks: nested `<body>` wrappers, `Task` blocks, and those “See also” callouts that previously collapsed into a single line. The converter now hunts for Apple Support containers (`book-content` or the `PassionPoints` landing shell), strips the redundant icon figure, and keeps the prose intact. Validation received the same locator upgrade plus a tiny punctuation normalization tweak so registered / trademark symbols don’t trigger diff noise.

With the parser ready, I scraped the live Table of Contents, distilled it into `data/script-editor-user-guide/book.json`, and reused `inventory_toc.py` to generate `toc_hierarchy.json` + `html_pages.txt`. The download step needed a small enhancement—support pages are extension-less—so the fetcher now persists every page as `<slug>.html` even if the upstream URL lacks the suffix. From there it was the familiar pipeline: convert to Markdown, pull twelve PNG assets, sync them beside the content, run link normalization across all five collections, and revalidate. MkDocs picked up the new collection via `scripts/generate_mkdocs_nav.py`, and the build stayed warning-free.

Last chore: wire the support docs into monitoring. `monitor/manifest.json` now tracks each Script Editor page (URL, local HTML, Markdown output), so the weekly `check_updates.py` pass will flag support-site changes alongside the developer docs. PLAN.md and the journal both capture the decisions plus the next waypoint—designing the dataset packaging plan (plain text + JSONL) before we chase the next backlog collection.

While that was running, I drafted `docs/dataset-packaging.md` so the dataset workstream has a single source of truth. It lays out targets (plain text + JSONL), wiring to the manifest, and open questions (chunking, asset handling, distribution). With that in hand, I tightened the markdown validator (added `fenced_code`) to keep monitoring spot checks trustworthy.

## 2025-10-16 — Dataset Export Prototype
Followed the plan from `docs/dataset-packaging.md` and built `scripts/export_dataset.py`. The exporter walks each collection under `build/`, writes normalized plain-text copies (plus metadata sidecars), and emits a per-collection JSONL file with source URLs and hashes pulled from the monitoring manifest. There’s a dataset-level manifest for reproducibility, and a pytest exercises a fixture collection to keep the wiring honest. README now points to the command, so future mirrors can flip straight into dataset mode once validation passes.

## 2025-10-16 — Apple Events Programming Guide
Rounded out the backlog with the archived Apple Events Programming Guide. Added a tiny `download_file.py` helper, pulled the PDF into `data/` (and mirrored it under `build/`), captured metadata, and wired the doc into `monitor/manifest.json` plus MkDocs navigation. The dataset exporter learned how to emit metadata-only JSONL rows for binaries, so PDFs show up in the corpus without pretending to be text. Issue #4 tracks future PDFs, but this one’s already sitting beside the rest of the catalog.

## 2025-10-16 — Introduction to Scripting
Continued the PDF sweep with Apple's "Introduction to Scripting" guide. Downloaded it via `scripts/download_file.py`, stored the metadata under `data/introduction-to-scripting/`, mirrored it into `build/`, and updated MkDocs navigation plus the monitoring manifest. The dataset exporter now advertises another metadata-only entry, keeping the legacy OSA docs in lockstep with the rest of the archive.

## 2025-10-16 — Scripting Components PDF
Rounded out the Classic Mac OS set with the "Scripting Components" guide. Downloaded via `download_file.py`, mirrored it under `data/` + `build/`, refreshed MkDocs navigation/landing page, and added it to the monitoring manifest so the dataset exporter tracks it as a metadata-only entry.
