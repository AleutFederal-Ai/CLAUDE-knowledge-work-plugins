---
name: architecture
description: Create or evaluate an architecture decision record (ADR). Use when choosing between technologies (e.g., Kafka vs SQS), documenting a design decision with trade-offs and consequences, reviewing a system design proposal, or designing a new component from requirements and constraints.
---

# /architecture — Aleut Federal

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

## Aleut Federal Context — Federal IT Architecture Constraints

Architecture decisions on federal contracts must consider:

- **FIPS 199 categorization** (Low / Moderate / High) per system CIA impact; controls flow from this.
- **NIST RMF (SP 800-37)** — every decision affects the system's ATO posture, SSP, and POA&M.
- **NIST SP 800-53 baseline** — controls matching the FIPS 199 level; inheritance from a FedRAMP provider where applicable.
- **CUI handling** — DFARS 252.204-7012 / NIST 800-171 for non-federal systems handling CUI; CMMC level required by the contract.
- **Cloud hosting** — FedRAMP Moderate or High; for DoD CUI, DoD IL4 / IL5; classified IL6.
- **Cryptography** — FIPS 140-2/140-3 validated modules only; CMVP certificate on file.
- **Software supply chain** — EO 14028 SBOM, NIST SP 800-218 SSDF attestation, Section 889, BAA/TAA/BABA on hardware.
- **Accessibility** — Section 508 / WCAG 2.1 AA for any UI delivered to or used by federal users.
- **Data residency / personnel** — CONUS storage; U.S.-person admin requirements; ITAR-controlled data requires controlled environments.
- **Records retention** — per the contract (often FAR 4.703 baseline: 3 years after final payment).

Every ADR records the federal authority driving the constraint, not just the technical trade-off.

Create an Architecture Decision Record (ADR) or evaluate a system design.

## Usage

```
/architecture $ARGUMENTS
```

## Modes

**Create an ADR**: "Should we use Kafka or SQS for our event bus?"
**Evaluate a design**: "Review this microservices proposal"
**System design**: "Design the notification system for our app"

See the **system-design** skill for detailed frameworks on requirements gathering, scalability analysis, and trade-off evaluation.

## Output — ADR Format

```markdown
# ADR-[number]: [Title]

**Status:** Proposed | Accepted | Deprecated | Superseded
**Date:** [Date]
**Deciders:** [Who needs to sign off]

## Context
[What is the situation? What forces are at play?]

## Decision
[What is the change we're proposing?]

## Options Considered

### Option A: [Name]
| Dimension | Assessment |
|-----------|------------|
| Complexity | [Low/Med/High] |
| Cost | [Assessment] |
| Scalability | [Assessment] |
| Team familiarity | [Assessment] |

**Pros:** [List]
**Cons:** [List]

### Option B: [Name]
[Same format]

## Trade-off Analysis
[Key trade-offs between options with clear reasoning]

## Consequences
- [What becomes easier]
- [What becomes harder]
- [What we'll need to revisit]

## Action Items
1. [ ] [Implementation step]
2. [ ] [Follow-up]
```

## If Connectors Available

If **~~knowledge base** is connected:
- Search for prior ADRs and design docs
- Find relevant technical context

If **~~project tracker** is connected:
- Link to related epics and tickets
- Create implementation tasks

## Tips

1. **State constraints upfront** — "We need to ship in 2 weeks" or "Must handle 10K rps" shapes the answer.
2. **Name your options** — Even if you're leaning one way, I'll give a more balanced analysis with explicit alternatives.
3. **Include non-functional requirements** — Latency, cost, team expertise, and maintenance burden matter as much as features.
