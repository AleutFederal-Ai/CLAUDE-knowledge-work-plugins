# process-doc

> **What this skill does:** Document a business process — flowcharts, RACI, and SOPs. Use when formalizing a process that lives in someone's head, building a RACI to clarify who owns what, writing an SOP for a handoff or audit, or capturing the exceptions and edge cases of how work actually gets done.

# /process-doc — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

## Aleut Federal Context — Federal-Contractor SOPs

Federal-contractor SOPs need to support DCAA / DCMA / IPA inspection. Always include:

- **Authority** the process implements (FAR / DFARS / agency supplement clause, NIST 800-171 control, EM 385-1-1 requirement, etc.).
- **Scope** — which contracts / contract types this SOP applies to.
- **Roles & responsibilities (RACI)** — including the CO / COR interface where applicable.
- **Inputs / triggers**.
- **Steps** with control points (who approves, what evidence is created).
- **Records to retain** — link to retention per FAR 4.703 (typically 3 years after final payment).
- **Exceptions / escalations** — e.g., mandatory-disclosure path (FAR 52.203-13), CO notification (FAR 52.243-x changes, FAR 52.232-20/-22 LoF/LoC).
- **Review cadence** — at minimum annual; refresh whenever the underlying clause or program changes.
- **Owner / signature**.

SOPs covering CUI must include "CUI handling" steps consistent with DFARS 252.204-7012 / NIST 800-171; SOPs covering construction safety must reference USACE EM 385-1-1 and OSHA 29 C.F.R. Part 1926.

Document a business process as a complete standard operating procedure (SOP).

## Usage

```
/process-doc $ARGUMENTS
```

## How It Works

Walk me through the process — describe it, paste existing docs, or just tell me the name and I'll ask the right questions. I'll produce a complete SOP.

## Output

```markdown
## Process Document: [Process Name]
**Owner:** [Person/Team] | **Last Updated:** [Date] | **Review Cadence:** [Quarterly/Annually]

### Purpose
[Why this process exists and what it accomplishes]

### Scope
[What's included and excluded]

### RACI Matrix
| Step | Responsible | Accountable | Consulted | Informed |
|------|------------|-------------|-----------|----------|
| [Step] | [Who does it] | [Who owns it] | [Who to ask] | [Who to tell] |

### Process Flow
[ASCII flowchart or step-by-step description]

### Detailed Steps

#### Step 1: [Name]
- **Who**: [Role]
- **When**: [Trigger or timing]
- **How**: [Detailed instructions]
- **Output**: [What this step produces]

#### Step 2: [Name]
[Same format]

### Exceptions and Edge Cases
| Scenario | What to Do |
|----------|-----------|
| [Exception] | [How to handle it] |

### Metrics
| Metric | Target | How to Measure |
|--------|--------|----------------|
| [Metric] | [Target] | [Method] |

### Related Documents
- [Link to related process or policy]
```

## If Connectors Available

If **~~knowledge base** is connected:
- Search for existing process documentation to update rather than duplicate
- Publish the completed SOP to your wiki

If **~~project tracker** is connected:
- Link the process to related projects and workflows
- Create tasks for process improvement action items

## Tips

1. **Start messy** — You don't need a perfect description. Tell me how it works today and I'll structure it.
2. **Include the exceptions** — "Usually we do X, but sometimes Y" is the most valuable part to document.
3. **Name the people** — Even if roles change, knowing who does what today helps get the process right.
