---
name: osha-recordkeeping
description: Manage Aleut Federal's OSHA injury and illness records — Form 300 (Log), Form 300A (Annual Summary), Form 301 (Incident Report). Includes recordability determination per 29 C.F.R. Part 1904, annual posting (Feb 1 – Apr 30), electronic submission to OSHA's ITA for establishments meeting the threshold, and TRIR / DART rate calculation for CPARS, EMR (workers' comp), and proposal past-performance volumes.
argument-hint: "<task — record-incident | annual-summary | ita-submit | rate-calc>"
---

# /osha-recordkeeping — Aleut Federal Safety

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Maintain Aleut Federal's OSHA injury and illness records to the letter of 29 C.F.R. Part 1904. These records are required by law, support our EMR (workers' comp experience modifier), feed past-performance claims in proposals, and surface in CPARS evaluations.

## Aleut Federal Context — Why This Matters Beyond OSHA

Federal customers care about safety records:

- **CPARS** "Regulatory Compliance" element includes safety performance.
- **Past performance** volumes in proposals routinely include TRIR / DART rates.
- **USACE / NAVFAC** prequalification considers safety record.
- **Workers' comp EMR** affects bid pricing on labor-heavy work.
- **OSHA inspections** triggered by elevated rates or a fatality bring scrutiny across all our sites.

Misrecording (under-recording especially) is its own violation. On a federal contract it can also be False Claims Act exposure where safety-billable line items are involved.

## Forms and Cadence

| Form | Purpose | Cadence |
|------|---------|---------|
| **OSHA 300 Log** | Running log of recordable injuries/illnesses for the calendar year. One per establishment. | Updated within 7 calendar days of recordability determination |
| **OSHA 301 Incident Report** | Detailed record for each 300 entry. May use insurance carrier's First Report of Injury as equivalent. | Within 7 calendar days |
| **OSHA 300A Annual Summary** | Year-end summary. | Completed by Feb 1; posted Feb 1 – Apr 30 in each establishment in a visible place |
| **OSHA ITA (Electronic Submission)** | For establishments with 250+ employees OR 20-249 employees in designated high-risk industries (construction is included for many NAICS). | Annual; due March 2 for the prior year |

Retention: **5 years following the year the records cover** (29 C.F.R. 1904.33).

## Workflow

### Recordability Determination

For each injury or illness, walk through 1904.5 through 1904.7:

1. **Work-related?** (1904.5) Default yes if it occurred at the worksite during the work activity, unless an exception applies (e.g., common cold, voluntary fitness activity, personal grooming).
2. **New case?** (1904.6) Or is this a continuation of a prior recordable case (in which case it's not a new entry, but may extend prior days).
3. **Meets a recording criterion?** (1904.7) Any of:
   - Death.
   - Days away from work.
   - Restricted work or transfer to another job.
   - Medical treatment beyond first aid.
   - Loss of consciousness.
   - Significant injury or illness diagnosed by a physician or other licensed health care professional.
4. **Special-case condition?** (1904.8 – 1904.12) Needlestick / sharps; medical removal; hearing loss; TB; HIV/HBV/HCV; cancer / chronic disease (always recordable).

If yes to all → record on OSHA 300 and 301 within 7 calendar days.

### What Is "First Aid" (Not Recordable)?

First aid is defined narrowly in 1904.7(b)(5)(ii). Examples (non-recordable):

- Using non-prescription medication at non-prescription strength.
- Tetanus shots.
- Cleaning, flushing, soaking surface wounds.
- Wound coverings (band-aids, gauze pads).
- Hot or cold therapy.
- Non-rigid means of support (elastic bandages, wraps, non-rigid back belts).
- Temporary immobilization while transporting an accident victim.
- Drilling fingernail or toenail to relieve pressure; draining fluid from a blister.
- Eye patches.
- Removing foreign bodies from eye using irrigation or a cotton swab.
- Removing splinters or foreign material by irrigation, tweezers, etc., except from the eye.
- Finger guards.
- Massages.
- Drinking fluids for relief of heat stress.

Anything beyond these counts as medical treatment → recordable if work-related.

### Form 300 Entry Fields

For each case:
- Case number.
- Employee name and job title.
- Date of injury or illness onset.
- Description (where, what was the employee doing, how it occurred, the parts of body affected).
- Classification (death; days away; job transfer or restriction; other recordable).
- Days away from work; days job transfer / restriction.
- Type (injury; illness category).

### Annual Summary (Form 300A)

Required totals for the calendar year:
- Total cases by classification.
- Total number of days away from work and restricted/transferred.
- Total cases by type.
- Annual average number of employees.
- Total hours worked by all employees.

**Posting**: Feb 1 – Apr 30 in each establishment, in a visible place.

**Certification**: Form 300A signed by a "company executive" (1904.32(b)(4)). Owner, CEO/President, highest-ranking officer at the establishment, or immediate supervisor of the highest-ranking officer.

### Electronic Submission (ITA)

If the establishment meets the threshold:
- Submit 300A annually by March 2.
- 250+ employees: 300A required.
- 20–249 employees in designated high-risk NAICS (construction is included for most NAICS we use): 300A required.
- 100+ employees in certain industries: 300 and 301 also required (verify under the current rule; OSHA has been expanding this).

Use OSHA's ITA portal: https://www.osha.gov/injuryreporting/

### Rate Calculations

For each rate, use the OSHA formula:

- **TRIR** (Total Recordable Incident Rate) = (Number of OSHA recordable cases × 200,000) / Total hours worked.
- **DART** (Days Away, Restricted, or Transferred) Rate = (Number of cases with days away, restricted, or transferred × 200,000) / Total hours worked.
- **Fatality rate** = (Number of fatalities × 200,000) / Total hours worked.

200,000 = 100 full-time employees × 2,000 hours per year — a normalization constant.

Compare AF rates against industry NAICS averages (BLS publishes annual data) for proposal past performance and self-assessment.

## Hard Rules

- **Never under-record.** Recordability is not a judgment call where the case meets a 1904.7 criterion.
- **Never let the 7-day window lapse** without an entry.
- **Always post 300A Feb 1 – Apr 30** in each establishment.
- **Always submit to ITA** by March 2 if the threshold applies.
- **Retention is 5 years** — preserve all records.
- **Employee access** — workers, former workers, and their representatives have a right to copies (1904.35). Don't refuse.
- **OSHA access** — inspectors and BLS have a right to records on request (1904.40).
- **Mandatory disclosure (FAR 52.203-13)** — if under-recording involved fraud / FCA exposure, route to GC.

## Output Format

```markdown
## OSHA Recordkeeping Action: [Record Incident / Annual Summary / ITA Submit / Rate Calc]

**Establishment:** [...] | **Reporting period:** [year]

### Recordability Determination (per incident)
- Case ID: [...]
- Work-related (1904.5): Yes / No
- New case (1904.6): Yes / No
- Criterion met (1904.7): [death / days away / restricted / med treatment beyond first aid / loss of consciousness / significant diagnosis]
- Decision: Recordable / First aid only / Not work-related
- Recorded on 300 (date): [...]
- 301 filed (date): [...]

### Annual Summary (300A)
| Category | Count |
| Total cases | |
| Cases with days away | |
| Cases with job transfer / restriction | |
| Cases with other recordable | |
| Total days away from work | |
| Total days job transfer / restriction | |
| Injuries | |
| Skin disorders | |
| Respiratory conditions | |
| Poisonings | |
| Hearing loss | |
| All other illnesses | |
| **Annual avg employees** | |
| **Total hours worked** | |
| **Certified by** | [executive name] |

### Rates
- TRIR: [calculation]
- DART: [calculation]
- Fatality rate: [calculation]
- Industry NAICS comparison: [BLS rate]

### ITA Submission Status
- Required? Yes / No
- Submitted (date): [...]
- Confirmation: [...]

### Posting Status (300A)
- Posted (date): [...]
- Location(s): [...]
- Removed (date, after Apr 30): [...]
```
