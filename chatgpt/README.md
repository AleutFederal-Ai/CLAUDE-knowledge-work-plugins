# Aleut Federal — ChatGPT Enterprise Export

This directory packages the Aleut Federal skill library as **ChatGPT Enterprise Custom GPT bundles**, one bundle per plugin. It is generated from the Claude plugin source elsewhere in this repo; do not edit files here by hand.

## What's in here

```
chatgpt/
  README.md          # this file
  build.py           # regenerates everything from the Claude plugin source
  <plugin>/          # one folder per plugin (legal, finance, sales, ...)
    INSTRUCTIONS.md  # paste into the Custom GPT "Instructions" field
    DESCRIPTION.md   # paste into the Custom GPT "Description" field
    README.md        # per-plugin operator guide (import steps, connectors)
    knowledge/       # upload every file in this folder to the GPT
      00-ALEUT-FEDERAL-CONTEXT.md
      <skill>.md     # one file per skill
```

Each plugin becomes one Custom GPT (e.g. **Aleut Federal — Legal**, **Aleut Federal — Finance**). The `00-ALEUT-FEDERAL-CONTEXT.md` file is the company-wide reference (ANC / 8(a) status, FAR/DFARS framework, hard constraints) and is included in every plugin's `knowledge/` folder.

## Plugins exported

| Folder | Custom GPT name | Skills |
|--------|-----------------|--------|
| [legal](./legal/) | Aleut Federal — Legal | 9 |
| [finance](./finance/) | Aleut Federal — Finance | 8 |
| [sales](./sales/) | Aleut Federal — BD & Capture | 9 |
| [operations](./operations/) | Aleut Federal — Operations | 9 |
| [human-resources](./human-resources/) | Aleut Federal — People Operations | 9 |
| [marketing](./marketing/) | Aleut Federal — Marketing | 8 |
| [engineering](./engineering/) | Aleut Federal — Engineering | 10 |
| [design](./design/) | Aleut Federal — Design | 7 |
| [data](./data/) | Aleut Federal — Data | 10 |
| [product-management](./product-management/) | Aleut Federal — Program & Product Management | 8 |
| [enterprise-search](./enterprise-search/) | Aleut Federal — Enterprise Search | 5 |
| [customer-support](./customer-support/) | Aleut Federal — Customer Support | 5 |
| [productivity](./productivity/) | Aleut Federal — Productivity | 4 |

The `partner-built/*` plugins (Apollo, Common Room, Slack, Brand Voice) and `cowork-plugin-management` are intentionally not exported — they're third-party / Claude-specific and don't translate to Custom GPTs.

## Importing one plugin into ChatGPT Enterprise

For each plugin you want as a Custom GPT in your Aleut Federal ChatGPT Enterprise workspace:

1. **ChatGPT** → **Explore GPTs** → **Create**.
2. Switch to the **Configure** tab.
3. **Name:** copy the "Custom GPT name" from the table above.
4. **Description:** paste the contents of `<plugin>/DESCRIPTION.md`.
5. **Instructions:** paste the contents of `<plugin>/INSTRUCTIONS.md`.
6. **Conversation starters:** copy 3–4 from `<plugin>/README.md` (suggested-starters section).
7. **Knowledge:** upload **every file in `<plugin>/knowledge/`**.
8. **Capabilities:** enable as appropriate (Web Browsing for federal market intel; Code Interpreter for data / finance work).
9. **Actions:** none included — see the connector notes in each plugin's README.
10. **Sharing:** restrict to the Aleut Federal workspace.

Each plugin's `README.md` has the full operator checklist, the list of MCP connectors the Claude version of the plugin assumes, and suggested conversation starters.

## When to rebuild

Re-run the build script any time you change:

- A `<plugin>/skills/<name>/SKILL.md` file in the Claude plugin source.
- `<plugin>/.claude-plugin/plugin.json` (plugin description).
- `ALEUT-FEDERAL-CONTEXT.md` at the repo root.

```bash
python3 chatgpt/build.py
```

The script overwrites every `chatgpt/<plugin>/` subdirectory. Commit the regenerated output so the ChatGPT side stays in sync with the Claude side.

## Tradeoffs to understand

- **Single source of truth:** the canonical SKILL.md files live in `<plugin>/skills/<name>/SKILL.md` (Claude plugin format). The `chatgpt/` tree is derived. Do not edit files under `chatgpt/<plugin>/knowledge/` by hand — they'll be overwritten.
- **No MCP in ChatGPT:** the Claude version of each plugin reaches external tools (SAM.gov, USAspending, Deltek Costpoint, PIEE/WAWF, CLM, etc.) via MCP. ChatGPT Enterprise does not run MCP. Options:
  1. Manually upload relevant data as additional knowledge.
  2. Build ChatGPT **Actions** (OpenAPI specs) for connectors that expose HTTP APIs.
  3. Have the user paste relevant content into the conversation.
- **Knowledge file limit:** ChatGPT Custom GPTs accept up to 20 knowledge files per GPT. The largest plugin (engineering, data, sales) bundles 11 files — well within limits.
- **Instruction length:** Custom GPT instructions have a character cap. Each `INSTRUCTIONS.md` here is ~5–6KB; well under the published limits.
- **Tenant settings:** confirm with the AF ChatGPT Enterprise admin that the workspace has data-handling settings appropriate for the content. CUI must not be uploaded into a tenant that isn't authorized; the GPTs here are designed to refuse CUI in their refusal triggers but the operator is responsible for tenant settings.

## Hard rules baked into every GPT

Every Custom GPT's instructions enforce Aleut Federal's hard constraints:

- No CUI in distributable outputs.
- No source-selection-sensitive information (FAR 3.104 / Procurement Integrity Act).
- No commitments outside Contracting Officer authority.
- No federal-employee testimonials or implied endorsement (5 C.F.R. § 2635.702).
- Mandatory disclosure under FAR 52.203-13 routes to General Counsel.
- Privileged work product marked "Attorney-Client Privileged / Attorney Work Product".

If a user request would violate any of these, the GPT is instructed to refuse and route to the appropriate authority, naming the rule.
