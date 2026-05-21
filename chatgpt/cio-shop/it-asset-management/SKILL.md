---
name: it-asset-management
description: Track Aleut Federal IT assets — hardware (laptops, mobile, networking, peripherals), software licenses, SaaS subscriptions, cloud tenants. Maintain CMDB with Section 889 compliance, BAA / TAA / BABA country-of-origin tracking on hardware, license utilization, lifecycle and refresh planning, and chain-of-custody for Government-furnished property (GFP). Use when adding / retiring an asset, doing annual inventory, responding to a property audit, or evaluating a refresh.
---

# /it-asset-management — Aleut Federal CIO Shop

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Track AF IT assets — corporate-owned and Government-furnished — with the federal-contractor accountability that goes with them.

## Aleut Federal Context — Why IT Asset Tracking Matters for Us

Three drivers force more discipline than a typical commercial shop:

1. **DFARS 252.245-7003 (Government Property Management System)** — when AF holds GFP, we run a property system to DFARS standards. Failure can disapprove the business system and trigger payment withholding.
2. **Section 889 compliance** — we must be able to demonstrate (at any time) that no covered telecom equipment from prohibited entities (Huawei, ZTE, Hytera, Hikvision, Dahua) is anywhere in our operations or supply chain.
3. **BAA / TAA / BABA country-of-origin** — on contracts with domestic-preference clauses, we must demonstrate hardware origin. The CMDB is the evidence source.

## CMDB Schema

Each asset record holds:

- **Asset ID** (AF-prefixed serial / barcode).
- **Type** (laptop / desktop / server / mobile / network / peripheral / storage / printer).
- **Make / Model / Serial Number**.
- **Country of manufacture / final assembly** (for BAA/TAA/BABA evidence).
- **Section 889 status** — confirmed not covered? Vendor attestation reference.
- **Owner** (employee / role / cost center).
- **Location** (site / address / OCONUS code).
- **Status** (active / in-stock / repair / retired / lost / stolen).
- **Acquisition date and PO**.
- **Cost** + **depreciation schedule** (cost-accounting impact).
- **Funding source** (corporate G&A / specific contract / B&P / IR&D / GFP).
- **CUI eligibility** — is this asset authorized for CUI? (Locked down per the SSP, encrypted, MDM enrolled, FIPS-validated.)
- **MDM / EDR enrollment status**.
- **Encryption status** (full-disk encryption verified; FIPS module).
- **Last access verified** (active or idle).
- **Disposition plan / refresh year**.

For GFP specifically:
- **Contract number** the property is associated with.
- **DD Form 1149 / SF 1428** receipt reference.
- **Custody** chain (who has it, signed for it, where it lives).
- **Return condition** at contract end.

## Workflow

### Add (joiner / refresh / new project)

1. Procurement step gates:
 - **Section 889 attestation** from the vendor (in our IT vendor onboarding).
 - **Country of origin** on the SKU; verify TAA-compliant country if a covered contract.
 - **BAA / BABA**: domestic-content evidence if needed for an infrastructure contract.
2. Imaging:
 - Standard AF image with full-disk encryption, MDM, EDR, baseline software set.
 - PIV/CAC reader / smartcard middleware if cleared role.
 - CUI-environment configuration if the role requires.
3. Enrollment:
 - MDM, EDR, AAD/Entra join, SIEM ingest.
 - Add to CMDB with all schema fields populated.
4. Assignment:
 - Issued to employee; signed receipt; serial captured.

### Retire / Lost / Stolen

1. **Immediate** on report of loss or theft:
 - Remote-wipe via MDM.
 - Notify CISO; assess for cyber incident.
 - For cleared / CUI device: notify FSO.
 - For potential cyber incident on CUI device: trigger DFARS 252.204-7012 evaluation; 72-hour DIBNet clock may apply.
2. **Routine retirement**:
 - Secure data wipe (NIST 800-88 sanitization).
 - Asset disposition: corporate-owned → e-waste vendor with certificate of destruction; GFP → return per contract terms with DD Form 1149.
 - CMDB updated; preserve the record for FAR 4.703 retention.

### Annual Inventory

- Full reconciliation between CMDB and physical / SaaS reality.
- Section 889 re-attestation pass: confirm nothing covered has crept into the supply chain.
- BAA/TAA/BABA evidence refreshed where required.
- License utilization analysis: drop unused; consolidate.
- GFP reconciliation against the prime contract's property accountability.
- Findings → property report to contract administration where required.

### Property Audit (DCMA / customer)

Prepare the audit package:
- CMDB extract for the in-scope items.
- DD Form 1149s / receipts.
- Custody chain.
- Disposition records.
- Section 889 attestations.
- TAA / BAA / BABA certifications.

Single point of contact for the auditor; log every RFI.

### Refresh Plan

- Lifecycle policy (typically 3–4 years for laptops; 5–7 for servers / network).
- Budget impact (G&A vs. allocable to specific contracts).
- Capacity, performance, and warranty drivers.
- Section 889 + TAA / BAA implications on new SKUs.
- CUI / CMMC posture impact (any control implementations affected).

## Hard Rules

- **Never acquire IT hardware without Section 889 / TAA evidence on file** for contracts that require it.
- **Never dispose of an asset without confirmed NIST 800-88 sanitization** when it ever held CUI / PII / sensitive AF data.
- **Never lose GFP without immediately notifying the COR and Contracts.** Loss of GFP must be reported per the contract; failure to report is its own exposure.
- **Annual Section 889 re-attestation** for the entire fleet.
- **Mandatory disclosure (FAR 52.203-13)** — if asset tracking reveals fraud, theft, or significant misappropriation, route to GC.

## Output Format

```markdown
## IT Asset Action: [Add / Retire / Inventory / Audit / Refresh Plan]

**Date:** [...] | **Owner:** [...]

### Items Affected
| Asset ID | Type | Make/Model | Country of Origin | Section 889 | TAA/BAA | Funding | Status |

### Compliance Cross-Check
- Section 889 attestations on file: [Yes / No / Action]
- TAA / BAA / BABA evidence (covered contracts): [Yes / No / Action]
- GFP reconciliation (if applicable): [Yes / No / Action]
- CUI-asset MDM/EDR/encryption: [Yes / No / Action]

### Findings
[discrepancies, missing evidence, items to remediate]

### Next Actions
[with owners and dates]
```
