---
name: environmental-aspects
description: Maintain Aleut Federal's ISO 14001 Environmental Aspects and Impacts register and the linked Compliance Obligations register. Identifies how AF's activities, products, and services interact with the environment, prioritizes significant aspects, and tracks the regulatory and customer obligations that apply. Required by ISO 14001 § 6.1.2 and § 6.1.3.
argument-hint: "<task — review | new-activity | compliance-update>"
---

# /environmental-aspects — Aleut Federal ISO

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Maintain the **Environmental Aspects and Impacts** register and the **Compliance Obligations** register required by ISO 14001.

## Aleut Federal Context — Federal Construction Drives Most of Our Environmental Aspects

AF's environmental footprint is dominated by federal construction work:

- **Site disturbance** — soil erosion, stormwater runoff, sediment.
- **Air quality** — fugitive dust, engine emissions, hot work.
- **Water quality** — stormwater (NPDES CGP), construction-water discharge.
- **Waste** — construction & demolition debris, hazmat (lead, asbestos, silica, beryllium), hazardous waste (paint, solvent, fuel).
- **Energy / fuel** — equipment fuel consumption, generator emissions.
- **Cultural and historic resources** — Section 106 NHPA compliance during disturbance.
- **Endangered species** — Section 7 ESA consultation where applicable.
- **OCONUS** — locality-specific environmental regimes (Alaska, Pacific Islands).

Federal-contract environmental obligations on top of ISO 14001:

| Regime | Applies when |
|--------|--------------|
| **NEPA** (42 U.S.C. § 4321 et seq.) | Government conducts the NEPA review; we comply with NTP conditions |
| **CWA / NPDES CGP** | Stormwater discharge from construction sites > 1 acre |
| **CAA** | Air permits for stationary sources; mobile source emission limits |
| **RCRA** | Hazardous waste generation, storage, disposal |
| **EPCRA** | Reportable releases of listed substances |
| **TSCA** | Asbestos / lead / PCB handling |
| **NHPA § 106** | Historic-resource consultation when ground-disturbing |
| **ESA § 7** | Endangered-species consultation when ground-disturbing in habitat |
| **State and tribal** | Locality-specific |
| **Customer-imposed** | USACE / NAVFAC / agency-specific environmental requirements |
| **Davis-Bacon adjacency** | None directly, but ties to construction-only requirements |

## Aspects and Impacts Register

For each AF activity, product, or service that interacts with the environment, capture:

- **Activity** (e.g., asphalt paving at Site X).
- **Environmental aspect** — the element of the activity that interacts with the environment (e.g., asphalt fume emissions; runoff during rain; equipment exhaust).
- **Environmental impact** — the change to the environment (e.g., air quality reduction; surface water contamination; soil compaction).
- **Conditions** — Normal / Abnormal / Emergency.
- **Lifecycle stage** — Procurement / Mobilization / Construction / Operations / Demobilization.
- **Significance** — Significant / Not Significant.

Significance criteria (from AF's documented methodology):
- Severity of the impact (regulatory consequences, scale, reversibility).
- Likelihood of occurrence.
- Stakeholder sensitivity (community, customer, regulator).
- Legal / regulatory exposure.

Significant aspects get **operational controls** (procedures, training, monitoring, equipment specifications).

## Compliance Obligations Register

For each environmental regime that applies, capture:

- **Source** (statute / regulation / permit / contract clause).
- **Specific requirement** (the operational rule).
- **Trigger** — when does this apply (project type, site, scale, substance).
- **Owner** — process / project owner accountable.
- **Monitoring** — how we verify compliance.
- **Records required** — what we retain and for how long.
- **Reporting** — to whom, on what cadence.

## Workflow

### Step 1: Identify New Activities

Triggers:
- New project award.
- New scope on an existing project.
- New technology / material in use.
- New site or geography.
- Mobilization to OCONUS.

For each new activity, identify aspects + impacts and add to the register.

### Step 2: Assess Significance

Apply the documented methodology. Document the rationale for significance — auditors will challenge it.

### Step 3: Update Compliance Obligations

For each new activity, identify the regulatory regimes that newly apply or change. Update the obligations register.

### Step 4: Map to Operational Controls

For each significant aspect, link to:
- **The procedure** that controls it (e.g., Stormwater Pollution Prevention Plan / SWPPP for stormwater).
- **The AHA** if there's a worker hazard component (cross-reference to `safety/aha-development`).
- **The monitoring** that verifies effectiveness.
- **The contingency** if controls fail (cross-reference to `safety/incident-investigation` for environmental releases).

### Step 5: Communicate

- Project team briefed on significant aspects and required controls.
- Subs briefed at orientation (cross-reference to `safety/subcontractor-safety-onboarding`).
- Customer environmental office notified of any aspect with their interest.

### Step 6: Review Cadence

- **Per project**: at NTP, mid-project, and demob.
- **Annually**: full register review before Management Review.
- **Triggered**: after an environmental release / near-miss; after a regulatory change.

### Step 7: Compliance Evaluation

Per ISO 14001 § 9.1.2, periodically evaluate compliance with the obligations register. Result feeds Management Review.

## Hard Rules

- **No NTP without confirmed environmental obligations.** NEPA, permits, Section 106, ESA — Government action complete before we ground-disturb.
- **Significant aspects must have documented operational controls.** A significant aspect with no control is a major finding.
- **Reportable releases follow the regulatory clock.** EPCRA, CWA reportable quantities, RCRA — release reporting deadlines are not paced by internal investigation.
- **Records retention** per the obligation (some are decades — asbestos / lead exposure records).
- **Mandatory disclosure (FAR 52.203-13)** — if a release or non-compliance involved fraud (e.g., billed for a control we didn't implement), route to GC.

## Output Format

```markdown
## Environmental Aspects / Compliance Update — [Period]

### New Activities Added
| Project | Activity | Aspect | Impact | Significance | Operational Control |

### Changed Activities
[any aspect/impact reassessments]

### Compliance Obligations Added / Changed
| Regime | Requirement | Trigger | Owner | Monitoring | Records |

### Compliance Evaluation Results
[per § 9.1.2; trends; any noncompliance findings]

### Action Items
[from Management Review and audit]
```
