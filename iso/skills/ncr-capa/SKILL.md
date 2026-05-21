---
name: ncr-capa
description: Manage a Nonconformity Report (NCR) and Corrective / Preventive Action (CAPA) across Aleut Federal ISO management systems — ISO 9001 § 10.2 / 14001 § 10.2 / 45001 § 10.2 / 27001 § 10.1. Containment, root cause analysis, correction, corrective action, verification of effectiveness, closure. Single process across all four standards; record systems aligned for surveillance auditor inspection.
argument-hint: "<NCR ID or description>"
---

# /ncr-capa — Aleut Federal ISO

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Single NCR / CAPA process covering all four AF ISO management systems. Triggered by internal audit findings, external audit findings, customer complaints, incidents, near-misses, supplier failures, monitoring data, or worker reports.

## Aleut Federal Context — Why One Process Across Four Standards

Every standard (ISO 9001 / 14001 / 45001 / 27001) requires the same conceptual process:

1. React to the nonconformity.
2. Evaluate the need for action to eliminate the cause(s).
3. Determine and implement action.
4. Verify effectiveness.
5. Make changes to the management system if needed.
6. Retain documented information.

Running one tool / one process across all four:
- Cross-pollinates lessons (a 27001 finding may reveal a 9001 issue and vice versa).
- Reduces duplicate tracking.
- Gives the surveillance auditor a single, complete view.
- Saves staff time.

## NCR Lifecycle

### 1. Identification and Logging

Triggers:
- Internal audit finding.
- External / surveillance / customer audit finding.
- Customer complaint or CPARS comment.
- Incident or near-miss (45001; cross-reference to `safety/incident-investigation`).
- Security incident (27001; cross-reference to `cio-shop/it-incident-response`).
- Process metric out-of-spec.
- Worker concern / whistleblower report.
- Supplier failure.
- Government property loss / damage (cross-reference to `cio-shop/it-asset-management` for GFP).

Each NCR is logged with:
- **Unique ID** (sequential or formatted by year + counter).
- **Source / trigger**.
- **Standard(s)** affected — often more than one.
- **Process(es)** affected.
- **Date raised**, **raised by**.
- **Description** — specific, evidence-based, dated.
- **Severity** — Critical / Major / Minor.
- **Owner** — process owner accountable for closure.
- **Target dates** — containment, RCA, CAPA implementation, verification.

### 2. Containment

Immediate action to stop the bleeding **before** RCA is complete. Examples:

- Quarantine non-conforming product.
- Suspend the affected process.
- Notify customer if their deliverable is affected.
- Disable the system / account / device.
- Stop work on a safety hazard.

Containment is documented and time-stamped.

### 3. Root Cause Analysis

Choose method by severity (5 Whys, Fishbone, Apollo / TapRooT, ABS / FMEA).

Push past "human error" — the question is **why did the system let this happen**.

Categories to probe:
- Training gap.
- Procedure absent, wrong, or unclear.
- Process design flaw.
- Supervision / oversight failure.
- Equipment / tool / system failure.
- External factor (supplier, weather, regulatory change).
- Resource constraint (time, money, people).
- Cultural / incentive misalignment.

### 4. Correction (Immediate Fix)

Address the specific instance:
- Rework the deliverable.
- Re-train the worker.
- Restore the system.
- Reissue the customer-affecting communication.

Correction is the visible fix. It's not the system change — that's the next step.

### 5. Corrective Action (System Fix)

Change the system so the same root cause cannot produce the same nonconformity again.

Examples:
- Revise the procedure.
- Update the AHA.
- Update training and re-train the population.
- Change the supplier qualification.
- Add an automated control (e.g., a workflow gate).
- Change the metric and the monitoring frequency.

Document the changed procedure / SSP / AHA with the revision number tied to the NCR.

### 6. Preventive Action (When Applicable)

ISO has stepped back from "preventive action" as a separate clause (it's now subsumed under risk-based thinking), but the concept remains useful: where the same root cause could produce a nonconformity in **adjacent** processes, address them proactively.

### 7. Verification of Effectiveness

After implementation, **verify** the fix actually works. Typically:

- Sample new output of the process after a defined interval.
- Re-audit the specific clause / control.
- Monitor a leading indicator metric.

If verification fails, the CAPA is not closed — reopen, deepen the RCA, try again.

### 8. Closure

NCR closes only when:
- Containment, correction, and corrective action all executed.
- Effectiveness verified.
- Documentation complete.
- Process owner and quality manager sign off.

Closed NCRs are reviewed in the next Management Review for trends.

## Severity Calibration

| Severity | Definition | Default response cadence |
|----------|-----------|-------------------------|
| **Critical** | Safety hazard with imminent injury risk; CUI / classified spillage; FCA exposure; customer-impacting delivery failure on a major program | Containment within 24 hours; RCA within 5 days; CAPA within 30 days |
| **Major** | Systemic process failure; recordable injury; significant data exposure; CPARS-risk customer complaint; external audit finding | Containment within 48 hours; RCA within 10 days; CAPA within 60 days |
| **Minor** | Isolated single-instance lapse; first-aid incident; minor procedural gap | Containment within 5 days; RCA within 21 days; CAPA within 90 days |

## Cross-Standard Notes

| Cue from | Implications |
|----------|--------------|
| **45001 incident** | Update AHA; possible APP change; cross-reference to `safety/incident-investigation`; OSHA recordability separately tracked |
| **27001 security incident** | Update SSP/POA&M; possible DFARS 252.204-7012 72-hour report; cross-reference to `cio-shop/it-incident-response` |
| **14001 environmental release** | Regulatory reporting (CWA/CAA/RCRA) on its own clock; CAPA addresses the underlying control |
| **9001 customer complaint** | CPARS narrative implication; coordinate with PMO on customer-facing response |

## Hard Rules

- **Containment is immediate.** Don't wait for RCA before stopping the bleeding.
- **Verification is required.** A CAPA without effectiveness verification is not a CAPA.
- **Aging CAPAs are reportable** at every Management Review and to the next surveillance auditor.
- **Pattern detection** — three CAPAs with the same root cause means the system change isn't holding; reopen.
- **Mandatory disclosure (FAR 52.203-13)** — if NCR surfaces FCA / criminal / significant overpayment evidence, route to GC.
- **Don't downgrade severity** to make a deadline. Honest classification supports the system.

## Output Format

```markdown
## NCR / CAPA: [ID]

**Source:** [internal audit / customer / incident / etc.]
**Standard(s) affected:** [9001 / 14001 / 45001 / 27001]
**Severity:** [Critical / Major / Minor]
**Owner:** [...]
**Status:** [Open / In Progress / Awaiting Verification / Closed]

### Description
[specific, evidence-based]

### Containment
[actions, owners, dates]

### Root Cause
[method used; cause(s) identified]

### Correction (immediate fix)
[actions, owners, dates]

### Corrective Action (system fix)
[actions, owners, dates, document references]

### Verification of Effectiveness
[method, sample, date verified, result]

### Cross-Standard Implications
[other standards' systems / procedures that need updating]

### Closure
- Process owner sign-off: [date]
- Quality Manager sign-off: [date]
- Closed: [date]
```
