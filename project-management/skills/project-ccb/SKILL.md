---
name: project-ccb
description: Run a project-level Change Control Board (CCB) for an Aleut Federal federal project — review and disposition proposed changes to scope, schedule, cost, technical approach, or risk treatment. Distinguishes in-scope changes (PM authority) from out-of-scope changes (require CO mod under FAR Subpart 43) and preserves Request for Equitable Adjustment (REA) rights for constructive changes.
argument-hint: "<change description>"
---

# /project-ccb — Aleut Federal Project Management

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). The `operations/change-request` skill handles federal contract changes that require CO action; this skill handles **project-internal** change control. The two interact — out-of-scope changes detected here route to Contracts / CO via `operations/change-request`.

Run the project Change Control Board (CCB) for proposed changes to the project plan.

## Aleut Federal Context — Three Change Tracks

Three distinct change pathways co-exist at AF projects:

| Track | Authority | When |
|-------|-----------|------|
| **Project-internal change** (this skill) | PM + functional leads; CCB decides | In-scope tweaks to plan, resource, schedule, technical approach within contract authority |
| **Federal contract change** | Contracting Officer (FAR Subpart 43; SF 30) | Any change to contract scope, price, period of performance, or terms |
| **Constructive change** | Implied by Government direction outside contract | We preserve REA rights under FAR 52.243-x while performing |

A project CCB **detects** which track a proposed change belongs to. Out-of-scope changes route immediately to Contracts.

## CCB Composition

Standing voting members:

- **PM** (chair).
- **AF executive sponsor or designee**.
- **Contracts representative** — critical for detecting CO-authority changes.
- **Finance** — cost impact.
- **Quality** — quality impact.
- **Safety** — safety impact (especially construction).
- **CISO / ISMS** — cyber / CUI impact.
- **Functional leads** (Engineering, Construction, IT) as applicable.

Sub / JV representatives invited for changes that affect their work.

## Change Categories

| Category | Authority | Approval path |
|----------|-----------|---------------|
| **Routine** | PM | PM alone |
| **Significant in-scope** | CCB | CCB vote |
| **Out-of-scope (requires CO mod)** | CO | CCB notes; routes to Contracts → CO |
| **Constructive change (Government-directed out-of-scope)** | CO ratification + REA | CCB notes; document; preserve REA via Contracts |

## Workflow

### Step 1: Change Request Submission

Anyone can submit a change request. The submission captures:

- **Description** — what's proposed.
- **Driver** — why (customer ask? lessons learned? risk treatment? resource constraint?).
- **Impact analysis (preliminary)** — scope, schedule, cost, technical, risk.
- **Submitter** — name, role.
- **Date submitted**.

### Step 2: Triage (PM)

PM triages within 24–48 hours:

- **Routine in-scope**: PM approves directly; logged for transparency.
- **Significant in-scope**: scheduled for CCB.
- **Possibly out-of-scope**: PM + Contracts review; if confirmed out-of-scope, route to `operations/change-request` workflow.
- **Constructive change**: if the customer has directed something out-of-scope without a mod, PM + Contracts document immediately and prepare REA via Contracts.

### Step 3: Impact Analysis (Pre-CCB)

For significant in-scope changes scheduled for CCB:

- **Cost** — direct and indirect implications; FAR 31.205 allowability if billable.
- **Schedule** — critical path impact; CDRL impact.
- **Technical** — design / specification implications.
- **Quality** — NCR risk; acceptance criteria implications.
- **Safety** — AHA / APP implications; new hazards.
- **Cyber / CUI** — SSP / POA&M implications; ATO boundary impact.
- **Subs / JV** — workshare impact; FAR 52.219-14 implications on set-asides.
- **Customer relationship** — does this change require CO notification even if in-scope (e.g., key personnel change under FAR 52.215-12)?

### Step 4: CCB Meeting

For each change:
- Submitter presents the proposal.
- Impact analysis presented.
- Discussion.
- Vote / decision: **Approve / Approve with conditions / Defer / Reject**.
- Conditions documented.
- Dissent documented if a member objects.

Approved changes get implementation owners and dates.

### Step 5: Implementation and Verification

- Execute the change per the CCB direction.
- Update affected artifacts (project plan, IMS, WBS dictionary, risk register, AHAs, SSP, etc.).
- Verify effectiveness — does the change produce the intended outcome.

### Step 6: Communication

- **Customer**: keep the CO/COR informed of in-scope changes that affect them (without overstepping into commitments the CO must make).
- **Project team**: communicate approved changes promptly.
- **Subs / JV**: communicate changes that affect their workshare.
- **Aleut Corp**: material changes elevated per parent reporting.

## Hard Rules

- **In-scope vs out-of-scope distinction is critical.** Out-of-scope changes never get approved at the project CCB — they go to the CO. Misclassifying creates constructive-change exposure.
- **REA preservation for constructive changes.** If the Government has directed out-of-scope work and we're performing while the mod catches up, document everything to preserve our REA under FAR 52.243-x.
- **No commitments outside CO authority.** A project CCB can decide to deploy resources differently; it cannot decide that scope expands.
- **Key personnel changes** — many federal contracts (FAR 52.215-12 / -13) require advance customer approval before substituting key personnel. CCB notes; Contracts coordinates with CO.
- **CMMC / CUI boundary changes** — if a change moves the ATO boundary or affects a CMMC control, CISO sign-off required.
- **Mandatory disclosure (FAR 52.203-13)** — if a change request reveals fraud / criminal / significant overpayment evidence, route to GC outside the CCB.

## Output Format

```markdown
## Project Change Control: [Change ID]

**Project:** [...]
**Submitter:** [...] | **Submitted:** [...]
**Category:** [Routine / Significant in-scope / Out-of-scope (to CO) / Constructive change (REA)]
**Status:** [Submitted / Triaged / CCB pending / Approved / Approved with conditions / Deferred / Rejected / Routed to CO]

### Description
[what's proposed]

### Driver
[why]

### Impact Analysis
- Cost (direct / indirect):
- Schedule (critical path / CDRL):
- Technical:
- Quality:
- Safety (AHA / APP):
- Cyber / CUI (SSP / POA&M / ATO boundary):
- Subs / JV (workshare / FAR 52.219-14):
- Customer relationship:

### Category Determination
- In-scope or out-of-scope? [...]
- Out-of-scope route: Contracts → CO (via `operations/change-request`)
- Constructive change? [Yes/No] — REA preserved via [Contracts]

### CCB Decision (if in-scope significant)
- Date:
- Attendees:
- Decision: Approve / Approve with conditions / Defer / Reject
- Conditions:
- Implementation owner / due date:

### Customer Communication
- CO notification needed: [Yes/No]
- Method: [via Contracts]

### Documentation Updates
- Project plan: ☑
- IMS: ☑
- WBS dictionary: ☑
- Risk register: ☑
- AHAs: ☑
- SSP / POA&M: ☑
- Other: [...]

### Mandatory-Disclosure Check
[None / Routed to GC]
```
