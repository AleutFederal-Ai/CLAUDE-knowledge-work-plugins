# Aleut Federal — OpenAI Skills

This directory contains the Aleut Federal skill library packaged as **native OpenAI Skills** (the format used by ChatGPT, Codex, Atlas, and API installations). Every Skill here is generated from the canonical `<plugin>/skills/<name>/SKILL.md` files elsewhere in this repo by [`build.py`](./build.py).

> **Skills vs. Custom GPTs.** OpenAI Skills are atomic, installable capabilities — each one a folder with `SKILL.md` + `agents/openai.yaml` + optional `assets/` and `references/`. They're structurally the same as Claude Skills. This is *not* a Custom GPT bundle. Earlier iterations of this directory shipped GPT bundles; that approach is retired.

## Layout

```
chatgpt/
  build.py                          # regenerates this tree
  README.md                         # this file
  aleut-federal-context/            # implicit-invoke companion Skill
    SKILL.md                        #   loads AF facts + hard constraints
    agents/openai.yaml              #   allow_implicit_invocation: true
    assets/icon.svg
    references/aleut-federal-context.md
  <plugin>/                         # one folder per Claude plugin
    <skill-name>/                   # one Skill per Claude skill
      SKILL.md
      agents/openai.yaml
      assets/icon.svg
      references/*.md               # if the source Claude skill has them
```

## The implicit-invoke context Skill

`aleut-federal-context/` is the only Skill with `allow_implicit_invocation: true`. It auto-fires for AF-related questions and loads:

- ANC / 8(a) status, sole-source authority, affiliation rules.
- FAR / DFARS / agency supplements, SCA / Davis-Bacon, CMMC, Section 889, etc.
- Hard constraints (no source-selection content, no commitments outside the CO, mandatory disclosure routing, CUI handling).

The full reference is in `aleut-federal-context/references/aleut-federal-context.md` (same content as the repo-root `ALEUT-FEDERAL-CONTEXT.md`).

Every other Skill is explicit-invoke. When a user invokes a role Skill (e.g. `legal-review-contract`) the implicit context Skill loads alongside it, so company facts are always in scope.

## Skills bundled

| `aleut-enterprise/` | 1 | `sba-anc-source-guide` |
| `legal/` | 9 | `brief`, `compliance-check`, `legal-response`, `legal-risk-assessment`, `meeting-briefing`, `review-contract`, `signature-request`, `triage-nda`, `vendor-check` |
| `finance/` | 8 | `audit-support`, `close-management`, `financial-statements`, `journal-entry`, `journal-entry-prep`, `reconciliation`, `sox-testing`, `variance-analysis` |
| `sales/` | 9 | `account-research`, `call-prep`, `call-summary`, `competitive-intelligence`, `create-an-asset`, `daily-briefing`, `draft-outreach`, `forecast`, `pipeline-review` |
| `operations/` | 9 | `capacity-plan`, `change-request`, `compliance-tracking`, `process-doc`, `process-optimization`, `risk-assessment`, `runbook`, `status-report`, `vendor-review` |
| `human-resources/` | 9 | `comp-analysis`, `draft-offer`, `interview-prep`, `onboarding`, `org-planning`, `people-report`, `performance-review`, `policy-lookup`, `recruiting-pipeline` |
| `marketing/` | 8 | `brand-review`, `campaign-plan`, `marketing-competitive-brief`, `content-creation`, `draft-content`, `email-sequence`, `performance-report`, `seo-audit` |
| `engineering/` | 10 | `architecture`, `code-review`, `debug`, `deploy-checklist`, `documentation`, `incident-response`, `standup`, `system-design`, `tech-debt`, `testing-strategy` |
| `design/` | 7 | `accessibility-review`, `design-critique`, `design-handoff`, `design-system`, `research-synthesis`, `user-research`, `ux-copy` |
| `data/` | 10 | `analyze`, `build-dashboard`, `create-viz`, `data-context-extractor`, `data-visualization`, `explore-data`, `sql-queries`, `statistical-analysis`, `validate-data`, `write-query` |
| `product-management/` | 8 | `pm-competitive-brief`, `metrics-review`, `product-brainstorming`, `roadmap-update`, `sprint-planning`, `stakeholder-update`, `synthesize-research`, `write-spec` |
| `enterprise-search/` | 5 | `digest`, `knowledge-synthesis`, `search`, `search-strategy`, `source-management` |
| `customer-support/` | 5 | `customer-escalation`, `customer-research`, `draft-response`, `kb-article`, `ticket-triage` |
| `productivity/` | 4 | `memory-management`, `start`, `task-management`, `update` |

| | | |
|---|---|---|
| **Total** | 102 explicit-invoke Skills + 1 implicit-invoke context Skill | |

## Importing into OpenAI

Each subfolder (`aleut-federal-context/` + every `<plugin>/<skill>/`) is a complete OpenAI Skill package. Import per your tenant's process (ChatGPT Enterprise admin console / OpenAI Skill Marketplace / direct upload via the relevant SDK). The Skills targeting the `chatgpt`, `codex`, `api`, and `atlas` products are scoped in each `agents/openai.yaml`.

## Naming and collisions

Skill names mostly match the source Claude skill name (e.g. `review-contract`, `account-research`). Where the same skill name exists in two plugins (currently only `competitive-brief` in `sales/` and `product-management/`), the second occurrence is prefixed with the plugin abbreviation (e.g. `pm-competitive-brief`).

## Rebuild

Re-run after any source change:

```bash
python3 chatgpt/build.py
```

The script overwrites every plugin folder under `chatgpt/`. Commit the regenerated output so the OpenAI Skill packages stay in sync with the Claude plugin source.

## Hard rules baked into every Skill

Inherited from the implicit-invoke context Skill plus per-Skill workflow text:

- No CUI in distributable outputs.
- No source-selection-sensitive information (FAR 3.104 / Procurement Integrity Act).
- No commitments outside Contracting Officer authority.
- No federal-employee testimonials or implied endorsement (5 C.F.R. § 2635.702).
- Mandatory disclosure under FAR 52.203-13 routes to General Counsel.
- Privileged work product marked "Attorney-Client Privileged / Attorney Work Product".

## Single source of truth

The canonical SKILL.md files live in `<plugin>/skills/<name>/SKILL.md`. **Do not edit files under `chatgpt/<plugin>/<skill>/` by hand** — they're regenerated.

## What's NOT here

- `partner-built/*` Skills (third-party authors).
- `cowork-plugin-management` (Claude-only meta-plugin for plugin authoring).
- The upstream `small-business` plugin (kept in marketplace.json for now but not Aleut-Federal-relevant — review and trim separately).
