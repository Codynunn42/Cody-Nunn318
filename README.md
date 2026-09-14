# Cody-Nunn318

E-commerce Store.

## AI Governance bootstrap

This repository now includes a governance implementation scaffold for **nunncorp-global-mono** under:

- `nunncorp-global-mono/`

It contains AIMS policy artifacts, risk workflows/registers, control mappings, an EU AI Act readiness checklist, and a working audit-pack generation script.

## Sentinel smoke billing workspace

This repository also includes a minimal `pnpm` workspace scaffold for running Sentinel smoke billing checks.

### Workspace layout

- `package.json` (root)
- `pnpm-workspace.yaml`
- `packages/sentinel/package.json`
- `packages/sentinel/scripts/smoke-billing.sh`

### Useful commands

From the repo root:

```bash
pnpm list --filter sentinel
pnpm --filter sentinel run smoke:billing
```

If your environment cannot run `pnpm` (for example, offline or restricted network), use the direct fallback:

```bash
pnpm run smoke:billing:direct
# or
bash ./packages/sentinel/scripts/smoke-billing.sh
```
