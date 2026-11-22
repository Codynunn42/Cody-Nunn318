# SentinelOS Restore and Startup Order

## Date
2026-08-26

## Purpose
Define a reversible startup sequence for resource-heavy SentinelOS components and preserve a separate restore point for each layer before operational changes.

## Restore-point policy
A restore point must identify its source, timestamp, scope, and verification state. A Git tag is a code restore point; it is not a Docker image, container, or database snapshot.

| Layer | Restore point | Required preservation | Verification |
| --- | --- | --- | --- |
| Repository code and governance | `sovereignty-promotion-ready-2026-08-19` | Git tag and commit reference | `git show sovereignty-promotion-ready-2026-08-19` |
| Evidence package | Current D1 reconciliation directory and governance records | Preserve separately before checkout or reset | File inventory and hash verification |
| Persistent data | `postgres_data`, `redis_data` volumes | Confirm volume names and capture an approved backup before destructive work | Volume inspection and application health |
| Docker configuration | `docker-compose.yml`, `.env`, image references | Preserve configuration; do not expose secrets in logs | Compose config validation |
| Docking state | Docking manifest and approval event | Preserve manifest, approval, and resulting event | `npm run check:docking` |
| Runtime state | Sentinel API and SSAI health/readiness outputs | Capture endpoint responses after startup | Healthcheck and runtime probes |

## Required startup order

### 1. System layer
Start foundational infrastructure first:

- Docker Desktop and the active `desktop-linux` context
- PostgreSQL (`sentinel-postgres`)
- Redis (`sentinel-redis`)
- Confirm both dependency health checks pass before continuing

Do not start application or docking operations while either dependency is unhealthy.

### 2. Docking layer
After system health is confirmed:

- load the approved docking manifest
- evaluate docking policy and required scopes
- obtain human approval for high-risk docking actions
- record the docking request and decision
- keep docking explicit and invoked; it is not an ambient runtime dependency

A denied or incomplete docking check is a stop condition, not a reason to bypass authorization.

### 3. Runtime layer
Only after system and docking gates pass:

- start `sentinel-api`
- verify its container healthcheck
- start or connect the SSAI runtime
- verify `/health`, `/sovereignty`, and `/runtime`
- record request IDs, timestamps, and results in the evidence package

Runtime readiness must not be inferred from Docker process state alone.

## Rollback order
If a startup gate fails, stop at the failed layer and restore only that layer first:

1. Runtime: stop or revert the application layer; preserve logs and receipts.
2. Docking: revoke or close the docking transition through the approved control path.
3. System: restore the affected service or persistent data from its separately verified backup.
4. Repository: return to the approved Git restore point only after untracked evidence is preserved.

Do not delete Docker volumes, reset Git state, or rerun a canary as a substitute for missing evidence without explicit human authorization.

## Closure gates
- [ ] Docker daemon responds on the active context.
- [ ] PostgreSQL is healthy.
- [ ] Redis is healthy.
- [ ] Docking manifest and approval are present.
- [ ] `npm run check:docking` passes.
- [ ] `sentinel-api` healthcheck passes.
- [ ] SSAI health and sovereignty responses are captured.
- [ ] Restore-point identifiers and timestamps are recorded.
- [ ] No D1 or promotion status changes are made without authoritative evidence and human authorization.

## Current evidence posture
D1 remains conditional / reconciliation in progress. This runbook changes no runtime state and does not close the canary provenance or SIEM continuity gaps.
