---
name: project-risk-management
description: Manage project-level risk for an Aleut Federal federal task order or project — risk identification, assessment, treatment, monitoring, and escalation. Smaller scope than program-level risk management (which spans multiple task orders); focused on the immediate project. Feeds the project status report, supports the PM's recovery planning, and rolls up to the program risk register.
argument-hint: "<project / period>"
---

# /project-risk-management — Aleut Federal Project Management

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). The `program-management/program-risk-management` skill handles program-level risk (spans multiple projects / task orders); this skill handles risk within a single project / task order. The two registers communicate — significant project risks roll up to the program register.

Manage risk at the project level.

## Aleut Federal Context — Project Risk Lens

Project risks are typically tighter, more time-bounded, and more operational than program risks:

| Risk dimension | Project-level examples |
|----------------|----------------------|
| **Schedule** | Specific critical-path slip; milestone miss; subcontractor delay on this project |
| **Cost** | This project's burn vs plan; this project's LoF/LoC posture; this project's indirect rate absorption |
| **Technical** | Specific deliverable's technical risk; design maturity for this task |
| **Quality** | NCRs on this project's deliverables; recurring quality issues |
| **Safety** | This site's safety conditions; this project's TRIR contribution |
| **Resource** | This project's key-personnel availability; clearance pipeline for this scope |
| **Supplier** | This project's specific subs / GFP / material lead times |
| **Customer** | This COR's responsiveness; this customer's mood; pending GFP delivery |
| **Cyber / CUI** | This project's specific CUI handling; this project's ATO posture |
| **Compliance** | This project's specific flow-downs; this project's specific WD; this project's CPARS posture |
| **Operational** | This project's specific dependencies; this project's transition risk |

## Workflow

### Step 1: Identify

- **Kickoff workshop** — at project initiation; involve customer where appropriate.
- **Weekly team scan** — at status meetings.
- **Customer signals** — CO/COR statements; corrective action requests.
- **Lessons learned** — from prior AF projects with similar scope.
- **Sub / JV input** — formal mechanism in subcontract.

### Step 2: Assess

Same rubric as program risk (P × I, 1–5 scale; severity by Cost / Schedule / Technical impact). Use the same matrix for consistency.

### Step 3: Treat

Mitigate / Transfer / Accept / Avoid. Each treatment action gets owner, date, expected effect.

### Step 4: Monitor

Weekly cycle in status report. Risk register reviewed at each status meeting.

### Step 5: Escalate to Program-Level

A project risk rolls up to the program risk register when:

- It affects multiple projects under the same program.
- It exceeds the PM's authority to treat.
- It implicates customer relationship at the program level.
- It implicates compliance / FCA / mandatory-disclosure.

The PM coordinates with the Program Manager on escalation.

### Step 6: Issue Tracking

When a risk's trigger is met → it's now an issue:

- Move to issue tracking (separate from risk register).
- Customer notification per contract if material.
- BCR / mod request if scope/cost/PoP affected (cross-reference to `operations/change-request`).

## Cross-Plugin Touchpoints

| When risk type appears... | Coordinate with... |
|----|----|
| Safety risk | `safety/incident-investigation`, `safety/safety-inspection` |
| Cyber / CUI risk | `cio-shop/it-incident-response`, `cio-shop/cmmc-poam-management` |
| Compliance risk | `legal/legal-risk-assessment`, `legal/compliance-check` |
| Cost overrun risk | `finance/variance-analysis`, `program-management/evms-monthly` |
| Schedule risk | `program-management/integrated-master-schedule` |
| Quality risk | `iso/ncr-capa` |
| Subcontractor risk | `operations/vendor-review`, `safety/subcontractor-safety-onboarding` |

## Hard Rules

- **Every risk has an owner.** Unowned risks don't get treated.
- **Treatment strategy is required**, not optional.
- **Aged risks escalate.** > 60 days without review at project level is a signal.
- **Realized risks become issues** in a separate tracker.
- **Escalation to program risk** when triggers apply — don't sit on a project risk that affects more than this project.
- **Mandatory disclosure (FAR 52.203-13)** — credible-evidence concerns route to GC immediately.

## Output Format

```markdown
## Project Risk Register — [Project] — [Period]

**PM:** [...]
**Project status:** [Active / Transition / Closeout]

### Summary
- Total open risks: [...]
- High-priority (P × I ≥ 12): [...]
- Realized this period: [...]
- Escalated to program register: [...]

### Top Risks
| # | Title | Category | P | I | Score | Treatment | Owner | Status | Escalated? |

### Realized Risks (Now Issues)
| # | Title | Realized | Impact | Action | Customer notified? |

### Treatment-Action Cadence
| # | Risk | Action | Owner | Due | Status |

### Cross-Plugin Implications
[items routed to safety / cio-shop / legal / iso / etc.]
```
