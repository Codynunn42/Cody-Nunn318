# ATP Follow-up Review

## Review date
2026-08-23

## Review scope

This review answers the four follow-up questions from the prior ATP assessment:

1. Are the current R-001 through R-004 scores still accurate?
2. Were any new risks introduced since the last register update?
3. Is evidence freshness within the operating cadence?
4. Does the ATP formula require review after the available operational data?

## Findings

| Question | Evidence reviewed | Disposition |
| --- | --- | --- |
| 1. Score accuracy | `governance/risk/risk_register.yml`; active controls and residual-risk acceptance dated 2026-04-07 | **PASS for continued use.** The four high-impact risk statements, impact/likelihood/detectability inputs, mapped controls, monitoring indicators, and accountable acceptance remain internally consistent. Re-score is not required by this review. |
| 2. New risks | Latest audit bundle for `sentinel-run-213`; one resolved medium incident, one recorded override, three healthy monitoring signals, and no new risk-register item | **No new risk recorded.** This means no new risk is evidenced in the reviewed records; it does not establish that risk is zero. The open canary-provenance exception remains separate and unresolved. |
| 3. Evidence freshness | Audit bundle generated 2026-08-23; latest operational evidence observed 2026-08-21; daily cadence rule blocks readiness after seven days | **PASS.** Evidence age is approximately 2.29 days and remains within the seven-day operating window. Manifest integrity is verified for `sentinel-run-213`. |
| 4. Formula review | Risk workflow scoring of impact x likelihood x detectability; ATP sensitivity check across 0, 1, 3, 7, 14, and 30 days | **Retain current formula.** The tested maximum ATP is 64.00 at 30 days, below the 100 escalation threshold. The formula should be revisited after additional operational data or a material change to risk scoring, evidence cadence, or escalation policy. |

## ATP decision

The current risk posture remains:

> No ATP-triggered escalation. Continue normal governance cadence.

This is a threshold decision, not a claim that residual risk is zero. The canary provenance exception remains an evidence-completeness issue and does not change this ATP disposition unless it produces evidence of a control failure, D1 regression, or threshold breach.

## Evidence references

- `governance/risk/risk_register.yml`
- `governance/risk/risk_workflow.md`
- `governance/audit_pack/out/2026-08-23-daily-cadence/audit_bundle.json`
- `governance/audit_pack/out/2026-08-23-daily-cadence/manifest.json`
- `governance/cadence/daily-cadence-2026-08.md`
- `governance/weekly-review-2026-08-22.md`

## Next review triggers

- Re-score R-001 through R-004 after a material capability, control, or operating-context change.
- Add and assess any newly identified risk rather than inferring completeness from the current register.
- Refresh evidence before the seven-day freshness limit.
- Revisit the ATP formula after enough operational observations exist to test calibration and predictive value.