---
name: draft-offer
description: Draft an offer letter with comp details and terms. Use when a candidate is ready for an offer, assembling a total comp package (base, equity, signing bonus), writing the offer letter text itself, or prepping negotiation guidance for the hiring manager.
---

# /draft-offer — Aleut Federal

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Draft a complete offer letter for a new hire at Aleut Federal. Federal-contractor offers have specific contingencies and compliance hooks that commercial offers don't.

## Aleut Federal Context — Required Offer Elements

Every Aleut Federal offer must address the following. Tailor by role and contract assignment.

### Contingencies (always)

- **Drug-Free Workplace Act compliance** (FAR 52.223-6) — pre-employment drug screen passed.
- **E-Verify** (FAR 52.222-54) — eligibility to work in the U.S. confirmed via E-Verify; new hires on covered contracts must be E-Verified within 3 business days of start.
- **Background check** appropriate to the role and the contract.
- **References** for senior roles.
- **Security clearance** — if the role requires a clearance, condition employment on the clearance being granted or maintained at the specified level.
- **Procurement Integrity Act / former-federal-official screen** (18 U.S.C. § 207, § 2104) — for candidates who held federal positions in the prior two years, the offer is contingent on completion of an ethics screen and any required cooling-off period.
- **FAR 3.104 source-selection screen** — for candidates from competitors or federal agencies whose recent work could implicate source-selection information.
- **Compliance with the role's contract-specific requirements** — wage determination acceptance, citizenship requirements (some federal positions), location-of-work requirements, OCONUS readiness, etc.

### Compensation elements

- Base salary or hourly rate. For SCA / DBA contracts, must meet or exceed the WD; for EO 14026-covered contracts, the contractor minimum.
- Fringe / H&W (cash or in-kind) for SCA roles per the WD.
- Bonus / variable pay (where applicable).
- Clearance premium (where applicable).
- OCONUS / hardship / locality premiums.
- Benefits summary referenced.

### Federal-employment-status disclosures

- At-will employment statement (subject to applicable state law).
- Contract assignment caveat — many roles are funded by a specific federal contract; the offer should reference that funding contingency and what happens if the contract ends, loses funding, or is descoped.
- Affirmative-action / EEO statement (EO 11246, VEVRAA, Section 503).
- E-Verify and IRCA Form I-9 requirements.
- Fitness-for-duty / fitness-for-clearance ongoing requirements.
- Mandatory ethics training (FAR 52.203-13) and code of conduct acknowledgment.
- Cyber security / CUI handling (NIST 800-171 SSP acknowledgments) if applicable.

### CBA / successor obligations

If the role is on an SCA recompete where the predecessor was under a CBA, the offer must reflect successor wages and fringe per FAR 52.222-41 / DOL guidance.

### Pay-transparency / disclosure

Comply with state pay-transparency laws (CA, CO, IL, MD, NY, WA) for the locality of the role's posting/performance.

### Document the candidate's status

- U.S. citizen / U.S. national / lawful permanent resident / visa class.
- ITAR-eligible "U.S. person" status if the role touches ITAR-controlled technical data.
- Clearance status (current, inactive, none) and adjudication agency.
- Veteran / disability / EEO category (for AAP purposes — voluntary self-ID).

## Offer-Letter Skeleton

```
[Aleut Federal letterhead]

[Candidate]
[Address]

Dear [Candidate]:

We are pleased to offer you the position of [title] at Aleut Federal, LLC, reporting to [manager]. This letter sets out the terms of our offer.

1. **Start date and location**: [date], [work site].
2. **Compensation**: $[base] [annually / hourly]. [If applicable: This position is on the [contract name / number], which is subject to the [SCA / DBA] Wage Determination [WD #, Rev #]. Your wage and [H&W / fringe] meet or exceed the applicable WD.] [If applicable: This position is covered by Executive Order 14026; your wage meets or exceeds the current federal contractor minimum.]
3. **Bonus / variable** (if applicable).
4. **Benefits**: [summary; full plan documents control].
5. **Premiums** (clearance / OCONUS / hardship): [if applicable].
6. **Employment type**: At-will, full-time. This position is funded under [contract / general overhead]. If contract funding ends, descopes, or the contract is terminated, your employment may be subject to change.

**Contingencies.** This offer is contingent on:
 a. Successful completion of a pre-employment drug screen (Drug-Free Workplace Act / FAR 52.223-6).
 b. E-Verify confirmation of eligibility to work in the U.S. (FAR 52.222-54).
 c. Successful background check appropriate to the role and contract.
 d. [If applicable] Grant and maintenance of a [SECRET / TS / TS-SCI] security clearance at the required level.
 e. [If applicable] Completion of post-employment ethics screen and any required cooling-off period under 18 U.S.C. § 207 / § 2104.
 f. Acknowledgment of and compliance with Aleut Federal's Code of Business Ethics and Conduct (FAR 52.203-13), Cyber / CUI handling policy [DFARS 252.204-7012; NIST 800-171] where applicable, and other policies in the Employee Handbook.

**Confidentiality and IP.** You will be required to sign a Confidentiality and Assignment of Inventions Agreement at start.

**Acceptance.** Please indicate acceptance by signing and returning this letter by [date]. Please feel free to contact me with questions.

Sincerely,
[Signatory — authorized officer]
```

## Hard Rules

- **Never** offer a wage below the applicable SCA / DBA WD or EO 14026 minimum on covered contracts.
- **Never** finalize an offer to a former federal official who hasn't cleared the 18 U.S.C. § 207 / § 2104 screen.
- **Never** include language committing to work that would breach Procurement Integrity Act restrictions on use of source-selection information.
- **Always** condition contract-funded roles on funding/clearance/E-Verify/drug-screen.
- **Always** route any offer for a former CO / source-selection authority / CTR / SSB member with active restrictions through Legal.

## Usage

```
/draft-offer $ARGUMENTS
```

## What I Need From You

- **Role and title**: What position?
- **Level**: Junior, Mid, Senior, Staff, etc.
- **Location**: Where will they be based? (affects comp and benefits)
- **Compensation**: Base salary, equity, signing bonus (if applicable)
- **Start date**: When should they start?
- **Hiring manager**: Who will they report to?

If you don't have all details, I'll help you think through them.

## Output

```markdown
## Offer Letter Draft: [Role] — [Level]

### Compensation Package
| Component | Details |
|-----------|---------|
| **Base Salary** | $[X]/year |
| **Equity** | [X shares/units], [vesting schedule] |
| **Signing Bonus** | $[X] (if applicable) |
| **Target Bonus** | [X]% of base (if applicable) |
| **Total First-Year Comp** | $[X] |

### Terms
- **Start Date**: [Date]
- **Reports To**: [Manager]
- **Location**: [Office / Remote / Hybrid]
- **Employment Type**: [Full-time, Exempt]

### Benefits Summary
[Key benefits highlights relevant to the candidate]

### Offer Letter Text

Dear [Candidate Name],

We are pleased to offer you the position of [Title] at [Company]...

[Complete offer letter text]

### Notes for Hiring Manager
- [Negotiation guidance if needed]
- [Comp band context]
- [Any flags or considerations]
```

## If Connectors Available

If **~~HRIS** is connected:
- Pull comp band data for the level/role
- Verify headcount approval
- Auto-populate benefits details

If **~~ATS** is connected:
- Pull candidate details from the application
- Update offer status in the pipeline

## Tips

1. **Include total comp** — Candidates compare total compensation, not just base.
2. **Be specific about equity** — Share count, current valuation method, vesting schedule.
3. **Personalize** — Reference something from the interview process to make it warm.
