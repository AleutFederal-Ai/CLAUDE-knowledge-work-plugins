---
name: pipeline-review
description: Analyze the Aleut Federal capture / BD pipeline through Shipley capture stages — prioritize pursuits, flag bid/no-bid hygiene, identify single-threaded teams, surface compliance gates (FAR 52.219-14, CMMC level, bonding, clearances), audit incumbency and recompete coverage. Use for weekly capture review, gate decisions, BD-leader portfolio review, or quarterly bid/no-bid retrospective.
argument-hint: "<segment, agency, vehicle, or capture manager>"
---

# /pipeline-review — Federal BD Pipeline Review

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

Federal BD pipelines work very differently from commercial sales pipelines. Stages are gated, evaluation timelines are predictable, and award decisions are driven by published criteria — not relationship momentum. This skill calibrates pipeline review to the **Shipley-style capture lifecycle** and the federal acquisition calendar.

## Capture Stages (Shipley-Aligned)

| # | Stage | What "done" looks like |
|---|-------|------------------------|
| 1 | **Identification** | Logged with agency, NAICS, PSC, set-aside guess, est. value, anticipated solicitation, source |
| 2 | **Qualification** | Initial bid/no-bid score: strategy fit, Pwin hypothesis, vehicle, set-aside fit, past performance, capacity, teaming |
| 3 | **Pursuit / Capture** | Capture plan approved; named capture mgr; customer engagement plan executing; teaming letters/NDAs; PTW range; competitor analysis; gap analysis |
| 4 | **Proposal Planning** | Pink-team prep; Sections L/M/H/C/J understood; proposal team named; color reviews scheduled; pricing strategy approved |
| 5 | **Proposal Development** | Pink → Red → Gold → White Glove on schedule; volumes coordinated; compliance matrix complete |
| 6 | **Submission** | Submitted; receipt acknowledged; PIA wall up; evaluation begins |
| 7 | **Evaluation / Q&A** | Respond to ENs, FPRs, clarifications; hold posture; protect PTW |
| 8 | **Award / Debrief** | Award notice; debrief requested within 3 days (FAR Part 15); lessons learned |
| 9 | **Protest Window** | GAO 10-day timeliness; counsel coordination |
| 10 | **Transition / NTP** | Kickoff; contract handoff to Operations; CDRL inception; CPARS baseline |

## Workflow

### Step 1: Pull the Pipeline

For each active opportunity, pull from CRM / capture system:
- Name, solicitation #, agency / sub-agency, vehicle.
- NAICS, PSC, set-aside type, contract type, PoP, est. value.
- Capture stage, capture mgr, color-review schedule, key dates.
- Pwin; fit score; PTW hypothesis.
- Teaming structure (prime / sub / JV; partners; workshare; FAR 52.219-14 plan).
- Incumbent (recompetes); CPARS where known.
- Compliance gates: CMMC level, clearances, bonding (Miller Act), CAS posture, OCONUS, ITAR/EAR, Section 889.

### Step 2: Hygiene Audit — Flag Each Opportunity That Has

- Stage age > standard (Identification stuck > 60 days; Qualification > 30; Capture without engagement in 30; Proposal Planning without pink scheduled within release window).
- Missing capture manager or proposal manager.
- Missing bid/no-bid decision at the appropriate gate.
- Solicitation released but no compliance matrix drafted.
- Pwin not updated in 30 days (or last gate).
- Single-threaded teaming — only one teammate where multiple disciplines required.
- FAR 52.219-14 risk — set-aside where staffing plan can't show self-performance.
- CMMC gap — L2 required, no clear path within timeline.
- Bonding gap — federal construction > $150K and surety capacity not confirmed.
- Clearance gap — facility / personnel clearances missing.
- Vehicle gap — we don't hold the prime vehicle and no teaming letter to a holder.
- OCI risk — flag for legal.

### Step 3: Prioritize

- **Must win** — strategic; on-vehicle; clear path; protect resources.
- **Will pursue** — favorable Pwin; resourceable; on-vehicle or teaming-clear.
- **Will participate / no-bid** — low Pwin or fit; consider sub-only or formal no-bid.

Apply realistic resource constraints (B&P budget, proposal-staff capacity, SME bandwidth).

### Step 4: Coverage View

| Slice | Win plan ($) | Pipeline 12-mo ($) | Probability-weighted ($) | Coverage ratio |
|-------|--------------|--------------------|--------------------------|----------------|
| Total | | | | (target 3–4×) |
| By customer agency | | | | |
| By contract type (FFP / T&M / CR / IDIQ) | | | | |
| By set-aside (8(a) SS / 8(a) competitive / SB / F&O) | | | | |
| By vehicle (GSA MAS / OASIS+ / SeaPort / SS / etc.) | | | | |
| By line of business (services / construction) | | | | |

Flag where coverage is < 2× on a critical slice.

### Step 5: Top Actions for the Week

5–10 specific actions tied to opportunity IDs and owners; each advances a stage, closes a hygiene flag, or unblocks a compliance gate.

### Step 6: Strategic Issues for Leadership

- Coverage gaps; capacity / B&P constraints; vehicle investments.
- 8(a) sole-source utilization vs plan.
- Recompete exposure — existing revenue up for competition in 12–24 months.
- Compliance posture risks (CMMC, bonding, clearances).

## Output Format

```markdown
## Pipeline Review — [Segment / Period]

**Period**: ...
**Reviewer**: ...
**Scope**: [agencies / vehicles / capture mgrs]

### Headline
- Active: ...
- Probability-weighted pipeline ($): ...
- Plan ($): ...
- Coverage: ...×
- Submitted, awaiting award ($): ...
- Win rate (trailing 12 mo): ...%

### Stage Distribution
[counts and $ by stage]

### Hygiene Flags
| Opportunity | Flag | Owner | Due |

### Top Priorities (Must Win / Will Pursue)

### Recommended No-Bids

### Coverage View
[table]

### Compliance / Vehicle Gaps to Close

### Recompete Watchlist (12–24 mo)

### Actions This Week
[5–10 specific, owner, due]
```

## Hard Rules

- No commitments to teammates outside written TA / JVA — coordinate with legal.
- FAR 52.219-14 plan must be credible at the stage when set-aside is in play.
- 8(a) sole-source eligibility is not a guarantee — SBA acceptance and CO discretion still apply.
- Mandatory disclosure under FAR 52.203-13 supersedes pipeline considerations — route credible evidence to GC.
