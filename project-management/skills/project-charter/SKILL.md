---
name: project-charter
description: Draft a project charter for an Aleut Federal federal task order or project — PMBOK-aligned but federal-flavored. Scope (PWS/SOW/SOO traceable), success criteria (acceptance, CDRLs, CPARS factors), authority (PM authority, CO interface), key stakeholders, high-level schedule and budget, assumptions, constraints, and risks. Initiates the project formally; signed by the AF executive sponsor and PM.
argument-hint: "<task order / project>"
---

# /project-charter — Aleut Federal Project Management

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Draft a **project charter** to formally authorize an AF federal project.

## Aleut Federal Context — Project vs. Program at AF

- **Program** = the broader contract instrument (an IDIQ vehicle, a multi-year prime contract). Managed under `program-management/`.
- **Project** = a discrete deliverable effort under a contract — typically a **task order**, a delivery order, or a self-contained scope. Managed under `project-management/`.

A single program can have many concurrent projects (task orders), each with its own charter.

## Charter Authority

- **PMBOK** (Project Management Body of Knowledge) provides the charter pattern.
- **AF Quality Management System (ISO 9001)** typically requires a documented project initiation for each new project — the charter satisfies it.
- **Contract** (PWS/SOW/SOO) is the source of authority — the charter translates the contract into AF's internal operating plan.

## Required Content

1. **Project name and identifier**.
2. **Contract reference** — prime contract number, task order number, modification numbers in scope.
3. **Customer** — agency, sub-agency, CO, COR, end-user POC.
4. **Period of Performance** — start, end, option periods if applicable.
5. **Contract type** — FFP, T&M, Labor-Hour, CR (CPFF / CPIF / CPAF), IDIQ task order.
6. **Funded value** + **total ceiling** (if different).
7. **Set-aside type** — 8(a) sole-source, 8(a) competitive, small business, F&O, etc.
8. **Vehicle** — GSA MAS, OASIS+, SeaPort-NxG, etc.
9. **Scope statement** — concise, traceable to PWS/SOW/SOO sections.
10. **Out-of-scope** — explicit statement of what's NOT included.
11. **Acceptance criteria** — how the customer will accept work; CDRL list summary.
12. **Success criteria for AF** — CPARS factor targets; project margin target; on-time delivery target.
13. **Key stakeholders** — internal (executive sponsor, functional leads), customer (CO, COR, end-users), subs / JV partners.
14. **PM authority** — what the PM can decide unilaterally; what requires escalation; CO interface rules.
15. **High-level schedule** — major milestones; WBS to be developed in the project plan.
16. **High-level budget** — funded value vs estimated total cost; indirect rate assumptions.
17. **Assumptions** — about scope, schedule, GFP/GFE arrival, customer responsiveness, weather/site conditions.
18. **Constraints** — fixed dates, fixed scope, fixed budget, regulatory.
19. **High-level risks** — top risks identified at initiation; full risk register lives separately.
20. **Approvals** — executive sponsor, PM, Contracts, Finance.

## Workflow

### Step 1: Pull the Contract Materials

- Prime contract + the task order awarding the work.
- Most recent mods.
- All referenced FAR / DFARS / agency-supplement clauses.
- PWS / SOW / SOO.
- All exhibits (CDRLs, DIDs, wage determinations, drawings, security forms).

### Step 2: Identify the Customer Team

- **CO** — the only Government authority on scope / price / PoP / terms.
- **COR** — day-to-day technical / administrative.
- **End-users** — the actual mission consumers; may include foreign national end-users on OCONUS work.
- **Customer safety office** — for construction projects.
- **Customer security office** — for cleared work.

### Step 3: Define Scope and Boundaries

- **In-scope** — drawn directly from PWS / SOW / SOO; trace each scope statement to a source paragraph.
- **Out-of-scope** — explicit; preserves AF position on any future scope-creep questions (and supports REA preservation under FAR 52.243-x via the `operations/change-request` skill).

### Step 4: Identify Acceptance Criteria

For each major deliverable:
- The CDRL number and DID (if applicable).
- The acceptance criteria (factual, measurable).
- Who accepts (CO / COR / technical rep).
- How acceptance is documented.

### Step 5: Define Success Criteria for AF

Beyond customer acceptance:

- **CPARS factor targets**: aim for "Very Good" or better on each factor.
- **Project margin** target.
- **On-time delivery rate** target.
- **Safety**: TRIR / DART floor.
- **Quality**: NCR rate target.
- **FAR 52.219-14 self-performance** target (on set-asides).
- **Customer satisfaction** (formal or informal).

### Step 6: Define PM Authority

What the PM decides:
- Routine resource assignment.
- Risk-treatment actions within the risk register.
- Minor sub coordination.
- Internal communications.

What requires escalation:
- Scope or price-affecting customer interactions → Contracts.
- Personnel actions → HR.
- Safety stop-work → SSHO can act unilaterally; PM notified.
- Cyber incidents → CISO.
- Out-of-scope direction from customer → Contracts (preserve REA).
- Mandatory-disclosure triggers (FAR 52.203-13) → GC.

### Step 7: Approve and Distribute

Signed by:
- **PM** (proposed).
- **AF executive sponsor** (typically a program manager or VP).
- **Contracts** (acknowledges the contract translation).
- **Finance** (acknowledges the budget / rate assumptions).

Distribute to the project team. The charter is the reference for "what's this project supposed to do?"

## Hard Rules

- **Scope traces to PWS / SOW / SOO.** Don't add scope; don't drop scope.
- **CO is the only customer authority.** PMs talk to CORs and end-users routinely, but commitments come from the CO.
- **Out-of-scope explicit.** Future REA preservation depends on this.
- **No promises beyond the contract.** If the customer asks for more, route to Contracts.
- **CPARS factors visible.** Project plan is built to support a strong CPARS narrative.
- **CUI / classified handling** noted in the charter where applicable.
- **Mandatory disclosure (FAR 52.203-13)** routing baked into the PM authority section.

## Output Format

```markdown
## Project Charter — [Project Name]

**Charter version:** 1.0 | **Effective date:** [...]

### 1. Project Identification
- Project: [name + AF project #]
- Contract: [prime #, task order #, current mod #]
- Customer: [agency, sub-agency, CO, COR]
- PoP: [start – end]
- Contract type: [FFP / T&M / CR / IDIQ TO]
- Funded value: $[...] | Total ceiling: $[...]
- Set-aside / vehicle: [...]

### 2. Scope
**In-scope** (PWS/SOW/SOO traceable):
- [...]

**Out-of-scope** (explicit):
- [...]

### 3. Acceptance Criteria
| Deliverable | CDRL / DID | Acceptor | Criteria |

### 4. Success Criteria (AF Internal)
- CPARS factor targets:
- Project margin target:
- On-time delivery target:
- Safety target (TRIR/DART):
- Quality target (NCR rate):
- FAR 52.219-14 self-performance target:

### 5. Stakeholders
- AF executive sponsor: [...]
- AF PM: [...]
- AF functional leads (Eng, Construction, Quality, Safety, ISO, IT, Finance): [...]
- Customer: CO [...]; COR [...]; end-user POC [...]
- Subs / JV: [...]

### 6. PM Authority
- Unilateral decisions: [...]
- Escalation matrix: [...]
- CO interface rules: [...]

### 7. High-Level Schedule
[major milestones; WBS development scheduled in project plan]

### 8. High-Level Budget
[funded vs estimated; indirect rate assumptions]

### 9. Assumptions
[...]

### 10. Constraints
[...]

### 11. Top Risks (Full Register Maintained Separately)
[...]

### 12. Approvals
| Role | Name | Signature | Date |
| Executive Sponsor | | | |
| PM | | | |
| Contracts | | | |
| Finance | | | |
```
