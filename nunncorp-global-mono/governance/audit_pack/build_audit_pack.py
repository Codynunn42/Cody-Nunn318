#!/usr/bin/env python3
"""Build an audit evidence bundle and checksum manifest for Sentinel AI + Nunn Cloud releases/runs."""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

INPUT_FILES = {
    "policies": "policies.json",
    "approvals": "approvals.json",
    "incidents": "incidents.json",
    "monitoring": "monitoring.json",
    "overrides": "overrides.json",
    "decommissioning": "decommissioning.json",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(8192):
            digest.update(chunk)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def ensure_input_files(input_dir: Path) -> dict[str, Path]:
    files: dict[str, Path] = {}
    for key, filename in INPUT_FILES.items():
        file_path = input_dir / filename
        if not file_path.exists():
            raise FileNotFoundError(f"Missing required input file: {file_path}")
        files[key] = file_path
    return files


def build_bundle(release: str, run_id: str, files: dict[str, Path]) -> dict[str, Any]:
    loaded = {key: load_json(path) for key, path in files.items()}
    policy_hashes = [
        {
            "policy_id": item["policy_id"],
            "hash": item["policy_hash"],
            "effective_at": item["effective_at"],
        }
        for item in loaded["policies"]
    ]

    return {
        "bundle_schema": "nunn.audit.pack/v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "release": release,
        "run_id": run_id,
        "summary": {
            "approval_count": len(loaded["approvals"]),
            "incident_count": len(loaded["incidents"]),
            "override_count": len(loaded["overrides"]),
            "monitor_signal_count": len(loaded["monitoring"]),
        },
        "evidence": {
            "policies": policy_hashes,
            "approvals": loaded["approvals"],
            "incidents": loaded["incidents"],
            "monitoring": loaded["monitoring"],
            "overrides": loaded["overrides"],
            "decommissioning": loaded["decommissioning"],
        },
    }


def write_outputs(output_dir: Path, bundle: dict[str, Any], files: dict[str, Path]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    bundle_path = output_dir / "audit_bundle.json"
    with bundle_path.open("w", encoding="utf-8") as handle:
        json.dump(bundle, handle, indent=2)
        handle.write("\n")

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "inputs": {key: sha256_file(path) for key, path in files.items()},
        "outputs": {"audit_bundle.json": sha256_file(bundle_path)},
    }

    manifest_path = output_dir / "manifest.json"
    with manifest_path.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2)
        handle.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", required=True, help="Release identifier (for example 2026.04.07)")
    parser.add_argument("--run-id", required=True, help="High-impact run identifier")
    parser.add_argument("--input-dir", required=True, type=Path, help="Directory containing required JSON evidence files")
    parser.add_argument("--output-dir", required=True, type=Path, help="Directory to write bundle and manifest")

    args = parser.parse_args()

    files = ensure_input_files(args.input_dir)
    bundle = build_bundle(args.release, args.run_id, files)
    write_outputs(args.output_dir, bundle, files)


if __name__ == "__main__":
    main()
