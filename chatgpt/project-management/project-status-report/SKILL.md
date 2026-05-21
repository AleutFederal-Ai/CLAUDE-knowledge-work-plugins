---
name: project-status-report
description: Produce a weekly or biweekly project status report for an Aleut Federal federal project — concise narrative + key metrics for AF leadership, the CO/COR, and the broader project team. Smaller-cadence than the program-level Monthly Status Report; surfaces issues fast and supports CPARS-quality routine engagement with the customer.
---

# /project-status-report — Aleut Federal Project Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Produce the routine **project status report** — weekly or biweekly snapshot for the project team and customer.

## Aleut Federal Context — Status Report Distinct from MSR

| Report | Cadence | Audience | Authority |
|--------|---------|----------|-----------|
| **Project Status Report (this skill)** | Weekly / biweekly | Project team, COR (often), PM | Internal practice + customer routine engagement |
| **Monthly Status Report (MSR)** | Monthly | Customer (CDRL deliverable) | Contract CDRL (often DI-MGMT-81646) |
| **IPMR (EVMS)** | Monthly | DCMA, customer | DFARS 252.234-7002 (EVMS only) |
| **PMR (Program Management Review)** | Monthly / quarterly | Customer (live meeting) | Contract-specified |

The status report is shorter, more frequent, and feeds the MSR / PMR. On smaller projects without a formal MSR, this is the customer's main read.

## Standard Status Report Content

Tight, single-page typical structure:

1. **Period covered**.
2. **Health indicators** (Cost / Schedule / Technical / Risk — Green/Yellow/Red).
3. **Accomplishments this period** — what got done.
4. **Plans next period** — what's coming.
5. **Issues / concerns** — open items needing attention; asks of the customer.
6. **Schedule update** — milestones met, slipping, ahead.
7. **CDRL status** — submitted, accepted, pending.
8. **Risks tripped this period** — new realized risks.
9. **Safety summary** — incidents, near-misses (construction).
10. **Action items** — open + closed this period.

## Workflow

### Step 1: Pull Data (End of Period)

- IMS data (current status).
- CDRL delivery log.
- Risk register changes.
- Safety register entries.
- Open action items.
- NCRs / customer feedback.

### Step 2: Synthesize

PM writes:

- **Honest health indicators.** Yellow / Red is fine; hidden Yellow / Red is not.
- **Concrete accomplishments.** "Worked on X" is not an accomplishment; "Completed milestone X.Y; submitted CDRL Z; closed NCR #N" is.
- **Forward-looking plans.** Specific deliverables and milestones for the next period.
- **Direct asks.** If we need a CO decision, a GFP delivery, an end-user response — say so.
- **Recovery plans** for any slipping items.

### Step 3: Internal Review

- Functional leads scan their areas.
- Contracts reviews any customer-facing language that touches scope / price / PoP — these go through Contracts, not the status report.

### Step 4: Distribute

- Project team always.
- COR per contract / customer expectation.
- AF leadership in summary (top-line health roll-up).
- Subs / JV — typically a tailored extract.

### Step 5: File

- Archive each status report in the project records.
- Useful for CPARS narrative — accumulated weekly reports demonstrate consistent communication.
- Retain per FAR 4.703.

## CDRL Format Caveat

If the contract specifies a status report CDRL (some do, with a DID), the status report format **must conform** to that DID. CDRL-driven status reports are formal deliverables and follow CDRL discipline (data date, page count, format, transmission method).

## Hard Rules

- **Weekly / biweekly is not optional** on active projects — cadence builds the customer relationship.
- **Honest health indicators.** Hiding Red trends to bigger problems.
- **Specific accomplishments** with deliverable / milestone names — not vague activity descriptions.
- **Recovery plans** for slipping items with named owners and dates.
- **CDRL-conformant format** where the contract requires.
- **No scope / price / PoP changes** in a status report — those are CO mods via Contracts.
- **No CUI in distributable reports** outside the authorized environment.
- **Mandatory disclosure (FAR 52.203-13)** — credible-evidence concerns route to GC outside the status-report channel.

## Output Format

```markdown
## Project Status Report — [Project] — Week of [...]

**PM:** [...] | **Distribution:** [project team / COR / leadership]

### Health Indicators
| Area | Status | Trend |
| Cost | G/Y/R | ↑↓→ |
| Schedule | | |
| Technical | | |
| Risk | | |

### Accomplishments This Period
- [specific deliverable / milestone / closure]
- [...]

### Plans Next Period
- [specific deliverable / milestone planned]
- [...]

### Issues / Concerns
- [item; impact; ask / next step]

### Schedule Update
| Milestone | Baseline | Forecast | Actual | Variance |

### CDRLs
| CDRL # | Title | Due | Submitted | Accepted | Notes |

### Risks This Period
- New: [...]
- Treatment-action updates: [...]
- Realized: [...]

### Safety (construction projects)
- Hours worked this period:
- Recordables / first-aids / near-misses:
- Open EM 385-1-1 findings:

### Action Items
| # | Description | Owner | Due | Status |

### Asks of the Customer
[explicit; with desired response date]
```
