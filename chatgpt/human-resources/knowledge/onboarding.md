# onboarding

> **What this skill does:** Generate an onboarding checklist and first-week plan for a new hire. Use when someone has a start date coming up, building the pre-start task list (accounts, equipment, buddy), scheduling Day 1 and Week 1, or setting 30/60/90-day goals for a new team member.

# /onboarding — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

## Aleut Federal Context — Federal-Contractor Onboarding

### Day 0 / pre-start
- I-9 + E-Verify within 3 business days (FAR 52.222-54).
- Pre-employment drug screen (FAR 52.223-6).
- Background check appropriate to role/contract.
- Cleared roles: clearance passback via DCSA; SF-86 if new; continuous-evaluation briefing.
- CUI roles: SSP / NIST 800-171 acknowledgments; account in authorized environment.
- Code of Business Ethics acknowledgment (FAR 52.203-13).
- Workplace posters at site (DOL, OFCCP, whistleblower).
- SCA / DBA roles: WD posted; H&W enrollment.

### Day 1
- Timekeeping training and acknowledgment (DFARS 252.242-7006(c)(6) — daily total time accounting).
- Charge codes for assigned contract / indirect pool.
- IT provisioning aligned to clearance and CUI level.
- Safety briefing — construction: EM 385-1-1 / OSHA 1926 site-specific, APP/AHA.
- Ethics training enrollment (FAR 52.203-13).

### Week 1
- Annual ethics training (if due).
- Cybersecurity awareness (NIST 800-171 3.2.x).
- Mentor / buddy.
- Contract / program orientation: PWS, CDRLs, key personnel, CO/COR.
- 30/60/90 plan tied to contract scope.

### Within 90 days
- Probationary review and contract-readiness confirmation.
- Whistleblower-protection refresher (FAR 52.203-17).
- OCONUS: country clearance; TCP briefing if ITAR.

Document each step with date and acknowledger; retain per FAR 4.703 / agency rules.

Generate a comprehensive onboarding plan for a new team member.

## Usage

```
/onboarding $ARGUMENTS
```

## What I Need From You

- **New hire name**: Who's starting?
- **Role**: What position?
- **Team**: Which team are they joining?
- **Start date**: When do they start?
- **Manager**: Who's their manager?

## Output

```markdown
## Onboarding Plan: [Name] — [Role]
**Start Date:** [Date] | **Team:** [Team] | **Manager:** [Manager]

### Pre-Start (Before Day 1)
- [ ] Send welcome email with start date, time, and logistics
- [ ] Set up accounts: email, Slack, [tools for role]
- [ ] Order equipment (laptop, monitor, peripherals)
- [ ] Add to team calendar and recurring meetings
- [ ] Assign onboarding buddy: [Suggested person]
- [ ] Prepare desk / remote setup instructions

### Day 1
| Time | Activity | With |
|------|----------|------|
| 9:00 | Welcome and orientation | Manager |
| 10:00 | IT setup and tool walkthrough | IT / Buddy |
| 11:00 | Team introductions | Team |
| 12:00 | Welcome lunch | Manager + Team |
| 1:30 | Company overview and values | Manager |
| 3:00 | Role expectations and 30/60/90 plan | Manager |
| 4:00 | Free time to explore tools and docs | Self |

### Week 1
- [ ] Complete required compliance training
- [ ] Read key documentation: [list for role]
- [ ] 1:1 with each team member
- [ ] Shadow key meetings
- [ ] First small task or project assigned
- [ ] End-of-week check-in with manager

### 30-Day Goals
1. [Goal aligned to role]
2. [Goal aligned to role]
3. [Goal aligned to role]

### 60-Day Goals
1. [Goal]
2. [Goal]

### 90-Day Goals
1. [Goal]
2. [Goal]

### Key Contacts
| Person | Role | For What |
|--------|------|----------|
| [Manager] | Manager | Day-to-day guidance |
| [Buddy] | Onboarding Buddy | Questions, culture, navigation |
| [IT Contact] | IT | Tool access, equipment |
| [HR Contact] | HR | Benefits, policies |

### Tools Access Needed
| Tool | Access Level | Requested |
|------|-------------|-----------|
| [Tool] | [Level] | [ ] |
```

## If Connectors Available

If **~~HRIS** is connected:
- Pull new hire details and team org chart
- Auto-populate tools access list based on role

If **~~knowledge base** is connected:
- Link to relevant onboarding docs, team wikis, and runbooks
- Pull the team's existing onboarding checklist to customize

If **~~calendar** is connected:
- Create Day 1 calendar events and Week 1 meeting invites automatically

## Tips

1. **Customize for the role** — An engineer's onboarding looks different from a designer's.
2. **Don't overload Day 1** — Focus on setup and relationships. Deep work starts Week 2.
3. **Assign a buddy** — Having a go-to person who isn't their manager makes a huge difference.
