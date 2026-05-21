---
name: app-development
description: Draft an Accident Prevention Plan (APP) for an Aleut Federal construction project per USACE EM 385-1-1 Section 01.A and OSHA 29 C.F.R. Part 1926. Covers project-specific safety requirements, site safety personnel and qualifications, hazard identification and controls, training, emergency procedures, subcontractor safety integration, and the SSHO authority. Use when starting a new construction project or recompeting one with a USACE / NAVFAC / AFCEC customer.
argument-hint: "<project name or contract>"
---

# /app-development — Aleut Federal Safety

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Draft an **Accident Prevention Plan (APP)** for a federal construction project. The APP is the project's master safety document and is required by USACE EM 385-1-1 and most federal construction contracts.

## Aleut Federal Context — APP Authority and Audience

| Item | Authority |
|------|-----------|
| **EM 385-1-1** (latest revision) | USACE Safety and Health Requirements Manual — mandatory on Corps work and many other federal construction contracts |
| **OSHA 29 C.F.R. Part 1926** | Construction industry standards — applies to all federal construction |
| **FAR 52.236-13** | Accident Prevention clause |
| **Section 01.A of EM 385-1-1** | APP content requirements |
| **CWHSSA** (40 U.S.C. ch. 37) | Overtime safety standards |

The APP is reviewed by the customer's safety office (often the USACE District Safety Office or NAVFAC equivalent) **before NTP**. NTP can be held if the APP is not accepted.

## APP Required Content (per EM 385-1-1 Section 01.A)

Minimum sections (verify against the latest EM 385-1-1 revision applicable to the contract):

1. **Background information** — contractor, project, location, contract number, dates.
2. **Statement of safety and health policy** — signed by AF executive.
3. **Responsibilities and lines of authority** — at every level including subs.
4. **Subcontractors and suppliers** — how their safety integrates.
5. **Training** — initial site orientation, ongoing training, special-task qualifications.
6. **Safety and health inspections** — frequency, methodology, documentation.
7. **Accident reporting** — internal, OSHA, customer; near-misses.
8. **Plans (Programs, Procedures) required by the SOH Requirements Manual** — required appendices include:
   - **Activity Hazard Analysis (AHA)** procedure — see `aha-development` skill.
   - **Emergency response** — fire, medical, severe weather, active shooter, hazmat, evacuation.
   - **Hazard communication** — SDS access, labeling.
   - **Respiratory protection program** (if applicable).
   - **Hearing conservation program** (if applicable).
   - **Lead, asbestos, silica, beryllium** programs (if applicable).
   - **Fall protection program** (almost always applicable; see EM 385-1-1 Section 21).
   - **Excavation and trenching** (if applicable; OSHA 1926 Subpart P).
   - **Confined space entry** (if applicable; OSHA 1926 Subpart AA).
   - **Lockout/tagout** (if applicable; OSHA 1926.417).
   - **Crane and rigging** (if applicable; EM 385-1-1 Section 16).
   - **Steel erection** (if applicable; OSHA 1926 Subpart R).
   - **Demolition** (if applicable; OSHA 1926 Subpart T).
   - **Hot work / welding / cutting** (if applicable).
   - **Electrical safety** (always required).
   - **Diving operations** (if applicable; EM 385-1-1 Section 30).
   - **Marine operations** (if applicable; EM 385-1-1 Section 19).
9. **Risk management process** — formal risk assessment methodology.
10. **Medical support** — qualified first aid, medical evacuation plan.

## Workflow

### Step 1: Gather Project Inputs

- Contract number, customer, agency.
- Site location and conditions (urban, remote, OCONUS, climate, soil, environmental).
- Scope of work and major activities.
- Anticipated trades and special activities (heights, confined space, hot work, etc.).
- Identified subs.
- AF site-safety personnel: **Site Safety and Health Officer (SSHO)** name and qualifications.
- Government POC (typically a Quality Assurance Representative + Safety Office).

### Step 2: Verify SSHO Qualifications

EM 385-1-1 Section 01.A specifies SSHO qualifications. Verify before naming in the APP:

- Required training (typically OSHA 30 + EM 385-1-1 / USACE Construction Quality Management for Contractors / 40 CFR HAZWOPER if applicable).
- Years of construction safety experience (typically 5+ for general; project complexity may require more).
- Authority to **stop work** for safety reasons — must be explicit.
- Site presence requirement (typically full-time on-site; alternate when SSHO is off-site).

### Step 3: Draft Each APP Section

Use the EM 385-1-1 Section 01.A outline as the template. Customize to the project — generic boilerplate APPs are rejected by USACE safety offices.

### Step 4: Build the AHA Index

Each major activity gets its own Activity Hazard Analysis (AHA). The APP includes the index; individual AHAs are appendices or living documents updated on-site (see the `aha-development` skill).

### Step 5: Subcontractor Integration

How AF integrates subs into the safety program:
- Sub-specific orientation at site.
- Sub APP / safety plan acceptance (or sub adopts our APP).
- Sub responsibilities in the AHA process.
- Daily / weekly safety coordination meetings.

### Step 6: Submit and Iterate

Customer safety office reviews and returns comments. Address every comment in writing. Re-submit. Get approval **before NTP**.

### Step 7: Maintain and Update

The APP is a living document. Update when:
- Scope changes.
- New activities or trades arrive.
- An incident or near-miss reveals a gap.
- New subs come on board.
- Regulatory change (new EM 385-1-1 revision, new OSHA standard).

## Hard Rules

- **No APP, no NTP.** Don't start construction without an accepted APP.
- **SSHO has stop-work authority.** Bake it into the APP and the SSHO's job description. Never override the SSHO on a safety stop without senior leadership + customer involvement.
- **Subcontractors don't get exemptions.** All subs comply with the APP or their own approved sub-APP.
- **Update on incident.** A recordable incident (OSHA 300 entry) triggers APP review for the activity involved.
- **Davis-Bacon CBA successor implications** — if a CBA covered the predecessor, safety-relevant provisions may transfer.

## Output Format

Use the EM 385-1-1 Section 01.A section structure as the deliverable outline; cite the EM 385-1-1 revision used. Note any contract-specific deviations the customer approved.
