---
name: it-vendor-onboarding
description: Onboard a new IT vendor (SaaS, hardware, software, MSP, MSSP) for Aleut Federal — full federal-contractor diligence including SAM exclusions / FAPIIS, Section 889 representation, Buy American / TAA on hardware, FedRAMP authorization for SaaS handling CUI, CMMC / SPRS posture if vendor handles our CUI, BAA on personal data, BAA on infrastructure. Use when introducing a new IT tool, replacing an existing tool, or renewing a vendor agreement.
argument-hint: "<vendor name or product>"
---

# /it-vendor-onboarding — Aleut Federal CIO Shop

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Onboard a new IT vendor with the full federal-contractor diligence stack. This skill is for **internal IT vendors** that AF uses for its own corporate operations; for **subcontractors on a federal customer contract**, use `operations/vendor-review`.

## Aleut Federal Context — Federal-Contractor IT Vendor Gates

Any IT vendor that touches AF systems carrying CUI, supports a federal contract, or is paid by federal indirect cost dollars must clear these gates.

| # | Gate | Authority | When required |
|---|------|-----------|---------------|
| 1 | Active **SAM.gov** registration; not in SAM exclusions list | FAR 9.405 | Always |
| 2 | **FAPIIS** review for adverse entries | FAR 42.1503 | Always |
| 3 | **Section 889** representation — vendor does not provide / use covered telecom (Huawei, ZTE, Hytera, Hikvision, Dahua) | FAR 52.204-25; DFARS 252.204-7018 | Always |
| 4 | **Buy American Act / TAA / BABA** for hardware | FAR 52.225-x; Public Law 117-58 Title IX | Hardware purchases on federal-funded work |
| 5 | **CAGE code** issued | DLA | Always for federal-billable spend |
| 6 | **OFAC SDN / sanctioned-party screen** | OFAC | Always |
| 7 | **FedRAMP authorization** at appropriate level | OMB M-22-18 | SaaS handling CUI for federal customer or AF internal CUI |
| 8 | **DFARS 252.204-7012 / NIST 800-171 compliance** + **SPRS score** posted | DFARS | Vendor handles AF CUI |
| 9 | **CMMC** level appropriate to data | DoD CIO | Vendor handles DoD CUI |
| 10 | **Privacy / BAA / DPA** | HIPAA / state law | Vendor handles PII / PHI |
| 11 | **EU GDPR / international transfer mechanism** | GDPR + Schrems II | EU data subjects involved |
| 12 | **Insurance** (cyber liability, E&O, GL) certificates of insurance with AF as additional insured | AF Policy | Standard for any IT vendor |
| 13 | **Audit access** rights in the contract | FAR 52.215-2 (if cost-billable) | Cost-reimbursable or T&M flow-down |
| 14 | **Termination / data-return** terms | AF Policy | Always |
| 15 | **Subprocessor / fourth-party** notification | AF Policy | SaaS / MSP / MSSP |

A vendor that fails any gate is **not approvable** without a documented compensating control and explicit GC + CISO sign-off.

## Workflow

### Step 1: Classify the Vendor

| Type | Examples | Diligence depth |
|------|----------|-----------------|
| **SaaS — handles CUI** | M365 GCC High, GovCloud, ServiceNow GCC | All 15 gates; deep |
| **SaaS — no CUI** | Slack Enterprise (commercial), Asana, Monday | Gates 1–6, 10, 12, 14, 15 |
| **Hardware vendor** | Laptops, switches, scanners | Gates 1–6, 12; BAA/TAA on each SKU |
| **MSP / MSSP** | Managed IT or security service | All 15 gates; deep + audit rights |
| **Software (on-prem)** | License-only software | Gates 1–6, 14, 15; CMMC if it ingests CUI |
| **Professional services (consulting, integration)** | Implementation partners | Gates 1–6, 12, 13, 14 |

### Step 2: Run the Gates

For each applicable gate:
- Document the evidence (screenshot of SAM.gov page, vendor's Section 889 attestation letter, FedRAMP marketplace listing URL, SPRS score, CMMC certification, COI PDF, BAA executed, etc.).
- File the evidence in the vendor record in the AF Vendor Master.
- Note any gaps with a compensating-control proposal.

### Step 3: Contract Review

- Standard MSA + appropriate addendums (DPA, BAA, SLA).
- Flow-downs we need: Section 889 reps refreshed annually, audit access on cost-type work, data return on termination, breach notification within 24–72 hours, subprocessor notification, FedRAMP / CMMC maintenance, AF-favorable termination for convenience.
- Coordinate review with Legal / GC for any IT vendor with material spend or CUI exposure.

### Step 4: Technical Integration

- Identity / SSO provisioning (Entra / Okta).
- MFA enforced.
- IP / network segmentation per role.
- Logging integration (SIEM ingest).
- Data classification labels propagate where vendor supports them.
- Backup / data-portability tested.

### Step 5: Approve, Document, and Add to Vendor Master

- Add to AF Approved Vendor List.
- Add to AF Subprocessor Registry (if relevant for downstream customer DPAs).
- Annual re-attestation calendar entry.
- CMMC POA&M / SSP update if a control was affected.

### Step 6: Annual Re-attestation

Run on each anniversary:
- SAM status active; not excluded.
- Section 889 rep refreshed.
- FedRAMP authorization still current (some lapse).
- CMMC level still met.
- SPRS score current.
- Insurance current.
- Subprocessor list current.

## Hard Rules

- **Never use a SAM-excluded / debarred vendor** for any IT purpose, ever.
- **Never use a covered Section 889 vendor** anywhere in AF operations (or its supply chain on Part B).
- **Never put AF CUI in a non-FedRAMP-authorized (or CMMC-equivalent) SaaS.**
- **Never accept a Section 889 representation that has expired.**
- **Never sign a vendor MSA without GC review** for any material IT contract.
- **Never use a vendor that fails the OFAC SDN screen.**

## Output Format

```markdown
## IT Vendor: [Vendor / Product]

**Vendor type:** [SaaS / Hardware / MSP / MSSP / Software / PS]
**Use case:** [what this is for]
**Data handled:** [public / PII / FOUO / CUI / classified]
**Federal-customer touch:** [None / Indirect / Specific contract]
**Spend tier:** [< $10K / $10–100K / $100K–1M / > $1M]

### Gate Status
| # | Gate | Status | Evidence |
| 1 | SAM.gov active, not excluded | ✅ / ❌ / N/A | [link] |
| ... | | | |

### Contract Posture
- MSA: signed / draft / not started
- DPA: ...
- BAA: ...
- Insurance: ...
- Audit rights: ...
- Termination / data-return: ...

### Technical Integration
- SSO / MFA: ...
- Logging / SIEM: ...
- Network segmentation: ...
- Data labeling: ...

### Approvals
| Role | Name | Decision | Date |
| CISO | | | |
| CIO | | | |
| GC (for material) | | | |
| CFO (for spend) | | | |

### Annual Re-attestation Due
[date]
```
