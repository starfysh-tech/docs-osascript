# Dataset Packaging Plan

## Purpose
Outline how to transform the mirrored Apple automation docs under `build/` into plain text and JSONL datasets suitable for downstream analysis and LLM fine-tuning.

## Source Inputs
- Primary content: Markdown files within `build/<collection>/`.
- Metadata: collection TOCs (`data/<collection>/toc_hierarchy.json`), monitoring manifest (`monitor/manifest.json`), and collection-specific context (e.g., WWDC note files).
- Optional: assets (images/PDFs) stay co-located but are not part of text exports.

## Target Outputs
1. **Plain Text Corpus**
- One `.txt` per Markdown file mirroring the relative path (`build/<collection>/Foo/Bar.md` → `dataset/plain/<collection>/Foo/Bar.txt`).
- Normalization: strip Markdown formatting while preserving headings, lists, and inline code markers where meaningful.
- Metadata sidecar (YAML or JSON) per file capturing collection ID, relative source path, original URL, and sha256 from `monitor/manifest.json` when available.

2. **JSONL Corpus**
- Records keyed by `{"collection": ..., "path": ..., "title": ..., "body": ...}`.
- `body` retains Markdown (or lightly cleaned text) to maintain structure for downstream chunking.
- Optional enrichment: section hierarchy from `toc_hierarchy.json`, anchor list, and detected code blocks.
- Binary artifacts (PDFs, ZIPs, etc.) appear as metadata-only rows with `"body": null` and `"binary": true` so downstream consumers can decide how to handle them. Their checksums/URLs are still captured in the record for integrity tracking.

## Processing Steps
1. **Discovery**
   - Enumerate Markdown sources via `build/`.
   - Map each file back to monitoring metadata using normalized paths.
2. **Normalization**
   - Use a shared utility (e.g., `scripts/export_dataset.py`) to:
     - Load Markdown, convert to plain text via `markdown` + BeautifulSoup pipeline (reuse `scripts/validate_markdown.py` canonicalization pieces where possible).
     - Preserve headings, list indentation, code fences.
3. **Serialization**
   - Write plain text files alongside JSONL entries in a central `dataset/` directory.
   - Include a manifest (`dataset/manifest.json`) summarizing counts, generation timestamp, and command used.
4. **Validation**
   - Diff spot checks between Markdown and text export to ensure content parity.
   - Schema validation for JSONL (simple schema file or pydantic model).

## Automation Hooks
- New script: `scripts/export_dataset.py` with CLI flags:
  - `--collections` (optional subset)
  - `--plain-dir`, `--jsonl-path`
  - `--metadata monitor/manifest.json`
- Integrate into workflow after link normalization and validation.
- Treat `dataset/` as build output: run the exporter on demand, then bundle the results (zip/tar + manifest) for release distribution rather than committing the directory to git.

## Open Questions
- Should JSONL records be single-page (`body`=whole doc) or chunked for LLM training (e.g., 1k token segments)?
- How to handle tables/inline images in plain text exports (text-only vs. structured representation)?
- Do we snapshot the dataset output in Git, or expect consumers to generate on demand?

## Next Actions
1. Design the `export_dataset.py` interface (arguments, reuse of existing utilities).
2. Prototype on one collection (e.g., `jxa-release-notes`) to validate format and metadata joins.
3. Document regeneration steps in `README.md` once the tooling is in place.
