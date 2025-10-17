# Manual Follow-ups

This note collects the outstanding manual cleanup items and open decisions
referenced throughout the project. Check these off (and update this list)
as each item is resolved.

## Asset Handling
- **WWDC video assets:** Decide whether we link out to developer.apple.com or
  host local copies. Capture the final approach in the asset workflow docs.
- **Large binary storage:** Confirm if big binaries (WWDC videos, high-res PDFs)
  should live alongside each collection or in a shared archive directory.

## Documentation Exports
- **Man-page captures:** Choose the canonical export format (plain text vs.
  Markdown) for man-page style references before we mirror them.
- **Non-HTML references:** When we encounter linked resources outside the Apple
  automation domain, document whether we mirror them or link out.

## Catalog & Publishing
- **GitHub Pages deployment:** Finalise the publishing workflow (branch or
  GitHub Actions) and document the steps once the site goes live.
- **Dataset releases:** Continue using the release checklist in
  `docs/dataset-packaging.md` each time we publish a new dataset snapshot.

## QA Checks
- **Table-heavy diffs:** When new collections introduce complex tables or other
  HTML structures, perform manual spot checks after conversion and note any
  acceptable deviations.

## Pre-release Checklist
- [ ] Scripted final validation (mirror comparisons, monitoring, site rebuild, link checks).
- [ ] Optional Playwright smoke tests if scripted validation flags issues or for extra assurance.
