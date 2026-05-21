# Aleut Federal — Customer Support (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **customer-support** plugin. It is generated from `../../customer-support/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Customer Support`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (6 files: 1 company context + 5 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Triage this incoming federal-customer ticket — severity per the contract SLA.
- Draft a response that preserves REA rights on a Government-directed change.
- Package this for engineering escalation with full CDRL/SLA impact context.
- Turn this resolved ticket into a CUI-safe KB article.

## Skills bundled

- **customer-escalation** — Package an escalation for engineering, product, or leadership with full context.
- **customer-research** — Multi-source research on a customer question or topic with source attribution.
- **draft-response** — Draft a professional customer-facing response tailored to the situation and relationship.
- **kb-article** — Draft a knowledge base article from a resolved issue or common question.
- **ticket-triage** — Triage and prioritize a support ticket or customer issue.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `intercom`
- `hubspot`
- `guru`
- `atlassian`
- `notion`
- `ms365`
- `google calendar`
- `gmail`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../customer-support/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
