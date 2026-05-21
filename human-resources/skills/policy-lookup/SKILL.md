---
name: policy-lookup
description: Find and explain company policies in plain language. Trigger with "what's our PTO policy", "can I work remotely from another country", "how do expenses work", or any plain-language question about benefits, travel, leave, or handbook rules.
argument-hint: "<policy topic — PTO, benefits, travel, expenses, etc.>"
---

# /policy-lookup — Aleut Federal

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Look up and explain Aleut Federal policies in plain language. Many of our policies are driven by federal law and contract clauses, not just internal preference — when answering, identify both.

## Aleut Federal Context — Frequent Federal-Driven Policies

These policies are rooted in federal law or contract clauses. When an employee asks about them, give the plain-language answer **and** the authority so they understand it isn't optional.

| Topic | Federal authority | Practical effect |
|-------|-------------------|------------------|
| Drug-free workplace | Drug-Free Workplace Act; FAR 52.223-6 | Pre-employment screen; for-cause testing; drug-conviction reporting within 5 days |
| Work authorization / E-Verify | FAR 52.222-54; IRCA | Form I-9 + E-Verify queries; required reverification on certain federal contracts |
| Equal employment | EO 11246, VEVRAA, Section 503, Title VII | Recruitment, posting, AAP, VETS-4212, EEO-1 obligations |
| Affirmative action plan | OFCCP regulations | Required when contract ≥ $50K and headcount ≥ 50 |
| Service Contract Act wages and benefits | 41 U.S.C. ch. 67; FAR 52.222-41 | WD posted at site; pay no less than WD wage + H&W |
| Davis-Bacon wages (construction) | 40 U.S.C. ch. 31; FAR 52.222-6 | WD posted at site; weekly certified payroll (WH-347) |
| EO 14026 minimum wage | EO 14026 | Federal contractor minimum (updated annually) |
| Paid sick leave (federal contractors) | EO 13706 | 1 hour earned per 30 worked; 56-hour cap per year |
| Whistleblower protections | 41 U.S.C. § 4712; 10 U.S.C. § 4701; FAR 52.203-17 | Protected disclosures of fraud / abuse on federal contracts; required posting |
| Workplace anti-trafficking | FAR 52.222-50 | Prohibitions and compliance plan for covered contracts |
| Ethics & conduct | FAR 52.203-13 | Code, training, hotline, internal-control system, mandatory disclosure |
| Cyber / CUI handling | DFARS 252.204-7012; NIST 800-171 | SSP-aligned procedures; incident reporting within 72 hours |
| Travel | FTR / JTR for federally reimbursed travel | Per diem caps; lodging tax exemption where applicable |
| Foreign travel / OCONUS | ITAR/EAR if applicable; agency country clearance | TCP, country clearance, foreign-national interaction rules |
| Off-duty conduct affecting clearance | SF-86 / DCSA / agency-specific | Continuous-evaluation reportable incidents (financial issues, foreign contact, etc.) |
| Gift / entertainment with federal officials | 5 C.F.R. Part 2635; FAR 3.101 | $20/$50 de minimis; coordinate with Ethics |
| Outside employment / moonlighting | OCI; FAR Subpart 9.5 | Disclose; conflicts with federal customer or competitor work prohibited |
| Lobbying | 31 U.S.C. § 1352 (Byrd); FAR 52.203-11/-12; SF-LLL | Federal funds may not be used for lobbying; reporting |
| Davis-Bacon Apprentice / Trainee programs | 29 C.F.R. § 5.5 | Approved program required; ratios |

For each policy, when answering:

1. Provide the **plain-language answer**.
2. Cite the **federal authority** (clause or statute).
3. Note any **contract-specific variations** (e.g., this contract's WD has a different H&W amount).
4. Identify **who to contact** for the authoritative interpretation (HR, FSO, Ethics, Contracts, Legal).
5. For anything implicating whistleblower / FCA / mandatory-disclosure, advise the employee of the FAR 52.203-13 hotline path and protections under FAR 52.203-17.

## Usage

```
/policy-lookup $ARGUMENTS
```

Search for policies matching: $ARGUMENTS

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    POLICY LOOKUP                                   │
├─────────────────────────────────────────────────────────────────┤
│  STANDALONE (always works)                                       │
│  ✓ Ask any policy question in plain language                    │
│  ✓ Paste your employee handbook and I'll search it              │
│  ✓ Get clear, jargon-free answers                               │
├─────────────────────────────────────────────────────────────────┤
│  SUPERCHARGED (when you connect your tools)                      │
│  + Knowledge base: Search handbook and policy docs automatically │
│  + HRIS: Pull employee-specific details (PTO balance, benefits) │
└─────────────────────────────────────────────────────────────────┘
```

## Common Policy Topics

- **PTO and Leave**: Vacation, sick leave, parental leave, bereavement, sabbatical
- **Benefits**: Health insurance, dental, vision, 401k, HSA/FSA, wellness
- **Compensation**: Pay schedule, bonus timing, equity vesting, expense reimbursement
- **Remote Work**: WFH policy, remote locations, equipment stipend, coworking
- **Travel**: Booking policy, per diem, expense reporting, approval process
- **Conduct**: Code of conduct, harassment policy, conflicts of interest
- **Growth**: Professional development budget, conference policy, tuition reimbursement

## How to Answer

1. Search ~~knowledge base for the relevant policy document
2. Provide a clear, plain-language answer
3. Quote the specific policy language
4. Note any exceptions or special cases
5. Point to who to contact for edge cases

**Important guardrails:**
- Always cite the source document and section
- If no policy is found, say so clearly rather than guessing
- For legal or compliance questions, recommend consulting HR or legal directly

## Output

```markdown
## Policy: [Topic]

### Quick Answer
[1-2 sentence direct answer to their question]

### Details
[Relevant policy details, explained in plain language]

### Exceptions / Special Cases
[Any relevant exceptions or edge cases]

### Who to Contact
[Person or team for questions beyond what's documented]

### Source
[Where this information came from — document name, page, or section]
```

## If Connectors Available

If **~~knowledge base** is connected:
- Search employee handbook and policy documents automatically
- Cite the specific document, section, and page number

If **~~HRIS** is connected:
- Pull employee-specific details like PTO balance, benefits elections, and enrollment status

## Tips

1. **Ask in plain language** — "Can I work from Europe for a month?" is better than "international remote work policy."
2. **Be specific** — "PTO for part-time employees in California" gets a better answer than "PTO policy."
