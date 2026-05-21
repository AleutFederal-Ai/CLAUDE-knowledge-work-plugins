---
name: integrated-baseline-review
description: Prepare Aleut Federal for an Integrated Baseline Review (IBR) — joint customer-contractor assessment that the Performance Measurement Baseline (PMB) is realistic, traceable to scope, resource-loaded, and ready for EVMS reporting. Required within 180 days of award on most major EVMS programs (DFARS PGI 234.201). Single highest-stakes program-management event in the first 6 months of a contract.
---

# /integrated-baseline-review — Aleut Federal Program Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Prepare for an **Integrated Baseline Review (IBR)** — the joint customer-contractor review of the Performance Measurement Baseline (PMB) on an EVMS-covered program.

## Aleut Federal Context — IBR Authority and Stakes

| Item | Authority |
|------|-----------|
| **DFARS PGI 234.201** | IBR guidance for DoD programs |
| **EIA-748 Guideline 10** | EVMS guideline requiring management of the PMB |
| **NDIA / DoD IBR Guide** | Industry guidance |
| **DCMA IBR support** | DCMA participates in IBRs on DoD programs |

The IBR is **not** a defense of cost or schedule estimates — it is a joint verification that:

- The technical scope is **fully captured** in the PMB.
- Schedule logic is **defensible**.
- Cost / resource estimates are **realistic**.
- Risk is **identified and managed**.
- Management processes are **adequate** to execute.

A failed IBR can trigger re-baselining; in extreme cases, contract restructuring.

## Prerequisites Before IBR

The PMB must exist:

1. **Contract scope** decomposed into the **WBS** approved by the customer.
2. **WBS dictionary** with clear scope statements per element.
3. **OBS** (Organizational Breakdown Structure) defining who.
4. **RAM** (Responsibility Assignment Matrix) mapping WBS to OBS — each intersection is a **Control Account**.
5. **Control Account Plans (CAPs)** with budgets, schedules, and metrics for each CA.
6. **Work Authorization Documents (WADs)** authorizing CAMs to execute their CAs.
7. **IMS** with full network logic, resource loading, and a critical path (see `integrated-master-schedule`).
8. **Risk register** with identified risks, ownership, treatment plans.
9. **Management Reserve (MR)** held above the PMB.
10. **EVMS Description** documenting our EVMS processes.

If any of these are missing or thin, do the work **before** scheduling the IBR.

## Workflow

### Step 1: Self-Assessment (6–8 Weeks Before)

Run an internal mock IBR:

- **WBS / CAP completeness** — every scope element has a CAP.
- **CAM readiness** — each CAM can defend their CAP scope, schedule, cost, risk.
- **IMS health** — DCMA 14-point check passing.
- **Cost realism** — bottom-up estimates traceable to historical actuals or industry data; not just allocation of the proposal price.
- **Risk identification** — comprehensive; not just the "easy" risks.
- **EVMS process readiness** — earning rules documented per CA; mechanisms for ETC and EAC updates.

Findings remediated before the external IBR.

### Step 2: Discussion Topics List (DTL)

Develop the DTL — the structured walk-through agenda. Typical topics per CAP:

- Scope (matched to WBS dictionary).
- Schedule (matched to IMS extract).
- Cost (BAC; breakdown by labor / material / ODC / G&A).
- Earned value technique (0/50/100 / milestone / LOE / units-complete / etc.).
- Resource plan.
- Risk register entries.
- CAM authority and accountability.

### Step 3: CAM Coaching

Each CAM defends their CAP at the IBR. Brief them:

- **Be honest.** Hiding uncertainty is the wrong move.
- **Show your math.** Cost basis, schedule basis, risk basis.
- **Acknowledge risk.** The IBR is for surfacing it.
- **Don't speculate** beyond the CAP you own — defer to others.
- **Have your evidence at hand** — scope documents, schedule extract, cost rollup, risk entries.

### Step 4: Logistics

- Joint AF + customer + DCMA / customer IBR team.
- Multi-day for large programs.
- Conference room with display capability; CAM workspace with their CAP materials.
- Customer-visit considerations if on a federal customer site.
- CUI handling — IBR materials likely include CUI; environment must support.

### Step 5: The IBR

Structure (per NDIA IBR Guide):

- **Opening** — purpose, ground rules, agenda.
- **Program overview** — scope, contract type, key milestones.
- **PMB / control-account walks** — each CA discussed per the DTL.
- **Cross-cutting topics** — risk, MR, EVMS process, indirect rates.
- **Daily wrap-ups** — emerging concerns, requests for additional info.
- **Closing meeting** — concerns documented, action items, path forward.

### Step 6: Concerns and Resolution

The IBR team documents **concerns** (not formal findings — concerns are joint observations). Each concern has:

- Description.
- Risk level.
- Suggested action.
- Owner.
- Due date.

Concerns are resolved in the following weeks/months:

- Re-plan a CAP that's not realistic.
- Update a risk treatment.
- Strengthen a management process.
- Document a clarification.

A small number of unresolved low-risk concerns is normal. Unresolved material concerns trigger re-IBR or PMB rework.

### Step 7: Concern Closure and Baseline Acceptance

When all concerns are closed (or accepted), the customer accepts the PMB as the baseline. From that point:

- The PMB is **frozen** at the IBR baseline.
- Changes require **Baseline Change Requests (BCRs)** with customer approval for material changes.
- EVMS reporting begins (IPMR; see `evms-monthly`).

## Hard Rules

- **Don't IBR an unready baseline.** Better to delay the IBR than to fail it.
- **Honest CAP discussions.** The IBR is the customer's opportunity to flag concerns; surface them with us first.
- **No "we'll figure it out later" answers.** Either we have the basis, or we don't and the CAP needs more work.
- **Management Reserve is for unknowns**, not for absorbing under-estimated scope.
- **EVMS Description matches actual practice.** Surveillance audit will compare.
- **Mandatory disclosure (FAR 52.203-13)** — if the IBR uncovers prior misrepresentation (proposal numbers not actually achievable), route to GC.

## Output Format

```markdown
## IBR Status — [Program] — [Date]

**Customer:** [...] | **DCMA support:** [Yes / No]
**Contract:** [...] | **Award date:** [...] | **IBR due (180 days):** [...]
**IBR scheduled:** [...]

### Readiness Self-Assessment
| Area | Status | Gap |
| WBS / Dictionary | | |
| OBS / RAM | | |
| CAPs / WADs | | |
| IMS (DCMA 14-pt) | | |
| Cost realism | | |
| Risk register | | |
| EVMS Description | | |
| Management Reserve | | |

### Internal Mock IBR Results
[findings; remediation status]

### CAM Readiness
| CAM | CAP # | Coaching done | Confident? |

### Open Concerns from Prior Mock / Surveillance
[items needing resolution before external IBR]

### IBR Day Logistics
[location, attendees, CUI considerations]
```
