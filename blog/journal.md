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
