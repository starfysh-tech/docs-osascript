# Apple Automation Archive

Offline-ready mirrors of Apple's automation documentation, organised by collection and kept in Markdown for easy reuse.

## Collections

- [AppleScript Overview](https://developer.apple.com/library/archive/applescript-overview/AppleScriptX.md) — glossary-friendly introduction to scripting concepts.
- [AppleScript Language Guide](https://developer.apple.com/library/archive/applescript-language-guide/introduction/ASLR_intro.md) — the canonical language reference.
- [Mac Automation Scripting Guide](https://developer.apple.com/library/archive/mac-automation-scripting-guide/index.md) — practical automation workflows and recipes.
- [JavaScript for Automation (JXA) Release Notes](https://developer.apple.com/library/archive/jxa-release-notes/Articles/Introduction.md) — change history and WWDC resources.

## About This Catalog

- Source inputs live under `data/<collection>/` (read-only mirrors of Apple's originals).
- Markdown outputs and colocated assets sit in `build/<collection>/`.
- Run `mkdocs serve` for local previews or `mkdocs build` to generate the static site under `site/` (ignored from version control).
