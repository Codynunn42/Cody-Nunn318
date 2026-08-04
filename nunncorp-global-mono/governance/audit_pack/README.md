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
  --input-dir sample_inputs \
  --output-dir out
```

## Outputs

- `audit_bundle.json`: signed-ready evidence package content.
- `manifest.json`: SHA-256 checksum manifest for input and output integrity.
