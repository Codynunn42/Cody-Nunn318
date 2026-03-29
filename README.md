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

If your environment cannot run `pnpm` (for example, offline or restricted network), use the direct fallback:

```bash
pnpm run smoke:billing:direct
# or
bash ./packages/sentinel/scripts/smoke-billing.sh
```
