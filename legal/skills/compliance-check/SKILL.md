---
name: compliance-check
description: Run a compliance check on a proposed Aleut Federal action — a pursuit, teaming arrangement, hire, marketing claim, vendor selection, technology deployment, or process change — against the federal regulatory framework (FAR, DFARS, SBA 8(a), labor, environmental, cyber). Surface applicable authorities, required approvals, and risk areas before proceeding.
argument-hint: "<action or initiative to check>"
---

# /compliance-check -- Federal Compliance Review

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Run a compliance check on a proposed action, pursuit decision, business arrangement, hire, vendor selection, technology deployment, or process change.

**Important:** This skill assists with compliance analysis; it does not provide legal advice. Compliance assessments must be reviewed by qualified counsel. Federal acquisition and labor regulations change frequently; verify current requirements at authoritative sources (acquisition.gov, sam.gov, ecfr.gov, dol.gov, sba.gov, dcaa.mil, dcma.mil).

## Usage

```
/compliance-check $ARGUMENTS
```

## What I Need From You

Describe the proposed action. Useful examples in our world:

- "We want to bid an 8(a) sole-source award to USDA at $145M ceiling."
- "We're forming a JV with [Company X] for a Navy NAVFAC MATOC."
- "We're hiring a former Air Force CO who managed our incumbent contract."
- "We want to use [supplier]'s switches on a CMMC L2 project."
- "Marketing wants to publish a case study naming the Army customer and contract number."
- "We're moving incurred-cost workpapers to a new GovCloud tenant."
- "We're adding a 25% workshare bump to our JV partner mid-performance."
- "We want to recompete an SCA contract at a lower bill rate than the WD allows."

## Workflow

1. **Classify the action** — pursuit, teaming, hire, marketing, vendor, technology, process change, cost/pricing action, labor/HR action, environmental, ethics/PIA.
2. **Identify applicable authorities** — FAR/DFARS/agency supplements, SBA, DOL, EPA, NIST/CMMC, EEOC/OFCCP, ITAR/EAR, state law where applicable.
3. **Run the applicable checklist(s)** from the libraries below.
4. **Score severity** — Proceed / Proceed with conditions / Hold / Stop and route to counsel.
5. **List approvals required** — internal (GC, CFO, COO, FSO, Compliance Officer) and external (CO, SBA, agency authorities).
6. **Surface mandatory-disclosure triggers** under FAR 52.203-13.

## Output

```markdown
## Compliance Check: [Initiative]

### Summary
[Proceed / Proceed with conditions / Hold / Stop and escalate]

### Applicable Authorities
| Authority | Relevance | Key Requirements |
|-----------|-----------|------------------|
| FAR Subpart 19.8 / 13 C.F.R. Part 124 | 8(a) program | ... |
| DFARS 252.204-7012 / NIST SP 800-171 | CUI safeguarding | ... |
| 41 U.S.C. § 2101 et seq. (Procurement Integrity Act) | Former officials, source-selection info | ... |
| DOL Wage Determination [#] | SCA / Davis-Bacon wages | ... |

### Requirements
| # | Requirement | Status | Action Needed |
|---|-------------|--------|---------------|
| 1 | ... | Met / Not met / Unknown | ... |

### Risk Areas
| Risk | Severity | Mitigation |
|------|----------|------------|

### Recommended Actions
1. ...

### Approvals Needed
| Approver | Why | Status |
|----------|-----|--------|

### Mandatory-Disclosure / FCA / PIA Check
[Any credible-evidence concerns under FAR 52.203-13; escalate to GC]

### Further Review Recommended
[Outside counsel, CO consultation, SBA coordination]
```

## Checklist Libraries

### A. 8(a) / Set-Aside Eligibility (FAR Subpart 19.8, 13 C.F.R. Part 124)

- [ ] **Entity is an SBA-certified 8(a) participant** in good standing (verify in DSBS / certify.SBA.gov).
- [ ] **Sole-source threshold:** civilian — unlimited for ANC; DoD — currently $100M (verify against current DFARS).
- [ ] **Sole-source justification:** D&F or J&A drafted; rationale documented; competition not feasible under 13 C.F.R. § 124.506.
- [ ] **NAICS size:** under the SBA size standard for the assigned NAICS at offer date.
- [ ] **Affiliation:** ANC subsidiaries — generally not affiliated under 13 C.F.R. § 121.103(b)(2); confirm no other affiliation triggers (common management, identity of interest).
- [ ] **Non-manufacturer rule** (if supplies): waiver in place or compliance documented.
- [ ] **Limitations on subcontracting (FAR 52.219-14):** staffing plan supports self-performance (services 50% cost of personnel; general construction 15%; specialty 25%); JVs count partners' work; flow-downs do not cause similarly-situated entity gaps.
- [ ] **Bona-fide place of business:** for construction set-asides where required.
- [ ] **Past performance and capability** documented to meet "responsible offeror" threshold (FAR 9.104).
- [ ] **SBA acceptance:** sole-source offered into the program; SBA acceptance letter received prior to award.

### B. 8(a) Joint Venture (13 C.F.R. § 124.513)

- [ ] **Managing venturer** is the 8(a) participant.
- [ ] **Written JV agreement** addresses all 13 C.F.R. § 124.513(c) elements (project manager from 8(a) firm, profit allocation by workshare, equipment/facilities, records, accounting).
- [ ] **Workshare:** 8(a) protégé performs at least **40%** of the work done by the JV.
- [ ] **Profit distribution** matches workshare percentages.
- [ ] **Mentor-Protégé Agreement** active and SBA-approved if relying on mentor exception.
- [ ] **SBA approval** of the JV obtained **before award** for sole-source (and tracked as needed for competitive).
- [ ] **Compliance reporting** — annual JV performance reports filed with SBA.
- [ ] **No prohibited affiliation** created (size, control).
- [ ] **Three-in-Two rule:** JV can receive max 3 contract awards over a 2-year period.

### C. Procurement Integrity Act / Former-Official Hiring (41 U.S.C. § 2101 et seq.; FAR 3.104)

- [ ] **Source-selection information** — no current or former federal official has shared non-public source-selection information with us.
- [ ] **Contractor bid or proposal information** — no improper exchange.
- [ ] **Former federal officials we're hiring:**
  - Identify their last position(s) and contracts they personally and substantially worked on.
  - Apply **18 U.S.C. § 207** post-employment restrictions (lifetime ban on particular-matter representation; two-year ban on related matters; one-year cooling-off for senior officials).
  - **§ 2104 one-year compensation ban** if served as procuring contracting officer, source-selection authority, evaluation board member, or contracting officer's technical representative on a contract > $10M with us.
  - **Ethics letter** obtained from their former agency where required.
- [ ] **Gifts and gratuities** — no improper offers to federal officials.
- [ ] **Document** the screening in the personnel file and notify the CO if § 2104 applies.
- [ ] **Mandatory disclosure** under FAR 52.203-13 if credible evidence of a violation arises.

### D. CUI / DFARS 252.204-7012 / NIST SP 800-171 / CMMC 2.0

- [ ] **Identify CUI** in the scope (CDRLs, deliverables, technical data, personnel data).
- [ ] **SSP and POA&M** current; NIST 800-171 controls implemented to the extent applicable.
- [ ] **SPRS score** posted (within 3 years); plan for remediation if below target.
- [ ] **CMMC level** required by the contract (Level 1 for FCI, Level 2 for CUI, Level 3 for select higher-sensitivity); compliance pathway (self-assessment, C3PAO assessment, DIBCAC) chosen.
- [ ] **Cyber incident reporting** — 72-hour reporting infrastructure to DIBNet operational.
- [ ] **Flow-downs** — DFARS 252.204-7012 flows down to subs handling CUI.
- [ ] **Cloud services** — if CUI processed in cloud, FedRAMP Moderate (equivalent) baseline plus DFARS supplement; for DoD, DoD IL4/IL5 may apply.
- [ ] **GovCloud tenancy** — verify storage location (CONUS), administrator citizenship, and key management.

### E. Section 889 (Covered Telecommunications)

- [ ] **No covered equipment or services** from Huawei, ZTE, Hytera, Hikvision, Dahua, or their affiliates anywhere in our operations or supply chain (Part A & Part B).
- [ ] **Annual representation** in SAM.gov is accurate.
- [ ] **Supply chain audit** for new vendors; reasonable inquiry documented.
- [ ] **Flow-down** to subs under FAR 52.204-25.

### F. Buy American Act / BABA / TAA

- [ ] **Identify domestic preference rules** applicable to the contract (FAR 52.225-3 Buy American; 52.225-5 TAA; BABA for federally-funded infrastructure).
- [ ] **Material origin** — verify country of origin and domestic content thresholds (per BABA — manufactured products 55%/65% per phase-in; iron & steel 100% melted and poured; construction materials per material-specific rule).
- [ ] **Waivers** — identify whether a public-interest, non-availability, or unreasonable-cost waiver applies.
- [ ] **Commercial item exception** — if commercial COTS, generally exempt from BAA but not from BABA on infrastructure.

### G. SCA / Davis-Bacon / CWHSSA / Copeland (Labor)

- [ ] **Determine applicability** — services > $2,500 (SCA); construction > $2,000 (DBA); both for hybrid work.
- [ ] **Wage determination** — current WD attached / referenced; rates per labor category meet/exceed WD wages and fringe.
- [ ] **Conformance** — labor categories not in the WD have proper SF 1444 conformance.
- [ ] **CBA** — if a CBA covers the prior contract employees (successor-contractor obligation), bake into bid.
- [ ] **Health & welfare** — pay or provide; track bona-fide fringe benefit credit.
- [ ] **EO 14026 minimum wage** — current federal contractor minimum applied where applicable.
- [ ] **CWHSSA overtime** — > 40 hours / week.
- [ ] **Copeland Act** — weekly payroll certification on construction.
- [ ] **DBRA-recipient training** — supervisors trained.

### H. Construction-Specific (FAR Subpart 36; Miller Act; EM 385-1-1; OSHA 1926)

- [ ] **Performance & payment bonds** (Miller Act > $150K) — bonding capacity confirmed.
- [ ] **Differing site conditions** clause present (FAR 52.236-2).
- [ ] **Liquidated damages** — rate justified; capped where possible.
- [ ] **Site safety** — APP and AHA per EM 385-1-1 (USACE) or OSHA 1926 (other agencies).
- [ ] **NEPA / Cultural / Environmental** — applicable reviews completed by Government before NTP; we don't begin ground-disturbing work prior.
- [ ] **Permits and tap fees** — responsibilities clearly allocated.
- [ ] **Bondable, insurable subs** — qualifications confirmed.
- [ ] **Wage decision posting** at the site.

### I. Cost / Pricing / DCAA

- [ ] **Contract type alignment** — cost-type / T&M / FFP-LOE appropriate for the risk profile; cost-type only allowed where accounting system is DCAA-adequate (SF 1408 criteria).
- [ ] **TINA** — certified cost or pricing data required if > $2M and no exception (commercial item, adequate competition, set by law/regulation).
- [ ] **FAR Part 31 cost allowability** — all costs in the basis pass allowable/allocable/reasonable test.
- [ ] **Unallowables** — lobbying, alcohol, entertainment, bad debts, fines, advertising (non-recruiting), excess executive comp, etc. — segregated.
- [ ] **Provisional billing rates** — current; aligned to ICS forecast.
- [ ] **CAS coverage** — modified vs full; disclosure statement filed where triggered.
- [ ] **Forward-pricing rate agreement (FPRA)** — leverage where active.
- [ ] **Defective pricing exposure** — data current/accurate/complete at certification date.

### J. Ethics / FAR 52.203-13 / FCA / Anti-Kickback

- [ ] **Ethics program** in place: code of business ethics, training, hotline, internal-control system.
- [ ] **Mandatory disclosure (FAR 52.203-13(b)(3)(i))** — credible evidence of FCA violations, certain criminal violations (fraud, conflict of interest, bribery, gratuity), or **significant overpayment** triggers disclosure to OIG and the Contracting Officer within a reasonable time.
- [ ] **Anti-kickback** — FAR 3.502; 41 U.S.C. § 8702. No payments to obtain or reward favorable subcontract treatment.
- [ ] **Gifts/gratuities to federal officials** — strictly limited; check 5 C.F.R. Part 2635.
- [ ] **Conflict of interest screen** — personal and organizational (OCI) per FAR Subpart 9.5.
- [ ] **Suspension/debarment search** — SAM.gov check on subs and key hires.

### K. OFCCP / EEO / VEVRAA / Section 503

- [ ] **AAP** in place if contract ≥ $50K and headcount ≥ 50.
- [ ] **EO 11246 obligations** — recruitment, posting, recordkeeping.
- [ ] **VEVRAA** — protected veterans outreach, VETS-4212 report.
- [ ] **Section 503** — individuals with disabilities outreach; 7% utilization goal.
- [ ] **E-Verify (FAR 52.222-54)** — enrolled; queries for new hires and existing employees on covered contracts.

### L. Export Control (ITAR / EAR)

- [ ] **Classification** — USML category (ITAR) or ECCN (EAR) for items, technical data, software, or services.
- [ ] **Registration** — DDTC registration current if ITAR.
- [ ] **License requirements** — for foreign nationals (deemed export), foreign travel, OCONUS performance.
- [ ] **TCP** — Technology Control Plan in place where required.

### M. Environmental (NEPA, CWA, CAA, ESA, NHPA — construction)

- [ ] **NEPA** — categorical exclusion, EA, or EIS completed by the Government before NTP.
- [ ] **Permits** — stormwater (NPDES CGP), air, dredge/fill (404), hazardous materials.
- [ ] **Cultural / Historic** — Section 106 NHPA review completed.
- [ ] **Endangered species** — Section 7 ESA consultation if applicable.

### N. Marketing / Publicity About Federal Customers

- [ ] **Contract permits publicity** — many federal contracts restrict use of agency name, logo, or contract number without CO approval.
- [ ] **Source-selection information** — never disclose unawarded source-selection data.
- [ ] **CUI / Sensitive** — no mission-sensitive details (capabilities, personnel cleared, classified efforts).
- [ ] **Testimonial / endorsement** rules — federal employees generally cannot endorse contractors (5 C.F.R. § 2635.702); avoid implying endorsement.
- [ ] **CO approval** in writing where required.

## Severity Levels

| Level | Meaning | Action |
|-------|---------|--------|
| **PROCEED** | All checklist items met; routine action | Document and proceed |
| **PROCEED WITH CONDITIONS** | Most met; specific conditions or approvals needed | Get approvals; document; then proceed |
| **HOLD** | Material requirement unmet or unclear | Pause; resolve before proceeding |
| **STOP / ESCALATE** | Likely violation, mandatory-disclosure trigger, or hard-constraint breach | Notify GC immediately; do not proceed |

## Automatic STOP / ESCALATE Triggers

- Any indication of FCA, Anti-Kickback Act, or Procurement Integrity Act violation.
- Source-selection information improperly obtained.
- Hiring a former CO/SSA/CTR/SSB member with active 18 U.S.C. § 207 or § 2104 restrictions that have not been screened.
- 8(a) JV without SBA approval prior to award on sole-source.
- FAR 52.219-14 self-performance not achievable on a set-aside award.
- DFARS 252.204-7012 / CMMC level unmet for CUI work.
- Section 889 violation in active operations or supply chain.
- Use of agency identity / contract number without CO approval.
- Disclosure of CUI or classified data outside an authorized environment.

## Tips

1. **Be specific.** "8(a) sole-source to USDA, $145M, 5-year IDIQ, services" is better than "new pursuit."
2. **Include the customer and vehicle.** Authorities differ by agency and contract type.
3. **Name the people.** Hiring, COI, and PIA screens depend on prior roles.
4. **State the dollars.** Many thresholds are dollar-driven (TINA, Miller Act, simplified acquisition, etc.).
5. **Tell us if it's already started.** A pending action gets a different answer than something already in execution.
