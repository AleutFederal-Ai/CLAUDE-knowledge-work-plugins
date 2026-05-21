---
name: surveillance-audit-prep
description: Prepare Aleut Federal for an external ISO surveillance, recertification, or transition audit by the certification body (CB) — ISO 9001 / 14001 / 45001 / 27001. Covers scoping confirmation, evidence package readiness, prior-audit follow-through, internal mock audit, personnel briefing, audit-day logistics, finding response. Cycle is typically Stage 1 + Stage 2 for initial cert, annual surveillance, every 3 years recertification.
---

# /surveillance-audit-prep — Aleut Federal ISO

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Prepare for an external audit by the certification body (CB) — surveillance, recertification, or transition (e.g., 27001:2013 → 27001:2022).

## Aleut Federal Context — Audit Cycles AF Lives With

Per IAF MD 5 (mandatory document for ISO certifications):

- **Initial certification** — Stage 1 (documentation review) + Stage 2 (implementation audit).
- **Annual surveillance** — sampled review against the standard in years 1 and 2 of the cycle.
- **Recertification** — full re-audit at the end of year 3.
- **Transition** — when ISO publishes a new revision (e.g., 27001:2022); CB performs a transition audit on a defined deadline.

AF runs four standards; many CBs combine surveillance audits across standards in a single visit if requested. Combined visits are cheaper and surface cross-standard findings (often positive).

## Pre-Audit Readiness (4–8 Weeks Out)

### Step 1: Confirm Audit Plan with CB

The CB sends an audit plan ahead of time covering:

- Scope (sites, processes, clauses).
- Schedule (date, days, hours).
- Auditor team (lead + technical experts).
- Sample sizes.
- Required pre-reads from us.

Confirm or negotiate the plan:
- Sites we propose to host the visit at.
- Personnel availability.
- Customer-site visits (federal customers may not allow external auditors on-site — confirm with the CO or use alternate site arrangements).
- CUI / classified considerations — auditors will not enter cleared environments unless they themselves are cleared AND the customer agrees. Coordinate.

### Step 2: Evidence Package Assembly

For each clause in scope, assemble:

- **Procedure(s)** that implement the clause.
- **Records** demonstrating procedure followed (sample defensibly).
- **Metrics / monitoring data** showing the process is producing the intended outcome.
- **Audit history** (internal + prior external).
- **CAPA history** for findings in this scope.
- **Management review minutes** addressing this area.

Per-standard specifics:

- **9001**: customer satisfaction data, supplier performance, CDRL on-time delivery, calibration records.
- **14001**: aspects/impacts register, compliance evaluations, environmental incidents, communications.
- **45001**: hazard ID + AHA system, incident investigations, worker consultation evidence, TRIR/DART trends.
- **27001**: SoA, risk treatment plan, ISMS POA&M (cross with NIST 800-171 POA&M), incident-response tests, access reviews, vulnerability management.

### Step 3: Address Prior-Audit Findings

- Confirm every prior major NCR closed and verified effective.
- Confirm every prior minor NCR has documented response and is closed or has a plan.
- Confirm OFIs were considered (no obligation to implement; obligation to consider).
- Don't let an aged prior finding be the first thing the auditor finds open again.

### Step 4: Internal Mock Audit

3–6 weeks out, run an internal mock audit:

- Use a different lead auditor than the routine internal audit team — fresh eyes.
- Test the worst cases (most-questioned clauses, highest-risk processes).
- Interview personnel — surface answers people will actually give the external auditor.
- Document findings; remediate before the CB arrives.

### Step 5: Personnel Briefing

Workers and process owners likely to be interviewed:

- **Be honest.** Don't speculate. If you don't know, say so.
- **Answer only what's asked.** Don't volunteer beyond the question.
- **Show the documented procedure** when asked how something is done — that's the right answer.
- **Don't admit liability** — the CB is auditing the management system, not driving FCA exposure.
- **Know where the policy / procedure / record lives** — fumbling for documents is a finding.
- **CUI / classified discipline** — never bring controlled material into an unauthorized environment for the audit.

### Step 6: Logistics

- Audit room / virtual platform booked.
- Access to controlled libraries pre-staged.
- Escort for the auditor at the site (always escorted; especially in cleared / CUI areas).
- Catering / break logistics.
- Customer notification — if the audit visits a federal-customer site, coordinate with the CO and the customer security office.

## Audit Day(s)

### Opening Meeting

- Confirm scope and plan.
- Confirm rules (sample sizes, confidentiality, what's in/out of scope).
- Introduce the AF audit team and escorts.

### Fieldwork

Auditor will:
- Review documents.
- Interview personnel.
- Walk processes / sites.
- Trace records to procedures and procedures to standard requirements.

AF support:
- Lead audit liaison stays with the auditor.
- Each interviewee gets a brief just before their session — what's in scope, who'll be there.
- Document requests handled within agreed turnaround (typically same day).

### Daily Closing

CB shares emerging findings at the end of each day. Address what we can in writing same-day; gather evidence for what we can't.

### Closing Meeting

CB delivers findings:
- **Major nonconformities** — must be closed (with evidence) within an agreed window (often 90 days) or the certification is suspended.
- **Minor nonconformities** — closed within an agreed window (often 6 months).
- **OFIs** — for our consideration.

Note: a major NCR on a recertification audit can block recert if not closed in time.

## Post-Audit

### Step 1: Confirm Audit Report

CB issues the formal report within a few weeks. Review for accuracy; challenge factual errors in writing.

### Step 2: Respond to Findings

Each NCR gets:
- Containment.
- Root cause analysis.
- Correction.
- Corrective action.
- Verification of effectiveness.

Cross-reference to `iso-ncr-capa`.

Submit responses to CB within their deadline. CB verifies (often via document review; sometimes site visit) before closing.

### Step 3: Update Management Review and Next Internal Audit

- External findings feed the next Management Review.
- Adjust internal audit program to revisit areas where the CB found issues.

## Hard Rules

- **Never hide a finding.** Surfacing it is far better than the CB finding it.
- **Never coach interviewees on what to say** — coach them on how to behave.
- **Never let CUI / classified material into an audit environment unauthorized.**
- **Cross-standard issues** — if a finding under one standard implies issues under another, raise it proactively.
- **Closure deadlines on Major NCRs are not negotiable.** Suspension of certification follows missed deadlines.
- **Mandatory disclosure (FAR 52.203-13)** — if external audit surfaces evidence of fraud / criminal / significant overpayment, route to GC outside the CB response.

## Output Format

```markdown
## Surveillance Audit Prep: [Standard or Combined] — [CB] — [Audit Date]

**Audit type:** [Stage 1 / Stage 2 / Surveillance Y1 / Y2 / Recertification / Transition]
**Standards:** [...]
**Sites in scope:** [...]
**Lead auditor:** [...] | **CB:** [...]

### Audit Plan
[scope, schedule, sampling]

### Evidence Readiness
[per clause / process; status]

### Prior-Finding Status
| Finding | Severity | Status | Verification |

### Mock Audit Results
[summary; remediation in progress]

### Personnel Briefing Status
[who briefed, when]

### Logistics
[room, escort, customer coordination, CUI considerations]

### Open Risks
[areas of concern; remediation underway]

### Post-Audit Tracker
| Finding | Severity | Owner | Due | Status | CB Verification |
```
