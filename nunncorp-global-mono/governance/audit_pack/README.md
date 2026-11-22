# Audit Pack Pipeline

Build an evidence bundle per release and per high-impact run.

## Inputs

The input directory must contain these files:

- `policies.json`
- `approvals.json`
- `incidents.json`
- `monitoring.json`
- `overrides.json`
- `decommissioning.json`

## Run

```bash
python3 build_audit_pack.py \
  --release 2026.04.07 \
  --run-id sentinel-run-001 \
  --require-run-approval \
  --input-dir sample_inputs \
  --output-dir out
```

## Outputs

- `audit_bundle.json`: signed-ready evidence package content.
- `manifest.json`: SHA-256 checksum manifest for input and output integrity.
- `source_inputs/`: immutable copies of the exact inputs referenced by the manifest.

## Verify

```bash
python3 verify_audit_manifest.py out/manifest.json
```

Use `--require-run-approval` for every high-impact run. The command fails unless
at least one approval record has a `run_id` exactly matching the requested run.
