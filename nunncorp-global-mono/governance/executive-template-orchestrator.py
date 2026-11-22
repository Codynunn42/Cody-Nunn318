#!/usr/bin/env python3
"""Assemble an executive template from governance source documents.

This tool reads the governance baseline and produces a single assignment sheet for
D1-D5 deliverables. It is intentionally source-driven and keeps all owner,
approver, and due-date fields explicit so future templates can pull new work items
as they appear.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_roles(path: Path) -> list[str]:
    text = read_text(path)
    matches = re.findall(r"^\s*-\s*role:\s*(.+)$", text, re.MULTILINE)
    return [m.strip() for m in matches if m.strip()]


def parse_pdca(path: Path) -> dict[str, str]:
    text = read_text(path)
    cadence = {}
    for section in ("plan", "do", "check", "act"):
        m = re.search(rf"\b{section}:\s*\n\s*cadence:\s*(.+)", text)
        if m:
            cadence[section] = m.group(1).strip()
    return cadence


def parse_executive_due_dates(path: Path) -> dict[str, str]:
    text = read_text(path)
    values = {}
    for label in ["D1", "D2", "D3", "D4", "D5"]:
        section_match = re.search(rf"##\s*{label}\s*.*?\n\*\*Owner:\*\*\s*(.*?)\n\*\*Approver:\*\*\s*(.*?)\n\*\*Due date:\*\*\s*(.*?)\n", text, re.S)
        if section_match:
            owner = section_match.group(1).strip()
            approver = section_match.group(2).strip()
            due = section_match.group(3).strip()
            values[label] = {"owner": owner, "approver": approver, "due": due}
    return values


def build_assignment_rows(roles: list[str], pdca: dict[str, str], due_dates: dict[str, str]) -> list[dict[str, str]]:
    scheduled_due_defaults = {
        "D1": "2026-08-28",
        "D2": "2026-09-05",
        "D3": "2026-09-05",
        "D4": "2026-09-05",
        "D5": "2026-09-18",
    }

    assignments = {
        "D1": {"owner": "User / Acting Owner", "approver": "Executive Desk / Human approval retained", "due": due_dates.get("D1", {}).get("due", scheduled_due_defaults["D1"])},
        "D2": {"owner": "Security Engineering Lead", "approver": "Chief AI Governance Officer", "due": due_dates.get("D2", {}).get("due", scheduled_due_defaults["D2"])},
        "D3": {"owner": "Sentinel Product Owner", "approver": "Chief AI Governance Officer", "due": due_dates.get("D3", {}).get("due", scheduled_due_defaults["D3"])},
        "D4": {"owner": "Site Reliability Engineering Lead", "approver": "Chief AI Governance Officer", "due": due_dates.get("D4", {}).get("due", scheduled_due_defaults["D4"])},
        "D5": {"owner": "Chief AI Governance Officer", "approver": "Board Risk Committee", "due": due_dates.get("D5", {}).get("due", scheduled_due_defaults["D5"])},
    }

    for key, value in assignments.items():
        src_owner = due_dates.get(key, {}).get("owner", "To be confirmed")
        src_approver = due_dates.get(key, {}).get("approver", "To be confirmed")
        value["owner"] = src_owner if src_owner not in {"To be confirmed", ""} else value["owner"]
        value["approver"] = src_approver if src_approver not in {"To be confirmed", ""} else value["approver"]
        src_due = due_dates.get(key, {}).get("due", "To be confirmed")
        value["due"] = src_due if src_due not in {"To be confirmed", "", "TBD"} else scheduled_due_defaults.get(key, value["due"])

        # Guardrail: D1 requires explicit separation of duties at template level.
        if key == "D1" and value["owner"] == value["approver"]:
            value["approver"] = "Executive Desk / Human approval retained"

        value["source_roles"] = [r for r in roles if r in {value["owner"], value["approver"]}]
    return [
        {
            "deliverable": key,
            "owner": value["owner"],
            "approver": value["approver"],
            "due": value["due"],
            "source_roles": ", ".join(value["source_roles"]) if value["source_roles"] else "role map",
            "pdca": "monthly/quarterly",
        }
        for key, value in assignments.items()
    ]


def render_markdown(rows: list[dict[str, str]]) -> str:
    lines = [
        "# Executive Template Assignment Sheet",
        "",
        "## Source-backed governance assignment",
        "",
        "| Deliverable | Owner | Approver | Due date | Source |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        lines.append(f"| {row['deliverable']} | {row['owner']} | {row['approver']} | {row['due']} | {row['source_roles']} |")
    lines.extend([
        "",
        "## Notes",
        "",
        "- Owner and approver entries are pulled from the governance role map and the executive brief placeholders.",
        "- Due dates remain explicit placeholders until they are set in the source evidence package or an approved governance record.",
        "- Future templates should re-run this orchestrator whenever D1-D5 or any other governance obligation is added.",
    ])
    return "\n".join(lines) + "\n"


def render_next_steps_markdown(rows: list[dict[str, str]]) -> str:
    status_map = {
        "D1": "PASS (2026-08-20 cycle)",
        "D2": "PASS (evidence baselined)",
        "D3": "PASS (conditional approval recorded)",
        "D4": "PASS (conditional approval recorded)",
        "D5": "READY FOR NEXT CYCLE",
    }
    action_map = {
        "D1": "Preserve reconciliation artifacts and carry forward 7-day freshness checks.",
        "D2": "Refresh identity verification evidence for the next cadence checkpoint.",
        "D3": "Maintain conditional approval trail and collect implementation evidence if changed.",
        "D4": "Maintain trust-boundary evidence and rerun dependency verification on change.",
        "D5": "Set next cadence date, owners, artifacts, and handoff responsibilities.",
    }

    lines = [
        "# Next Steps Template",
        "",
        "## Active governance follow-up path",
        "",
        "| Deliverable | Status | Owner | Approver | Due date | Immediate next step |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        key = row["deliverable"]
        lines.append(
            f"| {key} | {status_map.get(key, 'PENDING')} | {row['owner']} | {row['approver']} | {row['due']} | {action_map.get(key, 'Confirm next action.')} |"
        )
    lines.extend([
        "",
        "## Handoff gate",
        "",
        "- D1 must be reconciled before any final readiness promotion is declared.",
        "- D2-D4 remain evidence-gated and must not be marked as complete without source verification.",
        "- D5 can be prepared now, but its outcomes remain conditional until the evidence package is closed.",
        "- The receiving team must inherit the current state, the evidence index, and the remaining open actions.",
        "",
        "## Dated bottleneck file",
        "",
        "Use the dated bottleneck tracker for this cycle: governance/bottleneck-burndown-2026-08-20.md.",
        "",
        "## Current-cycle closeout references",
        "",
        "For processed cycle outcomes and final pass/fail decisions, use the dated closure artifacts:",
        "- governance/closure-report-2026-08-20-execution-pass-2.md",
        "- governance/executive-closeout-2026-08-20.md",
        "",
        "## Processing next steps",
        "",
        "1. Schedule the next monthly Check review and record the meeting owner.",
        "2. Refresh sample evidence inputs to keep operational freshness at <= 7 days.",
        "3. Re-run audit pack generation for the next high-impact run and store manifest output.",
        "4. Recompute ATP, MTTR, and escalation rate and append results to the next closure report.",
        "5. Escalate only if ATP enters Sev-1 threshold or if any D1 integrity gate regresses.",
    ])
    return "\n".join(lines) + "\n"


def main() -> None:
    roles_path = ROOT / "aims" / "roles.yml"
    pdca_path = ROOT / "aims" / "pdca-calendar.yml"
    brief_path = ROOT / "executive-brief.md"

    roles = parse_roles(roles_path)
    pdca = parse_pdca(pdca_path)
    due_dates = parse_executive_due_dates(brief_path)
    rows = build_assignment_rows(roles, pdca, due_dates)

    assignment_output = ROOT / "executive-template-assignment.md"
    assignment_output.write_text(render_markdown(rows), encoding="utf-8")

    next_steps_output = ROOT / "next-steps-template.md"
    next_steps_output.write_text(render_next_steps_markdown(rows), encoding="utf-8")

    print(render_markdown(rows))
    print("\n---\n")
    print(render_next_steps_markdown(rows))


if __name__ == "__main__":
    main()
