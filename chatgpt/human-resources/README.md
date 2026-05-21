# Aleut Federal — People Operations (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **human-resources** plugin. It is generated from `../../human-resources/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — People Operations`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (10 files: 1 company context + 9 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Draft an offer letter for a cleared SECRET engineer on a SCA contract.
- Comp analysis: what's the WD floor for this labor category at this locality?
- What's our policy on hiring a former federal CO under 18 USC 207 / 2104?
- Build the 30/60/90-day onboarding plan for a new CUI-cleared analyst.

## Skills bundled

- **comp-analysis** — Analyze compensation — benchmarking, band placement, and equity modeling.
- **draft-offer** — Draft an offer letter with comp details and terms.
- **interview-prep** — Create structured interview plans with competency-based questions and scorecards.
- **onboarding** — Generate an onboarding checklist and first-week plan for a new hire.
- **org-planning** — Headcount planning, org design, and team structure optimization.
- **people-report** — Generate headcount, attrition, diversity, or org health reports.
- **performance-review** — Structure a performance review with self-assessment, manager template, and calibration prep.
- **policy-lookup** — Find and explain company policies in plain language.
- **recruiting-pipeline** — Track and manage recruiting pipeline stages.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `google calendar`
- `gmail`
- `notion`
- `atlassian`
- `ms365`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../human-resources/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
