#!/usr/bin/env python3
"""Verify an audit pack manifest against its preserved source inputs and output."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8192):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def verify(manifest_path: Path) -> list[str]:
    manifest = load_json(manifest_path)
    output_dir = manifest_path.parent
    input_dir = output_dir / manifest.get("source_inputs", {}).get(
        "directory", "source_inputs"
    )
    input_names = {
        "policies": "policies.json",
        "approvals": "approvals.json",
        "incidents": "incidents.json",
        "monitoring": "monitoring.json",
        "overrides": "overrides.json",
        "decommissioning": "decommissioning.json",
    }
    failures = []

    for key, expected in manifest.get("inputs", {}).items():
        path = input_dir / input_names[key]
        if not path.exists():
            failures.append(f"missing preserved source input: {path}")
            continue
        actual = sha256_file(path)
        if actual != expected:
            failures.append(
                f"input hash mismatch: {key}: expected {expected}, got {actual}"
            )

    for name, expected in manifest.get("outputs", {}).items():
        path = output_dir / name
        if not path.exists():
            failures.append(f"missing output: {path}")
            continue
        actual = sha256_file(path)
        if actual != expected:
            failures.append(
                f"output hash mismatch: {name}: expected {expected}, got {actual}"
            )

    return failures


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="Path to manifest.json")
    args = parser.parse_args()

    failures = verify(args.manifest)
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)
    print(f"PASS: {args.manifest}")


if __name__ == "__main__":
    main()
