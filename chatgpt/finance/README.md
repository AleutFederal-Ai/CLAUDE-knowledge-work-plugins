# Aleut Federal — Finance (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **finance** plugin. It is generated from `../../finance/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Finance`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (9 files: 1 company context + 8 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Build the workpapers for an upcoming DCAA incurred-cost audit.
- Draft the journal entries to true up provisional indirect rates against actuals.
- What's the limitation-of-funds notification threshold and timing for this cost-type contract?
- Run a FAR Part 31 allowability review on this expense list.

## Skills bundled

- **audit-support** — Support DCAA, DCMA, IPA, and CO/COR audits of Aleut Federal — incurred cost audits, accounting-system reviews, business-system audits, forward-pricing rate audits, T&M / cost-reimbursable invoice audits, floor checks, CPSR purchasing system reviews, and CAS compliance audits.
- **close-management** — Manage the month-end close process with task sequencing, dependencies, and status tracking.
- **financial-statements** — Generate financial statements (income statement, balance sheet, cash flow) with period-over-period comparison and variance analysis.
- **journal-entry** — Prepare journal entries with proper debits, credits, and supporting detail.
- **journal-entry-prep** — Prepare journal entries with proper debits, credits, and supporting documentation for month-end close.
- **reconciliation** — Reconcile accounts by comparing GL balances to subledgers, bank statements, or third-party data.
- **sox-testing** — Generate sample selections, testing workpapers, and control assessments for federal-contractor internal controls — DCAA-adequate accounting system (SF 1408), DFARS 252.242-7005 contractor business systems (accounting, estimating, MMAS, purchasing, property, EVMS), FAR Part 31 cost-allowability controls, CAS compliance, and FAR 52.203-13 ethics program.
- **variance-analysis** — Decompose financial variances into drivers with narrative explanations and waterfall analysis.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `snowflake`
- `databricks`
- `bigquery`
- `slack`
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

If anything in `../../finance/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
