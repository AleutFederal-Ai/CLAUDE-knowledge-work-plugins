---
name: review-contract
description: Review a federal prime contract, task order, subcontract, teaming agreement, or commercial agreement against Aleut Federal's negotiation playbook and the FAR/DFARS framework — flag deviations, generate redlines, and provide business-impact analysis. Use when reviewing federal solicitations, awards, subcontract flow-downs, teaming/JV agreements, NDAs, vendor agreements, or modifications.
---

# /review-contract -- Federal Contract Review Against Playbook

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Review the agreement against Aleut Federal's playbook and the federal regulatory framework (FAR, DFARS, agency supplements). Analyze each clause, flag deviations, generate redline suggestions, and provide business-impact analysis.

**Important:** This skill assists with contract analysis; it does not provide legal advice. All outputs must be reviewed by qualified counsel before being relied upon. For any item raising potential False Claims Act, Procurement Integrity Act, or FAR 52.203-13 mandatory disclosure issues, route to senior counsel immediately.

## Invocation

```
/review-contract <contract file or URL>
```

Review the contract: @$1

## Workflow

### Step 1: Accept the Document

Accept any of:
- **File upload** (PDF, DOCX, etc.).
- **URL** in our CLM, SharePoint, Egnyte, or Box.
- **Pasted text**.
- **SAM.gov solicitation number** — if given a solicitation/RFP number, pull the latest from SAM.gov (Sections L, M, H, C, J as a minimum).

If nothing is provided, prompt the user for one.

### Step 2: Identify the Document Type

Federal agreements fall into a small set of buckets; the review changes by type:

| Type | What to look for first |
|------|------------------------|
| **Prime federal solicitation / RFP** (Section L/M/H/C/J) | Set-aside, NAICS, size standard, evaluation criteria, FAR clauses incorporated by reference, page limits, Q&A deadlines |
| **Prime federal award (SF 1449, SF 33, DD 1155, task/delivery order)** | CLINs, period of performance, funding (incremental vs fully-funded), FAR/DFARS clauses, options, ceiling, CPARS reporting |
| **IDIQ / MAC / GWAC / GSA Schedule** | Ordering procedures, fair opportunity, minimum/maximum, scope, fee/IFF, on-ramp/off-ramp |
| **Subcontract under federal prime** (us as prime or sub) | FAR flow-downs, FAR 52.244-6 commercial-item flow-downs, indemnity caps, payment terms vs prime, T&M ceilings, change control |
| **Teaming Agreement / Joint Venture Agreement** | 8(a) JV rules (13 C.F.R. § 124.513), workshare allocation, FAR 52.219-14 self-performance, exclusivity, term, dissolution, SBA approval |
| **NDA / PIA** | Use of CUI, ITAR/EAR, Section 889, source-selection sensitivity, term, governing law |
| **Commercial vendor agreement** (purchase of goods/services) | Whether federal flow-downs apply, Section 889 reps, Buy American / TAA, payment timing vs prime payment, data rights |
| **Modification (SF 30) / Engineering Change Proposal** | Scope vs out-of-scope, REA implications, equitable adjustment basis, novation/assignment |

Confirm the type out loud before continuing.

### Step 3: Gather Context

Ask the user for context. If they don't have all of it, proceed with assumptions and flag them.

1. **Our role** — prime, subcontractor, teaming partner, JV member/managing venturer, vendor, customer, mentor, protégé?
2. **Counterparty** — federal agency (which one?), prime contractor, sub, commercial vendor?
3. **Contract type** — FFP, FFP-LOE, T&M, Labor Hour, CPFF, CPIF, CPAF, IDIQ?
4. **Set-aside / vehicle** — 8(a) sole-source, 8(a) competitive, SB set-aside, HUBZone, SDVOSB, F&O, GSA MAS, OASIS+, SeaPort-NxG, CIO-SP4, USACE MATOC?
5. **Estimated value & period of performance.**
6. **Deadline** for review (CO response deadline, proposal due date, signature date).
7. **Critical concerns** the user has (e.g., "FAR 52.227-14 data rights are the issue," "we can't accept open-ended indemnity," "ceiling is too low to absorb risk").
8. **Special facts** — JV vehicle, Mentor-Protégé arrangement, ANC sole-source justification, OCONUS performance, classified work, CUI handling.

### Step 4: Load the Playbook and Context

In order, consult:

1. **Aleut Federal company context** — `ALEUT-FEDERAL-CONTEXT.md` at the repo root (authoritative facts about ANC/8(a) status, regulatory framework, hard constraints).
2. **Local legal playbook** — `legal.local.md` or similar (specific risk thresholds, approval authority matrix, preferred indemnity caps).
3. **Prior similar agreements** in our CLM, if connected.

If no local playbook is set, use the default Aleut Federal positions in **Step 6** and clearly mark the review as "based on default federal-contractor positions; not yet calibrated to a written local playbook."

### Step 5: Read the Entire Document

Before flagging anything, read end-to-end. In federal documents this means:

- **Solicitations:** Section L (instructions), Section M (evaluation), Section H (special), Section C (PWS/SOW), Section I (clauses by reference), Section J (attachments — wage determinations, CDRLs, drawings, security forms).
- **Awards:** all CLINs, all referenced clauses (FAR/DFARS/agency supplement), all attached exhibits.
- **Subcontracts:** the body, the flow-down exhibit (often "Exhibit A" or "Attachment 1"), and any prime contract incorporated by reference.

Clauses interact. A reasonable indemnity may be undone by a broad warranty; a tight FAR 52.227-14 data-rights position may conflict with a CDRL that demands deliverables in proprietary format.

### Step 6: Clause-by-Clause Analysis

Apply this systematic review. For each clause, mark **GREEN / YELLOW / RED** per Step 7.

#### A. Federal-specific clauses (always check on federal contracts and flow-downs)

| Clause / Topic | What to look for | Default AF position |
|----------------|------------------|---------------------|
| **FAR 52.212-4 / FAR 52.212-5** (Commercial items, contract terms and conditions required to implement statutes/EOs) | Whether commercial-item terms apply; if so, scope of flow-downs from FAR 52.244-6 | Accept commercial-item treatment where lawful; resist non-commercial flow-downs in commercial-item subs |
| **FAR 52.215-2** (Audit and Records — Negotiation) | Records retention, government audit access | Accept; coordinate with Finance on records retention (3 years after final payment) |
| **FAR 52.216-7** (Allowable Cost and Payment) | Provisional billing rates, ICS submission obligation, final indirect rate settlement | Required on cost-type; ensure rate structures align with our DCAA-approved pools |
| **FAR 52.219-8 / 52.219-9** (Small Business Subcontracting) | SB subcontracting plan thresholds; goals | Accept; ensure achievable goals; align with our Master SB Plan if applicable |
| **FAR 52.219-14** (Limitations on Subcontracting) | Self-performance % (services 50% cost of personnel; general construction 15%; specialty 25%); JV treatment | **Hard constraint.** Verify staffing plan can comply. Flag RED if PWS makes compliance impossible |
| **FAR 52.222-6** (Construction Wage Rate Requirements — Davis-Bacon) | DBA applicability; attached WD; conformance process | Accept; coordinate with HR/Payroll on WD enforcement and Copeland anti-kickback certification |
| **FAR 52.222-41 / 52.222-42 / 52.222-43** (Service Contract Labor Standards) | SCA applicability; attached WD(s); price adjustment on WD updates | Accept; insist on FAR 52.222-43 price-adjustment mechanism on multi-year |
| **FAR 52.222-54** (E-Verify) | Required for most federal contracts; flow-down to subs | Accept; HR maintains E-Verify enrollment |
| **FAR 52.223-18** (Texting while driving) | Standard | Accept |
| **FAR 52.227-14 / 52.227-17** (Rights in Data — General / Special Works) | Government data rights; assertion of limited rights | Default to **limited rights** in pre-existing IP; assert restrictions in proposal where appropriate |
| **DFARS 252.227-7013 / 7014** (Technical Data / Noncommercial Computer Software) | Government Purpose Rights, Limited Rights, Restricted Rights | Negotiate **Government Purpose Rights** at most for software developed at private expense; assert restrictions |
| **DFARS 252.204-7012** (Safeguarding CUI / Cyber Incident Reporting) | NIST SP 800-171 implementation; 72-hour incident reporting; flow-down | **Hard constraint.** Verify our SSP and POA&M support; flow down to subs handling CUI |
| **DFARS 252.204-7019/7020/7021** (NIST SP 800-171 / CMMC) | SPRS score current; CMMC level required | Verify SPRS posted within 3 years; track CMMC level required |
| **FAR 52.203-13** (Code of Business Ethics) | Required ethics program, hotline, **mandatory disclosure** | **Hard constraint.** Maintain program; route credible-evidence findings to senior counsel |
| **FAR 52.203-17** (Whistleblower) | Posting and policy | Accept |
| **FAR 52.204-25 / DFARS 252.204-7018** (Section 889 — covered telecom) | Reps; flow-downs | **Hard constraint.** Verify supply chain free of covered entities |
| **FAR 52.225-3 / 52.225-9 / 52.225-11 / 52.225-13 / DFARS 252.225-7001** (Buy American / TAA / BABA) | Domestic content; designated-country exceptions | Default to compliant sources; flag any non-compliant materials |
| **FAR 52.232-39 / 52.232-40 / Prompt Payment Act** | Payment timing | Insist on Prompt Payment Act protections in subs |
| **FAR 52.249-x** (Termination) | Termination for Convenience / Default mechanics | Verify T4C settlement language; protect unrecovered costs and fee on work performed |
| **FAR 52.243-x** (Changes) | Unilateral vs bilateral; REA process; constructive change | Preserve right to equitable adjustment; require written direction before performance |
| **FAR 52.244-6** (Subcontracts for Commercial Items) | Mandatory commercial-item flow-downs | Use as cap on what we flow down to commercial subs |
| **Limitation of Cost / Funds (FAR 52.232-20 / -22)** | Funding cap and notification | On cost-type, track at ≤ 75% / ≤ 85% notification triggers |

#### B. Commercial clause categories (review regardless of contract type)

| Clause Category | Key review points (federal-flavored) |
|-----------------|--------------------------------------|
| **Limitation of Liability** | Federal primes often resist any LoL; in subs, push for cap at fees paid in trailing 12 months; carveouts for IP and gross negligence acceptable. **Note**: many flow-downs disclaim LoL — flag risk in those cases. |
| **Indemnification** | Mutual where possible; in federal primes, indemnity to the Government is limited by Anti-Deficiency Act and FAR — beware language requiring indemnity "without limit." Push for cap aligned to LoL. |
| **IP Ownership / Data Rights** | Map to FAR 52.227-14 / DFARS 252.227-7013/7014. Mark pre-existing IP in assertions table. |
| **Confidentiality** | Cover CUI, source-selection information, and proprietary marking under FAR 3.104. Bilateral terms; 5-year default; perpetual for trade secrets and CUI. |
| **Reps & Warranties** | Watch for warranties broader than FAR-required reps; disclaim where commercially reasonable. |
| **Term & Termination** | Mirror Government T4C/T4D through to subs; require pass-through of stop-work and termination costs. |
| **Governing Law / Dispute Resolution** | Federal primes: Contract Disputes Act (41 U.S.C. § 7101 et seq.) and ASBCA/CBCA + COFC. Subs: prefer state of our HQ; resist consolidation clauses that subordinate sub claims to prime claims without our consent. |
| **Insurance** | FAR 28.307 / 52.228-5 minimums for service contracts; construction must meet Miller Act bonding (perf + payment) > $150K. Verify EM 385-1-1 site insurance where USACE. |
| **Assignment / Anti-Assignment Act** | Federal prime assignment governed by Anti-Assignment Act (41 U.S.C. § 6305) — novation requires Government consent. Bake into mods. |
| **Force Majeure** | Excusable delays under FAR 52.249-14 are more restrictive than generic FM. Don't accept commercial FM clauses that override. |
| **Payment Terms** | Federal: Prompt Payment Act. Subs: insist on pay-when-paid not pay-if-paid (most states limit pay-if-paid on federal subs anyway). |

#### C. Construction-only clauses (when document touches Davis-Bacon / Miller Act work)

- **Differing Site Conditions** (FAR 52.236-2) — preserve right; require written CO notice before disturbance.
- **Site Investigation** (FAR 52.236-3) — accept but document assumptions.
- **Permits and Responsibilities** (FAR 52.236-7).
- **Schedules for Construction Contracts** (FAR 52.236-15) — preserve flexibility on critical path.
- **Performance and Payment Bonds** (FAR 52.228-15 / 52.228-16) — Miller Act > $150K; verify bonding capacity with Finance.
- **Safety: USACE EM 385-1-1** (where Corps customer) — verify SSHP requirements; APP/AHA cadence.
- **Buy American / BABA** for materials.
- **Liquidated damages** (FAR 52.211-12) — verify daily rate is a reasonable forecast, not a penalty; cap exposure.

#### D. Teaming and JV agreements (when reviewing those)

- **8(a) JV rules** — 13 C.F.R. § 124.513: 8(a) participant must be managing venturer; JV must perform requirements; profit allocation in proportion to workshare. SBA approval required before award on sole-source.
- **Workshare** — define percentages by labor category / CLIN to support FAR 52.219-14 compliance.
- **Exclusivity** — bilateral and limited to the specific opportunity; carveouts for separate pursuits.
- **Dissolution** — IP and data return; ongoing past-performance attribution per FAR 15.305(a)(2)(iii).
- **Mentor-Protégé** — confirm SBA-approved Mentor-Protégé Agreement is in effect and applicable.

### Step 7: Flag Deviations (GREEN / YELLOW / RED)

#### GREEN — Acceptable
Aligns with the Aleut Federal default position or is better. Note for awareness.

#### YELLOW — Negotiate
Outside default but within range. Provide:
- Exact redline language.
- Fallback position.
- Business impact of accepting as-is vs negotiating.

#### RED — Escalate
Outside acceptable range, triggers an escalation criterion, or poses material risk. Provide:
- Why it's RED (specific risk: FCA exposure, uncapped indemnity, unlawful flow-down, IP loss, FAR 52.219-14 violation, CMMC/CUI gap, etc.).
- Standard market or AF-required alternative.
- Exposure estimate.
- Escalation path (GC, CFO, COO, Mandatory Disclosure Committee).

**Automatic RED triggers (always escalate):**
- Anything implicating False Claims Act, Procurement Integrity Act, FAR 52.203-13 mandatory disclosure, or Anti-Kickback Act.
- Uncapped indemnity in a subcontract or commercial agreement.
- Loss of pre-existing IP (Unlimited Rights granted in proposal IP).
- FAR 52.219-14 self-performance compliance impossible under the staffing plan.
- DFARS 252.204-7012 / NIST 800-171 / CMMC requirements we cannot meet.
- Section 889 reps we cannot honestly make.
- Buy American / TAA / BABA representations we cannot honestly make.
- Cost or pricing data certifications under TINA where we lack adequate basis.
- Non-novated assignment of a federal prime contract.
- LD rates that exceed a reasonable forecast of actual damages.
- 8(a) JV without SBA approval prior to award on sole-source.

### Step 8: Generate Redline Suggestions

For each YELLOW and RED:

```
**Clause**: [Section / FAR-DFARS reference]
**Current language**: "[exact quote]"
**Proposed redline**: "[specific alternative with additions in bold]"
**Rationale**: [1–2 sentences citing FAR/DFARS authority or AF policy, suitable for sharing with the counterparty's counsel]
**Priority**: [Must-have / Should-have / Nice-to-have]
**Fallback**: [Alternative if primary rejected]
```

Best practices:

1. **Cite authority.** Federal reviewers respect FAR/DFARS citations; "we just prefer it this way" doesn't move primes.
2. **Be specific.** Drafted language ready to paste.
3. **Mirror the prime.** In subs, never accept terms worse than the prime contract.
4. **Cap flow-downs.** Use FAR 52.244-6 as the ceiling for commercial-item subs.
5. **Prioritize.** Identify must-haves vs nice-to-haves — federal reviews have hard CO deadlines.

### Step 9: Business Impact Summary

Provide:

- **Overall risk:** High / Medium / Low; brief narrative.
- **Top 3–5 issues** with severity.
- **Negotiation strategy:** what to lead with; what to trade.
- **8(a) / set-aside considerations:** any threat to set-aside validity, FAR 19.8 compliance, or SBA approval requirements.
- **Capacity considerations:** bonding (Miller Act), insurance, cleared personnel, CMMC posture.
- **Timeline:** CO deadlines, proposal deadlines, signature windows.

### Step 10: Routing and Approvals

Recommend the right path:

- **CLM intake** — log the document; assign reviewer.
- **Senior counsel** — for any RED automatic trigger above.
- **Mandatory Disclosure Committee** — if credible evidence of FCA/criminal/significant-overpayment per FAR 52.203-13.
- **CO communication path** — when changes require Government action, identify whether a request for clarification (RFI), a question on the solicitation, a REA, or a mod request is the right channel. Never bypass the CO.
- **SBA coordination** — for 8(a) sole-source justifications, JV approval, novations.

If a CLM is connected via MCP, log the review and route automatically.

## Output Format

```
## Federal Contract Review Summary

**Document**: [name / solicitation / award number]
**Type**: [RFP / Award / Subcontract / Teaming / NDA / Mod / ...]
**Parties / Roles**: [agency, prime, sub roles]
**Vehicle / Set-aside**: [8(a) SS, 8(a) competitive, MAS, OASIS+, F&O, etc.]
**Contract Type**: [FFP / T&M / CPFF / IDIQ ...]
**Estimated Value / PoP**: ...
**Our Role**: [prime / sub / JV member / vendor]
**Review Basis**: [Aleut Federal default playbook + local playbook if loaded]
**Deadline**: ...

## Key Findings (Top 3–5)

[Severity flag + 1-line issue + clause cite]

## FAR / DFARS Flow-Down & Compliance Scan

[Table of incorporated clauses; presence/absence; AF position; flag]

## Clause-by-Clause Analysis

### [Category / Clause #] — [GREEN / YELLOW / RED]
**Contract says**: ...
**AF playbook / FAR position**: ...
**Deviation**: ...
**Business impact**: ...
**Redline**: ...

[repeat]

## 8(a) / Set-Aside Considerations
[Any issues with set-aside validity, FAR 19.8, SBA approval, JV compliance]

## Capacity / Capability Considerations
[Bonding, insurance, cleared staff, CMMC level, accounting system adequacy]

## Negotiation Strategy
[Lead-with items, concession candidates, must-haves]

## Mandatory-Disclosure / FCA / PIA Check
[Any credible-evidence concerns; route to senior counsel]

## Next Steps
[Specific actions, approvals required, deadlines]
```

## Notes

- For very long solicitations or awards (100+ pages), offer to scope to Sections L/M/H/C/I first, then full review.
- If the document is classified or contains CUI in an unauthorized environment, **stop** and route to the FSO and Information Security.
- Always remind the user that this analysis must be reviewed by qualified counsel and the Contracting Officer (for prime contract changes) before reliance.
