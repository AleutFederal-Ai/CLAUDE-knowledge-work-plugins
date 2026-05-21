# Aleut Federal — Engineering (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **engineering** plugin. It is generated from `../../engineering/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Engineering`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (11 files: 1 company context + 10 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Write an ADR for moving this system from on-prem to FedRAMP Moderate.
- Code review: flag NIST 800-171 / FIPS / Section 889 / Section 508 issues.
- Build the deploy checklist with ATO boundary and POA&M evidence steps.
- We had a possible cyber incident on a DFARS 7012 system — walk me through the response.

## Skills bundled

- **architecture** — Create or evaluate an architecture decision record (ADR).
- **code-review** — Review code changes for security, performance, and correctness.
- **debug** — Structured debugging session — reproduce, isolate, diagnose, and fix.
- **deploy-checklist** — Pre-deployment verification checklist.
- **documentation** — Write and maintain technical documentation.
- **incident-response** — Run an incident response workflow — triage, communicate, and write postmortem.
- **standup** — Generate a standup update from recent activity.
- **system-design** — Design systems, services, and architectures.
- **tech-debt** — Identify, categorize, and prioritize technical debt.
- **testing-strategy** — Design test strategies and test plans.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `linear`
- `asana`
- `atlassian`
- `notion`
- `github`
- `pagerduty`
- `datadog`
- `google calendar`
- `gmail`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../engineering/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
