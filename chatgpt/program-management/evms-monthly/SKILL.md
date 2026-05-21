---
name: evms-monthly
description: Produce monthly Earned Value Management System (EVMS) reports for an Aleut Federal federal program — Format II–V reports per DI-MGMT-81466A, SPI / CPI / TCPI calculations, variance narratives, EAC / ETC updates, and Format VI (variance analysis report) for material variances. Required on programs flowed-down with DFARS 252.234-7002 and on civilian programs with EVM clauses.
---

# /evms-monthly — Aleut Federal Program Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Produce the monthly EVMS reporting deliverable.

## Aleut Federal Context — EVMS Authority

| Item | Authority |
|------|-----------|
| **EIA-748** | Industry standard for EVMS (32 guidelines) |
| **DI-MGMT-81466A** | Standard DID for IPMR (Integrated Program Management Report) — the monthly EVMS report format on DoD programs |
| **DFARS 252.234-7002** | EVMS clause; triggers IPMR reporting on covered DoD contracts |
| **DFARS 252.234-7001** | EVMS Compliance — system itself must be EIA-748-compliant |
| **DCMA Business System review** | DFARS 252.242-7005 includes EVMS as one of the six business systems |
| **NDIA EVMS guides** | Industry implementation guidance |

DCMA EVMS Center performs system reviews; reviews can result in approval, conditional approval, or disapproval (with payment withholding).

## IPMR Formats

| Format | Content | Cadence |
|--------|---------|---------|
| **I** | Work Breakdown Structure dictionary | Initial + change |
| **II** | Organizational Categories — labor / materials / overhead / G&A | Monthly |
| **III** | Baseline (PMB) | Monthly |
| **IV** | Staffing (FTE by labor category by month) | Monthly |
| **V** | Explanations and problem analyses | Monthly |
| **VI** | Variance Analysis Report (VAR) for material variances | When threshold tripped |
| **VII** | Schedule (IMS) — see `integrated-master-schedule` | Monthly |

CDRL specifies which formats are required and the submission cadence.

## Monthly Workflow

### Step 1: Data Collection (typically by WD 5 of the following month)

- **Actual costs (ACWP)** from the cost-accounting system (Costpoint / Unanet) by Control Account.
- **Schedule actuals** from the IMS (BCWP based on % complete or earned value method per the Control Account).
- **Baseline (BCWS)** from the Performance Measurement Baseline.
- **Forecast data** — Estimate to Complete (ETC) updated by Control Account Manager (CAM).
- **Headcount and FTE actuals** for Format IV.

### Step 2: Calculate Earned Value Metrics

For each Control Account and program-wide:

- **BCWS** (Budgeted Cost of Work Scheduled) = planned value at the data date.
- **BCWP** (Budgeted Cost of Work Performed) = earned value at the data date.
- **ACWP** (Actual Cost of Work Performed) = actual cost incurred at the data date.

Derived metrics:

- **Schedule Variance (SV)** = BCWP − BCWS.
- **Cost Variance (CV)** = BCWP − ACWP.
- **Schedule Performance Index (SPI)** = BCWP / BCWS.
- **Cost Performance Index (CPI)** = BCWP / ACWP.
- **Variance at Completion (VAC)** = Budget at Completion (BAC) − Estimate at Completion (EAC).
- **To-Complete Performance Index (TCPI)** = (BAC − BCWP) / (EAC − ACWP). Indicates the CPI needed for remaining work to meet EAC.

### Step 3: Forecast EAC

Multiple EAC formulas — use the appropriate one(s):

- **EAC₁ = AC + (BAC − BCWP) / CPI** — assumes future work continues at current cost efficiency.
- **EAC₂ = AC + (BAC − BCWP) / (CPI × SPI)** — assumes future cost efficiency degrades with schedule slip.
- **EAC₃ = AC + bottom-up ETC** — CAM-based forecast.

Convention: report the bottom-up EAC₃ as the official EAC, with EAC₁ and EAC₂ as sanity checks.

### Step 4: Variance Analysis (Format VI when triggered)

Per the contract, Variance Analysis Reports (VARs) are required when variances exceed thresholds. Common defaults:

- Cumulative or current-period cost or schedule variance > ± 10% AND > $50K, or
- Customer-specific dollar / percentage thresholds.

Each VAR covers:
- **What happened** — the variance, where, when.
- **Why** — root cause (not symptom).
- **Impact** — to cost, schedule, technical performance.
- **Corrective action plan** — specific actions, owners, dates, expected effect.
- **Trend** — improving / stable / deteriorating.

### Step 5: Generate Formats

Use the EVMS tool (often Deltek Cobra, MS Project + custom, or vendor system) to generate each required format. Validate cross-format consistency (Format II labor hours roll up to Format IV; Format III baseline ties to IMS schedule baseline).

### Step 6: Internal Review

Before submission:
- **CAM sign-off** on Format VI variances and ETC updates.
- **Program Manager** sign-off on the integrated report.
- **Controller** review for cost-data accuracy.
- **DCMA-mock check** — apply the same scrutiny DCMA would apply.

### Step 7: Submit

Submit per the CDRL — PIEE/WAWF or contract-specific portal. Track receipt and any feedback.

### Step 8: Customer Brief (PMR)

EVMS results are the backbone of the Program Management Review (see `program-management-review`). Be prepared to walk customer through:

- This month's metrics.
- Trends over 3, 6, 12 months.
- VARs and corrective action status.
- EAC posture vs BAC and customer-funded value.
- Schedule risk (SRA results).
- Any DCMA / customer-system surveillance findings.

## Hard Rules

- **EVMS data ties to the cost-accounting system.** No "EVMS-only" numbers that don't match Costpoint. DCAA / DCMA reconcile.
- **BCWP is earned, not claimed.** % complete methods (0/50/100, 0/100, milestone, LOE) used per CAP / WAD; don't game.
- **Baseline integrity preserved.** Replans / reprogrammings only with the right authority.
- **VARs are evidence-based** — not editorial.
- **No retroactive baseline changes** without explicit BCR / customer approval.
- **Mandatory disclosure (FAR 52.203-13)** — if EVMS data manipulation is uncovered, route to GC.

## Output Format

```markdown
## EVMS Monthly Report — [Program] — [Period: YYYY-MM]

**Data date:** [...] | **BAC:** $[...] | **Funded value:** $[...]
**Submission due (CDRL):** [...]

### Headline Metrics
- **SPI:** [...]
- **CPI:** [...]
- **SV ($):** [...]
- **CV ($):** [...]
- **EAC ($):** [...] (vs BAC $[...] → VAC $[...])
- **TCPI:** [...] (vs current CPI [...])

### Format II — Organizational Categories
[table]

### Format III — Baseline / Performance
[table]

### Format IV — Staffing
[table]

### Format V — Explanations and Problem Analyses
[narrative]

### Format VI — VARs (Variances Tripping Threshold)
| Control Account | Variance | Cause | Corrective Action | Owner | Status |

### EAC Sensitivity
- EAC₁ (CPI-only): $[...]
- EAC₂ (CPI×SPI): $[...]
- EAC₃ (bottom-up — official): $[...]

### DCMA / Customer-Surveillance Status
[any open findings; remediation status]
```
