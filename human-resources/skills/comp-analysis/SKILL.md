---
name: comp-analysis
description: Analyze compensation — benchmarking, band placement, and equity modeling. Trigger with "what should we pay a [role]", "is this offer competitive", "model this equity grant", or when uploading comp data to find outliers and retention risks.
argument-hint: "<role, level, or dataset>"
---

# /comp-analysis — Aleut Federal

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Analyze compensation data for benchmarking, band placement, and offer planning at Aleut Federal. As a federal services and construction contractor, our comp model has constraints — and floors — that purely commercial benchmarking misses.

## Aleut Federal Context — Federal-Contractor Comp Floors and Ceilings

Several authorities **set or constrain** the wage we may pay or charge. Always check these before benchmarking against generic salary surveys.

### Service Contract Act (SCA) — services contracts > $2,500

For employees performing on an SCA-covered contract, the **DOL Wage Determination (WD)** for the contract's labor categories and locality is the **minimum** wage and fringe rate. Steps:

1. Identify the contract (or solicitation) and pull the current WD revision.
2. Map the role to the SCA labor category (often by SCA Directory of Occupations / OPM / WD title — not necessarily our internal title).
3. Confirm the **base wage** and the **health & welfare (H&W)** fringe at the WD rate.
4. For roles not in the WD, run **SF 1444 conformance** via the contracting officer.
5. Apply EO 14026 minimum wage if higher than the WD base.
6. For multi-year contracts, ensure FAR 52.222-43 price-adjustment is in the contract to recover WD updates.

### Davis-Bacon Act (DBA) — federal construction > $2,000

For laborers and mechanics on federal construction sites:

- Use the applicable **DBA WD** for the locality and work classification (Building, Heavy, Highway, Residential — pick the right schedule).
- Pay no less than the WD wage and provide WD fringe (or equivalent cash).
- CBA successor employees may inherit higher rates if the predecessor was covered.
- **Copeland Act** weekly payroll certification (WH-347 or equivalent).
- **CWHSSA** overtime > 40 hours/week.

### FAR 31.205-6(p) Executive Compensation Cap

For top executives (covered employees), comp claimed in the indirect rates as billable is capped per the annual benchmark (set by OFPP each year). Comp over the cap is **unallowable** for federal billing — but can still be paid; it just doesn't flow into the billable indirect pool.

### EO 14026 Minimum Wage

Federal contractors must pay at least the EO 14026 rate (updated annually by DOL) on covered contracts. This is a floor that supersedes a lower SCA WD wage on covered contracts.

### CBA Successor-Contractor Obligations

When we win an SCA-covered recompete where the predecessor was under a CBA, FAR 52.222-41 requires us to pay at least the CBA wages and benefits for the first contract option period (with limited exceptions). Pull the predecessor CBA before benchmarking.

### Indirect Rate Implications

Total comp must support our overall **indirect rate posture**. Comp that breaches our forward-pricing rate assumptions on indirect costs causes rate drift; coordinate with Finance before approving significant raises in indirect roles.

### State / Locality

Aleut Federal performs in multiple states (CONUS) and OCONUS (Alaska, Pacific). State minimum wage, paid sick leave, paid family leave, overtime rules, and pay-transparency laws apply alongside federal. Match the locality of the work site, not the HQ.

## Benchmarking Approach

For each role, build a comp recommendation by:

1. **Federal floor** — SCA WD or DBA WD if applicable; EO 14026 minimum; CBA successor wage.
2. **Federal ceiling for indirect billable** — FAR 31.205-6(p) cap for executives; indirect-rate posture for non-cap roles.
3. **Market benchmark** — commercial surveys (Radford, Mercer, BLS, Salary.com); GovCon-specific surveys (Govini, ERI, AFCEA); GSA Schedule pricing for similar LCATs as a sanity check; competitor postings.
4. **Internal equity** — band placement and parity across our team.
5. **Set-aside / clearance / location premiums** — clearance level (SECRET / TS / TS/SCI premiums), OCONUS posts, remote-Alaska sites.
6. **Recommendation** — base + variable + benefits, with federal-floor compliance, indirect-rate impact, and offer-letter language consistent with the contract.

## Outputs

```markdown
## Comp Analysis: [Role / Candidate / Cohort]

### Federal Floors and Constraints
| Authority | Rate / Cap | Source |
|-----------|-----------|--------|
| SCA WD [LCAT] / [Locality] | $... base + $... H&W | WD ref # |
| EO 14026 contractor minimum | $... | DOL |
| FAR 31.205-6(p) cap | $... | OFPP |
| State / locality minimum | $... | ... |

### Market Benchmark Range
| Source | P25 | P50 | P75 |

### Internal Equity Check
[band placement; comparison to peers]

### Recommendation
- Base: ...
- Variable: ...
- Premiums (clearance, OCONUS, etc.): ...
- Fringe (cash vs in-kind): ...
- **Federal-floor compliance**: [confirm above floor]
- **Indirect-rate impact**: [direct vs indirect; if indirect, rate impact estimate]

### Risks / Open Items
[CBA successor obligations? WD conformance needed? cap exposure?]
```

## Hard Rules

- **Never approve a wage below the applicable SCA / DBA WD** or EO 14026 minimum on covered contracts.
- **Never bill executive comp above the FAR 31.205-6(p) cap** to the government — pay it from non-billable accounts.
- **Coordinate with Contracts** before offering a wage on an SCA / DBA contract that requires conformance.
- **Pay-transparency laws** — comply with disclosure obligations in CA, CO, IL, MD, NY, WA, etc., where the role will be posted or performed.


## Usage

```
/comp-analysis $ARGUMENTS
```

## What I Need From You

**Option A: Single role analysis**
"What should we pay a Senior Software Engineer in SF?"

**Option B: Upload comp data**
Upload a CSV or paste your comp bands. I'll analyze placement, identify outliers, and compare to market.

**Option C: Equity modeling**
"Model a refresh grant of 10K shares over 4 years at a $50 stock price."

## Compensation Framework

### Components of Total Compensation
- **Base salary**: Cash compensation
- **Equity**: RSUs, stock options, or other equity
- **Bonus**: Annual target bonus, signing bonus
- **Benefits**: Health, retirement, perks (harder to quantify)

### Key Variables
- **Role**: Function and specialization
- **Level**: IC levels, management levels
- **Location**: Geographic pay adjustments
- **Company stage**: Startup vs. growth vs. public
- **Industry**: Tech vs. finance vs. healthcare

### Data Sources
- **With ~~compensation data**: Pull verified benchmarks
- **Without**: Use web research, public salary data, and user-provided context
- Always note data freshness and source limitations

## Output

Provide percentile bands (25th, 50th, 75th, 90th) for base, equity, and total comp. Include location adjustments and company-stage context.

```markdown
## Compensation Analysis: [Role/Scope]

### Market Benchmarks
| Percentile | Base | Equity | Total Comp |
|------------|------|--------|------------|
| 25th | $[X] | $[X] | $[X] |
| 50th | $[X] | $[X] | $[X] |
| 75th | $[X] | $[X] | $[X] |
| 90th | $[X] | $[X] | $[X] |

**Sources:** [Web research, compensation data tools, or user-provided data]

### Band Analysis (if data provided)
| Employee | Current Base | Band Min | Band Mid | Band Max | Position |
|----------|-------------|----------|----------|----------|----------|
| [Name] | $[X] | $[X] | $[X] | $[X] | [Below/At/Above] |

### Recommendations
- [Specific compensation recommendations]
- [Equity considerations]
- [Retention risks if applicable]
```

## If Connectors Available

If **~~compensation data** is connected:
- Pull verified market benchmarks by role, level, and location
- Compare your bands against real-time market data

If **~~HRIS** is connected:
- Pull current employee comp data for band analysis
- Identify outliers and retention risks automatically

## Tips

1. **Location matters** — Always specify location for benchmarking. SF vs. Austin vs. London are very different.
2. **Total comp, not just base** — Include equity, bonus, and benefits for a complete picture.
3. **Keep data confidential** — Comp data is sensitive. Results stay in your conversation.
