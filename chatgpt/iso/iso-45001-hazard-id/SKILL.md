---
name: iso-45001-hazard-id
description: Maintain Aleut Federal's ISO 45001 hazard identification, risk assessment, and OH&S risk treatment process (clauses 6.1.2 and 8.1.2). Crosswalks with the EM 385-1-1 / OSHA 1926 Activity Hazard Analysis (AHA) program so 45001 hazard-ID and construction-site AHAs are the same operational practice satisfying both regimes. Includes worker consultation, both routine and non-routine activities, and emergency situations.
---

# /iso-45001-hazard-id — Aleut Federal ISO

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Run AF's ISO 45001 hazard identification, risk assessment, and risk treatment process — aligned with our EM 385-1-1 AHA program so one practice satisfies both.

## Aleut Federal Context — One Hazard System, Two Regimes

AF runs construction work governed by **USACE EM 385-1-1** and **OSHA 29 C.F.R. Part 1926**, alongside ISO 45001 certification. ISO 45001 clauses 6.1.2 (hazard ID) and 8.1.2 (operational planning and control) closely parallel EM 385-1-1's AHA process.

**Single source of truth:** the AHA system (see `safety/aha-development` and `safety/app-development`).

This skill provides the 45001 framing on top of that operational backbone — making sure the AHA program **also** satisfies:

- Worker consultation and participation (45001 § 5.4).
- Coverage of routine, non-routine, and emergency activities (45001 § 6.1.2.1).
- Past incident learning (45001 § 6.1.2.2).
- Legal & other requirements integration (45001 § 6.1.3).
- Documented hierarchy of controls (45001 § 8.1.2; this also exists in EM 385-1-1 / OSHA).

## ISO 45001 Hazard ID Requirements (§ 6.1.2)

The OH&S management system must:

1. **Identify hazards** including:
 - Routine and non-routine activities.
 - Activities of all persons (workers, contractors, visitors).
 - Past relevant incidents.
 - Emergency situations.
 - Human factors (fatigue, ergonomic, stress).
 - Conditions / changes in the workplace.
 - Hazards arising from the operations (including legacy hazards on a site).
2. **Assess OH&S risks and other risks**.
3. **Determine and assess opportunities** for OH&S improvement.
4. **Determine legal & other requirements** applicable to hazards.

## Workflow

### Step 1: Coverage Check (Annual + Project)

The AHA program covers construction-site activities well. Verify the 45001-required coverage is complete by adding 45001-driven entries the AHA program might miss:

- **Office work** — ergonomics, slips/trips/falls, fire egress.
- **Vehicle operations** — driving to sites (especially OCONUS / remote routes).
- **Office visitor hazards.**
- **Remote / telework** — ergonomic, home-office safety, isolation.
- **Mental health and human factors** — workload, harassment, work hours.
- **Travel** — federal-customer site travel, OCONUS travel.
- **Emergency situations** beyond construction (active shooter, weather event, IT outage's safety implications).

### Step 2: Worker Consultation (§ 5.4)

ISO 45001 differentiates itself from prior standards by requiring **active worker consultation and participation** in hazard ID and risk assessment. EM 385-1-1 implies this through toolbox talks; 45001 makes it explicit and documented.

Mechanisms AF uses:

- **Daily toolbox talks** — workers raise concerns; documented in the talk record.
- **Site safety committees** with worker representatives.
- **Anonymous reporting** channel for safety concerns.
- **Annual worker safety survey.**
- **Worker review of significant AHAs** before approval.
- **Worker participation in incident investigations** where appropriate.

Document the consultation:
- Who was consulted.
- What was raised.
- How it was addressed.

### Step 3: Hierarchy of Controls (§ 8.1.2)

For each identified hazard, controls applied in order:

1. **Eliminate** the hazard.
2. **Substitute** with less hazardous.
3. **Engineering controls** (guardrails, shielding, ventilation).
4. **Administrative controls** (training, signs, procedures, permits, scheduling).
5. **PPE** as last resort.

Document why higher-order controls weren't used where PPE is the primary control — that documentation is itself audit evidence.

### Step 4: Legal & Other Requirements (§ 6.1.3)

Maintain a **legal & other requirements register** for OH&S:

- **OSHA 29 C.F.R. Part 1926** (construction).
- **OSHA 29 C.F.R. Part 1910** (general industry, for office).
- **EM 385-1-1** (USACE work).
- **State OSHA equivalents** where they're more stringent.
- **Customer-specific safety requirements** flowed down in contracts.
- **CWHSSA** (40 U.S.C. ch. 37) — overtime safety standards on federal contracts.
- **Drug-Free Workplace Act** (FAR 52.223-6).
- **State workers' comp** regulations.
- **Davis-Bacon successor** CBA safety provisions, if applicable.

### Step 5: Past Incident Learning (§ 6.1.2.2)

ISO 45001 explicitly requires the hazard ID process to learn from past incidents:

- Incidents investigated under `safety/incident-investigation`.
- Near-misses.
- Industry incidents in similar work (e.g., USACE district safety bulletins; OSHA enforcement bulletins).
- Customer-reported incidents.

Each AHA review checks: "Did anything happen — to us or in our industry — since the last review that should change this AHA?"

### Step 6: Risk Assessment and Significance

For each identified hazard, assess:

- **Severity** if the hazard materializes (fatality, hospitalization, lost-time, first-aid).
- **Likelihood** given current controls.
- **Significance** — significant hazards get formal controls, monitoring, and management-review attention.

Significance methodology should be documented and consistent.

### Step 7: Integration with Other Standards

- **27001** — physical-security hazards (intrusion, theft, ergonomic for cleared work).
- **14001** — environmental incidents that also injure (chemical exposure, hazmat).
- **9001** — quality failures with safety implications (e.g., defective PPE).

A finding under 45001 often has implications under the others; raise them.

## Hard Rules

- **All four 45001-required activity types** (routine, non-routine, emergency, all-persons including visitors) covered. Gaps are findings.
- **Worker consultation documented.** Not asserted — recorded.
- **Hierarchy of controls applied in order.** Don't lead with PPE.
- **AHA system is the operational hub.** Don't run a separate 45001-only hazard register that doesn't match the AHA in use on the site — the surveillance auditor will find the mismatch.
- **Mandatory disclosure (FAR 52.203-13)** — if hazard ID reveals fraud (e.g., we billed for controls that don't exist), route to GC.

## Output Format

```markdown
## OH&S Hazard ID / Risk Assessment — [Scope / Project]

**Scope:** [activity, site, period]
**Standards covered:** ISO 45001 § 6.1.2 + EM 385-1-1 (AHA program) + OSHA 1926 / 1910 as applicable
**Method:** [AHA template; risk matrix in use]

### Activities Covered
- Routine:
- Non-routine:
- Emergency:
- Visitor / non-worker:
- Human-factors entries:

### Worker Consultation Evidence
- Mechanisms used:
- Personnel consulted:
- Concerns raised and how addressed:

### Legal & Other Requirements Register
[link to register; new / changed entries]

### Past Incident Learning Integrated
[incidents reviewed; resulting AHA changes]

### Significant Hazards (this period)
| Hazard | Severity | Likelihood | Significance | Controls (hierarchy) | Owner |

### Cross-Standard Implications
[9001 / 14001 / 27001 issues raised]
```
