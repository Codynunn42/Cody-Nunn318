# Month-End Closeout Runbook - 2026-08-31

## Purpose
Fast execution order for August month-end governance closeout.

## Target duration
5-10 minutes once evidence files are refreshed.

## Preconditions
- Sample inputs updated for final August cycle under governance/audit_pack/sample_inputs.
- No unresolved D1 integrity regressions.
- Canary provenance resolved or formally dispositioned by the designated owner and reviewer.

## Command sequence
1. Build final August audit pack:

```bash
python3 nunncorp-global-mono/governance/audit_pack/build_audit_pack.py \
  --release 2026.08.31 \
  --run-id sentinel-run-231 \
  --input-dir nunncorp-global-mono/governance/audit_pack/sample_inputs \
  --output-dir nunncorp-global-mono/governance/audit_pack/out/2026-08-31-month-end
```

2. Confirm artifacts exist:

```bash
ls -la nunncorp-global-mono/governance/audit_pack/out/2026-08-31-month-end
```

3. Verify preserved inputs and outputs against the manifest:

```bash
python3 nunncorp-global-mono/governance/audit_pack/verify_audit_manifest.py \
  nunncorp-global-mono/governance/audit_pack/out/2026-08-31-month-end/manifest.json
```

The command must report PASS. A missing file or checksum mismatch blocks closeout.

4. Capture manifest path for closeout:

```bash
cat nunncorp-global-mono/governance/audit_pack/out/2026-08-31-month-end/manifest.json
```

## Document update order
1. Update governance/cadence/daily-cadence-2026-08.md with final day metrics.
2. Update governance/cadence/weekly-cadence-2026-08.md W5 checkpoint.
3. Fill governance/cadence/monthly-closeout-2026-08.md placeholders.
4. Write month-end metric addendum report (ATP, MTTR, escalation decision).
5. Publish board update for month-end date.

## Fill-in values required in monthly closeout template
- Final high-impact run ID
- Final manifest path
- Final ATP table values
- Final MTTR and escalation rate
- Final D1 integrity gate status
- Final escalation decision
- Sign-off names and timestamp

## Escalation gate at closeout
Escalate immediately if either condition is true:
1. Any ATP >= 100
2. Any D1 integrity gate regression
3. Unauthorized or unapproved high-impact execution
4. Identity or MFA validation failure
5. Anomaly or payout override outside policy
6. Public API contract deviation
7. Repeated incident pattern or unresolved required-evidence gate

## Completion criteria
- Manifest verified and recorded.
- Canary provenance resolved or formally dispositioned.
- Month-end template fully filled and signed off.
- Board update published with authoritative references.
