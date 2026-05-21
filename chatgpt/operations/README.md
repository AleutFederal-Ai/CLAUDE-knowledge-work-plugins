# Aleut Federal — Operations (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **operations** plugin. It is generated from `../../operations/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Operations`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (10 files: 1 company context + 9 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Status of our compliance posture — contracts, CMMC, OFCCP, FAR 52.203-13.
- Vendor diligence: walk a new sub through SAM, Section 889, FAPIIS, flow-downs.
- Risk assessment on adding 25 percent workshare to our JV mid-performance.
- Write a runbook for the DFARS 252.204-7012 72-hour cyber incident report.

## Skills bundled

- **capacity-plan** — Plan resource capacity — workload analysis and utilization forecasting.
- **change-request** — Create a change management request with impact analysis and rollback plan.
- **compliance-tracking** — Track Aleut Federal's federal-contractor compliance posture and audit readiness — FAR/DFARS clauses on active contracts, DCAA business systems, CMMC 2.0 / NIST 800-171, OFCCP / EEO / VEVRAA / Section 503, EO 14026 / SCA / Davis-Bacon, EM 385-1-1 / OSHA 1926 for construction, Section 889, Buy American / TAA / BABA, FAR 52.203-13 ethics, SAM registration, FAPIIS, CPARS.
- **process-doc** — Document a business process — flowcharts, RACI, and SOPs.
- **process-optimization** — Analyze and improve business processes.
- **risk-assessment** — Identify, assess, and mitigate operational risks.
- **runbook** — Create or update an operational runbook for a recurring task or procedure.
- **status-report** — Generate a status report with KPIs, risks, and action items.
- **vendor-review** — Evaluate a vendor or subcontractor for Aleut Federal — federal-contractor responsibility check, cost analysis with allowable-cost screen, risk assessment with SAM/FAPIIS/CMMC posture, flow-down readiness, and recommendation.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `google calendar`
- `gmail`
- `notion`
- `atlassian`
- `asana`
- `ms365`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../operations/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
