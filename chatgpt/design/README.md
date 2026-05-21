# Aleut Federal — Design (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **design** plugin. It is generated from `../../design/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Design`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (8 files: 1 company context + 7 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Run a Section 508 / WCAG 2.1 AA audit on this page.
- Critique this design for federal-user constraints (PIV/CAC, low connectivity).
- Generate a VPAT / ACR draft for this product.
- What USWDS components should we use for this agency form?

## Skills bundled

- **accessibility-review** — Run a WCAG 2.1 AA accessibility audit on a design or page.
- **design-critique** — Get structured design feedback on usability, hierarchy, and consistency.
- **design-handoff** — Generate developer handoff specs from a design.
- **design-system** — Audit, document, or extend your design system.
- **research-synthesis** — Synthesize user research into themes, insights, and recommendations.
- **user-research** — Plan, conduct, and synthesize user research.
- **ux-copy** — Write or review UX copy — microcopy, error messages, empty states, CTAs.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `figma`
- `linear`
- `asana`
- `atlassian`
- `notion`
- `intercom`
- `google calendar`
- `gmail`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../design/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
