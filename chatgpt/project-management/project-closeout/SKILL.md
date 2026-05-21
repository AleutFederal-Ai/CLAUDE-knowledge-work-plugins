---
name: project-closeout
description: Run formal closeout of an Aleut Federal federal project — final CDRL delivery, customer acceptance, financial reconciliation, property return (GFP / GFE), CPARS final input, subcontractor closeout, lessons learned, record archival, and option-period planning if applicable. The most underrated phase of a federal contract — sloppy closeout costs revenue, hurts CPARS, and complicates the next pursuit with the same customer.
---

# /project-closeout — Aleut Federal Project Management

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Run formal closeout of a federal project.

## Aleut Federal Context — Closeout Has Federal Teeth

Closeout is not optional housekeeping. Federal contracts have specific closeout mechanics:

| Item | Authority | Timing |
|------|-----------|--------|
| **Final CDRL delivery and acceptance** | Contract | Per CDRL schedule |
| **Final invoice / public voucher** | FAR 52.216-7 / 52.232-25 / contract | Per the closeout DD Form 1594 (FFP) or final voucher (cost-type) timeline |
| **Cumulative claim and reservation of rights** | Per contract | With final invoice on cost-type |
| **CPARS final evaluation** | FAR 42.15 | Within ~120 days of completion (the Government's clock) |
| **GFP / GFE return** | FAR 52.245-1 / contract | At contract end |
| **Property disposition reporting (DD Form 1149)** | DFARS 252.245-7003 | Per the contract |
| **Records retention** | FAR 4.703 | 3 years after final payment (longer for some records) |
| **Indirect rate finalization (cost-type)** | FAR 52.216-7 | Annual ICS feeds rate negotiation; affects this contract's final billing |
| **Subcontractor closeouts** | Per sub agreements | Cascade per prime closeout |
| **Bond release (construction)** | Per surety / Miller Act | After final acceptance |

Closeout poorly done leaves money on the table (unbilled cost on cost-type; unreleased retainage on construction; bond release delayed; final invoicing past statute), poisons the CPARS narrative ("Closeout — Marginal"), and complicates recompete or future pursuits with the same customer.

## Workflow

### Phase 1: Pre-Closeout Planning (60–90 Days Before PoP End)

- **CDRL final-submission plan** — list every remaining CDRL, owner, target submission, expected acceptance.
- **Financial wind-down plan** — final invoicing schedule, indirect rate true-up status, MR drawdown closure.
- **Property return plan** — every GFP item identified, custody confirmed, return condition assessed, DD Form 1149 prepared.
- **Subcontractor closeout plan** — final invoices, releases of claims, evaluations for the AF sub-performance library.
- **CPARS strategy** — anticipate the COR's narrative; coordinate to ensure accurate accounting.
- **Customer engagement plan** — set the closeout meeting; confirm acceptance procedures.

### Phase 2: Final Deliverables (Last 30 Days of PoP)

- **Final CDRLs delivered** per the contract; acceptance documented.
- **Final reports** — close-out / lessons-learned / transition documents as required.
- **Demobilization** of construction sites or office space — final safety walks, environmental sign-offs, key returns.
- **Knowledge transfer** if the contract includes transition assistance to a successor (FAR 52.249-6 termination assistance or specific transition CDRL).

### Phase 3: Customer Acceptance

- **Final acceptance** documented in writing (often DD Form 250 / SF 1449 acceptance block; sometimes a separate acceptance letter).
- **No verbal acceptance** is sufficient — get it in writing.
- **Outstanding NCRs** addressed before acceptance.
- **Customer satisfaction survey** if formally requested.

### Phase 4: Financial Closeout

For each contract type:

**FFP / FFP-LOE:**
- Final invoice for the remaining balance.
- Verify retainage release (construction).
- Indirect rate not applicable to closeout — already burdened in the FFP price.

**T&M / Labor-Hour:**
- Final invoice for hours and ODCs incurred.
- Verify against the contract ceiling.
- Indirect rates already applied via burdened bill rates.

**Cost-Reimbursable (CPFF / CPIF / CPAF):**
- Final voucher with cumulative claim and reservation of rights.
- Confirm indirect rates — interim rates used in billings; finalized via the Incurred Cost Submission (ICS) process per FAR 52.216-7.
- **Cumulative claim**: invoice all unbilled costs (subject to the contract ceiling).
- **Reservation of rights**: preserves AF's right to bill the difference once final rates are settled (which can be years later, when DCAA closes the ICS).
- **Fee payments**: confirm any CPIF / CPAF formula payments are right.

**Construction (FFP):**
- Final invoice; retainage release; Miller Act bond release coordination.
- Lien waivers from subs and suppliers.

### Phase 5: Property and Bond Closure

- **GFP / GFE returned** per the contract; DD Form 1149 or equivalent.
- **Property loss / damage** reported (DD Form 1149 or specific contract form).
- **Bond release** — coordinate with surety once final acceptance is in hand.

### Phase 6: Subcontractor and JV Closeout

- **Sub final invoices** processed.
- **Releases of claims** from subs.
- **Sub performance evaluations** in the AF sub-performance library — supports future award decisions.
- **JV accounting closeout** per 13 C.F.R. § 124.513(d) requirements.

### Phase 7: CPARS Final Evaluation

- **AF self-evaluation** — what to claim and document.
- **Coordinate with COR** on the narrative.
- **Respond to the CPARS rating** within the 60-day comment window per FAR 42.1503; rebut factual inaccuracies in writing.
- **CPARS feeds future awards** — past-performance volumes in proposals draw from CPARS.

### Phase 8: Lessons Learned

Internal lessons-learned exercise within 30 days of closeout:

- What went well.
- What didn't.
- What changes to AF practice would help on the next similar project.
- Feedback to capture / proposal teams.
- Feedback to functional leads (Quality, Safety, Cyber, etc.).

### Phase 9: Records Archive

- **All records** retained per FAR 4.703 (3 years after final payment baseline; some categories longer).
- **Cost-type records** retained for DCAA ICS audit reach (often 6+ years from FY).
- **Safety records** per OSHA / EM 385-1-1 retention (often 5+ years; asbestos / lead 30 years).
- **Security clearance records** per DCSA / NISPOM.
- **CUI records** per the controlling agency.

### Phase 10: Option / Recompete Handoff (If Applicable)

If a follow-on option is anticipated → coordinate with `program-management/option-exercise-prep`.

If a recompete is anticipated → coordinate with `sales/account-research` and `sales/call-prep` for the BD team.

## Hard Rules

- **Final acceptance in writing.** No verbal acceptance.
- **Cumulative claim and reservation of rights** on every cost-type final voucher — protects rate-settlement money.
- **Property closeout per DFARS 252.245-7003** — losses unreported are a finding.
- **Sub final closeouts** — don't leave sub liabilities open after AF closeout.
- **CPARS factual rebuttal** — rebut errors within the 60-day window; silence is acceptance.
- **Records retention** — preserve until the longest applicable regime expires.
- **Mandatory disclosure (FAR 52.203-13)** — if closeout reveals fraud / criminal / significant overpayment evidence, route to GC.

## Output Format

```markdown
## Project Closeout — [Project / Contract]

**Contract:** [...] | **PoP end:** [...] | **Final acceptance date:** [...]
**Closeout target completion:** [PoP end + 90/120 days]

### Phase Status
| Phase | Status | Owner |
| Pre-closeout planning | | |
| Final deliverables | | |
| Customer acceptance | | |
| Financial closeout | | |
| Property / bond | | |
| Sub / JV closeout | | |
| CPARS | | |
| Lessons learned | | |
| Records archive | | |
| Option / recompete handoff | | |

### Outstanding Items
| Item | Owner | Due | Risk if late |

### Final Financial Position
- Contract type: [...]
- Total funded: $[...]
- Final invoiced: $[...]
- Outstanding (cost-type rate true-up reserved): $[...]
- Retainage released (construction): $[...]

### CPARS Status
- COR draft narrative shared: [Yes/No]
- AF response submitted: [Yes/No]
- 60-day comment window closes: [date]
- Rebuttals filed: [...]

### Lessons Learned Highlights
[for distribution to capture, functional leads, sister projects]

### Mandatory-Disclosure Check
[None / Routed to GC]
```
