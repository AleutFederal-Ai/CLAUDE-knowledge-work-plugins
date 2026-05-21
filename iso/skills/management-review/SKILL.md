---
name: management-review
description: Plan, run, and document the annual Management Review meeting for an Aleut Federal ISO management system (ISO 9001 / 14001 / 45001 / 27001 clause 9.3). Covers required inputs (audits, customer feedback, performance metrics, risks, opportunities), required outputs (decisions on improvement, resource allocation, policy/objective changes), and follow-through. The single highest-leverage management-system activity each year.
argument-hint: "<standard — 9001 | 14001 | 45001 | 27001 | combined>"
---

# /management-review — Aleut Federal ISO

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Run the **Management Review** required by every ISO management system (clause 9.3). This is the formal annual or semi-annual sit-down where top management evaluates the management system's effectiveness and decides what to change.

## Aleut Federal Context — One Combined Review or Four?

Some AF entities run one combined review covering all four standards; some run them separately. Either is acceptable to certification bodies. Combined is more efficient and cross-pollinates lessons; separate gives each standard's owners more depth.

If combined, dedicate enough time per standard that the review meaningfully covers all four. A 90-minute combined review is theater — the audit will say so.

## Required Inputs (clause 9.3.2 across all four standards)

1. **Status of actions from previous management reviews.**
2. **Changes in external and internal issues** relevant to the management system.
3. **Information on performance and effectiveness**, including:
   - Customer satisfaction and feedback (9001).
   - Compliance obligations status (14001 / 45001 / 27001).
   - Audit results (internal and external).
   - Process performance and product/service conformity.
   - Nonconformities and corrective actions.
   - Monitoring and measurement results.
   - Audit findings.
4. **Adequacy of resources.**
5. **Effectiveness of actions to address risks and opportunities.**
6. **Opportunities for improvement.**

Standard-specific add-ons:

- **9001 (QMS)**: CDRL on-time delivery, CPARS trends, customer complaints, supplier performance.
- **14001 (EMS)**: Environmental performance, compliance evaluations, communications from interested parties.
- **45001 (OH&S)**: OHS performance (TRIR / DART), incidents and near-misses, worker consultation results, results of monitoring.
- **27001 (ISMS)**: Risk treatment plan status, ISMS performance, results of risk assessment, vulnerability management, security incidents.

## Required Outputs (clause 9.3.3)

Documented decisions on:

1. **Opportunities for improvement.**
2. **Any need for changes to the management system.**
3. **Resource needs.**

Plus standard-specific outputs:

- **45001**: Actions to communicate to workers and worker representatives.
- **27001**: Updated risk treatment plan; revised SoA if needed.

## Workflow

### Step 1: Pre-Work (4–6 weeks before)

- Confirm meeting date; book top management calendars.
- Assign each input owner.
- Collect data — automate where possible (incident counts from incident-investigation system; audit findings from the audit log; customer satisfaction from CSAT surveys / CPARS).
- Distribute pre-read 1 week before the meeting.

### Step 2: Run the Meeting

A 3–4 hour meeting is typical for a combined review at AF scale.

Structure:

1. **Opening** — confirm attendees, scope, prior-action status.
2. **External/internal context** — what's changed.
3. **Performance** — metrics dashboard; trend lines preferred over snapshots.
4. **Customer / interested parties** — feedback, complaints, CPARS, compliance.
5. **Audits** — internal + external (surveillance, certification, customer).
6. **NCRs / CAPAs** — trends, aging, effectiveness.
7. **Risks and opportunities** — significant changes; effectiveness of treatments.
8. **Improvement opportunities** — proposals from process owners.
9. **Decisions** — formal sign-off on changes, investments, resource adds.
10. **Communications** — what gets briefed to workers, customers, Aleut Corp.

Required attendees:
- Top management (CEO / President / COO at minimum).
- Management Representative for each standard.
- Quality Manager (always).
- Process owners for material processes.
- Optional invitees: CFO (resource decisions), CISO (27001), Safety Director (45001), Environmental Manager (14001).

### Step 3: Document the Minutes

Detailed minutes are required evidence. Per item:

- **What was reviewed** — data and trend.
- **Discussion** — what was said by whom (concise; not transcription).
- **Decision** — explicit; not implied.
- **Action** — owner, due date.

The certification auditor will review these. Sparse or vague minutes are themselves a finding.

### Step 4: Follow-Through

Every action gets:

- Tracked in the CAPA / project-tracking system.
- Owner accountable to the Management Representative.
- Reviewed at the next Management Review for status.

If actions aren't tracked or aren't closed, the next Management Review starts with the same items — and the auditor notices.

## Hard Rules

- **All required inputs covered.** If a clause 9.3.2 item is absent from minutes, that's a minor at minimum.
- **All required outputs documented.** Decisions on opportunities, system changes, and resources must be explicit.
- **Top management presence.** A Management Review without top management is non-conforming.
- **Worker consultation (45001)** results presented — not skipped.
- **No magic numbers.** "Things are going well" is not a substitute for trended data.
- **Mandatory disclosure (FAR 52.203-13)** — if review surfaces credible-evidence concerns, route to GC outside the routine minutes.

## Output Format

```markdown
## Management Review — [Period] — [Standard or Combined]

**Date:** [...] | **Location/Modality:** [...]
**Attendees:** [name, role, standard ownership]
**Management Representative(s):** [...]
**Quality Manager:** [...]
**Top Management:** [...]

### Inputs Reviewed
(For each clause 9.3.2 item, a section with the data, trend, discussion, decision.)

### Standard-Specific Inputs
- 9001: customer satisfaction, CPARS, supplier perf
- 14001: env performance, compliance, interested parties
- 45001: OH&S performance, incidents, worker consultation
- 27001: risk treatment plan, ISMS performance, security incidents

### Outputs / Decisions
1. Improvement opportunities approved:
2. System changes approved:
3. Resource changes approved:
4. (45001) Worker communications:
5. (27001) Risk treatment plan / SoA updates:

### Action Register
| # | Action | Owner | Due | Standard | Status |

### Next Review Date
[scheduled]
```
