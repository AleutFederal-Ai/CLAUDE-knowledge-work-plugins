---
name: integrated-master-schedule
description: Develop and maintain an Integrated Master Schedule (IMS) for an Aleut Federal federal program — DCMA-compliant schedule structure, network logic (FS/SS/FF/SF), critical path identification, schedule risk analysis, and the program's Integrated Master Plan (IMP) linkage. Required on many DoD programs (DI-MGMT-81861A or contract-specific DID) and good practice on civilian programs.
---

# /integrated-master-schedule — Aleut Federal Program Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Develop and maintain the **Integrated Master Schedule (IMS)** — the time-based, logic-linked, resource-loaded baseline plan for a federal program.

## Aleut Federal Context — IMS Authority and Audience

| Item | Authority |
|------|-----------|
| **DI-MGMT-81861A** | Standard DID for IMS on DoD programs |
| **DCMA 14-Point Assessment** | Common health-check applied by DCMA to contractor schedules |
| **EIA-748** | Industry standard for EVMS that IMS supports |
| **DFARS 252.234-7002** | EVMS clause that ties IMS to earned-value reporting |
| **GAO Schedule Assessment Guide** | Government schedule-quality guidance |

Customers (CO, COR, agency PMO, DCMA) review the IMS at:
- **Integrated Baseline Review (IBR)** post-award.
- **Program Management Reviews (PMRs)** regularly.
- **EVMS surveillance** ongoing.
- **At any change request** (REA, mod) that affects schedule.

## IMS Required Content

1. **Work scope** at the appropriate WBS level (typically the Control Account level for EVMS programs).
2. **Tasks** with clear scope statements.
3. **Durations** in defensible time units (days; weeks for high level).
4. **Predecessor / successor logic** — network linkages (FS, SS, FF, SF) reflecting actual dependencies.
5. **Resources** — labor categories with hour estimates per task.
6. **Constraints** — only when justified (contractual milestone dates, NTP-driven mobilization, customer-furnished delivery dates).
7. **Milestones** — contractual + internal.
8. **Critical path** — identifiable, defensible, current.
9. **Risk-loaded** — tasks tagged with the risk register entries that affect them.
10. **Baseline** vs **forecast** — both maintained; baseline frozen, forecast updated monthly (at minimum).

## DCMA 14-Point Assessment (apply continuously)

Targets used by DCMA — keep ours within these or document why:

1. **Logic** — tasks with missing predecessors / successors: < 5%.
2. **Leads** — negative lag on relationships: 0%.
3. **Lags** — positive lag (delay) on relationships: < 5%.
4. **Relationship Types** — FS predominates; SS / FF / SF used sparingly: FS > 90%.
5. **Hard Constraints** — Must-Finish / Must-Start: < 5%.
6. **High Float** — total float > 44 working days: < 5%.
7. **Negative Float** — < 0%.
8. **High Duration** — tasks > 44 working days: < 5%.
9. **Invalid Dates** — actuals after data date or forecasts before data date: 0%.
10. **Resource** — tasks with no resources assigned: target = all loaded.
11. **Missed Tasks** — tasks completed late vs baseline: track trend.
12. **Critical Path Test** — adding test slip to terminal task moves the critical-path end date: must hold.
13. **Critical Path Length Index (CPLI)** — (Critical path duration + Total float) / Critical path duration: ≈ 1.00.
14. **Baseline Execution Index (BEI)** — Tasks completed / Tasks scheduled to complete: ≈ 1.00.

## Workflow

### Step 1: Establish the Plan

- **WBS** approved by the customer.
- **IMP** (Integrated Master Plan) — events, accomplishments, criteria; IMS is the time-phased instantiation.
- **OBS** (Organizational Breakdown Structure) — who does what.
- **RAM** (Responsibility Assignment Matrix) — RACI for each WBS element.

### Step 2: Build the Network

- Start with a flat task list at the right level (terminal task = Control Account or below).
- Define each task's clear scope, owner, duration, resource estimate.
- Establish predecessor/successor logic — focus on *real* dependencies, not "we usually do X before Y."
- Avoid constraints unless the customer or external party imposes them (deliveries, GFE arrival, customer reviews).
- Verify the network calculates a critical path and a finish date.

### Step 3: Resource-Load and Cost-Load

- Each task gets the labor categories and hour estimates that will execute it.
- For EVMS programs, costs flow through the labor / ODC / material categories aligned to the Performance Measurement Baseline (PMB).
- Indirect rates applied per the cost-accounting setup.

### Step 4: Risk-Load

Each significant task tagged with risk register entries that could affect it. Schedule Risk Analysis (SRA) using Monte Carlo (or similar) produces probabilistic finish dates — typically presented at the 50th, 70th, and 90th percentile confidence levels.

### Step 5: Baseline

After customer approval (typically at IBR), the baseline is **frozen**. From that point:

- Forecast can change with progress.
- Baseline changes require formal **Baseline Change Request (BCR)** — internal approval and (for in-scope or out-of-scope changes) customer approval.

### Step 6: Maintain (Monthly)

- **Status** progress at the data date — actual start, actual finish, % complete, remaining duration.
- **Re-forecast** based on actuals.
- **Re-calculate** the critical path.
- **Run DCMA 14-point check** before submitting to the customer.
- **Generate variance narratives** for any task or milestone slipping.
- **Submit** the monthly IMS to the customer per the CDRL (often DI-MGMT-81861A submission).

### Step 7: Change Control

- BCR for any baseline change (in-scope changes, replanning, OTBs / OTSs in extremis).
- CO approval required for out-of-scope changes (FAR Subpart 43; cross-reference `operations/change-request`).
- IMS reflects approved baseline + approved changes, not informal direction.

## Hard Rules

- **No constraints without justification.** They mask logic and the auditor / DCMA will find them.
- **No negative float quietly.** Visible; addressed in the variance narrative; recovery plan if material.
- **Critical path is honest.** Don't game it to make the schedule look prettier.
- **Baseline is sacred.** Changes only through BCR / customer approval.
- **EVMS programs:** schedule and cost are coupled; IMS quality drives EVMS quality.
- **Mandatory disclosure (FAR 52.203-13)** — if schedule manipulation is uncovered (intentional misreporting), route to GC.

## Output Format

```markdown
## IMS Status — [Program] — [Data Date]

**Contract:** [...] | **CO/COR:** [...] | **Customer PMO:** [...]
**Baseline date:** [...] | **Approved BCRs through:** [...]

### DCMA 14-Point Health Check
| # | Metric | Target | Actual | Trend |

### Critical Path
- Driving tasks (top 10):
- Forecast finish (50% / 70% / 90% confidence):
- Critical Path Length Index (CPLI):

### Baseline Execution Index (BEI)
- Tasks completed on or before baseline finish: [...] / [...]
- BEI: [...]

### Variance Narratives
[per major task / milestone slip]

### Open Schedule Risks
[from SRA]

### Pending Baseline Change Requests
| BCR # | Description | Impact | Status |

### Next Submission Due
[CDRL date, format]
```
