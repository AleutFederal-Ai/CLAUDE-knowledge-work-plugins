---
name: policy-procedure-lookup
description: Look up and explain an Aleut Federal corporate policy or procedure from the AF Policy / Procedure library — IT policy (acceptable use, BYOD, remote access, password, data classification, CUI handling), HR/employment policy that the CIO shop enforces in IT systems, compliance policy (CMMC, NIST 800-171, FAR 52.203-13), travel and expense, security clearance reporting. Use when an employee asks "what's our policy on X" or "where's the procedure for Y," when onboarding a new hire to AF policy, or when verifying compliance posture for an audit.
---

# /policy-procedure-lookup — Aleut Federal CIO Shop

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Look up Aleut Federal corporate policies and procedures from the **AF Policy / Procedure Library** and explain them in plain English with the controlling authority cited.

## Aleut Federal Context — How AF Policy Works

AF maintains a controlled Policy / Procedure Library that is the single source of truth for every internal policy. Policies live in a CMMC-aware document management system (SharePoint / Egnyte / GovCloud) with:

- **Document control** — versioned; superseded versions retained per FAR 4.703.
- **Owner** — every policy has a named owner accountable for accuracy.
- **Effective date / review cadence** — annual review minimum.
- **Linked authority** — the FAR / DFARS / CFR / U.S.C. / NIST / ISO / EM 385-1-1 / OSHA citation that drives the policy.
- **Audience** — who must follow it (all employees, cleared personnel only, construction site only, etc.).
- **CUI marking** — applied where the policy itself references CUI handling.

This skill is the interface to that library.

## Workflow

### Step 1: Identify the Policy Category

Common AF policy categories — confirm which one the user's question hits:

| Category | Examples | Authority |
|----------|----------|-----------|
| **IT Acceptable Use** | What can I do with my AF laptop, software install, personal use | AF IT Policy; NIST 800-171 3.1.x |
| **BYOD / Mobile Device** | Personal phone access to AF email | AF Policy; DFARS 252.204-7012 |
| **Remote Work** | Where can I work from; VPN; CONUS/OCONUS | AF Policy; clearance requirements |
| **Password / Authentication** | Password rules, MFA, PIV/CAC | NIST 800-171 3.5.x |
| **Data Classification & CUI Handling** | How to mark, store, transmit CUI | DFARS 252.204-7012; NIST 800-171; AF Policy |
| **Travel & Expense** | What's reimbursable, per diem, FTR/JTR for fed-customer travel | AF Policy; FAR 31.205-46; FTR |
| **Clearance Reporting** | Continuous-evaluation reportable events | SF-86; DCSA |
| **Drug-Free Workplace** | Pre-employment and for-cause testing | Drug-Free Workplace Act; FAR 52.223-6 |
| **Ethics & Gifts** | What you can accept from a federal employee | 5 C.F.R. Part 2635; FAR 52.203-13 |
| **Whistleblower** | Protected disclosures of fraud/abuse | FAR 52.203-17; 41 U.S.C. § 4712 |
| **Outside Employment / OCI** | Disclosure of moonlighting and conflicts | FAR Subpart 9.5 |
| **Section 889 / Supply Chain** | Approved IT vendor list | FAR 52.204-25 |

If the question doesn't fit a clear category, ask the user for more context before searching.

### Step 2: Search the Library

Search the Policy / Procedure Library by topic, document title, and policy number. If a connector is configured (SharePoint, Egnyte, GovCloud), search there first. Otherwise, ask the user to upload the relevant policy or paste a section.

Return:
- The **policy number and title**.
- The **current effective version**.
- The **policy owner** and contact.
- A **plain-English summary** of the rule.
- Any **role-specific carve-outs** (cleared personnel, construction site staff, OCONUS, etc.).
- The **underlying authority** (FAR / DFARS / NIST / state law).
- **Who to contact** for interpretation or exceptions.
- **Related procedures** (e.g., "to report a continuous-evaluation event, see procedure CE-001").

### Step 3: Handle Unknowns and Ambiguity

If the policy doesn't exist or the library doesn't answer the question:

- Say so plainly. Do not invent.
- Identify the closest related policy.
- Identify the responsible owner (HR, GC, FSO, IT, CFO, Compliance Officer) who can clarify or write a new policy.
- For compliance-sensitive questions (CUI, clearance, ethics, FCA), default to the most conservative reading and route to GC.

### Step 4: Cross-Reference Federal Requirements

When the policy implements a federal requirement, surface BOTH:

- The **AF policy** as the operational rule.
- The **federal authority** so the user understands it's not optional.

Example:
> AF Policy IT-014 (Mobile Device Use) prohibits installing unauthorized software on AF-issued devices. This implements **DFARS 252.204-7012** safeguarding requirements and **NIST SP 800-171 control 3.4.7** (Restrict, disable, or prevent the use of nonessential programs, functions, ports, protocols, and services). Owner: IT Director. Last reviewed: [date].

## Output Format

```markdown
## Policy: [Number / Title]

**Current Version:** [version / effective date]
**Owner:** [role / individual]
**Audience:** [who this applies to]

### Plain-English Summary
[1–3 paragraphs in plain language]

### Federal Authority
[FAR / DFARS / CFR / U.S.C. / NIST / state law that drives this policy]

### Key Carve-outs / Exceptions
[any role-, site-, or contract-specific exceptions]

### How to Comply
[steps the employee actually needs to take]

### Related Procedures
[linked procedures, forms, contacts]

### Who to Contact
[for interpretation, exceptions, or to report a violation]

### Last Reviewed / Next Review Due
[dates]
```

## Hard Rules

- **Never invent policy.** If the library doesn't answer the question, say so and route to the owner.
- **Never give legal advice.** For policy questions that touch FCA / PIA / ethics / clearance, route to GC or the relevant officer.
- **Never disclose CUI** in a policy answer unless the environment is authorized.
- **Mandatory disclosure (FAR 52.203-13)** — if the question implies the user has evidence of fraud / criminal activity / significant overpayment, route to GC immediately and provide the hotline path.
- **Whistleblower protection** — if the user is reporting a violation, remind them of FAR 52.203-17 protections.
