---
name: iso-internal-audit
description: Plan and conduct an internal audit of an Aleut Federal ISO management system — ISO 9001 (QMS), ISO 14001 (EMS), ISO 45001 (OH&S), or ISO 27001 (ISMS). Covers audit program planning, individual audit scoping, evidence collection, finding classification (major / minor / OFI), audit report, and follow-up to closure. Required annually by all four standards to feed the management review and surveillance audit cycle.
argument-hint: "<standard — 9001 | 14001 | 45001 | 27001>"
---

# /iso-internal-audit — Aleut Federal ISO

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Run an internal audit of one of AF's four ISO management systems. Internal audits are required by all four standards (ISO 9001 clause 9.2; ISO 14001 clause 9.2; ISO 45001 clause 9.2; ISO 27001 clause 9.2). They feed the management review (clause 9.3) and protect the external surveillance audit by surfacing nonconformities first.

## Aleut Federal Context — Why We Run These Together

AF maintains all four standards because federal customers increasingly require them:

- **ISO 9001** for the underlying QMS that supports CDRL quality.
- **ISO 14001** for environmental management on construction sites.
- **ISO 45001** to align with OH&S obligations (overlaps with EM 385-1-1).
- **ISO 27001** for ISMS — aligns to NIST 800-171 / CMMC controls.

Where the standards overlap (e.g., 45001 hazard ID ↔ EM 385-1-1 AHA; 27001 controls ↔ NIST 800-171), AF maintains a single set of operational procedures that satisfies both. Internal audits verify both alignments.

## Audit Program (Annual)

Per ISO 19011 (auditing guideline):

- **Frequency**: every clause of every standard audited at least once per year.
- **Risk-weighted depth**: clauses with prior findings or higher operational risk get deeper coverage.
- **Auditor independence**: auditors don't audit work they're responsible for.
- **Auditor competence**: trained on the standard + audit technique (lead auditor cert preferred for the lead).
- **Documented program**: schedule, scope, auditor assignments, criteria.

## Workflow — Single Audit

### Step 1: Planning (1–2 weeks before the audit)

- **Scope** — which clauses, which processes, which sites.
- **Criteria** — the standard's requirements + AF's procedures.
- **Auditees** — process owners; book their time.
- **Audit plan** — sent to auditees in advance; agenda, attendees, locations.
- **Evidence requests** — list of records the audit will sample.
- **Audit team** — lead auditor + subject-matter expert(s).
- **Pre-read** — prior findings; management-review minutes; relevant procedures.

### Step 2: Opening Meeting

With the process owner(s):

- Confirm scope and criteria.
- Confirm the audit is to assess **effectiveness**, not to catch individuals.
- Confirm confidentiality (findings go through the formal report; ad-hoc disclosure is not the channel).
- Confirm the auditor's right of access to records and personnel.

### Step 3: Fieldwork

- **Document review** — verify procedures match the standard.
- **Sample records** — pull a defensible sample of the process output (e.g., 10 CAPAs over the year; 5 calibration records; 3 incident investigations).
- **Interview** process owners and operators.
- **Walk the work** — observe the process as actually performed.
- **Trace forward and backward** — from a customer complaint to root cause and back to corrective action; from a regulatory requirement to the procedure that implements it.

### Step 4: Finding Classification

Each finding is one of:

| Type | Definition | Examples |
|------|-----------|----------|
| **Major nonconformity** | Absence of, or systemic failure of, a required process or control. Likely to result in customer impact, regulatory exposure, or system breakdown. | No documented procedure for required process; controls not implemented; repeated failure to address a previously identified issue. |
| **Minor nonconformity** | An isolated lapse — single instance of a procedure not followed; documentation gap; partial implementation. | One CAPA missed its closure date; one calibration record missing; one training record incomplete. |
| **Opportunity for Improvement (OFI)** | Not a nonconformity but a recommendation to strengthen the system. | Procedure could be clearer; a process could be more efficient; alignment across standards could be tighter. |

Be honest. Calling a major a minor erodes the system.

### Step 5: Audit Report

For each finding:
- **Clause cited** (e.g., ISO 9001 clause 8.5.1).
- **AF procedure cited** (if applicable).
- **Evidence** — what was observed.
- **Statement of nonconformity / OFI** — clear, specific, evidence-based.
- **Severity** — Major / Minor / OFI.
- **Owner** — process owner accountable for response.

Report distributed to:
- Process owner(s).
- Management Representative for the standard.
- Quality Manager.
- Top management (summary).
- Audit log (formal record for surveillance auditor review).

### Step 6: Closing Meeting

Walk the findings with process owners. Confirm understanding. Set due dates for responses (typically 30 days for response plan; 60–90 days for closure depending on severity).

### Step 7: Follow-Up

Each nonconformity gets:
- **Containment** — immediate stop the bleeding.
- **Root cause analysis**.
- **Correction** — fix the immediate occurrence.
- **Corrective action** — system change to prevent recurrence.
- **Verification of effectiveness** — sample new output to confirm the fix held.

CAPA process is the same across the four standards. See `iso-ncr-capa` skill.

## Standard-Specific Cues

### ISO 9001 (QMS)
- Customer focus, leadership, process approach.
- CDRL traceability through the QMS.
- Past-performance impact on CPARS.
- Calibration records, test records, design records.

### ISO 14001 (EMS)
- Environmental aspects and impacts register.
- Compliance obligations register (CWA, CAA, RCRA, EPCRA, state law).
- Operational controls on construction sites.
- Emergency preparedness for environmental releases.

### ISO 45001 (OH&S)
- Hazard identification (overlaps with EM 385-1-1 AHA).
- Worker consultation and participation.
- Incident investigation (overlaps with `safety/incident-investigation`).
- Legal & other requirements register.

### ISO 27001 (ISMS)
- Statement of Applicability (SoA) — alignment with the Annex A controls.
- Risk assessment and risk treatment.
- Crosswalk to NIST 800-171 / CMMC.
- DFARS 252.204-7012 incident-response procedure tested.
- Asset inventory consistency with CIO-shop CMDB.

## Hard Rules

- **Auditor independence** — auditors do not audit their own work.
- **Honest classification** — major findings are major; do not soften because someone is uncomfortable.
- **Evidence-based** — every finding tied to objective evidence (record, observation, interview note).
- **Cross-standard issues** — a finding under one standard often surfaces a related issue under another; surface it.
- **Surveillance audit prep** — internal audit findings the certification body will look at; remediate aggressively before they visit.
- **Mandatory disclosure (FAR 52.203-13)** — if an audit surfaces credible evidence of fraud / criminal / significant overpayment, route to GC.

## Output Format

```markdown
## Internal Audit Report

**Standard:** ISO [9001 / 14001 / 45001 / 27001]
**Scope:** [clauses, processes, sites]
**Period audited:** [...]
**Audit dates:** [...]
**Lead auditor:** [...]
**Audit team:** [...]
**Auditees:** [...]

### Audit Plan Conformance
[any deviations from the audit plan]

### Findings
| # | Clause | AF procedure | Severity | Statement |
| 1 | 9001 § 8.5.1 | QP-PR-001 | Minor | [evidence-based statement] |

### Observations and OFIs
[positive observations and improvement opportunities]

### Cross-Standard Implications
[where this audit's findings affect another management system]

### Conclusion
[overall effectiveness of the audited scope]

### Required Responses
[owners, due dates for response plans and closure]
```
