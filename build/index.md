# Apple Automation Archive

Offline-ready mirrors of Apple's automation documentation, organised by collection and kept in Markdown for easy reuse.

## Core Collections

- [AppleScript Overview](applescript-overview/AppleScriptX.md) — glossary-friendly introduction to scripting concepts.
- [AppleScript Language Guide](applescript-language-guide/introduction/ASLR_intro.md) — the canonical language reference.
- [Mac Automation Scripting Guide](mac-automation-scripting-guide/index.md) — practical automation workflows and recipes.
- [JavaScript for Automation (JXA) Release Notes](jxa-release-notes/Articles/Introduction.md) — change history and WWDC resources including WWDC 2014 Session 306.
- [Script Editor User Guide](script-editor-user-guide/welcome/mac.md) — Apple Support documentation for Script Editor.

## Archived References

- [Apple Events Programming Guide (PDF)](apple-events-programming-guide/apple-events-programming-guide.pdf) — historical Apple Events documentation.
- [AppleScript Scripting Additions Guide (PDF)](applescript-scripting-additions-guide/applescript-scripting-additions-guide.pdf) — comprehensive Standard Additions reference.
- [Introduction to Scripting (PDF)](introduction-to-scripting/intro-to-scripting.pdf) — Classic Mac OS introduction to OSA scripting components.

> Looking for more? Review `apple-official-docs.md` in the repository for the remaining backlog of Apple automation resources queued for mirroring.

## About This Catalog

- Source inputs live under `data/<collection>/` (read-only mirrors of Apple's originals).
- Markdown outputs and colocated assets sit in `build/<collection>/`.
- Run `mkdocs serve` for local previews or `mkdocs build` to generate the static site under `site/` (ignored from version control).
