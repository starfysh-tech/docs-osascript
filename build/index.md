# Apple Automation Archive

Offline-ready mirrors of Apple's automation documentation, organised by collection, and kept in Markdown for easy reuse.

---

## How to Use

### Readers

- Browse the sidebar to explore its chapters.
- Use the sticky table of contents on the right to jump around within the current page.
- Need a full offline bundle? Grab the latest dataset snapshot from the [releases page](https://github.com/starfysh-tech/docs-osascript/releases) (the header button links there); each drop includes every Markdown file plus JSONL exports.

## Core Collections

- [AppleScript Overview](https://developer.apple.com/library/archive/applescript-overview/AppleScriptX.md) — glossary-friendly introduction to scripting concepts.
- [AppleScript Language Guide](https://developer.apple.com/library/archive/applescript-language-guide/introduction/ASLR_intro.md) — the canonical language reference.
- [Mac Automation Scripting Guide](https://developer.apple.com/library/archive/mac-automation-scripting-guide/index.md) — practical automation workflows and recipes.
- [JavaScript for Automation (JXA) Release Notes](https://developer.apple.com/library/archive/jxa-release-notes/Articles/Introduction.md) — change history and WWDC resources including WWDC 2014 Session 306.
- [Script Editor User Guide](https://support.apple.com/guide/script-editor/welcome/mac.md) — Apple Support documentation for Script Editor.

## Archived References

- [Apple Events Programming Guide (PDF)](https://developer.apple.com/library/archive/apple-events-programming-guide/apple-events-programming-guide.pdf) — historical Apple Events documentation.
- [AppleScript Scripting Additions Guide (PDF)](https://developer.apple.com/library/archive/applescript-scripting-additions-guide/applescript-scripting-additions-guide.pdf) — comprehensive Standard Additions reference.
- [Introduction to Scripting (PDF)](https://developer.apple.com/library/archive/introduction-to-scripting/intro-to-scripting.pdf) — Classic Mac OS introduction to OSA scripting components.
- [Scripting Components (PDF)](https://developer.apple.com/library/archive/scripting-components/scripting-components.pdf) — details of Classic Mac OS scripting component architecture.

> Looking for more? Review `apple-official-docs.md` in the repository for the remaining backlog of Apple automation resources queued for mirroring.

### Coding agents & CLIs

- Search the Markdown corpus directly:

  ```sh
  rg "do shell script" build/
  ```

  Each result is a path under `build/` that you can open or parse on demand.

- Prefer structured data? Scan the JSONL datasets under `dataset/jsonl/`:

  ```python
  python3 - <<'PY'
  import json, pathlib
  term = "do shell script"
  for jsonl in pathlib.Path("dataset/jsonl").glob("*.jsonl"):
      with jsonl.open(encoding="utf-8") as fh:
          for line in fh:
              obj = json.loads(line)
              if term in (obj.get("body") or ""):
                  print(f"{jsonl.stem}: {obj['path']}")
                  raise SystemExit
  PY
  ```

- Need metadata or hashes? See `dataset/manifest.json`.

## About This Catalog

- Source inputs live under `data/<collection>/` (read-only mirrors of Apple's originals).
- Markdown outputs and colocated assets sit in `build/<collection>/`.
- Run `mkdocs serve` for local previews or `mkdocs build` to generate the static site under `site/` (ignored from version control).
