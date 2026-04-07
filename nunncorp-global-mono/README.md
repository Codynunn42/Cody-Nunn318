# nunncorp-global-mono: AI Governance Baseline

This package converts Sentinel AI + Nunn Cloud governance strategy into implementation-ready artifacts.

## What is included

- **AIMS wrapper (ISO/IEC 42001 style)**: policy, ownership model, and PDCA management cadence.
- **Risk workflow (ISO/IEC 23894 style)**: repeatable hazard → treatment → residual risk acceptance flow.
- **Control mapping backbone (NIST AI RMF + CSA AICM)**: control objectives mapped to enforceable execution policies.
- **EU AI Act high-risk readiness kit**: checklist aligned to lifecycle risk management, logging, oversight, and post-market monitoring.
- **Audit pack pipeline**: script that builds signed evidence bundles per release and high-impact run.

> **Compliance note:** these files are compliance-engineering scaffolds, not legal advice.

## Quick start

```bash
python3 nunncorp-global-mono/governance/audit_pack/build_audit_pack.py \
  --release 2026.04.07 \
  --run-id sentinel-run-001 \
  --input-dir nunncorp-global-mono/governance/audit_pack/sample_inputs \
  --output-dir nunncorp-global-mono/governance/audit_pack/out
```

The generated bundle contains:
- release metadata
- policy hashes
- approvals and control attestations
- incident/override records
- monitoring and post-market indicators
- integrity manifest with SHA-256 checksums

## Suggested rollout sequence

1. Adopt `governance/aims` files as the formal AI management system seed.
2. Load `governance/risk/risk_register.yml` into engineering/program review cadence.
3. Connect `governance/controls/sentinel_policy_rules.yml` to your execution policy engine.
4. Run the audit pack pipeline on each release and on every high-impact run.
5. Review `governance/eu_ai_act/high_risk_readiness_checklist.yml` monthly until all controls are evidence-backed.
