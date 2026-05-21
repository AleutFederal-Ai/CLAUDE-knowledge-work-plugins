---
name: it-change-management
description: Plan, document, approve, and execute an internal IT change at Aleut Federal — production system changes, configuration baseline updates, identity / access changes, network changes, endpoint changes. Includes Change Advisory Board (CAB) review, CMMC / NIST 800-171 control impact assessment, ATO boundary check for AF systems handling CUI, rollback plan, and post-implementation review.
argument-hint: "<change description>"
---

# /it-change-management — Aleut Federal CIO Shop

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Manage IT change requests on Aleut Federal **corporate** systems. For changes to systems we operate for federal customers under a contract, the `engineering/deploy-checklist` skill handles customer-facing change procedures.

## Aleut Federal Context — Internal IT Change vs. Federal Contract Change

Two different change tracks live in this skill family:

1. **Internal IT change** (this skill) — AF corporate systems, end-user services, internal cloud tenants.
2. **Federal contract change** — see `operations/change-request` and `engineering/deploy-checklist`. Only the Contracting Officer can change scope/price/PoP on a federal contract (FAR Subpart 43).

For internal IT changes:

- **CMMC / NIST 800-171 control impact** — any change that affects a SP 800-171 control implementation needs SSP / POA&M update.
- **Internal authorization boundary** — AF corporate systems handling CUI have an authorization boundary; changes that move the boundary are significant and need an internal accreditation re-review.
- **Section 889 / supply chain** — never approve a change that introduces covered telecom from prohibited entities.
- **Configuration baseline** — every approved change updates the baseline; CCB records baseline state.
- **Records** — change tickets retained per the AF retention schedule (FAR 4.703 baseline: 3 years after final payment on any federal contract the system supports).

## Change Categories

| Category | Approval path | Examples |
|----------|---------------|----------|
| **Standard** | Pre-approved; ticket only | Password reset, account disable on offboarding, routine patching |
| **Normal** | CAB review | New service install, role permission change, network ACL change |
| **Major** | CAB + executive sign-off | New SaaS tenant, new system integration, CMMC boundary change |
| **Emergency** | Expedited CAB + post-action review | Security patch in response to active vulnerability |

## Workflow

### Step 1: Open the Change Request

Capture in the ticket:

- **Change ID**
- **Requestor / owner**
- **Category** (Standard / Normal / Major / Emergency)
- **What changes** (clear, specific scope)
- **Why** (business / compliance / security driver)
- **When** (proposed window)
- **Systems / services affected**
- **Users / contracts affected**
- **Data classification touched** (public / FOUO / CUI / classified)

### Step 2: Impact and Risk Analysis

For Normal and Major changes:

- **Compliance impact:** which NIST 800-171 controls / CMMC practices does this affect? Update SSP / POA&M as needed.
- **Boundary impact:** does this change the authorization boundary of a system handling CUI? If yes, significant change → re-accreditation.
- **Supply chain:** does this introduce a new vendor or component? Run the IT vendor onboarding gates (Section 889, SAM exclusions, FedRAMP / CMMC posture, BAA / TAA).
- **Customer impact:** does this affect a system that hosts data or services for a federal contract? If yes, coordinate with the program team for customer notification.
- **Rollback:** define the exact steps to revert, including pre-staged data.
- **Downstream effects:** what other systems, integrations, or workflows could break.
- **Operational risk** (likelihood × impact).

### Step 3: CAB Review

Normal and Major changes go to the Change Advisory Board:

- **Attendees:** CIO / IT Director, CISO, Compliance Officer, FSO (for any cleared-system change), Program lead (when a federal-customer system is affected), responsible owner.
- **Required pre-reads:** change ticket, impact analysis, rollback plan.
- **Decision:** Approve / Approve with conditions / Defer / Reject.
- **Recorded outcome:** in the ticket; signed off by named approver.

Emergency changes can be approved by the on-call senior with expedited CAB; document the deviation and present at the next CAB.

### Step 4: Execute the Change

- Implement in the approved window.
- Each step logged with timestamp and operator.
- Configuration baseline updated on completion.
- Validation tests (security + functional) pass before declaring the change complete.

### Step 5: Post-Implementation Review

- Did the change achieve the intended outcome?
- Did any rollback or stabilization activity happen?
- Update SSP / POA&M for any compliance-impacting changes.
- Update CMDB / baseline.

## Hard Rules

- **No change without an approved ticket.** Even Emergency changes need an after-the-fact ticket.
- **No CUI-relevant change without CISO sign-off.**
- **No introduction of Section 889 / non-TAA / non-FedRAMP-compliant component without an explicit waiver.**
- **No removal or weakening of a SP 800-171 control** without compensating control and POA&M entry.
- **No bypass of CAB** for Normal or Major changes, even under schedule pressure.

## Output Format

```markdown
## Change Request: [Title]

**Change ID:** [...] | **Category:** [Standard / Normal / Major / Emergency]
**Requestor:** [...] | **Owner:** [...] | **CAB Approver:** [...]
**Proposed Window:** [...] | **Status:** [Draft / CAB Review / Approved / In Progress / Complete / Rolled Back]

### Scope
[clear and specific]

### Compliance & Boundary Impact
- NIST 800-171 controls affected:
- CUI authorization boundary change? Yes / No
- Section 889 / supply-chain impact:
- Federal-customer notification needed? Yes / No, route via Contracts:

### Risk
| Risk | Likelihood | Impact | Mitigation |

### Rollback Plan
[exact steps]

### Validation Tests
[security + functional]

### Approvals
| Role | Name | Decision | Date |
| CIO | | | |
| CISO | | | |
| FSO (if applicable) | | | |
| Program lead (if applicable) | | | |

### Post-Implementation Notes
[outcome; baseline updated; SSP/POA&M updated; lessons learned]
```
