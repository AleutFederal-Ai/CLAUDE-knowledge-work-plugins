---
name: cmmc-poam-management
description: Manage Aleut Federal's internal CMMC / NIST SP 800-171 posture — Plan of Action and Milestones (POA&M) tracking, System Security Plan (SSP) updates, SPRS score management, control implementation status, evidence collection, internal self-assessment, and C3PAO assessment readiness. Use when planning CMMC remediation, updating SPRS, preparing for a CMMC assessment, or responding to a customer asking for our SPRS score / CMMC level.
---

# /cmmc-poam-management — Aleut Federal CIO Shop

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Manage AF's **internal** CMMC / NIST 800-171 posture. This is about AF as the contractor, not about systems we deliver to customers.

## Aleut Federal Context — Our CMMC Posture

| Item | Status / Target |
|------|----------------|
| **Highest CMMC level required by an AF contract** | Track this per the contract requirements; commonly Level 2 for DoD CUI work |
| **Current self-assessment level** | Per the latest SPRS posting |
| **SPRS score** | Posted in https://piee.eb.mil/sprs/ within 3 years; refreshed when material changes occur |
| **SSP (System Security Plan)** | Current, controlled in the document library |
| **POA&M (Plan of Action & Milestones)** | Living document; reviewed monthly; aging items escalated |
| **C3PAO assessment** | Required for Level 2 by contract; timing per phase-in |

The authoritative framework:
- **NIST SP 800-171** — 110 security requirements for CUI on non-federal systems.
- **CMMC 2.0** — three levels; Level 2 aligned to NIST 800-171.
- **DFARS 252.204-7012** — 72-hour cyber incident reporting; flow-down to subs.
- **DFARS 252.204-7019 / 7020 / 7021** — NIST 800-171 / CMMC representations and reporting.

## Workflow

### Assess (self-assessment cadence)

1. **Score each of the 110 NIST 800-171 controls** as implemented / partially / not implemented / not applicable.
2. **Calculate SPRS score**: starts at 110; subtracts the SP 800-171A weights for each gap (1, 3, or 5 points per control depending on impact).
3. **Compare against the prior posting**. Material change → re-post.
4. **Generate the artifact set**: SSP excerpts per control, evidence of implementation, identified gaps.

### POA&M Update

For every control not fully implemented:

- **Control ID** (e.g., 3.1.1).
- **Current implementation status** (Not / Partial / Planned).
- **Description of the gap** (specific, not "we're working on it").
- **Remediation steps** with owners and target dates.
- **Compensating controls** in place until remediation lands.
- **Risk acceptance** if remediation isn't planned (rare; needs senior sign-off).
- **Last reviewed date**.
- **Linked tickets** in the work-tracking system.

POA&M discipline:
- Monthly review by CISO + CIO + Compliance Officer.
- Items aging > 90 days escalated to executive review.
- POA&M older than the system's authorization period is a finding in itself.
- POA&M items that affect a contract's CMMC level required → notify the affected program team.

### SPRS Update

When to update SPRS:
- After any material change (control implementation, new system in scope, major incident).
- At least every 3 years (DFARS 252.204-7019/20 baseline cadence).
- When a customer or prospect formally requests an updated score.

Post via PIEE/SPRS portal. Capture confirmation; retain in document library.

### C3PAO Assessment Readiness

For DoD Level 2 contracts, an authorized third-party assessor (C3PAO) certifies the contractor at the contract's required cadence. Preparing for C3PAO:

- SSP and POA&M current and consistent.
- Evidence package: policies, procedures, screenshots, system inventories, training records, change records, access reviews, audit logs.
- Pre-assessment "mock" run by an outside consultant or internal IA.
- Personnel briefed: be honest, answer what's asked, don't volunteer beyond the question.
- Document control: only authorized environment, no CUI in public chat / email.

### Customer Inquiry Response

When a federal customer or prime asks "what's your CMMC level / SPRS score":

- For Level 1 contracts: provide the current self-assessment level.
- For Level 2 contracts: provide the SPRS score + C3PAO certification status.
- Coordinate the response through Contracts; do not freelance.
- Never overstate the posture. Misrepresentation has FCA implications.

## Hard Rules

- **Never misrepresent the CMMC level or SPRS score.** Misrepresentation in SAM reps, contract proposals, or to customers can be False Claims Act exposure.
- **Never bid a contract requiring a CMMC level we don't have a credible plan to meet.** Coordinate with Capture + GC.
- **Never share the SSP or POA&M outside the authorized environment.**
- **Cyber incidents on systems carrying CUI** trigger DFARS 252.204-7012 72-hour reporting to DIBNet — coordinate with `it-incident-response`.
- **Mandatory disclosure (FAR 52.203-13)** — if assessment evidence surfaces credible-evidence concerns, route to GC.

## Output Format

```markdown
## CMMC Posture Report — [Date]

**Current self-assessment level:** [...]
**SPRS score:** [...] (posted [date]; valid for 3 years through [date])
**Highest CMMC level required by an active contract:** [...]
**C3PAO assessment status:** [Not required / Scheduled [date] / Completed [date]]

### Control Implementation Summary
| Family | Implemented | Partial | Not Implemented | N/A |
| AC (Access Control) | x / 22 | | | |
| AU (Audit) | x / 9 | | | |
| ... | | | | |

### POA&M Status
| Total open | Aging > 90 days | Aging > 180 days | Closed this period |

### Top 5 POA&M Items by Risk
| Control | Gap | Owner | Target | Risk |

### Material Changes Since Last Report
[summary]

### Action Items
[for monthly review]
```
