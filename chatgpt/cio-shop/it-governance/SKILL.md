---
name: it-governance
description: Aleut Federal IT governance and policy decisions — IT investment / portfolio reviews, technology standards setting, enterprise architecture decisions, IT policy authoring and approval cycle, exception requests, executive IT reporting up to AF leadership and Aleut Corp. Use when proposing a major IT investment, writing or revising an IT policy, granting a policy exception, or preparing IT updates for leadership.
---

# /it-governance — Aleut Federal CIO Shop

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Run the IT governance cycle for Aleut Federal: investment decisions, technology standards, policy authoring, exception handling, executive reporting.

## Aleut Federal Context — Federal-Contractor IT Governance Drivers

Standard IT governance plus federal-contractor-specific drivers:

- **Allowable cost (FAR Part 31)** — IT investments billable to the Government must be allowable, allocable, and reasonable. Some IT spend is direct (single-contract); some is indirect (G&A or OH pool).
- **CAS compliance** — material IT cost reclassifications can trigger Cost Accounting Standards considerations on CAS-covered awards.
- **Aleut Corp reporting** — material IT decisions surface in parent reporting.
- **CMMC / NIST 800-171** posture — every technology standard must work within the SP 800-171 control baseline.
- **Section 889 / supply chain** — standards must specify only compliant vendors.
- **BAA / TAA / BABA** — hardware standards must be domestic-preference compliant on covered work.
- **FedRAMP** — cloud SaaS handling CUI must be FedRAMP-authorized.
- **Records retention** — IT decisions retained per FAR 4.703.
- **OCONUS** — Alaska / Pacific operations need locality-aware tooling.

## Workflow

### IT Investment / Portfolio Review

Standing quarterly review of the IT investment portfolio:

1. **Inventory the active IT investments** — projects + run-rate spend by category (infrastructure, security, productivity, contract-specific tooling, etc.).
2. **Map to AF strategy** — does this investment support a strategic capability?
3. **Cost classification** — direct vs indirect; allowable vs unallowable under FAR Part 31.
4. **Rate impact** — what does this do to our indirect rates? Coordinate with Finance before approval.
5. **Compliance posture** — does this strengthen or weaken our CMMC / NIST 800-171 / Section 889 posture?
6. **Decision** — fund / continue / defer / kill.

Investment threshold for IT Governance Board approval typically $X (set by local policy); below that, CIO discretion.

### Technology Standards

Standard sets the approved choice for a category (e.g., "AF endpoint EDR standard = CrowdStrike Falcon for cleared and CUI environments; Microsoft Defender for Endpoint on standard laptops").

When proposing or revising a standard:

- **Federal compliance** — meets NIST 800-171 / CMMC level applicable to the use case; Section 889 / TAA-compliant; FedRAMP-authorized if cloud + CUI.
- **Aleut Corp alignment** — coordinate with parent if there's a shared-standard expectation.
- **Cost** — total cost of ownership, including federal-cost-allowability.
- **Exit cost** — replacing the standard later.
- **Owner** — who maintains the standard.
- **Effective date and review cadence** — annual minimum.

### IT Policy Authoring and Approval

For new or revised policies entering the Policy / Procedure Library:

1. **Draft** by the policy owner (typically CIO, CISO, Compliance Officer).
2. **Identify the controlling authority** (FAR / DFARS / CFR / U.S.C. / NIST / state law).
3. **Audience** and **scope** clearly defined.
4. **Review** by Legal (compliance fit), CISO (security fit), HR (employee-facing fit), Aleut Corp (if material).
5. **Approve** at the appropriate level (IT Governance Board, executive committee).
6. **Publish** in the Policy / Procedure Library; communicate broadly.
7. **Training and acknowledgment** for affected populations.
8. **Annual review** by the owner.

### Policy Exception

When an employee or team needs to deviate from policy:

- **Documented justification** (business need; why standard doesn't work).
- **Compensating control** (what mitigates the risk).
- **Time-bound** (rare to grant permanent exceptions).
- **Approver** per the policy's exception matrix (often CISO + CIO; CO/COR for contract-affecting exceptions).
- **Compliance impact** — does this affect NIST 800-171 / CMMC posture? POA&M entry if yes.
- **Logged** in the exception register.

### Executive IT Report

Monthly or quarterly to AF leadership; quarterly summary to Aleut Corp.

Standard content:
- **CMMC / NIST 800-171 posture** — SPRS score; POA&M aging; material changes.
- **Cyber incidents** — number, severity, status; any DFARS 252.204-7012 reports filed.
- **Major investments** — status of in-flight projects.
- **Cost / rate posture** — IT spend vs budget; indirect-rate impact.
- **Vendor compliance** — Section 889 attestations refreshed; FedRAMP authorizations current.
- **Audits and assessments** — DCAA, DCMA, IPA, C3PAO findings; remediation status.
- **Headcount and talent** — IT headcount, cleared staff, key roles.
- **Risks** — top IT risks with mitigation status.

Mandatory-disclosure activity stays in a counsel-restricted appendix (FAR 52.203-13 disclosure log).

## Hard Rules

- **Never set a technology standard that fails federal-compliance gates** (Section 889 / TAA / CMMC / FedRAMP).
- **Never grant a policy exception that exposes us to FCA / mandatory-disclosure risk.**
- **Never approve a major IT investment without Finance signing off on indirect-rate impact.**
- **Mandatory disclosure (FAR 52.203-13)** — credible-evidence concerns from governance reviews route to GC.
- **Aleut Corp** — material IT governance decisions are reported up to parent per the AF–Aleut Corp reporting cadence.

## Output Format

Tailor to the governance action. Common pattern:

```markdown
## IT Governance Item: [...]

**Type:** [Investment / Standard / Policy / Exception / Report]
**Sponsor / Owner:** [...]
**Status:** [...]

### Summary
[1–2 paragraphs]

### Federal Compliance & Cost Implications
- Section 889 / TAA / BABA:
- CMMC / NIST 800-171 impact:
- FAR 31.205 allowability:
- Indirect-rate impact:

### Approvals
| Role | Name | Decision | Date |

### Action Items
[with owners and dates]
```
