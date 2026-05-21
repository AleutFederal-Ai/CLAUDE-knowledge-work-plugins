---
name: subcontractor-safety-onboarding
description: Onboard a new subcontractor to an Aleut Federal construction site's safety program — sub prequalification (EMR, OSHA history, prior CPARS-type safety record), site-specific orientation, integration into the AF APP and AHA program, sub safety personnel verification (SSHO, competent persons, qualified persons), insurance certificates, and ongoing safety coordination expectations.
---

# /subcontractor-safety-onboarding — Aleut Federal Safety

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Bring a new subcontractor into AF's safety program on a federal construction site.

## Aleut Federal Context — Why Sub Safety Is Our Problem

On a federal construction contract:

- **Multi-employer worksite doctrine** (OSHA) holds the controlling employer (often the prime — us) responsible for hazards across the site, including sub-created hazards.
- **EM 385-1-1 Section 01** requires the prime to integrate subs into the safety program.
- **CPARS** "Regulatory Compliance" includes sub safety performance.
- **Davis-Bacon CBA successor** considerations may affect sub workforce.
- **FAR 52.222-6 / 52.222-41** flow-downs apply to subs and may carry safety-relevant compensation requirements.
- **FCA exposure** — billing for safety performance the subs didn't actually deliver is fraud territory.

## Workflow

### Step 1: Prequalification (Before Award)

Before issuing a subcontract, verify:

- **EMR** (Experience Modification Rate from workers' comp). Industry baseline = 1.0; lower is better. We typically prequalify subs with EMR ≤ 1.0 (or evidence of trend down with current controls).
- **OSHA history** — recordable rates trended over 3 years; any willful, serious, or repeat citations in the last 5 years; any open inspections.
- **Past performance** — references on safety performance from prior federal projects.
- **Insurance** — Workers' Comp, GL, Auto, Umbrella; limits meet our contract flowdowns + customer requirements.
- **Section 889 / SAM / FAPIIS** (see also `operations/vendor-review` for the full federal-contractor gate set).
- **Safety personnel** — does the sub have an OSHA-30-trained competent person? Site-specific Safety and Health Officer if the work requires?

A sub that fails prequalification needs an explicit waiver from AF Safety + GC.

### Step 2: Sub Safety Program Documentation

Collect and file:

- Sub's safety program / written safety manual.
- Sub's EM 385-1-1 acknowledgment (where applicable).
- Sub's training matrix for personnel on this project.
- Sub's drug-free workplace program (FAR 52.223-6).
- Sub's emergency action plan.

### Step 3: Subcontract Safety Flow-Downs

The subcontract must carry these safety provisions (verify in the executed sub agreement):

- Compliance with AF APP and all applicable AHAs.
- Compliance with EM 385-1-1, OSHA 1926, OSHA 1910, and contract-specific requirements.
- Right of AF SSHO to stop sub work for safety reasons.
- Sub's affirmative obligation to participate in toolbox talks, safety meetings, and stand-downs.
- Sub responsibility for daily inspections of its own work.
- Sub recordkeeping cooperation — share incident reports, OSHA 300/301 entries that occurred on our site.
- Insurance certificates with AF as additional insured.
- Indemnification per AF standard.

### Step 4: Site-Specific Orientation (Before Sub Workers Start)

Every sub worker, on day 1 at the site:

- AF and customer rules summary.
- Site layout, hazards, access controls.
- Required PPE.
- Site-specific AHAs the worker will be involved in.
- Emergency procedures (evacuation, medical, severe weather).
- Reporting expectations (near-misses, incidents, concerns).
- Stop-work authority (the sub worker has it).
- FAR 52.203-17 whistleblower protections.
- Drug-free workplace and post-incident testing protocol.
- Photography / publicity rules (no agency logos / contract numbers without CO authorization).
- CUI handling rules if the site touches CUI.

Document attendance with a sign-in. Re-orient when significant work changes.

### Step 5: Integrate Into Daily Operations

- **Daily toolbox talks** — sub workers attend.
- **AHA briefings** — sub workers signed onto every AHA for activities they'll perform.
- **Daily safety walks** — AF SSHO inspects sub work alongside its own.
- **Sub competent person** participates in weekly safety coordination meetings.
- **Incident reporting** — sub reports all near-misses, first-aid cases, and recordables to the AF SSHO within 24 hours.

### Step 6: Performance Monitoring and Corrective Action

- **Track sub safety metrics** alongside AF's: TRIR, DART, near-misses, observations.
- **Escalation ladder** for noncompliance:
 1. **Verbal coaching** by AF SSHO.
 2. **Written notice** to sub project manager.
 3. **Stop-work** on the specific activity until corrected.
 4. **Removal of the worker / crew** from the project.
 5. **Termination of the subcontract** for cause.
- **Document everything** — fairness in escalation matters, and CPARS / future award decisions ride on it.

### Step 7: Offboarding (At Sub Completion)

- Final safety walk of sub's work areas.
- Confirm sub returned any AF / GFP loaned safety equipment.
- Document sub's performance for AF's internal sub-evaluation library — informs future award decisions and feeds CPARS narrative.

## Hard Rules

- **No sub on site without orientation.** No exceptions, including "they're just here for a few hours."
- **No sub work without an accepted AHA** for the activity.
- **No exceptions to PPE / fall protection / confined space / hot work** for subs.
- **AF SSHO stop-work authority over sub work** is absolute. Don't let production pressure override.
- **Document insurance and Section 889 status** before the sub signs.
- **Mandatory disclosure (FAR 52.203-13)** — if a sub safety issue surfaces FCA / criminal / significant overpayment evidence, route to GC.

## Output Format

```markdown
## Sub Safety Onboarding: [Sub name] — [Project / Site]

**Sub:** [legal name + DUNS / CAGE]
**Scope:** [work the sub is performing]
**Site start date:** [...]

### Prequalification Status
- EMR (current year): [...] (acceptable: ≤ 1.0 or trend down)
- OSHA history (3 yr): [Recordables / Citations / Open inspections]
- Past performance references: [list]
- Insurance certificates received: [Yes / No]
- Section 889 / SAM / FAPIIS gates cleared: [Yes / No]
- Sub safety personnel verified: [SSHO, competent persons named with training]

### Subcontract Safety Flow-Downs Verified
- AHA / APP compliance: ☑
- Stop-work authority: ☑
- Toolbox / coordination participation: ☑
- Sub safety program submitted: ☑
- Insurance with AF additional insured: ☑

### Site-Specific Orientation
- Date(s) conducted: [...]
- Workers oriented: [count, names attached]
- Drug screen post-incident protocol explained: ☑

### Ongoing Coordination
- Weekly safety coordination meeting: [day/time]
- Daily toolbox attendance: [confirmed]
- Sub incident reporting cadence: 24 hours

### Action Items / Open Gaps
[any pending items before sub workers can start; with owners and dates]
```
