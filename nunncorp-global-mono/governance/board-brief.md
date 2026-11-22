# Board AI Risk and Control Brief

## Date
2026-08-27

## Committee
Board Risk Committee

## Scope
This brief summarizes the AI governance posture, current control effectiveness, support triage outcomes, and residual risk status for the Sentinel operating model.

## Executive summary
The organization’s AI governance foundation remains operational and aligned to the approved management system model. Historical SSAI observations preserve a rollback option and support continued technical review, but do not authorize continued operation, release, or sovereign-runtime designation. The current disposition remains HOLD.

## Morning executive block (2026-08-27)
### Status
- Genesis Open Models: submitted; deadline met.
- DOE OSBP meeting: rescheduled for Friday, August 28, 1:30–1:45 PM.
- Capability sheet: submitted and acceptable as filed; minor cleanup items noted for future versions.
- DOE opportunity review: active; filtering now by actual work fit, then set-aside, then vehicle/access.
- D1: remains Conditional / reconciliation in progress.
- D1 preservation action: reconciliation artifacts should be hashed/preserved before any repo cleanup or reset.

### Approvals
I recommend we keep these in force today:
- Approve: no extra DOE outreach before tomorrow’s meeting.
- Approve: continue screening DOE opportunities, but only where the description fits Nunn Cloud’s actual technical/governance work.
- Approve: preserve D1 artifacts before any repository maintenance.
- Approve: use today to tighten Friday’s meeting readiness rather than expand scope.

### Bottlenecks
The main bottlenecks are now very clear:
- DOE contracting access: some forecast rows look attractive but are blocked by vehicle structure, OEM/reseller requirements, or special set-asides.
- D1: no further broad searching is justified without a new authoritative evidence source.
- Friday meeting: only 15 minutes, so message discipline matters more than more material.

### Today’s highest-value actions
1. Preserve/hash D1 reconciliation artifacts.
2. Finalize the one-page Friday meeting guide.
3. Prepare one clean answer for “What problem does Nunn Cloud solve for DOE?”
4. Continue DOE forecast screening only for strong-fit rows.
5. Have Genesis confirmation and capability statement ready in case Kent asks what you’ve already submitted.

Recommended focus order: D1 preservation → Friday meeting prep → selective DOE opportunity screening.

## Current operating posture
The key operational evidence reviewed this cycle indicates:
- public endpoint availability is stable
- the observed-health schema remains intact
- the validated runtime path is serving expected governance and runtime checks
- rollback path remains in place if a support issue or service regression is detected

## Completed support triage items
- runtime validation completed
- evidence-store validation completed
- public endpoint validation completed
- governance packet completed
- rollback readiness confirmed

## Risk register focus
| Risk ID | Capability | Residual risk | Status |
| --- | --- | --- | --- |
| R-001 | infrastructure_deploy | medium | monitored |
| R-002 | finance_payout | medium | monitored |
| R-003 | identity_admin | medium_high | monitored |
| R-004 | model_assisted_decisions | medium | monitored |

## Control effectiveness
The underlying control model is designed to enforce high-impact policy checks, including:
- dual approval for high-impact execution
- identity and MFA gating for privileged actions
- anomaly and override controls for financial actions
- human confirmation and lineage checks for model-assisted decisions

## Governance cadence
The organization is operating under the PDCA cadence defined in the governance baseline:
- Plan: quarterly
- Do: continuous
- Check: monthly
- Act: quarterly

## Board-ready checklist (2026-08-24)
This checklist is the minimum board-readiness gate for the current cycle.

### Evidence envelope
- [ ] Governance package complete: brief, support triage, risk review, cadence summary, and owner assignments are present.
- [ ] Evidence freshness verified and within the policy limit.
- [ ] Manifest verification completed and results recorded as PASS.
- [ ] Required input sets for the current audit pack are present and traceable.

### Control and threshold review
- [ ] ATP reviewed and below the escalatory threshold; current maximum ATP remains below 100.
- [ ] No D1 regression or material control breach recorded in the reviewed evidence.
- [ ] No unresolved override, identity fail, or out-of-policy execution has been accepted without a governing decision.

### Open exception handling
- [ ] Canaries and shutdown-related provenance are distinguished from routine operational evidence.
- [ ] Any open canary-provenance exception is recorded as an evidence gap, not a failed control result.
- [ ] Ownership and escalation path for the exception are assigned and retained in the governance record.

### Decision readiness
- [ ] Executive Desk acceptance is documented for the current review cycle.
- [ ] Residual-risk posture is unchanged and accepted by the appropriate governance owner.
- [ ] The board is presented with a PASS-with-exception posture only if the exception is clearly labeled as closed-open evidence gap rather than a failed control.

## Decisions required
- Confirm continued residual-risk acceptance posture for the current operating state
- Review whether any support item requires board-level escalation
- Approve or defer any remediation steps linked to the current risk review cycle

## Recommendation
Maintain HOLD for runtime release and continue routine monthly control testing and quarterly management review. Escalate ATP >= 100, D1 integrity regression, unauthorized high-impact execution, identity/MFA failure, out-of-policy anomaly or payout override, public API contract deviation, or a repeated incident pattern.
