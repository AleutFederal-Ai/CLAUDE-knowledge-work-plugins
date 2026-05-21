---
name: wbs-development
description: Develop a Work Breakdown Structure (WBS) and WBS dictionary for an Aleut Federal federal project — hierarchical decomposition of project scope into deliverable-oriented work packages traceable to the PWS/SOW/SOO. Aligned with MIL-STD-881F (DoD WBS) where applicable. Feeds the IMS, the Performance Measurement Baseline (on EVMS programs), the responsibility-assignment matrix, and the project budget structure.
---

# /wbs-development — Aleut Federal Project Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Develop a Work Breakdown Structure for a federal project.

## Aleut Federal Context — WBS Authority

| Item | Authority |
|------|-----------|
| **MIL-STD-881F** | DoD standard WBS templates by program type (services, construction, ships, aircraft, IT, R&D, etc.) — required on covered DoD programs |
| **PMBOK** | Industry guidance for decomposition |
| **Customer contract** | Some contracts specify the WBS in Section J or via CDRL |
| **EVMS programs** | The WBS is the spine of the Performance Measurement Baseline |
| **FAR 31 cost accounting** | Cost accumulated by WBS for cost-type/T&M billing and ICS |

The WBS is **deliverable-oriented** — each WBS element represents a piece of scope, not an activity or organizational entity.

## Workflow

### Step 1: Determine the WBS Source

In priority order:

1. **Customer-mandated WBS** — if the contract specifies one, use it. May be in Section J or via a CDRL.
2. **MIL-STD-881F template** for the program type — DoD programs covered.
3. **Internal AF template** for the work type (construction, IT services, professional services, R&D).
4. **Bespoke** — only when none of the above applies.

### Step 2: Decompose Top-Down

Standard decomposition:

- **Level 1**: Project / contract.
- **Level 2**: Major deliverable groups or phases (often aligned with PWS sections or MIL-STD-881F categories).
- **Level 3**: Deliverable categories.
- **Level 4**: Work packages — discrete pieces of scope that can be planned, scheduled, costed, and assigned to an owner.
- **Level 5+**: Sub-packages where useful (for very large projects).

Each work package should:

- Have **clear scope** statable in a few sentences.
- Have a **single owner** (Control Account Manager on EVMS programs).
- Be **estimable** (cost and duration).
- Be **measurable** (clear completion criteria).
- Roll up cleanly to its parent without double-counting.

### Step 3: WBS Dictionary

For each WBS element:

- **WBS code** (1.0, 1.1, 1.1.1, ...).
- **Title**.
- **Scope statement** — clear, traceable to PWS / SOW / SOO paragraphs.
- **Deliverables** produced.
- **Acceptance criteria**.
- **Owner / Control Account Manager**.
- **Earned value technique** (for EVMS) — 0/50/100, milestone, units complete, LOE, etc.
- **Linked contract CLINs** if applicable.
- **Linked CDRLs** if applicable.

### Step 4: 100% Rule

A WBS satisfies the **100% rule**:

- The sum of children = the parent. Nothing missing; nothing duplicated.
- All scope from the PWS / SOW / SOO is in the WBS.
- Nothing in the WBS that isn't in the contract scope (other than explicitly-internal project-management overhead like B&P / IR&D, which is allocable differently).

If the WBS misses scope, the IMS will miss tasks, EVMS won't capture costs correctly, and CDRL deliverables may be orphaned.

### Step 5: Construction-Specific WBS

For federal construction:

- Level 2 often by CSI MasterFormat divisions or by phase (Pre-construction, Sitework, Foundations, Superstructure, Envelope, Interiors, Systems, Commissioning, Closeout).
- Reconcile with the AIA G703 Schedule of Values — they should be alignable.
- Includes safety-program scope (APP / AHA development; SSHO presence; EM 385-1-1 compliance) as work-package elements.

### Step 6: Services-Specific WBS

For federal services:

- Level 2 by service line or by PWS section.
- Labor-driven; each work package has a clear labor-category mix.
- Includes transition-in and transition-out work packages as bookends.

### Step 7: Validate

- **Customer review** — share the WBS draft with the COR for sanity; even on contracts without a mandated WBS, customer acceptance reduces friction later.
- **CAM review** — each Control Account Manager owns their CA's scope and signs off.
- **Cross-functional review** — Engineering, Construction, Quality, Safety, ISO, IT, Finance, Contracts review for their scope coverage.

### Step 8: Baseline and Maintain

- The WBS is **baselined** at project initiation (and IBR on EVMS programs).
- Changes to the WBS go through formal change control.
- The dictionary is a living document — kept up to date as scope is clarified.

## Hard Rules

- **100% rule.** No missing scope; no extra scope.
- **Deliverable-oriented.** Not activity-oriented; not organizational.
- **One owner per work package.** Shared ownership = no ownership.
- **Traceable to the contract.** Each work package cites the PWS / SOW / SOO source.
- **Customer-mandated WBS used when specified.** Don't innovate where the customer has prescribed.
- **MIL-STD-881F template applied** for covered DoD programs.

## Output Format

```markdown
## WBS — [Project] — Rev [X.Y]

**Project:** [...]
**Source template:** [customer-mandated / MIL-STD-881F / AF internal / bespoke]
**Effective date:** [...]
**Baseline date:** [...]

### Hierarchy
1.0 [Project]
 1.1 [Level-2 element]
 1.1.1 [Level-3]
 1.1.1.1 [Work package]
 1.2 [Level-2 element]
 ...

### WBS Dictionary
| Code | Title | Scope | Deliverables | Acceptance | Owner | EV Technique | CLIN | CDRL |
| 1.1.1.1 | | | | | | | | |

### Coverage Check
- PWS sections covered: [list]
- CDRLs covered: [list]
- 100% rule passed: ☑ (by [reviewer], [date])

### Sign-Offs
| Role | Name | Date |
| PM | | |
| CAMs | | |
| Engineering / Construction lead | | |
| Quality | | |
| Safety | | |
| Contracts | | |
| Finance | | |
| Customer (acknowledgment) | | |
```
