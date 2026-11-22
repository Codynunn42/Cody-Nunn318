# Support Triage and Governance Review

## Purpose
This runbook governs how the Sentinel AI governance team triages operational issues, policy failures, and control exceptions for the SSAI service and related AI capabilities.

## Operating cadence
Use this on the current review cycle based on the PDCA cadence in `governance/aims/pdca-calendar.yml`.

- Plan: refresh risk context and treatment priorities
- Do: confirm controls and evidence remain in force
- Check: review support queue, incidents, overrides, and KRI trends
- Act: remediate, escalate, or accept residual risk

## Triage workflow

### 1) Intake
Capture:
- capability or service affected
- reporter and business impact
- date/time of first detection
- observed behavior and supporting screenshots or logs
- whether the issue touches a controlled action or a public endpoint

### 2) Severity classification
- Sev-1: impacts security, identity, financial action, public API integrity, or user safety
- Sev-2: partial outage, degraded control behavior, repeated override, or suspicious anomaly pattern
- Sev-3: minor operational issue, documentation gap, or limited workflow friction

### 3) Ownership assignment
- Infrastructure or runtime changes: Security Engineering Lead + Sentinel Product Owner
- Identity or privileged actions: Security Engineering Lead
- Finance or payout actions: Chief AI Governance Officer + Sentinel Product Owner
- Model-assisted decisions: Sentinel Product Owner + designated human reviewer

### 4) Evidence collection
Collect and attach:
- affected control ID
- relevant approval or override IDs
- command or API traces
- public endpoint health check results
- runtime contract response
- rollback evidence when applicable

### 5) Decision pathway
- Resolve and close if issue is fully addressed with evidence
- Escalate to Chief AI Governance Officer for residual risk or policy exception discussion
- Trigger rollback or fail-safe if a high-impact control is breached
- Open a board-level item if the issue affects residual risk acceptance or strategic posture

## Current operational check for SSAI
Status as of the current review:
- Public endpoint health is returning the expected observed-health schema through Cloudflare
- Local runtime validation of 3110 is returning the expected contract
- 3100 remains available as rollback target while the public route is validated

## KRI/KPI check list
- change_failure_rate
- rollback_success_rate
- privileged_action_review_sla
- anomaly_alert_volume
- manual_override_rate
- unauthorized_execution_attempts

## Quantitative triage scorecard
Use this model for all daily support triage decisions so escalations are evidence-based.

### Model
- Base risk priority number (RPN): `impact x likelihood x detectability`
- Cadence pressure multiplier (CPM): `1 + (days_since_last_evidence / 90)`
- Adjusted triage priority (ATP): `RPN x CPM`

### Severity-to-priority thresholds
- ATP >= 100: Sev-1 handling, immediate escalation, fail-safe readiness check
- ATP 70-99: Sev-2 handling, same-day remediation plan and owner assignment
- ATP 40-69: Sev-3 handling, next-checkpoint remediation and trend watch
- ATP < 40: monitor only, no immediate remediation unless trend worsens

### Daily support triage worksheet
Capture one row per active risk item or support case.

| Date | Risk/Case ID | Impact | Likelihood | Detectability | RPN | Days stale | CPM | ATP | Assigned severity | Decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | R-XXX / INC-XXX | 1-5 | 1-5 | 1-5 | n | n | n.nn | n.nn | Sev-1/2/3 | Resolve / Escalate / Monitor |

### Required quantitative evidence for closure
- `opened_at`, `closed_at`, and elapsed minutes for every incident
- control ID and policy ID for every high-impact case
- explicit escalation flag and approver for policy exception paths
- before/after ATP when a remediation action is applied

## Support escalation gate
Escalate immediately if any of the following occur:
- unauthorized or unapproved high-impact execution
- identity or MFA validation failure
- anomaly or payout override outside policy threshold
- public API contract deviates from observed-health or sovereignty schema
- repeated incident pattern across releases or environments

## Triage template

### Support case record
- Case ID:
- Capability:
- Severity:
- Date opened:
- Reporter:
- Impact summary:
- Control affected:
- Immediate action taken:
- Owner:
- Resolution status:
- Board notification required: Yes / No
