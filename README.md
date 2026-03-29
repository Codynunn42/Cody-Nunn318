# Cody-Nunn318

Minimal `pnpm` workspace scaffold for running Sentinel smoke billing checks.

## Workspace layout

- `package.json` (root)
- `pnpm-workspace.yaml`
- `packages/sentinel/package.json`
- `packages/sentinel/scripts/smoke-billing.sh`

## Useful commands

From the repo root:

```bash
pnpm list --filter sentinel
pnpm --filter sentinel run smoke:billing
```

Or via the root script alias:

```bash
pnpm run smoke:billing
```
