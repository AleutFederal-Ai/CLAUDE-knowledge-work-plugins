---
name: program-management-review
description: Prepare and run a Program Management Review (PMR) for an Aleut Federal federal program — periodic formal review with the customer covering cost, schedule, technical, risk, staffing, and CDRL deliverables. Typically monthly or quarterly per the contract. Single most important customer-facing routine for program-level engagement.
---

# /program-management-review — Aleut Federal Program Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Prepare and run a **Program Management Review (PMR)** — the periodic formal review of program status with the customer.

## Aleut Federal Context — PMR Audiences and Cadence

Audiences:
- **Customer** — CO, COR, program office, technical reps, sometimes DCMA / DCAA for EVMS programs.
- **AF internal** — Program Manager, CAMs, functional leads (Engineering, Construction, Quality, Safety, ISO), Contracts, Finance.
- **Subs / JV partners** — present when their work is in scope.
- **Aleut Corp** — material PMR findings may surface in parent reporting.

Cadence per contract. Typical:
- **Monthly** on most active federal programs.
- **Quarterly** on lower-activity programs.
- **Special** on milestone events (IBR, design reviews, test readiness reviews, transition reviews).

## Required Content

Standard PMR coverage:

1. **Executive summary** — health (Green/Yellow/Red) on cost, schedule, technical, risk.
2. **CDRL delivery status** — what's due, what's delivered, on-time rate.
3. **Cost** — EVMS metrics if applicable (SPI, CPI, EAC, VAC, TCPI); otherwise FFP / T&M cost-to-date vs plan.
4. **Schedule** — IMS critical path, milestones met/missed, recovery plans.
5. **Technical performance** — to TPMs (Technical Performance Measures) and acceptance criteria.
6. **Quality** — NCRs, customer concerns, CPARS feed.
7. **Safety** — TRIR/DART trend (especially on construction programs), open near-misses, EM 385-1-1 findings.
8. **Risk** — top 10 risks with mitigation status.
9. **Staffing** — actual vs plan; key personnel; cleared headcount where applicable; FAR 52.219-14 self-performance evidence on set-asides.
10. **Subcontractor / JV performance** — workshare actuals; flow-down compliance.
11. **Action items** — from prior PMR; status.

For EVMS programs, the PMR backbone is the monthly IPMR submission (see `evms-monthly`).

For construction programs, AIA G702/G703 progress billings and EM 385-1-1 safety metrics anchor the PMR.

## Workflow

### Pre-PMR (Week Before)

1. **Pull the data**:
 - EVMS / cost metrics.
 - IMS status.
 - CDRL delivery log.
 - NCR / CAPA register.
 - Safety metrics (TRIR / DART; recent incidents).
 - Risk register snapshot.
 - Action items from prior PMR.
2. **CAM and functional lead inputs** — each owner provides their slide / data with narrative.
3. **PM-level synthesis** — overall health assessment; key messages.
4. **Internal dry run** — full pre-brief 2 days before; surface gaps and red flags.
5. **Customer pre-read** — send 24–48 hours before per the customer's expectations.

### PMR Meeting

Typical agenda (90–180 minutes):

| Time | Topic | Owner |
|------|-------|-------|
| 5 min | Welcome, prior actions | PM |
| 10 min | Executive summary | PM |
| 15 min | CDRL delivery status | PM / Contracts |
| 20 min | Cost (EVMS or equivalent) | CFO / Controller |
| 20 min | Schedule (IMS) | Scheduler / PM |
| 20 min | Technical | Engineering / Construction lead |
| 10 min | Quality | Quality Manager |
| 10 min | Safety | Safety Director / SSHO |
| 15 min | Risk | Risk Manager |
| 10 min | Staffing & subs | HR / PM |
| 10 min | Action items | PM |
| 10 min | Customer Q&A | All |

Adjust per program criticality and customer norms.

### During the PMR

- **PM owns the room** — speaks for AF; functional leads support.
- **Be direct.** Yellow / Red status is fine — hiding it is worse.
- **Show trends.** Snapshots without trends underwhelm.
- **Map customer concerns to specific corrective actions.** Don't take a vague AI ("get back to us on X").
- **Document action items** with owner, date, and verification method.

### Post-PMR

- **Minutes** within 24 hours; sent to attendees and filed as a CDRL if required.
- **Action items** in the program action register; tracked to closure.
- **Internal lessons-learned** — what worked, what to improve.
- **CPARS implications** — note items that will affect the next CPARS evaluation; coordinate narrative.

## Hard Rules

- **Cancellation only with CO concurrence.** PMR is a deliverable on most programs; can't be skipped unilaterally.
- **Customer pre-read at least 24 hours before** — don't surprise the CO.
- **Honest status.** Yellow/Red is recoverable; hidden Red is not.
- **No commitments outside the CO's authority** in the PMR — scope/price/PoP changes still require a CO mod.
- **EVMS data integrity** — the PMR uses the same numbers as the IPMR submission and Costpoint actuals; reconcile.
- **CUI** content stays in CUI-authorized environments — don't include in distributable minutes.
- **Mandatory disclosure (FAR 52.203-13)** — if the review surfaces credible-evidence concerns, route separately to GC.

## Output Format

```markdown
## Program Management Review — [Program] — [Period]

**Date:** [...] | **Location/Modality:** [...]
**Customer attendees:** [CO, COR, PMO leads]
**AF attendees:** [PM, functional leads]
**Subs / JV attendees:** [...]

### Executive Summary
| Area | Health | Trend | Note |
| Cost | G/Y/R | ↑↓→ | |
| Schedule | | | |
| Technical | | | |
| Risk | | | |
| Quality | | | |
| Safety | | | |

### CDRL Status (this period)
| CDRL | Due | Delivered | Accepted | Notes |

### Cost
[EVMS metrics or FFP / T&M variance vs plan]

### Schedule
[IMS critical path; milestones]

### Technical Performance
[TPMs vs spec]

### Quality
[NCRs, customer concerns, CPARS feed]

### Safety
[TRIR/DART; recent incidents; corrective actions]

### Top Risks
| # | Risk | L | I | Score | Owner | Status |

### Staffing & Subs
[actuals; FAR 52.219-14 evidence on set-asides]

### Action Items from Prior PMR
| # | Action | Owner | Due | Status |

### Action Items from This PMR
| # | Action | Owner | Due | Verification |

### Customer Q&A and Open Items
[summary]
```
