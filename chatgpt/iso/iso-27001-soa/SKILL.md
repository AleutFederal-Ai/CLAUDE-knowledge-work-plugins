---
name: iso-27001-soa
description: Manage Aleut Federal's ISO 27001 Statement of Applicability (SoA) — the document that lists every Annex A control, whether it's applicable, how it's implemented, and the justification for any exclusions. Crosswalks to NIST SP 800-171 / CMMC controls so AF's federal and ISO compliance evidence reinforces each other. Required by ISO 27001 § 6.1.3(d) and inspected at every surveillance audit.
---

# /iso-27001-soa — Aleut Federal ISO

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Manage AF's **Statement of Applicability (SoA)** — the foundational document of the ISO 27001 Information Security Management System (ISMS).

## Aleut Federal Context — SoA as the Crosswalk to NIST 800-171 / CMMC

AF's ISMS exists alongside our NIST SP 800-171 / CMMC obligations on federal-customer work. The SoA is the right place to crosswalk these:

- ISO 27001:2022 **Annex A has 93 controls** organized into 4 themes (Organizational, People, Physical, Technological).
- NIST 800-171 has **110 controls** in 14 families.
- CMMC 2.0 Level 2 aligns to NIST 800-171.
- Significant overlap; the SoA can cite the corresponding NIST control for each Annex A item.

This crosswalk:
- Reduces duplicate evidence collection (one control implementation often satisfies both).
- Makes the certification body audit faster.
- Makes the C3PAO / DCMA cyber audit faster.
- Helps AF run a single ISMS that satisfies both regimes.

## SoA Required Content (per ISO 27001 § 6.1.3(d))

For every Annex A control:

1. **Control number and name** (Annex A 5.1, 5.2, …, 8.34).
2. **Applicability** (Applicable / Not Applicable / Excluded).
3. **Implementation status** (Implemented / Partially / Not Implemented / In Progress).
4. **Description of implementation** — how AF satisfies the control.
5. **Justification** — why we say the control is applicable or not, and (if not) why we exclude it.
6. **Owner** — who maintains the implementation.
7. **Linked policies / procedures** in the AF Policy / Procedure library.
8. **Linked evidence** — where surveillance auditors find proof.

For AF, also include:

9. **NIST 800-171 / CMMC crosswalk** — the SP 800-171 control(s) this Annex A item also satisfies (or vice versa).
10. **POA&M reference** for any partially-implemented or planned controls (so the ISMS POA&M and the NIST 800-171 POA&M are the same single source of truth).

## Workflow

### Step 1: Review (Annual + Triggered)

Review cadence:
- **Annual** — full review before the recertification audit.
- **Triggered** — when a new contract requires new controls; after a significant incident; after a major system change; when NIST or ISO 27001 publishes a new revision.

### Step 2: Per-Control Review

For each Annex A control:

- **Is it still applicable** given current operations? (E.g., A.5.21 about supply chain may broaden as we onboard more SaaS.)
- **Is the implementation still effective**? (Test or audit since last review?)
- **Has the linked NIST 800-171 control implementation changed**? Sync.
- **Is the linked POA&M item still open**? If closed, update status to Implemented and capture verification.
- **Is the evidence still good and accessible**?

### Step 3: Justify Any Exclusions

A control is excluded only when it does not apply to AF's ISMS scope. Examples:

- A.5.33 (Protection of records) — if we don't process the specific record type, justify.
- A.8.22 (Segregation of networks) — if our scope doesn't include networks of the type the control addresses, justify.

Each exclusion gets a written justification. "Doesn't apply to us" without explanation will be a finding.

### Step 4: Update Linked POA&M

Any control rated Partially Implemented or Not Implemented (and applicable) goes to the **POA&M**:

- Specific gap.
- Mitigation plan with owner and dates.
- Compensating control in place.
- Risk accepted with senior sign-off (rare).

This POA&M is the **same physical document** as the NIST 800-171 POA&M to the maximum extent — one tracker, two regimes.

### Step 5: Sign-Off and Publish

- Quality Manager + CISO + ISMS Manager sign the SoA.
- Top management acknowledges in the next Management Review.
- Distributed to relevant process owners.
- Filed in the controlled-document system.

### Step 6: Surveillance Audit Prep

Before the external audit:
- SoA is current.
- Evidence packages cited in the SoA are findable.
- Recent NCRs / CAPAs related to controls are documented.
- Cross-walked NIST evidence is referenced.

The certification body will sample controls; for each sampled control, they will trace the implementation in the SoA back to the operational reality.

## Common Pitfalls

- **Over-claiming.** Don't claim a control is Implemented when it's Partial. Reality on the ground will show it; the finding is worse.
- **Outdated cross-references.** When AF policy revision numbers change, the SoA's linked policies break.
- **No evidence path.** Saying "implemented via firewall configuration" without an audit trail to the actual configuration is incomplete.
- **Stale exclusions.** Scope grows; controls previously excluded may now apply.
- **Disconnected POA&Ms.** Maintaining a separate POA&M for ISO and a separate one for NIST 800-171 is double-work and risks them drifting apart.

## Hard Rules

- **The SoA is signed by named authority** (Quality Manager, CISO, ISMS Manager) — not just published.
- **Every Annex A control has an entry** — no gaps.
- **Exclusions have justifications** — not just "N/A".
- **Crosswalk to NIST 800-171** for every applicable control where there's a corresponding family — this is how AF gets leverage from running both regimes.
- **POA&M items don't expire silently.** Each surveillance audit reviews aged items.
- **Mandatory disclosure (FAR 52.203-13)** — if SoA review reveals fraud / criminal / significant overpayment evidence (e.g., we claimed Implemented but never were and billed for it on a federal contract), route to GC.

## Output Format

The SoA is a spreadsheet / table with one row per Annex A control. Each row carries the fields listed above. The summary report for Management Review uses:

```markdown
## Statement of Applicability — [Date] — Revision [X.Y]

**ISMS scope:** [...]
**Approving authorities:** Quality Manager [name], CISO [name], ISMS Manager [name]

### Annex A Coverage Summary
| Theme | Controls | Applicable | Excluded | Implemented | Partial | Not Implemented |
| Organizational (A.5) | 37 | | | | | |
| People (A.6) | 8 | | | | | |
| Physical (A.7) | 14 | | | | | |
| Technological (A.8) | 34 | | | | | |
| **Total** | **93** | | | | | |

### NIST 800-171 / CMMC Crosswalk Status
[count of A controls with a NIST 800-171 mapping; gaps]

### POA&M Summary
[count by aging; cross-reference to CIO-shop cmmc-poam-management]

### Changes This Revision
[summary of additions, status changes, exclusion changes]
```
