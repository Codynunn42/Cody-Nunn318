# Sentinel Closure Report Addendum

## Date
2026-08-21

## Scope
Step 4 execution: recompute ATP, MTTR, and escalation rate for the current high-impact run cycle.

## Source artifacts
- Manifest: governance/audit_pack/out/2026-08-21-high-impact-run-211/manifest.json
- Incident evidence: governance/audit_pack/sample_inputs/incidents.json
- Monitoring evidence: governance/audit_pack/sample_inputs/monitoring.json
- Risk model source: governance/risk/risk_register.yml

## Formula set
- RPN = impact x likelihood x detectability
- CPM = 1 + (days_since_last_evidence / 90)
- ATP = RPN x CPM

## Inputs used
- Evidence freshness baseline: 0 days (latest monitoring and incident timestamps are on 2026-08-21)
- CPM: 1 + (0/90) = 1.0000
- Incident MTTR: 45 minutes
- Escalation count: 0 of 1 incidents
- Escalation rate: 0%

## ATP recompute
| Risk ID | Capability | RPN | CPM | ATP |
| --- | --- | --- | --- | --- |
| R-001 | infrastructure_deploy | 30 | 1.0000 | 30.00 |
| R-002 | finance_payout | 45 | 1.0000 | 45.00 |
| R-003 | identity_admin | 40 | 1.0000 | 40.00 |
| R-004 | model_assisted_decisions | 48 | 1.0000 | 48.00 |

## Interpretation
- ATP values remain below Sev-1 threshold for this cycle.
- MTTR improved to 45 minutes in the refreshed sample evidence.
- Escalation rate remains 0%, indicating no escalation-trigger incidents in this sample window.

## Step 4 decision
Step 4 is complete for the current cycle; ATP, MTTR, and escalation rate have been recomputed and recorded.
