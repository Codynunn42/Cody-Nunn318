# AI Risk Workflow (ISO/IEC 23894-aligned)

## Purpose
Create a consistent lifecycle process for identifying, treating, monitoring, and accepting AI-related risk for Sentinel capabilities.

## Workflow

1. **Context + capability definition**
   - Define capability boundary, data types, actors, and intended outcomes.
   - Assign a capability owner.

2. **Hazard and misuse identification**
   - Enumerate foreseeable misuse, failure modes, and abuse paths.
   - Include model, policy, runtime, and integration-level hazards.

3. **Initial risk scoring**
   - Score impact × likelihood × detectability.
   - Classify whether capability is high-impact/high-risk by default.

4. **Control and treatment design**
   - Select preventive, detective, and corrective controls.
   - Link each control to executable policy rules and expected telemetry.

5. **Residual risk evaluation and acceptance**
   - Re-score after controls.
   - Route residual risk acceptance to defined accountable role.

6. **Operational monitoring and review**
   - Track KRIs/KPIs and incident indicators.
   - Trigger review on drift, incident threshold breaches, or major changes.

7. **Change/decommissioning governance**
   - Record major design changes, model changes, and decommissioning decisions.
   - Keep evidence chain in ledger-backed audit artifacts.

## Required evidence per risk item

- risk statement and affected assets
- control mapping (NIST/ISO/CSA/EU references)
- policy rule IDs
- latest test execution result
- residual risk approver + timestamp
- monitoring plan and alert thresholds
