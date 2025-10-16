#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Union

import yaml


CollectionNav = Union[str, Dict[str, Any]]

COLLECTIONS: List[Dict[str, str]] = [
    {"id": "applescript-overview", "title": "AppleScript Overview"},
    {"id": "applescript-language-guide", "title": "AppleScript Language Guide"},
    {"id": "mac-automation-scripting-guide", "title": "Mac Automation Scripting Guide"},
    {"id": "jxa-release-notes", "title": "JXA Release Notes"},
    {"id": "script-editor-user-guide", "title": "Script Editor User Guide"},
]


def load_toc(collection_id: str) -> List[Dict[str, Any]]:
    toc_path = Path("data") / collection_id / "toc_hierarchy.json"
    if not toc_path.exists():
        raise FileNotFoundError(f"Missing TOC file for {collection_id}: {toc_path}")
    return json.loads(toc_path.read_text(encoding="utf-8"))


def infer_title_from_markdown(md_path: Path) -> str:
    for raw in md_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("#"):
            return line.lstrip("#").strip()
    stem = md_path.stem.replace("_", " ")
    return stem.replace("-", " ").title()


def node_to_nav(
    node: Dict[str, Any],
    collection_id: str,
    seen: Set[str],
) -> Optional[CollectionNav]:
    title = node.get("title") or "Untitled"
    page = node.get("page")
    children = node.get("children") or []

    entry_path: Optional[str] = None
    if page:
        md_rel = Path(page).with_suffix(".md").as_posix()
        entry_path = f"{collection_id}/{md_rel}"
        if entry_path in seen:
            entry_path = None
        else:
            seen.add(entry_path)

    child_entries: List[CollectionNav] = []
    for child in children:
        nav_child = node_to_nav(child, collection_id, seen)
        if nav_child:
            child_entries.append(nav_child)

    if child_entries:
        if entry_path:
            child_entries.insert(0, {title: entry_path})
        if not child_entries:
            return None
        return {title: child_entries}

    if entry_path:
        return {title: entry_path}

    return None


def build_collection_nav(collection: Dict[str, str]) -> List[CollectionNav]:
    collection_id = collection["id"]
    seen: Set[str] = set()
    toc = load_toc(collection_id)
    nav_entries: List[CollectionNav] = []

    for node in toc:
        nav_entry = node_to_nav(node, collection_id, seen)
        if nav_entry:
            nav_entries.append(nav_entry)

    collection_dir = Path("build") / collection_id
    extras: List[CollectionNav] = []
    if collection_dir.exists():
        for md_path in sorted(collection_dir.rglob("*.md")):
            rel = md_path.relative_to(collection_dir).as_posix()
            nav_path = f"{collection_id}/{rel}"
            if nav_path in seen:
                continue
            seen.add(nav_path)
            extras.append({infer_title_from_markdown(md_path): nav_path})

    if extras:
        nav_entries.append({"Additional Resources": extras})

    return nav_entries


def generate_nav() -> List[CollectionNav]:
    nav: List[CollectionNav] = [{"Home": "index.md"}]
    for collection in COLLECTIONS:
        entries = build_collection_nav(collection)
        nav.append({collection["title"]: entries})
    return nav


def update_mkdocs_config(config_path: Path, nav: List[CollectionNav]) -> None:
    if not config_path.exists():
        raise FileNotFoundError(f"mkdocs config not found: {config_path}")
    config = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise ValueError("mkdocs configuration is not a mapping")
    config["nav"] = nav
    config_path.write_text(
        yaml.safe_dump(config, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def main(config_file: Path) -> None:
    nav = generate_nav()
    update_mkdocs_config(config_file, nav)
    print(f"Updated {config_file} with {sum(isinstance(item, dict) for item in nav)} top-level nav entries.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate MkDocs nav from mirrored collection TOCs.")
    parser.add_argument("--config", type=Path, default=Path("mkdocs.yml"))
    args = parser.parse_args()
    main(args.config)
