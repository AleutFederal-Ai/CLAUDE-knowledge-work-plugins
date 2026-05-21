---
name: sox-testing
description: Generate sample selections, testing workpapers, and control assessments for federal-contractor internal controls — DCAA-adequate accounting system (SF 1408), DFARS 252.242-7005 contractor business systems (accounting, estimating, MMAS, purchasing, property, EVMS), FAR Part 31 cost-allowability controls, CAS compliance, and FAR 52.203-13 ethics program. Use when planning monthly, quarterly, or annual internal-controls testing or preparing for a DCAA business-systems audit or IPA review.
argument-hint: "<control area> [period]"
---

# Federal-Contractor Internal Controls Testing — Aleut Federal

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

**Important:** This skill assists with internal-controls testing for a federal contractor; it does not provide audit, accounting, or legal advice. All testing workpapers and assessments should be reviewed by qualified personnel — the Controller, internal audit, our Independent Public Accountant (IPA), or external counsel — before use.

Aleut Federal is a privately held subsidiary of an Alaska Native Corporation and is **not subject to SOX** in its own right. The functional equivalent for our business is the **federal contractor controls environment**: DCAA accounting-system adequacy (SF 1408), DFARS 252.242-7005 contractor business systems, FAR Part 31 cost allowability, Cost Accounting Standards (CAS) compliance, and the FAR 52.203-13 ethics program. Use this skill to test those controls.

## Usage

```
/sox-testing <control-area> [period]
```

### Arguments

- `control-area` — the area to test:
  - `accounting-system` — DFARS 252.242-7006 / SF 1408 criteria (job costing, indirect pools, labor/timekeeping, billing).
  - `timekeeping` — daily total time accounting, supervisor approvals, electronic timesheet controls.
  - `labor-distribution` — labor to job/indirect pool routing accuracy.
  - `billing` — public voucher (SF 1034/1035) and invoice accuracy, T&M ceiling enforcement, Limitation of Funds/Cost notifications.
  - `indirect-rates` — provisional billing rates vs actuals; FAR 52.216-7 ICS prep controls.
  - `cost-allowability` — FAR Part 31.205 expressly-unallowable cost screening and segregation.
  - `estimating` — DFARS 252.215-7002 estimating system criteria; TINA support.
  - `purchasing` — DFARS 252.244-7001 contractor purchasing system review (CPSR) criteria; FAR 52.244-6 flow-downs.
  - `mmas` — DFARS 252.242-7004 material management and accounting system.
  - `property` — DFARS 252.245-7003 government property management.
  - `evms` — DFARS 252.234-7002 earned value management system.
  - `ethics` — FAR 52.203-13 code of business ethics & conduct; hotline; mandatory disclosure program.
  - `cas-compliance` — CAS 401-420 compliance for CAS-covered awards.
  - Any specific control ID or name.
- `period` — testing period (e.g., `2026-Q1`, `FY26`, `2026-H1`).

## Workflow

### 1. Identify Controls to Test

Present the control matrix for the area:

| Control # | Control Description | Type | Frequency | Key/Non-Key | Risk | Authority |
|-----------|---------------------|------|-----------|-------------|------|-----------|
| [ID] | [Description] | Manual / Automated / IT-Dependent Manual | Daily / Weekly / Monthly / Quarterly / Annual | Key | High / Med / Low | DFARS 252.242-7006 §(c)(2), FAR 31.205-22, etc. |

Examples by area:

**Accounting system (SF 1408 / DFARS 252.242-7006):**

| Control | Authority |
|---------|-----------|
| Job-cost ledger reconciles to GL by contract | DFARS 252.242-7006(c)(2) |
| Indirect costs accumulated in logical and consistent groupings (fringe, OH, G&A) | DFARS 252.242-7006(c)(4) |
| Direct vs indirect cost segregation | DFARS 252.242-7006(c)(3) |
| Daily total time accounting and timekeeping system | DFARS 252.242-7006(c)(6) |
| Labor distribution to cost objectives | DFARS 252.242-7006(c)(7) |
| Monthly determination of costs charged via routine posting to ledger | DFARS 252.242-7006(c)(8) |
| Identification and segregation of unallowable costs | DFARS 252.242-7006(c)(10), FAR 31.201-6 |
| Costs identified by line item if required | DFARS 252.242-7006(c)(11) |
| Integration with budgets to permit comparison of actuals to estimates | DFARS 252.242-7006(c)(13) |
| Internal management approvals for adjustments | DFARS 252.242-7006(c)(15) |

**Cost allowability (FAR Part 31.205):**

| Control | Authority |
|---------|-----------|
| Unallowable cost screening for advertising, lobbying, alcohol, entertainment, fines, bad debts, donations | FAR 31.205-1, -3, -8, -13, -14, -15, -22 |
| Executive compensation cap applied | FAR 31.205-6(p) |
| Travel costs within FTR/JTR limits | FAR 31.205-46 |
| Bonuses/incentive comp tied to written plan | FAR 31.205-6(f) |
| Legal costs in connection with proceedings — screening | FAR 31.205-47 |
| Penalty cost (FAR 42.709) — none claimed | FAR 42.709 |

**Ethics (FAR 52.203-13):**

| Control | Authority |
|---------|-----------|
| Written code of business ethics distributed to employees | 52.203-13(b)(1) |
| Ethics training cadence (initial + annual refresher) | 52.203-13(c)(1)(ii) |
| Internal reporting hotline with whistleblower protection | 52.203-13(c)(2)(ii)(E) |
| Internal-controls system to detect violations | 52.203-13(c)(2)(ii) |
| Mandatory disclosure log and process | 52.203-13(b)(3) |
| Annual review of code, training, and disclosures | 52.203-13(c)(1) |

### 2. Risk-Assess the Control

For each key control, document:

- **Inherent risk:** what could go wrong (mischarging labor, defective pricing, ineligible billing, unallowable cost reaching billing).
- **Likelihood and impact** if it fails.
- **Compensating controls.**

### 3. Determine Sample Size

Use a risk-adjusted approach, e.g.:

| Frequency | High risk | Medium risk | Low risk |
|-----------|-----------|-------------|----------|
| Daily / many times per day | 40–60 | 25–40 | 15–25 |
| Weekly | 12 | 8 | 5 |
| Monthly | 4–6 | 3 | 2 |
| Quarterly | 4 (all) | 4 (all) | 2 |
| Annual | 1 | 1 | 1 |

For substantive transaction testing (e.g., FAR 31.205 expressly-unallowable scan), use a stratified sample emphasizing high-risk vendors / GL accounts / cost categories.

### 4. Build the Sample Population and Selection

Define the population (e.g., all journal entries posted to a 31.205 unallowable-magnet account in the period). Pull the population (SQL via the data plugin if connected). Use a documented selection method:

- **Random** with seed documented.
- **Haphazard** for low-risk.
- **Stratified** by dollar value or risk.
- **Judgmental** for known-risk transactions.

Document the population control total and selected items.

### 5. Generate the Testing Workpaper

For each selected item, document:

- **Item identifier** (JE #, voucher #, timecard ID, PO #, etc.).
- **Test attributes** — exactly what to verify (approver name, date, dollar accuracy, supporting documentation, FAR 31 allowability check, contract number alignment, indirect-pool assignment).
- **Source documents reviewed.**
- **Tester, date.**
- **Result** — Pass / Fail / N/A.
- **Exceptions** — narrative of any deviation.

### 6. Classify Deficiencies

For federal contractors, use the DCAA business-systems language plus an internal severity tier:

| Severity | Federal-contractor analog | Internal action |
|----------|---------------------------|-----------------|
| **Significant deficiency** | A condition that could result in a "significant deficiency" finding from DCAA — could prevent the Government's needs from being met (e.g., a recurring control gap that lets unallowable costs into billings) | Document; remediate within 30 days; track in POA&M |
| **Material weakness** | A condition that would result in disapproval of the business system under DFARS 252.242-7005 — withholding of payments (typically 5%) may follow | Immediate escalation to CFO, GC; coordinate with CO; 90-day corrective action plan |
| **Audit-reportable noncompliance** | Noncompliance with FAR Part 31 / CAS / DFARS that affects pricing or billing | Quantify; consider voluntary refund; potential FAR 52.203-13 mandatory disclosure if "significant overpayment" |

Anything implicating FCA, Anti-Kickback Act, or PIA — stop and route to GC.

### 7. Output

Produce two artifacts:

**Workpaper:**

```
## [Control Area] Internal Controls Testing — [Period]

**Tester:** ...
**Reviewer:** ...
**Date:** ...

### Controls Tested
[matrix]

### Sample Population
- Definition:
- Source:
- Total population:
- Control total:
- Selection method:

### Test Results
| # | Item | Attribute(s) Tested | Result | Exception |
|---|------|---------------------|--------|-----------|

### Deficiencies Identified
[per item: description, severity, root cause, remediation plan, owner, due date]

### Conclusion
[Operating effectively / Deficiency identified / Significant / Material]
```

**Summary memo for the CFO and Controller:**

- Scope and period.
- Controls tested and results.
- Deficiencies and severity.
- Remediation plan with owners and dates.
- Any mandatory-disclosure or FCA implications (route to GC).
- DCAA / DCMA / IPA reporting implications.

## Notes

- If a control area is also subject to **CAS** (modified or full coverage), reference applicable CAS standards alongside FAR Part 31.
- For **incurred cost** controls, coordinate with the audit-support skill before final ICS submission.
- Keep workpapers in a system that supports DCAA request response (production typically within 5–10 business days).
- This skill does not generate FAR 52.203-13 mandatory disclosures; route any credible-evidence findings to GC.
