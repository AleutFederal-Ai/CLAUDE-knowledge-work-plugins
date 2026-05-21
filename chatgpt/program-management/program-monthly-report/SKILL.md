---
name: program-monthly-report
description: Produce the Monthly Status Report (MSR) for an Aleut Federal federal program — CDRL deliverable on most programs in a customer-specified format (often DI-MGMT-81646 or contract-specific DID). Synthesizes cost, schedule, technical, risk, safety, quality, staffing, and CDRL deliverable status into a single narrative-and-tables document for the COR / PMO.
---

# /program-monthly-report — Aleut Federal Program Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Produce the **Monthly Status Report (MSR)** required as a CDRL on most federal programs.

## Aleut Federal Context — MSR vs PMR vs IPMR

Three customer-facing program reports often coexist:

| Report | What it is | Cadence | Authority |
|--------|-----------|---------|-----------|
| **MSR** | Narrative + key metrics; cross-functional snapshot | Monthly (most programs) | Contract-specific DID (often DI-MGMT-81646 or similar) |
| **IPMR / EVMS Formats** | Detailed EVMS data per DI-MGMT-81466A | Monthly (EVMS programs only) | DFARS 252.234-7002 |
| **PMR** | Live meeting to walk the status | Monthly / quarterly | Contract-specific |

The MSR is the **shareable, archived narrative**. The IPMR is the EVMS data drop. The PMR is the live discussion. The three reinforce each other.

For non-EVMS programs (smaller T&M or FFP task orders), the MSR may be the only formal monthly report.

## Standard MSR Content

Sections vary by DID and customer; common backbone:

1. **Executive Summary** — overall health (Green/Yellow/Red), key accomplishments, key concerns, asks of the Government.
2. **Period of Performance Status** — % complete, time elapsed vs PoP, key milestones met or upcoming.
3. **Cost Status** — funded vs billed vs cost-to-date; LoF/LoC posture for cost-type; FFP burndown for FFP.
4. **Schedule Status** — milestones met/missed; critical-path summary; recovery plans for slips.
5. **Technical Performance** — TPMs, deliverable acceptance, design-review status.
6. **Quality** — NCRs, customer concerns, CPARS interim feedback.
7. **Safety** — TRIR/DART, recordable incidents, EM 385-1-1 findings (on construction).
8. **Risk** — top risks; treatment status; realized risks.
9. **Staffing** — actual vs plan; key personnel; FAR 52.219-14 self-performance evidence on set-asides.
10. **Subcontractor / JV Performance** — workshare actuals; flow-down compliance.
11. **CDRL Delivery Status** — table of CDRLs due this period and their status; CDRLs due next period.
12. **Trips and Travel** — Government-funded travel taken and planned.
13. **Action Items / Open Issues** — items requiring customer or contractor action.
14. **Next Period Plan** — what's planned.

## Workflow

### Step 1: Pull Data (WD 1–5 of the Following Month)

- Cost from Costpoint / Unanet.
- Schedule from IMS (data date set; see `integrated-master-schedule`).
- CDRL log.
- NCR / CAPA register.
- Safety register (TRIR/DART; incident log).
- Risk register (see `program-risk-management`).
- Staffing actuals from HRIS.
- Travel log.

### Step 2: Draft Section Inputs

Each functional lead provides their section input by WD 5–7:

- **Cost** — Controller / CAM-rollup.
- **Schedule** — Scheduler / PM.
- **Technical** — Engineering / Construction lead.
- **Quality** — Quality Manager.
- **Safety** — Safety Director / SSHO.
- **Risk** — Risk Manager.
- **Staffing** — HR liaison.
- **Subs / JV** — Subcontracts Admin.

### Step 3: PM Synthesis

PM authors the Executive Summary and Next Period Plan; cross-checks for consistency; ensures Yellow/Red items are addressed honestly.

### Step 4: Internal Review

- Functional leads review the integrated draft.
- Contracts reviews for any language that could imply a change request to the CO outside the formal process.
- Legal reviews any potentially privileged or mandatory-disclosure-relevant content (typically rare in an MSR; if present, it doesn't belong in the MSR — route separately).

### Step 5: Submit

Per the CDRL — PIEE/WAWF, agency portal, or email per the contract. Capture receipt. Within the timeline specified (typically WD 10–15 of the following month).

### Step 6: Walk in the PMR

The MSR feeds the PMR (see `program-management-review`). Customer attendees will read the MSR before the PMR.

### Step 7: Archive

- File the executed MSR in the program records.
- Retain per FAR 4.703 / agency rules.
- Use as evidence in CPARS interim and final evaluations.

## DID Compliance

The MSR must **conform exactly** to the contract's DID. Common pitfalls:

- Wrong cover page format.
- Missing required tables.
- Missing data-date / cutoff statement.
- Tables in the wrong order.
- Acronyms not defined.
- Missing CDRL block.

CDRL non-conformance is an audit finding and may surface in CPARS as a Quality issue.

## Hard Rules

- **DID-conformant format.** Don't innovate.
- **Honest status.** Yellow / Red is recoverable; hidden Red trends to disaster.
- **Data ties to source systems.** Costpoint actuals, IMS data date, OSHA-recordable register. Don't massage.
- **No commitments outside the CO.** The MSR is a status report, not a vehicle to redirect scope.
- **No CUI in distributable MSR** unless the distribution chain is authorized.
- **Mandatory disclosure (FAR 52.203-13)** — credible-evidence concerns route separately to GC.

## Output Format

```markdown
## Monthly Status Report — [Program] — [Reporting Period]

**Contract #:** [...] | **CO/COR:** [...] | **PoP:** [...]
**CDRL #:** [...] | **Data date:** [...] | **Submitted:** [...]

### 1. Executive Summary
**Health:** Cost [G/Y/R] · Schedule [G/Y/R] · Technical [G/Y/R] · Risk [G/Y/R] · Quality [G/Y/R] · Safety [G/Y/R]

[2-3 paragraph executive narrative; key accomplishments; key concerns; asks of the Government]

### 2. Period of Performance Status
- PoP: [start] – [end]
- Time elapsed: [%]
- Completion: [%]
- Key milestones this period:
- Key milestones next period:

### 3. Cost Status
[table; LoF/LoC posture if cost-type; FFP burndown if FFP]

### 4. Schedule Status
[critical path; milestones met / missed; recovery plans]

### 5. Technical Performance
[TPMs; deliverable acceptance; design-review status]

### 6. Quality
[NCRs; customer concerns; CPARS feed]

### 7. Safety
[TRIR / DART; incidents; EM 385-1-1 findings]

### 8. Risk
[top 5–10 risks with status]

### 9. Staffing
[actual vs plan; key personnel; FAR 52.219-14 evidence]

### 10. Subcontractor / JV Performance
[workshare; flow-down compliance; sub deliverables]

### 11. CDRL Delivery Status
| CDRL # | Title | Due | Submitted | Accepted | Notes |

### 12. Trips and Travel
| Date | Traveler(s) | Destination | Purpose | Cost |

### 13. Action Items / Open Issues
| # | Description | Owner (Govt / AF) | Due | Status |

### 14. Next Period Plan
[planned activities; planned CDRL submissions; planned milestones]
```
