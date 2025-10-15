#!/usr/bin/env python3
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main(assets_dir: Path, markdown_dir: Path) -> None:
    copied = 0
    for asset_path in sorted(assets_dir.rglob("*")):
        if asset_path.is_file():
            relative = asset_path.relative_to(assets_dir)
            dest = markdown_dir / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(asset_path, dest)
            copied += 1
    print(f"Copied {copied} asset file(s) into {markdown_dir}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copy downloaded assets into the Markdown output directory.")
    parser.add_argument("--assets-dir", required=True, type=Path)
    parser.add_argument("--markdown-dir", required=True, type=Path)
    args = parser.parse_args()
    main(args.assets_dir, args.markdown_dir)
