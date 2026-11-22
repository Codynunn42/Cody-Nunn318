# Board AI Risk Update (One Page)

## Date
2026-08-21

## Committee
Board Risk Committee

## Executive summary
The previously identified governance bottlenecks from the 2026-08-20 escalation brief have been addressed through execution passes and metric refresh. Runtime posture remains stable, integrity evidence is manifest-backed, and the active track has moved from remediation to cadence maintenance.

## Quantitative triage model
- RPN = impact x likelihood x detectability
- CPM = 1 + (days_since_last_evidence / 90)
- ATP = RPN x CPM

## Current quantitative posture
- Evidence freshness baseline: 0 days for current sample cycle
- MTTR: 45 minutes
- Escalation rate: 0%
- ATP values:
  - R-001: 30.00
  - R-002: 45.00
  - R-003: 40.00
  - R-004: 48.00

## Prior bottleneck status (from 2026-08-20 brief)
1. Evidence feed stale: CLEARED
2. D1 monitoring/manifest gate unresolved: CLEARED
3. D2-D4 unverified backlog: CLEARED to approved conditional/evidence-backed state
4. D1 owner/approver overlap: CLEARED with separation-of-duties guardrail in template generation
5. Missing support latency fields: CLEARED in incident sample schema and reflected in MTTR/escalation metrics

## Immediate corrective actions and gates status
1. Refresh 7-day extracts: COMPLETE
2. Reconcile D1 window + rerun manifest: COMPLETE
3. D2-D4 artifact + verifier output coverage: COMPLETE
4. Independent D1 approver requirement: COMPLETE
5. Standardized incident fields for MTTR/escalation: COMPLETE

## Decision requests (current state)
1. Continue strict evidence-first posture: CONFIRMED
2. Maintain independent approver requirement for D1 closure: CONFIRMED
3. Retain escalation threshold ATP >= 100 for Sev-1 board-visible handling: CONFIRMED

## 72-hour checkpoint disposition
- T+24h checkpoint (freshness + ATP recompute): MET
- T+48h checkpoint (D1 gate pass/fail documented): MET
- T+72h checkpoint (D2-D4 transitioned with accountable sign-off): MET

## Recommendation
Maintain HOLD for runtime authorization and shift governance focus to scheduled evidence review. Escalate on ATP >= 100, D1 integrity regression, unauthorized high-impact execution, identity/MFA failure, out-of-policy anomaly or payout override, public API contract deviation, or a repeated incident pattern.

## Authoritative references
- governance/closure-report-2026-08-20-execution-pass-2.md
- governance/closure-report-2026-08-21-step4-metrics.md
- governance/executive-closeout-2026-08-20.md
- governance/audit_pack/out/2026-08-21-high-impact-run-211/manifest.json
- governance/next-steps-template.md
