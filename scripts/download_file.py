#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from urllib.request import urlopen


def fetch(url: str) -> bytes:
    with urlopen(url) as response:
        return response.read()


def compute_sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def main(url: str, output: Path, expected_sha256: str | None = None) -> None:
    payload = fetch(url)
    digest = compute_sha256(payload)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(payload)
    print(f"Downloaded {len(payload)} bytes to {output} (sha256={digest})")
    if expected_sha256 and digest != expected_sha256.lower():
        raise SystemExit(
            f"Checksum mismatch for {output}: expected {expected_sha256}, got {digest}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download a single file and compute its sha256.")
    parser.add_argument("--url", required=True, help="Source URL to download.")
    parser.add_argument("--output", required=True, type=Path, help="Destination file path.")
    parser.add_argument(
        "--expected-sha256",
        help="Optional expected sha256 checksum (hex). Exit with error if mismatch.",
    )
    args = parser.parse_args()
    main(args.url, args.output, args.expected_sha256)
