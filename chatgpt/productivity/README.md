# Aleut Federal — Productivity (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **productivity** plugin. It is generated from `../../productivity/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Productivity`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (5 files: 1 company context + 4 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Start my day — what federal deadlines hit this week?
- Update tasks from my calendar; tag direct vs indirect charge codes.
- Add the Aleut Federal customer acronym glossary to memory.
- What did I commit to in yesterday's CO call?

## Skills bundled

- **memory-management** — Two-tier memory system that makes Claude a true workplace collaborator.
- **start** — Initialize the productivity system and open the dashboard.
- **task-management** — Simple task management using a shared TASKS.md file.
- **update** — Sync tasks and refresh memory from your current activity.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `notion`
- `asana`
- `linear`
- `atlassian`
- `ms365`
- `monday`
- `clickup`
- `google calendar`
- `gmail`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../productivity/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
