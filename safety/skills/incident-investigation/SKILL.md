---
name: incident-investigation
description: Investigate a workplace incident or near-miss at an Aleut Federal construction site or office — fact gathering, root cause analysis, corrective and preventive actions, OSHA 300/300A/301 entry, customer notification, lessons learned. Includes fatality and serious-injury reporting (OSHA 1904.39: 8 hours for fatality, 24 hours for amputation / loss of eye / inpatient hospitalization).
argument-hint: "<incident description>"
---

# /incident-investigation — Aleut Federal Safety

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Investigate a workplace incident with the federal-contractor reporting obligations baked in.

## Aleut Federal Context — Mandatory Notifications

When an incident occurs, multiple reporting tracks fire in parallel:

| Trigger | Authority | Timeline | Where |
|---------|-----------|----------|-------|
| **Fatality** | OSHA 29 C.F.R. 1904.39 | **Within 8 hours** of death | OSHA (1-800-321-OSHA or online) |
| **Amputation / loss of eye / inpatient hospitalization** | OSHA 29 C.F.R. 1904.39 | **Within 24 hours** | OSHA |
| **Recordable injury / illness** | OSHA 29 C.F.R. 1904 | Logged on OSHA 300; OSHA 301 within 7 days | Internal log; OSHA 300A annual posting |
| **Any incident on USACE site** | EM 385-1-1 Section 01 / ENG Form 3394 | Immediate to Government safety office | Customer safety office |
| **Federal customer site (non-USACE)** | Contract terms (often within 24 hours) | Immediate to COR | COR + contract administration |
| **Property damage to GFP** | Contract terms (often FAR 52.245-1) | Per contract; document immediately | CO and Contracts |
| **Environmental release** | Various (CWA, RCRA, EPCRA) | Often within 15 min – 24 hr depending on substance | NRC / state |
| **Possible FCA / fraud signals from the incident** | FAR 52.203-13 | "Reasonable time" | GC |
| **Aleut Corp parent** | Per parent reporting | Material incidents only | AF executive → Aleut Corp |

Service restoration and family communication run in parallel with these. **None of the regulatory deadlines pause for internal investigation.**

## Workflow

### Step 1: Immediate Response (Minutes 0–60)

1. **Care for the injured** — first aid, EMS, transport.
2. **Secure the scene** — preserve evidence; do not disturb beyond what's needed for medical or to prevent further injury.
3. **Notify** internally: Site Superintendent → SSHO → AF Safety Director → CEO / President for serious incidents.
4. **Notify customer** per the contract (USACE / NAVFAC / agency safety office).
5. **Notify family** of injured worker (HR + leadership; coordinate with medical providers; never speculate on cause).
6. **Start OSHA fatality / serious-injury clock** if applicable. Make the OSHA call.

### Step 2: Fact Gathering (Hours 1–48)

- **Photographs / video** of the scene from multiple angles before disturbance.
- **Witness statements** — separate witnesses; written + recorded if possible; date, time, location of statement.
- **Physical evidence** — equipment involved, PPE worn, materials, environmental conditions.
- **Documents** — the AHA for the activity, training records of involved workers, equipment inspection records, weather data, recent change records.
- **Time-stamped timeline** of what happened in what order.

Witness statements should focus on **what each person observed** — not opinions on cause. Avoid leading questions.

### Step 3: Root Cause Analysis

Choose a method appropriate to severity:

- **5 Whys** for minor incidents.
- **Fishbone / Ishikawa diagram** for moderate.
- **TapRooT, Apollo, or formal RCA** for serious / fatal.

Surface **systemic** causes, not just human error:

- Training adequacy?
- AHA captured the hazard? Briefed daily?
- Equipment maintained and inspected?
- Procedure followed? If not, why not?
- Supervision adequate?
- Time pressure / production pressure?
- Worker fatigue / shift schedule?
- Communication / coordination?
- Subcontractor integration?
- Site conditions vs. plan?

"Worker made a mistake" is not a root cause — it's a symptom. Keep asking why.

### Step 4: Corrective and Preventive Actions

For each root cause, an action with owner and date:

- **Corrective** — fix the immediate problem (repair, replace, retrain).
- **Preventive** — address the system so it doesn't happen elsewhere (update the AHA, revise the procedure, change the training, change supervision, change the equipment spec).

CAPAs feed back into the APP and AHA for the activity.

### Step 5: OSHA Recordkeeping

Determine recordability per OSHA 1904:

- **Death** — recordable + reportable (8 hr).
- **Days away from work** — recordable.
- **Restricted work or transfer** — recordable.
- **Medical treatment beyond first aid** — recordable.
- **Loss of consciousness** — recordable.
- **Significant injury or illness diagnosed by a physician** — recordable.
- **Cancer, chronic irreversible disease, fractured / cracked bone or tooth, punctured eardrum** — always recordable.

If recordable:
- **OSHA 301** Incident Report within 7 calendar days.
- **OSHA 300** Log entry.
- **OSHA 300A** Summary — posted Feb 1 – April 30 of the following year.

### Step 6: Customer Reporting

- Formal incident report to the customer safety office (typically ENG Form 3394 on USACE sites; agency-specific forms elsewhere).
- Provide the investigation report when complete.
- Coordinate with Contracts before any communication that could be characterized as admitting liability.

### Step 7: Mandatory-Disclosure Check (FAR 52.203-13)

If the investigation surfaces evidence of:

- **False claims** (e.g., the incident reveals we were billing for safety controls we didn't implement).
- **Significant overpayment** (similar).
- **Criminal violations** (e.g., gross safety violations rising to criminal negligence; intentional concealment of prior incidents).

→ Route to GC for FAR 52.203-13 evaluation.

### Step 8: Lessons Learned

- Brief site personnel on findings and CAPAs.
- Share across AF projects with similar work.
- Update master AHAs and the corporate safety program.
- Consider safety stand-down (see `safety-stand-down` skill).

## Hard Rules

- **OSHA fatality / serious-injury deadlines are non-negotiable.** Make the call.
- **Do not disturb the scene** until safety / EMS / OSHA / investigators clear it.
- **Do not speculate on cause** in any communication outside the investigation team. Stick to facts.
- **Do not admit liability** to the customer; coordinate communications through Contracts and GC.
- **Do not retaliate against the injured worker or witnesses.** Whistleblower protections apply (29 U.S.C. § 660(c); FAR 52.203-17).
- **Do not skip recordability evaluation.** Under-recording OSHA 300 logs is its own violation and can be FCA exposure on safety-billable work.

## Output Format

```markdown
## Incident Report: [Title]

**Incident ID:** [...] | **Date/Time:** [...] | **Location:** [...] | **Contract:** [...]
**Severity:** [Near-miss / First aid / Recordable / Hospitalization / Amputation / Fatality]
**Persons involved:** [...]

### Notifications Filed
| Recipient | Timestamp | Method | Confirmation |
| OSHA | | | (if applicable) |
| Customer safety office | | | |
| AF executive | | | |
| Aleut Corp (if material) | | | |

### Sequence of Events
[timeline]

### Root Causes
[with method used]

### Corrective Actions
[with owners and dates]

### Preventive Actions
[with owners and dates]

### OSHA Recordkeeping
- 300 log entry: [Yes/No, case #]
- 301 form: [Yes/No, filed date]
- 300A: included in [year]

### Mandatory-Disclosure Check
[None / Routed to GC]

### Lessons Learned
[summary for distribution]
```
