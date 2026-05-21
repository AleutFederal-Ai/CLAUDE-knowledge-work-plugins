# status-report

> **What this skill does:** Generate a status report with KPIs, risks, and action items. Use when writing a weekly or monthly update for leadership, summarizing project health with green/yellow/red status, surfacing risks and decisions that need stakeholder attention, or turning a pile of project tracker activity into a readable narrative.

# /status-report — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

## Aleut Federal Context — Federal-Contractor Status Reports

Calibrate to audience:

| Type | Audience | Key elements |
|------|----------|--------------|
| **Monthly Status Report (CDRL deliverable)** | Customer (CO/COR/PM) | Required CDRL format; period activities, deliverables, metrics, issues, risks, next-period work; submission via PIEE or agency channel |
| **CPARS-supportive interim** | Customer | Surfaces performance evidence aligned to CPARS elements (quality, schedule, cost, management, small-business utilization, regulatory compliance) |
| **EVMS report** | EVMS-covered customer | Format II–V; SPI/CPI; variance narratives; EAC |
| **Program review** | Internal + customer | Cost, schedule, risk, scope, staffing, subcontractor performance |
| **AIA G702/G703** | Customer / owner / surety | Schedule of values, % complete by line, retainage, change orders |
| **Internal weekly / monthly** | AF leadership | Bookings vs plan, revenue vs plan, GM, indirect rate posture, headcount, B&P burn, top opportunities, top risks |
| **Aleut Corp report-up** | Parent | High-level financials, headcount, regulatory posture, mandatory-disclosure activity (counsel-restricted summary) |

Customer-deliverable reports must follow the CDRL format exactly (mismatches show up in CPARS); never include CUI unless the distribution is authorized; never misrepresent performance but do explain root causes and corrective action; surface LoC / LoF posture early on cost-type (FAR 52.232-20/-22).

Generate a polished status report for leadership or stakeholders. See the **risk-assessment** skill for risk matrix frameworks and severity definitions.

## Usage

```
/status-report $ARGUMENTS
```

## Output

```markdown
## Status Report: [Project/Team] — [Period]
**Author:** [Name] | **Date:** [Date]

### Executive Summary
[3-4 sentence overview — what's on track, what needs attention, key wins]

### Overall Status: 🟢 On Track / 🟡 At Risk / 🔴 Off Track

### Key Metrics
| Metric | Target | Actual | Trend | Status |
|--------|--------|--------|-------|--------|
| [KPI] | [Target] | [Actual] | [up/down/flat] | 🟢/🟡/🔴 |

### Accomplishments This Period
- [Win 1]
- [Win 2]

### In Progress
| Item | Owner | Status | ETA | Notes |
|------|-------|--------|-----|-------|
| [Item] | [Person] | [Status] | [Date] | [Context] |

### Risks and Issues
| Risk/Issue | Impact | Mitigation | Owner |
|------------|--------|------------|-------|
| [Risk] | [Impact] | [What we're doing] | [Who] |

### Decisions Needed
| Decision | Context | Deadline | Recommended Action |
|----------|---------|----------|--------------------|
| [Decision] | [Why it matters] | [When] | [What I recommend] |

### Next Period Priorities
1. [Priority 1]
2. [Priority 2]
3. [Priority 3]
```

## If Connectors Available

If **~~project tracker** is connected:
- Pull project status, completed items, and upcoming milestones automatically
- Identify at-risk items and overdue tasks

If **~~chat** is connected:
- Scan recent team discussions for decisions and blockers to include
- Offer to post the finished report to a channel

If **~~calendar** is connected:
- Reference key meetings and decisions from the reporting period

## Tips

1. **Lead with the headline** — Busy leaders read the first 3 lines. Make them count.
2. **Be honest about risks** — Surfacing issues early builds trust. Surprises erode it.
3. **Make decisions easy** — For each decision needed, provide context and a recommendation.
