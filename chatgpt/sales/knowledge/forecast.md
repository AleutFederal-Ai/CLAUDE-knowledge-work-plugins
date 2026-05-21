# forecast

> **What this skill does:** Generate a weighted sales forecast with best/likely/worst scenarios, commit vs. upside breakdown, and gap analysis. Use when preparing a quarterly forecast call, assessing gap-to-quota from a pipeline CSV, deciding which deals to commit vs. call upside, or checking pipeline coverage against your number.

# /forecast — Aleut Federal BD Forecast

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

Generate a weighted federal BD forecast with bookings, revenue, and backlog views.

## Aleut Federal Context — Federal Forecasting Mechanics

Federal contracting requires a forecast model that separates **bookings** (award decisions) from **revenue** (delivered work) — they don't move together the way a SaaS forecast does.

### Probability calibration

Probability of award by capture stage (Pwin), tuned against our historical win rates. Default starting points (refine over time with retrospectives):

| Capture stage | Pwin range |
|---------------|------------|
| Identification | 5–10% |
| Qualification | 10–20% |
| Pursuit / Capture | 20–35% |
| Proposal Planning (post-solicitation) | 25–45% |
| Proposal Development | 35–50% |
| Submitted / Evaluation | 40–65% |
| Award Pending (oral confirmation / debrief due) | 75–90% |

8(a) sole-source pursuits with a Letter of Intent / customer signal of intent — start higher (60–80%) but always cap at award.

### Revenue forecasting (separate from bookings)

For each contract in the pipeline and current portfolio, build revenue by:

- **FFP / FFP-LOE**: schedule of values / milestones; recognize over time (percentage of completion) where applicable.
- **T&M / Labor Hour**: forecast hours × bill rate by labor category; pace against ceiling and PoP burn.
- **Cost-reimbursable (CPFF, CPIF, CPAF)**: forecast costs (direct + indirect) and fee; pace against funded value and ceiling (LoF/LoC at 75% / 85%).
- **Construction (FFP or cost-type)**: WIP schedule; cost-to-date / EAC; mobilization-loaded curves; weather/seasonality adjustments.
- **IDIQ task orders**: forecast at task-order level, not vehicle ceiling; assume ramp-up after award.

### Backlog views

- **Total backlog** — sum of unbilled funded + unfunded option periods at last contract value.
- **Funded backlog** — current funding minus billed-to-date.
- **Unfunded backlog (option years)** — value of unexercised options, decremented by historical option-exercise rate (default 85%).

### Risk overlays

- **Continuing Resolution risk** — federal FY starts Oct 1; under a CR, new starts and ceiling increases are constrained.
- **Recompete risk** — apply a haircut (default 30–40%) to revenue from contracts ending within the forecast window unless we are recompete-bidding.
- **Protest risk** — apply a timing slip if a protest is likely (typical 100 days for GAO; longer at COFC).
- **Workforce risk** — clearance pipeline, key-personnel retention.
- **CR / shutdown risk** — government shutdown impacts (mostly affects revenue timing, not bookings).

### Output bands

Always provide best / likely / worst:

- **Best**: 75% of unweighted pipeline + 100% of submitted + portfolio at full-burn.
- **Likely**: probability-weighted pipeline + portfolio at expected burn.
- **Worst**: 25% of weighted pipeline + portfolio at floor with recompete losses.

### Gap analysis

For each customer / line of business / set-aside:

- Plan vs Likely.
- Pursuits required to close the gap given Pwin distribution.
- B&P investment required.
- Specific candidate opportunities to accelerate (or de-prioritize) to close.

## Usage

```
/forecast [period]
```

Generate a forecast for: $ARGUMENTS

If a file is referenced: @$1

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│ FORECAST │
├─────────────────────────────────────────────────────────────────┤
│ STANDALONE (always works) │
│ ✓ Upload CSV export from your CRM │
│ ✓ Or paste/describe your pipeline deals │
│ ✓ Set your quota and timeline │
│ ✓ Get weighted forecast with stage probabilities │
│ ✓ Risk-adjusted projections (best/likely/worst case) │
│ ✓ Commit vs. upside breakdown │
│ ✓ Gap analysis and recommendations │
├─────────────────────────────────────────────────────────────────┤
│ SUPERCHARGED (when you connect your tools) │
│ + CRM: Pull pipeline automatically, real-time data │
│ + Historical win rates by stage, segment, deal size │
│ + Activity signals for risk scoring │
│ + Automatic refresh and tracking over time │
└─────────────────────────────────────────────────────────────────┘
```

---

## What I Need From You

### Step 1: Your Pipeline Data

**Option A: Upload a CSV**
Export your pipeline from your CRM (e.g. Salesforce, HubSpot). I need at minimum:
- Deal/Opportunity name
- Amount
- Stage
- Close date

Helpful if you have:
- Owner (if team forecast)
- Last activity date
- Created date
- Account name

**Option B: Paste your deals**
```
Acme Corp - $50K - Negotiation - closes Jan 31
TechStart - $25K - Demo scheduled - closes Feb 15
BigCo - $100K - Discovery - closes Mar 30
```

**Option C: Describe your territory**
"I have 8 deals in pipeline totaling $400K. Two are in negotiation ($120K), three in evaluation ($180K), three in discovery ($100K)."

### Step 2: Your Targets

- **Quota**: What's your number? (e.g., "$500K this quarter")
- **Timeline**: When does the period end? (e.g., "Q1 ends March 31")
- **Already closed**: How much have you already booked this period?

---

## Output

```markdown
# Sales Forecast: [Period]

**Generated:** [Date]
**Data Source:** [CSV upload / Manual input / CRM]

---

## Summary

| Metric | Value |
|--------|-------|
| **Quota** | $[X] |
| **Closed to Date** | $[X] ([X]% of quota) |
| **Open Pipeline** | $[X] |
| **Weighted Forecast** | $[X] |
| **Gap to Quota** | $[X] |
| **Coverage Ratio** | [X]x |

---

## Forecast Scenarios

| Scenario | Amount | % of Quota | Assumptions |
|----------|--------|------------|-------------|
| **Best Case** | $[X] | [X]% | All deals close as expected |
| **Likely Case** | $[X] | [X]% | Stage-weighted probabilities |
| **Worst Case** | $[X] | [X]% | Only commit deals close |

---

## Pipeline by Stage

| Stage | # Deals | Total Value | Probability | Weighted Value |
|-------|---------|-------------|-------------|----------------|
| Negotiation | [X] | $[X] | 80% | $[X] |
| Proposal | [X] | $[X] | 60% | $[X] |
| Evaluation | [X] | $[X] | 40% | $[X] |
| Discovery | [X] | $[X] | 20% | $[X] |
| **Total** | [X] | $[X] | — | $[X] |

---

## Commit vs. Upside

### Commit (High Confidence)
Deals you'd stake your forecast on:

| Deal | Amount | Stage | Close Date | Why Commit |
|------|--------|-------|------------|------------|
| [Deal] | $[X] | [Stage] | [Date] | [Reason] |

**Total Commit:** $[X]

### Upside (Lower Confidence)
Deals that could close but have risk:

| Deal | Amount | Stage | Close Date | Risk Factor |
|------|--------|-------|------------|-------------|
| [Deal] | $[X] | [Stage] | [Date] | [Risk] |

**Total Upside:** $[X]

---

## Risk Flags

| Deal | Amount | Risk | Recommendation |
|------|--------|------|----------------|
| [Deal] | $[X] | Close date passed | Update close date or move to lost |
| [Deal] | $[X] | No activity in 14+ days | Re-engage or downgrade stage |
| [Deal] | $[X] | Close date this week, still in discovery | Unlikely to close — push out |

---

## Gap Analysis

**To hit quota, you need:** $[X] more

**Options to close the gap:**
1. **Accelerate [Deal]** — Currently [stage], worth $[X]. If you can close by [date], you're at [X]% of quota.
2. **Revive [Stalled Deal]** — Last active [date]. Worth $[X]. Reach out to [contact].
3. **New pipeline needed** — You need $[X] in new opportunities at [X]x coverage to be safe.

---

## Recommendations

1. [ ] [Specific action for highest-impact deal]
2. [ ] [Action for at-risk deal]
3. [ ] [Pipeline generation recommendation if gap exists]
```

---

## Stage Probabilities (Default)

If you don't provide custom probabilities, I'll use:

| Stage | Default Probability |
|-------|---------------------|
| Closed Won | 100% |
| Negotiation / Contract | 80% |
| Proposal / Quote | 60% |
| Evaluation / Demo | 40% |
| Discovery / Qualification | 20% |
| Prospecting / Lead | 10% |

Tell me if your stages or probabilities are different.

---

## If CRM Connected

- I'll pull your pipeline automatically
- Use your actual historical win rates
- Factor in activity recency for risk scoring
- Track forecast changes over time
- Compare to previous forecasts

---

## Tips

1. **Be honest about commit** — Only commit deals you'd bet on. Upside is for everything else.
2. **Update close dates** — Stale close dates kill forecast accuracy. Push out deals that won't close in time.
3. **Coverage matters** — 3x pipeline coverage is healthy. Below 2x is risky.
4. **Activity = signal** — Deals with no recent activity are at higher risk than stage suggests.
