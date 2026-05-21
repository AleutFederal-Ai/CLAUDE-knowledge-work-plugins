# Aleut Federal — Program & Product Management (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **product-management** plugin. It is generated from `../../product-management/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Program & Product Management`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (9 files: 1 company context + 8 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Write a CDRL-compliant feature spec for this task-order requirement.
- Update the roadmap to reflect the new option-year exercise and CR risk.
- Sprint planning: load the backlog against direct-vs-indirect capacity and clearance constraints.
- Draft the stakeholder update for the CO and the AF leadership team.

## Skills bundled

- **competitive-brief** — Create a competitive analysis brief for one or more competitors or a feature area.
- **metrics-review** — Review and analyze product metrics with trend analysis and actionable insights.
- **product-brainstorming** — Brainstorm product ideas, explore problem spaces, and challenge assumptions as a thinking partner.
- **roadmap-update** — Update, create, or reprioritize your product roadmap.
- **sprint-planning** — Plan a sprint — scope work, estimate capacity, set goals, and draft a sprint plan.
- **stakeholder-update** — Generate a stakeholder update tailored to audience and cadence.
- **synthesize-research** — Synthesize user research from interviews, surveys, and feedback into structured insights.
- **write-spec** — Write a feature spec or PRD from a problem statement or feature idea.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `linear`
- `asana`
- `monday`
- `clickup`
- `atlassian`
- `notion`
- `figma`
- `amplitude`
- `amplitude-eu`
- `pendo`
- `intercom`
- `fireflies`
- `google-calendar`
- `gmail`
- `similarweb`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../product-management/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
