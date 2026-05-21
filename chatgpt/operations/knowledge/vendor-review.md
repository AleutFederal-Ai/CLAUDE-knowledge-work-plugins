# vendor-review

> **What this skill does:** Evaluate a vendor or subcontractor for Aleut Federal — federal-contractor responsibility check, cost analysis with allowable-cost screen, risk assessment with SAM/FAPIIS/CMMC posture, flow-down readiness, and recommendation. Use when onboarding a new vendor or sub, deciding renewal vs replacement, or comparing teaming candidates for a federal pursuit.

# /vendor-review — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

Evaluate a vendor or subcontractor with structured analysis covering federal-contractor responsibility, cost (with allowability screen), risk, past performance, and flow-down readiness.

## Usage

```
/vendor-review $ARGUMENTS
```

## What I Need From You

- **Vendor / sub name** and entity (verify legal name matches SAM).
- **Use case** — direct (charged to a contract / CLIN) or indirect (overhead / G&A / B&P).
- **Contract context** — which federal prime contract(s) the vendor would support; contract type (FFP / T&M / CR); any specific FAR clauses to flow down.
- **Spend profile** — annual estimate and 3-year TCO.
- **Source documents** — proposal, prior agreements, capability statement, SAM record.

## Federal-Contractor Responsibility Screen (Always First)

Before any cost or fit analysis, the vendor must clear these gates:

| # | Gate | Source |
|---|------|--------|
| 1 | **Active SAM.gov registration** with valid UEI; not in the SAM exclusions list | SAM.gov |
| 2 | **CAGE code** present and matches entity | SAM.gov / CAGE |
| 3 | **FAPIIS** — no adverse entries that disqualify (or compensating controls documented) | FAPIIS public |
| 4 | **Section 889 representation** — does not provide/use covered telecom entities | FAR 52.204-25; SAM annual reps |
| 5 | **OFAC sanctioned-party screen** clear | OFAC SDN |
| 6 | **Size and socioeconomic status** — captured per NAICS for FAR 52.219-9 reporting | DSBS / SAM |
| 7 | **DFARS 252.204-7012 / NIST 800-171 / CMMC posture** (if vendor will handle CUI) — SPRS score / CMMC level on file | SPRS / vendor-provided |
| 8 | **OCI screen** (FAR Subpart 9.5) — no conflicting work on the same procurement | Internal capture file + vendor disclosure |

A failure on any gate stops the review (or compensating control is required and documented).

## Cost Analysis with Allowability Screen

Standard TCO components:

| Component | Annual Cost | Notes |
|-----------|-------------|-------|
| Direct rates / unit prices | $[X] | Verify against benchmarks (GSA Schedule prices for similar labor categories where applicable) |
| Implementation / onboarding | $[X] | One-time |
| Support / maintenance | $[X] | Annual |
| Travel / per diem | $[X] | Subject to FTR/JTR if billed to government |
| Exit / data return | $[X] | Plan now |
| **Total Year 1** | **$[X]** | |
| **Total 3-Year** | **$[X]** | |

**FAR 31.205 allowability screen** — for each cost the vendor will charge into a federal billable pool or directly to a federal contract, confirm:

- No expressly unallowable categories (advertising, lobbying, alcohol, entertainment, donations, fines, bad debts, certain legal).
- Reasonable, allocable, and consistent with FAR 31.201-2.
- Travel within FTR/JTR.
- Compensation within FAR 31.205-6(p) caps if the vendor invoices labor at a fully-burdened rate.

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Financial instability | | | D&B / financial-stability report; advance-payment terms |
| Security / cyber (CUI exposure) | | | DFARS 252.204-7012 flow-down; SPRS verification; CMMC compliance evidence |
| Section 889 supply chain | | | Annual rep + spot supplier audit |
| OCI | | | Walling off; firewalled personnel; CO notification |
| Concentration / single source | | | Identify backups; long-term sole-source justification |
| Past-performance / litigation history | | | FAPIIS, GAO bid-protest history, court records |
| Country-of-origin / TAA / BABA | | | Material origin certifications |
| Set-aside compliance (if sub on small-business contract) | | | Verify size at contract level; track similarly-situated entity status |

## Past-Performance Evaluation

- Capture statement; relevant past performance (3–5 with customer, value, scope, recency).
- Public CPARS data where available.
- References from prior Aleut Federal contracts (CRM lookup).
- GAO bid-protest decisions involving this vendor.

## Flow-Down Readiness

Confirm the vendor accepts (or has equivalent in their MSA):

- **FAR 52.244-6** commercial-item flow-downs (always for commercial-item subs).
- **Contract-specific flow-downs** for the underlying prime: DFARS 252.204-7012, FAR 52.222-6 (DBA) / -41 (SCA), 52.222-54 (E-Verify), 52.203-13 (ethics), 52.204-25 (889), 52.225-x (BAA/TAA/BABA), 52.219-9 (subcontracting reporting), 52.215-2 (records), etc.
- **CDRL flow-downs** for deliverables.
- **Privacy / CUI** terms if applicable.
- **Audit access** (FAR 52.215-2) for cost-type / T&M subs.

## Output

```markdown
## Vendor Review: [Vendor Name]
**Date:** [Date] | **Type:** [New / Renewal / Sub for opp X / Comparison]

### Responsibility Screen
| Gate | Status |
[8 gates from above]

### Summary Recommendation
[Proceed / Negotiate / Pass] — [Reasoning]

### Cost & Allowability
[TCO table; FAR 31.205 allowability notes]

### Risk Matrix

### Past Performance

### Flow-Down Readiness

### Negotiation Points

### Open Items / Conditions Precedent
```

## Tips

1. Upload the SAM record + capability statement + proposal — extracts pricing, certs, status.
2. For comparisons, name both vendors and the federal contract / opportunity at issue.
3. For renewals, attach the current agreement so flow-down readiness is checked against the latest prime-contract clauses, not stale ones.
