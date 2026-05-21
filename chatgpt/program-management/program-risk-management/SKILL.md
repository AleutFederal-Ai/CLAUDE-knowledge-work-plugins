---
name: program-risk-management
description: Manage program-level risk for an Aleut Federal federal program — risk identification, assessment (probability x impact), treatment planning (mitigate / transfer / accept / avoid), monitoring, and escalation. Maintains the program risk register; feeds EVMS variance narratives, IBR risk discussion, PMR top-risks slide, and Management Reserve (MR) allocation decisions.
---

# /program-risk-management — Aleut Federal Program Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Maintain the program risk register and run the program-level risk management cycle.

## Aleut Federal Context — Risk on Federal Programs

| Risk dimension | Examples |
|----------------|----------|
| **Acquisition** | Scope ambiguity in PWS; CO directs out-of-scope work without mod; FAR 52.219-14 self-performance shortfall |
| **Cost** | Indirect rate drift; LoF/LoC triggered (FAR 52.232-20/-22); TINA defective pricing exposure; CAS noncompliance |
| **Schedule** | Critical path slip; key-personnel attrition; subcontractor non-performance; Government-furnished delivery delay |
| **Technical** | Requirement uncertainty; design maturity; performance test failure |
| **Quality / CDRL** | CDRL non-acceptance; recurring NCRs; CPARS trending below "Satisfactory" |
| **Safety** | Recordable injuries; EM 385-1-1 finding; OSHA inspection |
| **Cyber / CUI** | DFARS 252.204-7012 incident; NIST 800-171 control failure; CMMC level shortfall |
| **Workforce** | Cleared-staff pipeline; clearance loss; SCA / Davis-Bacon WD update; CBA successor obligation |
| **Compliance** | FCA exposure; PIA violation; mandatory-disclosure trigger (FAR 52.203-13) |
| **Subcontract / JV** | Sub default; JV partner dispute; 13 C.F.R. § 124.513 workshare drift |
| **External** | Continuing resolution / shutdown; recompete competition; protest |

## Risk Register Schema

Each risk entry:

- **Risk ID** — sequential.
- **Date raised**, **raised by**.
- **Title** — concise.
- **Description** — what could happen, why.
- **Category** — from the dimensions above.
- **Probability** (1–5 scale).
- **Impact** (1–5 scale) — typically broken into Cost, Schedule, Technical sub-impacts.
- **Risk score** (P × I, or matrix-mapped).
- **Owner** — accountable for treatment.
- **Treatment strategy** — Mitigate / Transfer / Accept / Avoid.
- **Treatment actions** — specific, with owners and dates.
- **Trigger / threshold** — when the risk becomes an issue.
- **Linked WBS / IMS / CAP** elements affected.
- **Status** — Open / Treatment in progress / Closed / Realized (became issue).
- **MR provision** if applicable — Management Reserve dollar allocation.
- **Last reviewed** — date.

## Workflow

### Step 1: Identify

Continuous, multi-source identification:

- **Workshops** — kickoff, IBR, milestone reviews.
- **CAM input** — control-account-level risks.
- **Functional input** — engineering, quality, safety, cyber, supply chain.
- **Customer signals** — CO/COR statements; FAQ during proposal phase that landed in scope ambiguity.
- **Subcontractor / JV input** — formal mechanism.
- **Lessons learned** — from prior programs.
- **External monitoring** — appropriations / CR risk; agency budget signals; competitor / recompete signals.

### Step 2: Assess

Apply consistent rubrics:

**Probability:**
1. Remote (< 10%)
2. Unlikely (10-30%)
3. Possible (30-50%)
4. Likely (50-80%)
5. Almost Certain (> 80%)

**Impact (Cost / Schedule / Technical — assess separately, use highest):**
1. Negligible
2. Minor
3. Moderate
4. Major
5. Critical (program-threatening)

**Score** = P × I (range 1–25). Or use a risk-matrix mapping (Green / Yellow / Orange / Red).

### Step 3: Treat

For each non-Green risk, a treatment strategy:

- **Mitigate** — reduce P or I (e.g., add a control, prototype, schedule margin, hire key personnel earlier).
- **Transfer** — shift to a third party (e.g., insurance, subcontract structure with risk-bearing sub).
- **Accept** — acknowledge and live with it; set aside MR.
- **Avoid** — change the approach to eliminate (e.g., out-of-scope work routed back to CO).

Each treatment action gets owner, date, expected effect on P × I, and a verification mechanism.

### Step 4: Monitor

Monthly cycle:

- Review every risk for changes in P, I, status.
- Confirm treatment actions on track.
- Close risks that no longer apply.
- Surface emerging risks.
- Track trigger conditions — when tripped, escalate.

### Step 5: Escalate

When a risk's trigger / threshold is met, it **becomes an issue**:

- The variance / impact is happening.
- Re-baselining may be needed (BCR; see `integrated-master-schedule`).
- MR drawdown may be needed.
- Customer notification per the contract (especially for cost-type LoC/LoF or schedule slips affecting CDRLs).
- Cross-reference to `operations/change-request` if scope/price/PoP changes are required.

### Step 6: Report

Standard reporting venues:

- **PMR (monthly / quarterly)** — top 10 risks with status; risks realized as issues.
- **IPMR Format V** — narrative on material risks affecting EVMS variances.
- **PMR action register** — risk-driven actions.
- **Aleut Corp** — material risks elevated to parent per the reporting cadence.

### Step 7: Close

Risks close when:

- The condition no longer applies.
- The treatment successfully mitigated to acceptable.
- The risk realized as an issue (move to issue tracking).

Closure documented with date and rationale.

## Management Reserve (MR) Discipline

- MR is **above the PMB**, held by the program manager.
- MR drawdowns require documented justification (which risk realized; which CAP receives the funds).
- MR is **not** to cover scope creep — those are mods through the CO.
- MR balance reported in IPMR / PMR.
- DCMA / customer surveillance reviews MR usage for abuse.

## Hard Rules

- **No "we'll see" risks.** Treatment strategy is required.
- **No risks without owners.** An unowned risk is a finding.
- **Aged risks** (> 90 days without review) are themselves a risk.
- **Realized risks become issues** with separate tracking; don't leave them in the risk register as still "open".
- **MR for risks, not scope creep.** Misuse can be FCA exposure if billed in a way that misrepresents.
- **Mandatory disclosure (FAR 52.203-13)** — if risk surfaces credible-evidence concerns (e.g., we knew the proposal numbers weren't achievable), route to GC.

## Output Format

```markdown
## Program Risk Register — [Program] — [Period]

**PM:** [...] | **Risk Manager:** [...]

### Summary
- Total open risks: [...]
- Red (P×I ≥ 15): [...]
- Realized this period: [...]
- Closed this period: [...]

### Top Risks
| # | Title | Category | P | I | Score | Treatment | Owner | Status |

### Realized Risks (Now Issues)
| # | Title | Realized date | Impact | Action |

### MR Status
- MR balance: $[...]
- Drawdowns this period: $[...]
- Reasons: [...]
- Forecast adequacy: [...]

### Treatment-Action Cadence
| # | Risk | Action | Owner | Due | Status |

### Cross-Standard / Cross-Plugin Implications
[safety risks → safety plugin; cyber risks → cio-shop; compliance → legal]
```
