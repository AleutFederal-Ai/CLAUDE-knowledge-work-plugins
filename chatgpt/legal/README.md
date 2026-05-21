# Aleut Federal — Legal (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **legal** plugin. It is generated from `../../legal/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Legal`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (10 files: 1 company context + 9 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Review this teaming agreement against our default playbook.
- Run a compliance check on hiring a former Air Force contracting officer.
- Triage this NDA from a prime — green / yellow / red?
- What's our exposure on this FAR 52.219-14 self-performance question?

## Skills bundled

- **brief** — Generate contextual briefings for legal work — daily summary, topic research, or incident response.
- **compliance-check** — Run a compliance check on a proposed Aleut Federal action — a pursuit, teaming arrangement, hire, marketing claim, vendor selection, technology deployment, or process change — against the federal regulatory framework (FAR, DFARS, SBA 8(a), labor, environmental, cyber).
- **legal-response** — Generate a response to a common legal inquiry using configured templates, with built-in escalation checks for situations that shouldn't use a templated reply.
- **legal-risk-assessment** — Assess and classify legal risks using a severity-by-likelihood framework with escalation criteria.
- **meeting-briefing** — Prepare structured briefings for meetings with legal relevance and track resulting action items.
- **review-contract** — Review a federal prime contract, task order, subcontract, teaming agreement, or commercial agreement against Aleut Federal's negotiation playbook and the FAR/DFARS framework — flag deviations, generate redlines, and provide business-impact analysis.
- **signature-request** — Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution.
- **triage-nda** — Rapidly triage an incoming NDA and classify it as GREEN (standard approval), YELLOW (counsel review), or RED (full legal review).
- **vendor-check** — Check the status of existing agreements with a vendor across all connected systems — CLM, CRM, email, and document storage — with gap analysis and upcoming deadlines.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `box`
- `egnyte`
- `atlassian`
- `ms365`
- `docusign`
- `google-calendar`
- `gmail`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../legal/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
