---
name: it-incident-response
description: Run an internal IT incident response workflow for Aleut Federal corporate systems — triage, contain, investigate, communicate, post-incident review. Includes DFARS 252.204-7012 72-hour cyber incident reporting to DIBNet, FSO escalation for classified spillage, FCA / FAR 52.203-13 mandatory-disclosure triggers, customer (CO/COR) notification when an incident touches a federal contract system. Use when an IT incident is detected, when an alert needs severity assessment, or when writing a post-incident report.
argument-hint: "<incident description or alert>"
---

# /it-incident-response — Aleut Federal CIO Shop

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Run an IT incident response on Aleut Federal corporate systems. This is the **internal** IT incident process (AF's own systems, end-user services, corporate cloud tenants); the `engineering/incident-response` skill handles incidents on systems we operate for federal customers.

## Aleut Federal Context — Two Reporting Tracks Run in Parallel

Every cyber-relevant incident has **two tracks**:

### Track 1: Service Restoration (Internal)

Standard IR steps: detect → triage → contain → eradicate → recover → review.

### Track 2: Regulatory Reporting (Federal)

| Trigger | Authority | Timeline | Where |
|---------|-----------|----------|-------|
| **CUI affected on AF system** | DFARS 252.204-7012 | 72 hours from discovery | DIBNet (https://dibnet.dod.mil) |
| **CUI affected on a federal-customer system we operate** | DFARS 252.204-7012 | 72 hours from discovery | DIBNet + CO + COR |
| **Classified spillage** | NISPOM (32 C.F.R. Part 117) | Immediate | FSO → DCSA |
| **Personally identifiable information (PII) breach affecting federal employees** | Agency Privacy Act SORN | Per agency SORN (often 24-72 hours) | Agency Privacy Officer |
| **Fraud / FCA / significant overpayment signals** | FAR 52.203-13 | "Reasonable time" | GC → DOJ / agency OIG |
| **State PII breach (employees / subs / customers)** | State breach notification laws | Varies (often 30-90 days) | State AG / affected individuals |

Both tracks run **in parallel**. Service-restoration urgency never delays a mandatory regulatory report.

## Workflow

### Step 1: Detect and Classify

When an alert or report arrives:

1. **Confirm the incident is real** — investigate the alert; rule out false positive.
2. **Classify severity** using AF's defined classes (Sev 1–4 typically).
3. **Identify scope** — what systems, data, users, and federal contracts are involved.
4. **Identify data classes touched** — public, FOUO, CUI, classified, ITAR.
5. **Snapshot evidence** — preserve logs, memory, disk images **before** any remediation steps that would destroy evidence.

### Step 2: Trigger the Right Reporting Tracks

Run through the trigger matrix above. For each trigger that fires:

- Identify the responsible owner (CISO, FSO, GC, Privacy Officer).
- Start the clock on the reporting deadline.
- Open the formal report ticket / case.

### Step 3: Contain

- Isolate affected systems from the network where possible without destroying evidence.
- Disable compromised accounts.
- Block the indicator of compromise (IOC) across the perimeter.
- Document every containment action with a timestamp and operator.

### Step 4: Investigate (in Parallel with Restoration)

- Determine the attack vector and timeline.
- Determine what data was exfiltrated or accessed.
- Identify affected users and contracts.
- Preserve forensic artifacts for 90 days (DFARS 252.204-7012 requirement when CUI is involved).
- If malicious software was isolated, prepare submission to DoD Cyber Crime Center (DC3).

### Step 5: Communicate

| Audience | What to share | Timing |
|----------|---------------|--------|
| Executive leadership (CEO / CFO / COO / GC) | Initial brief, then daily updates | Within 1 hour of confirmation |
| Affected employees | What happened, what to do, what NOT to do (don't speculate publicly) | After containment, before public knowledge |
| Federal customers (CO / COR) — when their contract is touched | Formal written notice through Contracts; do NOT communicate directly with end users | Per contract terms; coordinate with Contracts and GC |
| DIBNet | Cyber Incident Report (CIR) | Within 72 hours of discovery for CUI cases |
| FSO | Classified spillage report | Immediate |
| GC | Any FCA / FAR 52.203-13 trigger | Immediate |
| State AGs / affected individuals | Per state breach notification law | Per the controlling statute |
| Aleut Corp (parent) | High-level brief if material | Per parent reporting policy |

Coordinate ALL external communication through GC. Never speculate publicly about cause, attribution, or impact while the investigation is open.

### Step 6: Recover

- Eradicate the threat (patch, rebuild, rotate credentials, kill persistence).
- Restore systems from clean backups.
- Validate restoration with a security scan.
- Monitor for recurrence for at least 30 days.

### Step 7: Post-Incident Review

Blameless internal review within 10 business days of recovery:

- Timeline of events.
- What worked, what didn't.
- Root cause(s).
- Preventive measures (technical and procedural).
- Updates to runbooks, training, and policies.

For incidents reported to DIBNet, prepare any follow-up reports the Government requests.

## Hard Rules

- **Never destroy evidence** even if it's inconvenient or "obvious" cause. Preserve 90 days minimum on CUI cases.
- **Never delay mandatory disclosure** to chase service restoration. The 72-hour DIBNet clock starts at discovery, not at convenience.
- **Never speculate publicly** about cause, attribution, or impact while the investigation is open.
- **Never communicate directly with federal end users** on a customer-system incident. CO/COR through Contracts.
- **Never overwrite or "clean up"** logs, audit trails, or forensic artifacts.
- **Always escalate** any signal of fraud, criminal activity, or significant overpayment to GC for FAR 52.203-13 evaluation.

## Output Format

```markdown
## IT Incident: [Title]

**Incident ID:** [...]
**Detected:** [datetime] | **Confirmed:** [datetime] | **Contained:** [datetime] | **Recovered:** [datetime]
**Severity:** Sev [1–4]
**Status:** Open / Contained / Recovered / Closed
**Lead:** [name / role]

### Scope
- Systems affected:
- Data classes touched:
- Federal contracts involved:
- Users affected:

### Reporting Track Status
| Trigger | Authority | Deadline | Status | Owner |
| ... | ... | ... | ... | ... |

### Timeline
[chronological log]

### Containment Actions
[what was done, by whom, when]

### Communications Sent
[audience, message, timestamp]

### Post-Incident Actions
[corrective and preventive]
```
