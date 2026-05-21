# Aleut Federal — Marketing (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **marketing** plugin. It is generated from `../../marketing/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — Marketing`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` (9 files: 1 company context + 8 skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

- Draft a one-page capability statement for AFCEC HVAC/mechanical work.
- Build a federal-market campaign plan for AFCEA TechNet.
- Competitive brief on three primes likely to bid this SeaPort-NxG recompete.
- Review this case study for PIA, CUI, and CO-authorization issues.

## Skills bundled

- **brand-review** — Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes.
- **campaign-plan** — Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics.
- **competitive-brief** — Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats.
- **content-creation** — Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies.
- **draft-content** — Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations.
- **email-sequence** — Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks.
- **performance-report** — Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations.
- **seo-audit** — Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison.

## Connectors

The Claude version of this plugin references the following MCP connectors:

- `slack`
- `canva`
- `figma`
- `hubspot`
- `amplitude`
- `amplitude-eu`
- `notion`
- `ahrefs`
- `similarweb`
- `klaviyo`
- `supermetrics`
- `google-calendar`
- `gmail`

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../marketing/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
