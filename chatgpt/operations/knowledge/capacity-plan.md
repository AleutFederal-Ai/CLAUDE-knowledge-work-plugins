# capacity-plan

> **What this skill does:** Plan resource capacity — workload analysis and utilization forecasting. Use when heading into quarterly planning, the team feels overallocated and you need the numbers, deciding whether to hire or deprioritize, or stress-testing whether upcoming projects fit the people you have.

# /capacity-plan — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

## Aleut Federal Context — Federal-Contractor Capacity Planning

Federal contracting capacity has dimensions commercial planning doesn't:

- **Direct vs indirect headcount** — direct flows to contracts and revenue; indirect (BD, contracts, IT, HR, accounting) sits in pools and drives indirect rates. Increases in indirect drive rate creep.
- **B&P / IR&D capacity** — finite annual budget, allocable per FAR 31.205-18; track utilization vs plan.
- **Cleared personnel** — facility / personnel security-clearance pipeline; lead times often 6–18 months for SECRET, longer for TS/SCI.
- **CMMC-ready personnel** — for CUI work, staff must be trained on the SSP and NIST 800-171 controls.
- **Labor categories** — T&M bill-rate exposure requires the LCAT mix to match the contract LCAT pricing.
- **Site-specific** — construction PMs, superintendents, SSHOs, USACE EM 385-1-1-qualified staff for Corps projects.
- **OCONUS / Alaska** — travel, locality pay, lift logistics; Service Contract Act locality WD differences.
- **FAR 52.219-14 self-performance** — set-aside contracts require demonstrable compliance.
- **Subcontractor capacity** — JVA workshare allocations must be planable, not theoretical.

Output: required headcount by labor category, clearance, and contract; B&P / IR&D burn; subcontractor commitments; hiring lead times; FAR 52.219-14 compliance evidence per set-aside contract.

Analyze team capacity and plan resource allocation.

## Usage

```
/capacity-plan $ARGUMENTS
```

## What I Need From You

- **Team size and roles**: Who do you have?
- **Current workload**: What are they working on? (Upload from project tracker or describe)
- **Upcoming work**: What's coming next quarter?
- **Constraints**: Budget, hiring timeline, skill requirements

## Planning Dimensions

### People
- Available headcount and skills
- Current allocation and utilization
- Planned hires and timeline
- Contractor and vendor capacity

### Budget
- Operating budget by category
- Project-specific budgets
- Variance tracking
- Forecast vs. actual

### Time
- Project timelines and dependencies
- Critical path analysis
- Buffer and contingency planning
- Deadline management

## Utilization Targets

| Role Type | Target Utilization | Notes |
|-----------|-------------------|-------|
| IC / Specialist | 75-80% | Leave room for reactive work and growth |
| Manager | 60-70% | Management overhead, meetings, 1:1s |
| On-call / Support | 50-60% | Interrupt-driven work is unpredictable |

## Common Pitfalls

- Planning to 100% utilization (no buffer for surprises)
- Ignoring meeting load and context-switching costs
- Not accounting for vacation, holidays, and sick time
- Treating all hours as equal (creative work ≠ admin work)

## Output

```markdown
## Capacity Plan: [Team/Project]
**Period:** [Date range] | **Team Size:** [X]

### Current Utilization
| Person/Role | Capacity | Allocated | Available | Utilization |
|-------------|----------|-----------|-----------|-------------|
| [Name/Role] | [hrs/wk] | [hrs/wk] | [hrs/wk] | [X]% |

### Capacity Summary
- **Total capacity**: [X] hours/week
- **Currently allocated**: [X] hours/week ([X]%)
- **Available**: [X] hours/week ([X]%)
- **Overallocated**: [X people above 100%]

### Upcoming Demand
| Project/Initiative | Start | End | Resources Needed | Gap |
|--------------------|-------|-----|-----------------|-----|
| [Project] | [Date] | [Date] | [X FTEs] | [Covered/Gap] |

### Bottlenecks
- [Skill or role that's oversubscribed]
- [Time period with a crunch]

### Recommendations
1. [Hire / Contract / Reprioritize / Delay]
2. [Specific action]

### Scenarios
| Scenario | Outcome |
|----------|---------|
| Do nothing | [What happens] |
| Hire [X] | [What changes] |
| Deprioritize [Y] | [What frees up] |
```

## If Connectors Available

If **~~project tracker** is connected:
- Pull current workload and ticket assignments automatically
- Show upcoming sprint or quarter commitments per person

If **~~calendar** is connected:
- Factor in PTO, holidays, and recurring meeting load
- Calculate actual available hours per person

## Tips

1. **Include all work** — BAU, projects, support, meetings. People aren't 100% available for project work.
2. **Plan for buffer** — Target 80% utilization. 100% means no room for surprises.
3. **Update regularly** — Capacity plans go stale fast. Review monthly.
