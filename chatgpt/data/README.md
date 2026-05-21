# Aleut Federal — Data (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **data** plugin. It is generated from `../../data/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Data`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (11 files: 1 company context + 10 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Build a dashboard tracking indirect-rate posture vs provisional vs forecast.
- Write SQL to reconcile job-cost ledger to GL by contract for last quarter.
- Statistical analysis: is our subcontractor utilization meeting the FAR 52.219-9 plan?
- Pull recent USAspending awards for this NAICS / agency / set-aside slice.

## Skills bundled

- **analyze** — Answer data questions -- from quick lookups to full analyses.
- **build-dashboard** — Build an interactive HTML dashboard with charts, filters, and tables.
- **create-viz** — Create publication-quality visualizations with Python.
- **data-context-extractor** — Generate or improve a company-specific data analysis skill by extracting tribal knowledge from analysts.
- **data-visualization** — Create effective data visualizations with Python (matplotlib, seaborn, plotly).
- **explore-data** — Profile and explore a dataset to understand its shape, quality, and patterns.
- **sql-queries** — Write correct, performant SQL across all major data warehouse dialects (Snowflake, BigQuery, Databricks, PostgreSQL, etc.).
- **statistical-analysis** — Apply statistical methods including descriptive stats, trend analysis, outlier detection, and hypothesis testing.
- **validate-data** — QA an analysis before sharing -- methodology, accuracy, and bias checks.
- **write-query** — Write optimized SQL for your dialect with best practices.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `snowflake`
- `databricks`
- `bigquery`
- `hex`
- `amplitude`
- `amplitude-eu`
- `atlassian`
- `definite`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../data/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
