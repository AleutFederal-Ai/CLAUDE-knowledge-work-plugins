---
name: document-control
description: Manage controlled documents in Aleut Federal's ISO management systems — version control, approval workflow, distribution, retention, retrieval, and obsolete-document handling. Covers policies, procedures, work instructions, SSPs, APPs, AHAs, SoA, registers, training materials, and external documents (standards, regulations) required to operate. Required by ISO 9001 § 7.5 / 14001 § 7.5 / 45001 § 7.5 / 27001 § 7.5.
argument-hint: "<doc-id or category>"
---

# /document-control — Aleut Federal ISO

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Manage controlled documents across all four AF ISO management systems. Document control is the unglamorous backbone — uncontrolled documents are the most common finding at surveillance audits.

## Aleut Federal Context — What Gets Controlled

| Document type | Standard(s) | Owner |
|---------------|-------------|-------|
| **Quality Policy / Manual** | 9001 | Quality Manager |
| **Environmental Policy** | 14001 | Environmental Manager |
| **OH&S Policy** | 45001 | Safety Director |
| **ISMS Policy + SoA** | 27001 | ISMS Manager / CISO |
| **Procedures** | All | Process owners |
| **Work Instructions** | All | Process owners |
| **System Security Plans (SSPs)** | 27001 + cross to CIO-shop | CISO |
| **APPs (Accident Prevention Plans)** | 45001 + cross to Safety | Project SSHO |
| **AHAs** | 45001 + cross to Safety | SSHO / competent person |
| **Aspects / Impacts register** | 14001 | Environmental Manager |
| **Compliance Obligations register** | 14001 / 45001 / 27001 | Owners by regime |
| **Risk Treatment Plan + POA&M** | 27001 (and NIST 800-171) | CISO |
| **Training materials** | All | Training owner |
| **Forms and templates** | All | Process owners |
| **External documents** (FAR/DFARS, NIST, OSHA, EM 385-1-1, ISO standards themselves, customer specs) | All | Document control function |
| **Records** (output of the system — see below) | All | Per retention schedule |

Records (the outputs that prove the system ran — audit reports, inspection logs, training rosters, CAPA records, incident reports) are also controlled but under records management, not document control proper.

## Document Control Requirements (ISO 9001 § 7.5 et al.)

1. **Approval** — documents approved by authorized personnel before issue.
2. **Review and updates** — periodic review; re-approval after revision.
3. **Identification** — title, document ID, version, effective date, owner.
4. **Distribution** — relevant documents available at points of use.
5. **Legibility** — readable, retrievable.
6. **External documents** identified and their distribution controlled.
7. **Obsolete documents** — prevented from unintended use; retained obsolete copies marked.
8. **Suitable retention** — records retained per the retention schedule.

## Workflow

### Document Lifecycle

1. **Draft** — owner drafts; circulates for review.
2. **Review** — affected parties review; comments incorporated.
3. **Approve** — authorized approver(s) sign; effective date set.
4. **Distribute / publish** — document control places in the controlled library; notifies users; trains where required.
5. **Use** — users access the current version from the library only; no local copies in production.
6. **Review cycle** — annual at minimum; triggered when underlying authority changes (FAR/DFARS revision, ISO revision, customer requirement change, incident lessons-learned).
7. **Revise** — incorporate changes; bump version; loop back to Review/Approve.
8. **Supersede** — old version marked superseded; retained for retention period; current version replaces.
9. **Retire** — document no longer used; retained or destroyed per retention schedule.

### Document ID Convention

Suggested format: `<Org>-<Category>-<Type>-<Number> Rev <X.Y>`

Examples:
- `AF-QMS-PR-001 Rev 3.0` — Quality Management System Procedure 001, Rev 3.0.
- `AF-ISMS-WI-014 Rev 1.2` — ISMS Work Instruction 014, Rev 1.2.
- `AF-SAFETY-PLAN-USACE-123-001 Rev 0.1` — APP for USACE contract 123, project 001.

Stable IDs survive revisions; the revision number tracks change.

### Record vs. Document

- **Document** = "how we do it" (procedure, plan, policy). Lives in the controlled library.
- **Record** = "evidence we did it" (filled-out checklist, signed roster, audit report, incident report). Lives in the records management system with retention per regime.

A blank inspection form is a document. The signed form after inspection is a record.

### Retention Schedules

Default minimums (verify per regime):

| Record type | Minimum retention | Authority |
|-------------|-------------------|-----------|
| **Federal contract records (general)** | 3 years after final payment | FAR 4.703 |
| **OSHA injury/illness records** | 5 years following the year they cover | 29 C.F.R. 1904.33 |
| **Davis-Bacon payroll** | 3 years after contract completion | 29 C.F.R. 5.5(a)(3)(i) |
| **DCAA-auditable cost records** | Per FAR 4.703 + statute of limitations on FCA (often 6 years) | FAR / 31 U.S.C. § 3731 |
| **Cleared personnel records** | Per DCSA / agency security | Various |
| **CUI records** | Per the controlling agency** | Various |
| **Asbestos / lead / radiation exposure** | 30 years after termination of employment | 29 C.F.R. 1910.1020 |
| **Environmental compliance records** | Per the permit / regulation | Various |

Document retention combines the longest applicable regime — when in doubt, ask GC.

### Obsolete Document Handling

- Mark obsolete copies clearly (watermark or stamped).
- Move to obsolete archive in the controlled system.
- Prevent unintended use — make searches default to current; obsolete only by explicit request.
- Retain per retention schedule.
- Destroy per retention schedule and the destruction record itself becomes a record.

### External Documents

External documents we depend on (FAR, DFARS, NIST publications, OSHA standards, EM 385-1-1, ISO standards, customer specifications):

- Identified in the controlled library with the version we use.
- Distribution controlled — point of use has the right version.
- Subscription / alerting service for updates.
- Update process: when a new revision lands, evaluate impact and plan transition.

## Hard Rules

- **No uncontrolled documents in production use.** A worker following an obsolete procedure is the textbook finding.
- **Local copies are not allowed** unless explicitly designated as controlled-by-reference and managed.
- **Approval before issue** is non-negotiable.
- **Record retention follows the longest applicable regime.**
- **CUI documents** live only in CUI-authorized environments.
- **Mandatory disclosure (FAR 52.203-13)** — if document control failures contributed to fraud / criminal / significant overpayment, route to GC.

## Output Format

```markdown
## Document Control Action: [New / Revise / Obsolete / Retain]

**Document ID:** [...] | **Title:** [...]
**Owner:** [...] | **Approver(s):** [...]
**Standard(s):** [...]
**Effective date:** [...] | **Review due:** [...]

### Change Summary
[what changed in this revision]

### Distribution
- Library updated: ✓
- Users notified: [list / population]
- Training required: [Yes/No, scheduled]

### Cross-Standard Implications
[other documents this revision affects]

### Records Implications
[any new records this document generates; retention]

### Obsolete Version
- Marked obsolete: [version]
- Archive location: [...]
- Destruction date (if applicable): [...]
```
