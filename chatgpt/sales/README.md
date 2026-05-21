# Aleut Federal — BD & Capture (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **sales** plugin. It is generated from `../../sales/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — BD & Capture`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (10 files: 1 company context + 9 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Research USACE Mobile District — pipeline, vehicles, recompete watch.
- Prep me for an OSDBU capability briefing at GSA next week.
- Pipeline review for Q3 — flag hygiene issues and recommend no-bids.
- Build a competitive snapshot on [Prime X] for an OASIS+ recompete.

## Skills bundled

- **account-research** — Research a federal agency, prime contractor, or specific federal contract for Aleut Federal capture.
- **call-prep** — Prepare for a federal BD / capture call — agency or prime customer meeting, industry day, sources-sought interaction, teaming negotiation, debrief, post-award kickoff.
- **call-summary** — Process call notes or a transcript — extract action items, draft follow-up email, generate internal summary.
- **competitive-intelligence** — Research your competitors and build an interactive battlecard.
- **create-an-asset** — Generate tailored sales assets (landing pages, decks, one-pagers, workflow demos) from your deal context.
- **daily-briefing** — Start your day with a prioritized sales briefing.
- **draft-outreach** — Research a prospect then draft personalized outreach.
- **forecast** — Generate a weighted sales forecast with best/likely/worst scenarios, commit vs.
- **pipeline-review** — Analyze the Aleut Federal capture / BD pipeline through Shipley capture stages — prioritize pursuits, flag bid/no-bid hygiene, identify single-threaded teams, surface compliance gates (FAR 52.219-14, CMMC level, bonding, clearances), audit incumbency and recompete coverage.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `hubspot`
- `close`
- `clay`
- `zoominfo`
- `notion`
- `atlassian`
- `fireflies`
- `ms365`
- `apollo`
- `outreach`
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

If anything in `../../sales/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
