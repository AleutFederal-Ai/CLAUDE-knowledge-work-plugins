---
name: safety-inspection
description: Plan and execute a safety inspection at an Aleut Federal construction site or office — daily / weekly / monthly cadence; site walk-throughs; equipment inspections; PPE inspections; AHA compliance verification; subcontractor work area review. Documents findings and corrective actions. Required by EM 385-1-1 and OSHA 1926 across multiple frequencies.
---

# /safety-inspection — Aleut Federal Safety

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Plan and execute safety inspections at AF sites. EM 385-1-1 and OSHA require multiple inspection cadences; this skill helps you do them rigorously and document them for audit.

## Aleut Federal Context — Inspection Cadences That Apply to Us

| Inspection | Cadence | Authority |
|------------|---------|-----------|
| **Daily site walk** by SSHO / competent person | Every workday | EM 385-1-1 Sec 01.A; OSHA 1926.20(b)(2) |
| **Pre-task equipment inspection** | Before each use | Equipment-specific (cranes, scaffolds, ladders, hand tools, PPE, fall protection, etc.) |
| **Daily fall protection inspection** by user | Before each use | OSHA 1926.502; EM 385-1-1 Sec 21 |
| **Weekly site safety inspection** | Weekly | EM 385-1-1 Sec 01 / project-specific |
| **Crane / hoist daily and periodic** | Per OSHA 1926 Subpart CC | Daily by operator; periodic by competent person |
| **Scaffolding** | Before each work shift and after any event that could affect integrity | OSHA 1926.451(f)(3) |
| **Excavation daily** by competent person | Daily prior to start; after every rainstorm or other hazard-increasing event | OSHA 1926.651(k); EM 385-1-1 Sec 25 |
| **Monthly fire extinguisher** | Monthly visual | OSHA 1910.157(e); NFPA 10 |
| **Annual / specialty equipment** | Per OSHA / mfr | Crane, hoists, lifelines, pressure vessels, etc. |

USACE and other federal customer safety offices also conduct their own inspections — be ready.

## Workflow

### Step 1: Pre-Inspection Prep

- **Pull the AHAs** for activities running.
- **Pull prior inspection reports** for trends and open items.
- **Pull recent near-misses** for areas needing extra attention.
- **Bring** checklist, camera, PPE, measuring tools as needed.
- **Coordinate** with site superintendent so the inspection doesn't disrupt critical path unnecessarily.

### Step 2: Walk the Site Systematically

Follow a defined route — perimeter, then by trade work area. Cover:

- **Access and egress** — clear paths, fire lanes, emergency exits.
- **Housekeeping** — clutter, slip / trip / fall hazards, material storage.
- **Fall protection** — guardrails, lifelines, harnesses, anchor points, hole covers.
- **Excavations** — daily competent-person check, soil classification, protective system, atmospheric testing for confined spaces.
- **Scaffolding** — erected per spec, inspected, tags current.
- **Ladders** — condition, set-up angle, tied off.
- **Electrical** — GFCI on temp power, exposed wiring, energized work.
- **Hand and power tools** — guards in place, GFCI / double-insulated, condition.
- **PPE** — workers wearing required PPE, in serviceable condition.
- **Hot work** — permit issued, fire watch, extinguisher present.
- **Crane / hoist** — daily inspection log current, rigging condition, swing radius secured.
- **Vehicles / equipment** — daily inspection logs, operator certification, back-up alarms.
- **Hazmat** — SDS available, labels intact, storage compliant.
- **Confined spaces** — entry permit current, atmospheric testing logged, attendant present.
- **Fire prevention** — extinguishers in date, access clear, no smoking compliance.
- **Signage** — warning, regulatory, emergency.
- **Subcontractor work** — same rigor as our own work.

### Step 3: Document Findings

For each finding:

- **Location** — be specific.
- **Hazard** — what's the actual unsafe condition.
- **Severity** — Imminent danger / Serious / Moderate / Minor.
- **Standard cited** — EM 385-1-1 section, OSHA citation.
- **Photo** — visual evidence.
- **Owner** — who needs to fix it.
- **Due** — by when (immediate for imminent danger, 24 hours for serious, longer for moderate / minor).
- **Verification** — how we confirm the fix.

### Step 4: Imminent-Danger Stop-Work

If an inspection surfaces an imminent-danger condition (e.g., scaffold collapse risk, unprotected excavation with workers in it, energized exposed conductor):

- **Stop the work immediately** — SSHO has authority.
- **Remove workers** from the hazard zone.
- **Notify** site superintendent + program manager.
- **Document** what was found, what was stopped, and what fix is required.
- **Resume work** only after the fix is verified.

### Step 5: Communicate Findings

- **Daily summary** in the toolbox briefing the next morning.
- **Weekly report** to the project manager and AF Safety Director.
- **Monthly trend report** to program leadership; tied to TRIR/DART trend.
- **Customer reporting** per the contract (USACE / NAVFAC routinely review weekly safety reports).

### Step 6: Close the Loop

- Track every finding to closure.
- Aged findings (open > 14 days for moderate; > 7 days for serious; not allowed for imminent) escalate to Safety Director and PM.
- Trend findings — if the same hazard recurs in 3 inspections, it's a systemic issue → safety stand-down or APP / AHA revision.

## Hard Rules

- **Daily site walks are not optional.** Even quiet days require the walk and the documentation.
- **Imminent-danger conditions trigger stop-work.** Production pressure never overrides.
- **All findings get documented.** "Verbal correction" without writing it down is not enough on a federal site.
- **Sub work gets the same scrutiny as ours.** No exceptions.
- **Trend pattern** of findings triggers stand-down / APP-AHA update.
- **Mandatory disclosure (FAR 52.203-13)** — if an inspection reveals fraud (e.g., we billed for safety controls not implemented), route to GC.

## Output Format

```markdown
## Safety Inspection: [Site] — [Date]

**Inspector:** [SSHO / competent person / Safety Director]
**Type:** [Daily walk / Weekly / Monthly / Equipment / Activity-specific]
**Activities running:** [...]

### Findings
| # | Location | Hazard | Severity | Standard | Owner | Due | Photo |
| 1 | | | Imm / Serious / Mod / Minor | EM 385-1-1 / OSHA 1926.x | | | [link] |

### Imminent-Danger Stop-Works (this inspection)
[any work stopped; resumption status]

### Trends From Prior Inspections
[recurring findings → escalation recommendation]

### Distribution
- Site superintendent: ✓
- Project manager: ✓
- AF Safety Director: weekly digest
- Customer safety office: weekly (federal-customer site)
```
