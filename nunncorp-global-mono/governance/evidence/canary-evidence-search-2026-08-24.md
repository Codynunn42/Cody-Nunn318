# Canary Evidence Search Report

## Search date
2026-08-24

## Search target

Historical canary reported as completed at 2026-08-20 10:00 PM PDT, equivalent to 2026-08-21T05:00:00Z.

## Required records

1. Raw canary execution log with start and end timestamps.
2. Authorization or approval record explicitly linked to the canary run.
3. Runtime health check captured during or immediately after canary completion.

## Search results

| Required record | Result | Evidence assessment |
| --- | --- | --- |
| Raw execution log | **NOT FOUND** | The repository contains the operator attestation, but no raw canary log with start/end timestamps. |
| Run-linked authorization | **NOT FOUND** | Approval records cover `sentinel-run-208` through `sentinel-run-210`; no approval is linked to the reported canary event. `OVR-210` is timestamped 2026-08-21T10:08:00Z and is retained as unrelated contextual evidence. |
| Contemporaneous health evidence | **NOT FOUND** | Monitoring records end at 2026-08-21T10:10:00Z, contain no canary run identifier, and do not capture a health result during or immediately after the reported event. |

## Records located

- `governance/evidence/canary-attestation-2026-08-20-2200-local.md`: operator attestation only; explicitly records the provenance gap.
- `governance/evidence/d1-window-reconciliation-2026-08-20.md`: reconciles a monitoring window, but does not document the reported canary run.
- `governance/audit_pack/sample_inputs/approvals.json`: contains approvals for runs 208, 209, and 210; no canary-linked approval.
- `governance/audit_pack/sample_inputs/monitoring.json`: contains monitoring observations through 2026-08-21T10:10:00Z; no canary-linked health result.
- `governance/audit_pack/sample_inputs/overrides.json`: contains `OVR-210`; it is not time-correlated to the reported canary and must not be recast as authorization.

## Disposition

The canary provenance gap remains **OPEN**. No evidence supports closing the attestation or changing the reported event time. The current result is a formal source-unavailable finding, not a finding that the canary failed.

The issue remains separate from the daily and weekly ATP escalation gates. It must be resolved with the three required source records or accepted through a corrected operator attestation and accountable review before the August month-end closeout is signed off.

## Supplemental evidence supplied 2026-08-24

The pasted Docker and `curl` output provides useful corroborating runtime context:

- Docker healthcheck output shows successful `node scripts/healthcheck.js` probes on 2026-08-17, including `Health check passed: http://localhost:80/health`.
- Docker service checks on 2026-08-17 report PostgreSQL accepting connections and Redis returning `PONG`.
- SSAI `/health`, `/sovereignty`, and `/runtime` responses were captured on 2026-08-19 at approximately 22:44 UTC. They show the local runtime and evidence store passing, `sentinel_required: false`, and the Sentinel outage test still `pending`.
- One Docker record reports `Status: exited` with `ExitCode: 137`; the surrounding health output is historical container status, not a canary-linked execution record.

Classification: **CORROBORATING HISTORICAL CONTEXT**, not direct closure evidence. The supplied timestamps precede the reported canary completion at 2026-08-21T05:00:00Z, and the output does not identify a canary run ID, provide the canary start/end log, link an authorization to that run, or capture health during or immediately after the event. The `sentinel_required: false` and `sentinel_ai_outage_test: pending` fields also do not prove that the reported canary was executed.

The original evidence classification is unchanged: raw execution log, run-linked authorization, and contemporaneous health evidence remain **NOT FOUND** for the reported canary.

## Owners and next action

- Evidence owner: Sentinel Product Owner.
- Reviewer: Chief AI Governance Officer.
- Next action: obtain the missing records, or issue a corrected operator attestation explaining why the records are unavailable and obtain accountable acceptance.

## Search scope

- `governance/evidence/**`
- `governance/audit_pack/sample_inputs/**`
- governance cadence, closure, executive, and support-triage records
- exact event-time, canary, run ID, authorization, approval, and health terms