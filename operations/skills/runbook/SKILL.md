---
name: runbook
description: Create or update an operational runbook for a recurring task or procedure. Use when documenting a task that on-call or ops needs to run repeatably, turning tribal knowledge into exact step-by-step commands, adding troubleshooting and rollback steps to an existing procedure, or writing escalation paths for when things go wrong.
argument-hint: "<process or task name>"
---

# /runbook — Aleut Federal

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Aleut Federal Context — Common Federal-Contractor Runbooks

This skill commonly supports:
- Monthly cost-type voucher submission (SF 1034/1035) to PIEE/WAWF.
- DCAA / DCMA audit RFI response.
- Floor-check readiness drill on a worksite.
- CMMC SSP-aligned operating procedures for CUI.
- Mandatory-disclosure intake (FAR 52.203-13) routing to GC / disclosure committee.
- Cyber incident response under DFARS 252.204-7012 (72-hour DIBNet report).
- Construction safety incident response (EM 385-1-1 / OSHA 1926: recordable, DART, near-miss, fatal).
- CO / COR escalation for constructive changes (preserve REA rights).
- Limitation of Cost / Funds notification triggers (FAR 52.232-20/-22) at 75% / 85%.
- CPARS interim/final response.

Each runbook should include: authority, scope, trigger conditions, steps with commands or actions, decision branches, escalation contacts (legal / FSO / CO / CMMC L2 lead), evidence captured, and post-action review.

Create a step-by-step operational runbook for a recurring task or procedure.

## Usage

```
/runbook $ARGUMENTS
```

## Output

```markdown
## Runbook: [Task Name]
**Owner:** [Team/Person] | **Frequency:** [Daily/Weekly/Monthly/As Needed]
**Last Updated:** [Date] | **Last Run:** [Date]

### Purpose
[What this runbook accomplishes and when to use it]

### Prerequisites
- [ ] [Access or permission needed]
- [ ] [Tool or system required]
- [ ] [Data or input needed]

### Procedure

#### Step 1: [Name]
```
[Exact command, action, or instruction]
```
**Expected result:** [What should happen]
**If it fails:** [What to do]

#### Step 2: [Name]
```
[Exact command, action, or instruction]
```
**Expected result:** [What should happen]
**If it fails:** [What to do]

### Verification
- [ ] [How to confirm the task completed successfully]
- [ ] [What to check]

### Troubleshooting
| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| [What you see] | [Why] | [What to do] |

### Rollback
[How to undo this if something goes wrong]

### Escalation
| Situation | Contact | Method |
|-----------|---------|--------|
| [When to escalate] | [Who] | [How to reach them] |

### History
| Date | Run By | Notes |
|------|--------|-------|
| [Date] | [Person] | [Any issues or observations] |
```

## If Connectors Available

If **~~knowledge base** is connected:
- Search for existing runbooks to update rather than create from scratch
- Publish the completed runbook to your ops wiki

If **~~ITSM** is connected:
- Link the runbook to related incident types and change requests
- Auto-populate escalation contacts from on-call schedules

## Tips

1. **Be painfully specific** — "Run the script" is not a step. "Run `python sync.py --prod --dry-run` from the ops server" is.
2. **Include failure modes** — What can go wrong at each step and what to do about it.
3. **Test the runbook** — Have someone unfamiliar with the process follow it. Fix where they get stuck.
