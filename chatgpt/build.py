#!/usr/bin/env python3
"""Build ChatGPT Enterprise Custom GPT exports from the Claude plugin source.

This script is the single source of truth for generating the chatgpt/ tree.
Every skill in this repo lives canonically as <plugin>/skills/<name>/SKILL.md
(Claude plugin format). This script reads those, plus the company-wide
ALEUT-FEDERAL-CONTEXT.md, and emits a per-plugin Custom GPT bundle ready to
upload to ChatGPT Enterprise.

Usage:
    python3 chatgpt/build.py

Output structure:
    chatgpt/
      README.md           # top-level import guide (hand-written, not regenerated)
      build.py            # this script
      <plugin>/
        INSTRUCTIONS.md   # paste into the Custom GPT "Instructions" field
        DESCRIPTION.md    # paste into the Custom GPT "Description" field
        README.md         # per-plugin import / operator guide
        knowledge/
          00-ALEUT-FEDERAL-CONTEXT.md
          <skill-name>.md  (one per skill)

Rerun this script any time a SKILL.md or plugin.json changes.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTEXT_FILE = REPO_ROOT / "ALEUT-FEDERAL-CONTEXT.md"
CHATGPT_ROOT = REPO_ROOT / "chatgpt"

# Plugins to export. Order here drives the order in the top-level README.
# Skip partner-built/* (third-party authors) and cowork-plugin-management
# (meta-plugin for building Claude plugins — not useful in ChatGPT).
PLUGINS = [
    "legal",
    "finance",
    "sales",
    "operations",
    "human-resources",
    "marketing",
    "engineering",
    "design",
    "data",
    "product-management",
    "enterprise-search",
    "customer-support",
    "productivity",
]

# Per-plugin disclaimer text injected into INSTRUCTIONS. Falls back to a
# generic disclaimer if a plugin isn't listed.
PLUGIN_DISCLAIMERS = {
    "legal": (
        "You assist with legal workflows; you do NOT provide legal advice. "
        "All outputs must be reviewed by qualified counsel before reliance. "
        "For any matter implicating the False Claims Act, Procurement "
        "Integrity Act, or FAR 52.203-13 mandatory disclosure, route to "
        "General Counsel immediately."
    ),
    "finance": (
        "You assist with finance and accounting workflows for a federal "
        "contractor; you do NOT provide financial, tax, or audit advice. "
        "All outputs must be reviewed by qualified personnel (Controller, "
        "internal audit, IPA) before reliance. Any matter implicating the "
        "False Claims Act, defective pricing, or FAR 52.203-13 mandatory "
        "disclosure goes to General Counsel."
    ),
    "human-resources": (
        "You assist with people-operations workflows for a federal "
        "contractor; you do NOT provide legal employment advice. All "
        "outputs must be reviewed by qualified HR and counsel before "
        "reliance. SCA / Davis-Bacon / OFCCP questions coordinate with "
        "Contracts and Legal."
    ),
    "operations": (
        "You assist with federal-contractor operations workflows; you do "
        "NOT provide legal or contracting-officer-level advice. Scope, "
        "schedule, and price changes on federal contracts require the "
        "Contracting Officer's written direction (FAR Subpart 43)."
    ),
    "sales": (
        "You assist with federal business-development and capture; you "
        "do NOT replace the Contracting Officer or the Procurement "
        "Integrity firewall. Never surface or use source-selection-"
        "sensitive information (FAR 3.104)."
    ),
    "marketing": (
        "You assist with federal-market marketing; you do NOT make "
        "endorsement, scope, or pricing commitments. Customer references "
        "and agency logos require Contracting Officer authorization."
    ),
    "engineering": (
        "You assist with federal IT and systems-engineering workflows; "
        "you do NOT replace the AO/ATO process or Contracting Officer "
        "authority. Changes that affect the ATO boundary, CUI handling, "
        "or contracted scope require the appropriate Government action."
    ),
    "design": (
        "You assist with design workflows for federal-customer "
        "deliverables. Section 508 / WCAG 2.1 AA accessibility is "
        "mandatory; never publish federal-customer references without "
        "Contracting Officer authorization."
    ),
    "data": (
        "You assist with data analysis in a federal-contractor "
        "environment. Never process CUI in an unauthorized environment; "
        "never surface source-selection-sensitive content outside the "
        "cleared capture team."
    ),
    "product-management": (
        "You assist with federal program and product management; you do "
        "NOT replace the Contracting Officer. Out-of-scope work requires "
        "a contract mod (FAR Subpart 43); preserve REA rights under FAR "
        "52.243-x for constructive changes."
    ),
    "enterprise-search": (
        "You search across Aleut Federal's authorized data sources. Honor "
        "classification markings, privilege markings, source-selection "
        "sensitivity (FAR 3.104), and litigation-hold notices. Refuse to "
        "surface CUI / classified content in unauthorized environments."
    ),
    "customer-support": (
        "You assist with federal-customer help-desk and end-user support. "
        "Route any scope / schedule / cost matter through the Contracting "
        "Officer (only the CO can authorize changes). Never include CUI in "
        "tickets, responses, or KB articles that traverse unauthorized "
        "channels."
    ),
    "productivity": (
        "You assist with personal productivity. Never write CUI, "
        "classified, source-selection-sensitive, or privileged content "
        "into TASKS.md or memory files - those environments are not "
        "authorized for controlled data."
    ),
}

INSTRUCTIONS_TEMPLATE = """\
You are **Aleut Federal — {plugin_title}**, a {plugin_role} for Aleut Federal, LLC.

# Company Context

Aleut Federal is an Alaska Native Corporation (ANC) 8(a) federal services and construction contractor. Your authoritative reference for company facts, regulatory environment, federal vocabulary, and hard constraints is **`ALEUT-FEDERAL-CONTEXT.md`** (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md` in your knowledge files). Read it before answering any non-trivial question and treat its contents as ground truth on:

- Special federal status (ANC / 8(a) sole-source authority, affiliation rules, Mentor-Protégé Program).
- Regulatory framework (FAR, DFARS, SBA 8(a), SCA, Davis-Bacon, CWHSSA, EO 14026, Miller Act, EM 385-1-1, OSHA 1926, FAR Part 31, CAS, DCAA, NIST 800-171, CMMC 2.0, Section 889, BAA/TAA/BABA, FAR 52.203-13, FCA, Anti-Kickback, PIA, ITAR/EAR, OFCCP/EEO).
- NAICS codes, contract vehicles, set-aside posture, pipeline / BD sources.
- Hard constraints / do-not-dos.

# Plugin Purpose

{plugin_description}

# Important Disclaimer

{disclaimer}

# Available Skills

Each skill below is a separate document in your knowledge files. When a user request matches a skill's "use when" guidance, follow that skill's workflow end-to-end. Cite authority (FAR / DFARS / CFR / U.S.C. / NIST publication) inline where applicable.

{skill_index}

# Output Conventions

- **Federal vocabulary by default** — use FAR/DFARS terminology, not commercial equivalents.
- **Cite authority** — FAR/DFARS clauses, NIST publications, CFR parts, U.S.C. titles inline.
- **No CUI in distributable outputs.** If the user provides CUI, ask whether the ChatGPT Enterprise tenant is authorized; do not embed CUI in answers that may leave the tenant.
- **No source-selection-sensitive information** (FAR 3.104) — refuse if offered; never invent.
- **No commitments outside Contracting Officer authority.** Only the CO can change scope, price, period of performance, or contract terms.
- **No federal-employee testimonials / implied endorsement** (5 C.F.R. § 2635.702).
- **Mark privileged work product** "Attorney-Client Privileged / Attorney Work Product" when prepared for or at the direction of counsel.
- **Default tone**: dry, factual, credentials-first, agency-mission-focused — not commercial-sales hype.

# Tools and Connectors

This Custom GPT does NOT include direct MCP connectors. The Claude version of this plugin references external tools (SAM.gov, USAspending, PIEE/WAWF, Deltek Costpoint, etc.) via MCP. See `README.md` in this plugin's export folder for the connector list and notes on whether to (a) attach the data as additional knowledge uploads, (b) build a ChatGPT Action with an OpenAPI spec, or (c) ask the user to paste relevant content into the conversation.

# Refusal Triggers

Refuse and route to the appropriate authority when the user's request:
- Would disclose CUI / classified / ITAR-controlled material in an unauthorized environment.
- Would surface or use source-selection-sensitive information (FAR 3.104 / Procurement Integrity Act).
- Implicates the False Claims Act, Anti-Kickback Act, or FAR 52.203-13 mandatory disclosure — route to General Counsel.
- Would commit Aleut Federal to a scope/price/PoP change without the Contracting Officer.
- Would publish federal-customer references (logos, contract numbers, mission details) without CO authorization.

When you refuse, name the authority and the route (e.g., "this requires CO direction under FAR 52.243-x — please coordinate through Contracts").
"""

# Per-plugin metadata for the INSTRUCTIONS template.
PLUGIN_META = {
    "legal": ("Legal", "federal-contracting legal workflow assistant"),
    "finance": ("Finance", "DCAA-compliant federal-contractor finance and accounting assistant"),
    "sales": ("BD & Capture", "federal business-development and capture assistant"),
    "operations": ("Operations", "federal-contractor compliance-operations assistant"),
    "human-resources": ("People Operations", "federal-contractor people-operations assistant"),
    "marketing": ("Marketing", "federal-market marketing and capability-positioning assistant"),
    "engineering": ("Engineering", "federal IT / systems-engineering assistant calibrated for NIST RMF, FedRAMP, CMMC, and ATO workflows"),
    "design": ("Design", "design assistant for federal-customer UX, A&E, and construction-design work"),
    "data": ("Data", "data analysis assistant for federal-contractor cost accounting, capture intelligence, and compliance posture"),
    "product-management": ("Program & Product Management", "program/product management assistant for federal task orders and contracts"),
    "enterprise-search": ("Enterprise Search", "enterprise-search assistant honoring classification, privilege, source-selection, and litigation-hold markings"),
    "customer-support": ("Customer Support", "federal-customer help-desk and end-user support assistant"),
    "productivity": ("Productivity", "personal-productivity assistant for Aleut Federal staff"),
}


def parse_skill(skill_md_path: Path) -> dict:
    """Extract name, description, frontmatter, and body from a SKILL.md file."""
    text = skill_md_path.read_text()
    if text.startswith("---"):
        end = text.index("---", 3)
        frontmatter = text[3:end]
        body = text[end + 3:].lstrip()
    else:
        frontmatter = ""
        body = text

    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    # description may be multi-line with > or |
    desc_match = re.search(r"^description:\s*(>-?|[|]-?)?\s*(.+(?:\n\s+.+)*)", frontmatter, re.MULTILINE)
    description = ""
    if desc_match:
        # Take everything after the description: marker, collapse whitespace.
        raw = desc_match.group(2)
        description = " ".join(line.strip() for line in raw.splitlines() if line.strip())

    return {
        "name": name_match.group(1).strip() if name_match else skill_md_path.parent.name,
        "description": description,
        "body": body,
    }


def normalize_body(body: str) -> str:
    """Strip Claude-specific links that don't work in a ChatGPT knowledge file."""
    # ALEUT-FEDERAL-CONTEXT.md links → point at the bundled copy.
    body = re.sub(
        r"\[ALEUT-FEDERAL-CONTEXT\.md\]\([^)]+\)",
        "`ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`)",
        body,
    )
    # Strip the "If you see unfamiliar placeholders..." sentence wherever it
    # appears — inline or standalone, with or without leading blockquote.
    body = re.sub(
        r"\s*If you see unfamiliar placeholders or need to check which tools are connected, see \[CONNECTORS\.md\]\([^)]+\)\.",
        "",
        body,
    )
    # Any remaining CONNECTORS.md links → operator note.
    body = re.sub(
        r"\[CONNECTORS\.md\]\([^)]+\)",
        "the plugin export README (tool / connector mapping)",
        body,
    )
    # Tidy up double spaces and triple newlines created by the deletions.
    body = re.sub(r"  +", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def build_plugin(plugin_name: str) -> None:
    """Build chatgpt/<plugin>/ from <plugin>/skills/*/SKILL.md."""
    plugin_dir = REPO_ROOT / plugin_name
    skills_dir = plugin_dir / "skills"
    out_dir = CHATGPT_ROOT / plugin_name
    knowledge_dir = out_dir / "knowledge"

    if out_dir.exists():
        shutil.rmtree(out_dir)
    knowledge_dir.mkdir(parents=True)

    # Company context: copy in as 00-* so it sorts first in ChatGPT's upload UI.
    shutil.copy(CONTEXT_FILE, knowledge_dir / "00-ALEUT-FEDERAL-CONTEXT.md")

    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    manifest = json.loads(manifest_path.read_text())

    # Collect skills.
    skills = []
    for skill_dir in sorted(skills_dir.iterdir()):
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        skill = parse_skill(skill_md)
        skills.append(skill)

        body = normalize_body(skill["body"])
        # Strip the YAML frontmatter from the exported file (it isn't meaningful
        # to ChatGPT) but keep the name + description as a clear header so the
        # GPT can still scan the knowledge file index.
        out_md = (
            f"# {skill['name']}\n\n"
            f"> **What this skill does:** {skill['description']}\n\n"
            f"{body}".rstrip()
            + "\n"
        )
        (knowledge_dir / f"{skill['name']}.md").write_text(out_md)

    skill_index = "\n".join(
        f"- **{s['name']}** — {first_sentence(s['description'])}"
        for s in skills
    )

    plugin_title, plugin_role = PLUGIN_META.get(
        plugin_name, (plugin_name.title().replace("-", " "), "Aleut Federal workflow assistant")
    )
    disclaimer = PLUGIN_DISCLAIMERS.get(
        plugin_name,
        "You assist Aleut Federal staff with workflows; your outputs are not "
        "professional advice and must be reviewed by qualified personnel.",
    )

    instructions = INSTRUCTIONS_TEMPLATE.format(
        plugin_title=plugin_title,
        plugin_role=plugin_role,
        plugin_description=manifest.get("description", "").strip(),
        disclaimer=disclaimer,
        skill_index=skill_index,
    )
    (out_dir / "INSTRUCTIONS.md").write_text(instructions)

    description = manifest.get("description", "").strip()
    (out_dir / "DESCRIPTION.md").write_text(description + "\n")

    (out_dir / "README.md").write_text(build_plugin_readme(plugin_name, plugin_title, manifest, skills))


def first_sentence(text: str) -> str:
    """Return the first sentence of a description (period-terminated)."""
    if not text:
        return ""
    match = re.search(r"^(.+?[.!?])(\s|$)", text)
    return match.group(1) if match else text


def build_plugin_readme(plugin_name: str, plugin_title: str, manifest: dict, skills: list) -> str:
    """Per-plugin operator README for the ChatGPT export."""
    file_count = len(skills) + 1  # +1 for the company context

    # Look for an .mcp.json in the source plugin to list connectors the
    # Claude version assumes.
    mcp_path = REPO_ROOT / plugin_name / ".mcp.json"
    if mcp_path.exists():
        try:
            mcp = json.loads(mcp_path.read_text())
            servers = list(mcp.get("mcpServers", {}).keys())
        except json.JSONDecodeError:
            servers = []
    else:
        servers = []
    connector_block = (
        "The Claude version of this plugin references the following MCP connectors:\n\n"
        + "\n".join(f"- `{s}`" for s in servers)
        if servers
        else "No MCP connectors are configured in the Claude version of this plugin."
    )

    skill_block = "\n".join(
        f"- **{s['name']}** — {first_sentence(s['description'])}"
        for s in skills
    )

    return f"""# Aleut Federal — {plugin_title} (ChatGPT Enterprise Export)

This directory is the ChatGPT Enterprise Custom GPT bundle for the **{plugin_name}** plugin. It is generated from `../../{plugin_name}/` by `../build.py`; do not edit files in this directory by hand — edit the source SKILL.md files and re-run the build script.

## Quick import (ChatGPT Enterprise)

1. **Explore GPTs → Create**.
2. **Configure** tab.
3. **Name:** `Aleut Federal — {plugin_title}`
4. **Description:** paste the contents of `DESCRIPTION.md`.
5. **Instructions:** paste the contents of `INSTRUCTIONS.md`.
6. **Conversation starters:** suggested below.
7. **Knowledge:** upload **every file** in `knowledge/` ({file_count} files: 1 company context + {len(skills)} skill files).
8. **Capabilities:** enable Web Browsing (federal-market intel), Code Interpreter (data / finance work), DALL·E only if needed. Leave **all conversation data settings** at the most restrictive defaults appropriate for our tenant.
9. **Actions:** none included — see "Connectors" below.
10. **Sharing:** restrict to the Aleut Federal workspace; do not publish publicly.

## Suggested conversation starters

(Adapt as needed; pick 3–4 that fit the audience.)

{suggested_starters(plugin_name, skills)}

## Skills bundled

{skill_block}

## Connectors

{connector_block}

ChatGPT Enterprise does not run MCP. Options to bridge the gap:

- **Manual upload** — paste relevant data or upload as additional knowledge.
- **ChatGPT Actions** — build an OpenAPI spec for each connector's HTTP API. Works for SAM.gov, USAspending, FPDS, and any REST API; less direct for tools that only expose internal MCP.
- **Wait for native MCP** — OpenAI has signaled MCP-like extensibility; revisit when stable.

## Company context

`knowledge/00-ALEUT-FEDERAL-CONTEXT.md` is the company-wide reference (ANC/8(a) status, FAR/DFARS framework, hard constraints). Every other skill file assumes this context is loaded.

## Rebuild

If anything in `../../{plugin_name}/skills/` or `../../ALEUT-FEDERAL-CONTEXT.md` changes, regenerate this bundle:

```bash
python3 chatgpt/build.py
```

The script will overwrite this directory.
"""


def suggested_starters(plugin_name: str, skills: list) -> str:
    """Build a few conversation-starter suggestions from skill descriptions."""
    starters_map = {
        "legal": [
            "Review this teaming agreement against our default playbook.",
            "Run a compliance check on hiring a former Air Force contracting officer.",
            "Triage this NDA from a prime — green / yellow / red?",
            "What's our exposure on this FAR 52.219-14 self-performance question?",
        ],
        "finance": [
            "Build the workpapers for an upcoming DCAA incurred-cost audit.",
            "Draft the journal entries to true up provisional indirect rates against actuals.",
            "What's the limitation-of-funds notification threshold and timing for this cost-type contract?",
            "Run a FAR Part 31 allowability review on this expense list.",
        ],
        "sales": [
            "Research USACE Mobile District — pipeline, vehicles, recompete watch.",
            "Prep me for an OSDBU capability briefing at GSA next week.",
            "Pipeline review for Q3 — flag hygiene issues and recommend no-bids.",
            "Build a competitive snapshot on [Prime X] for an OASIS+ recompete.",
        ],
        "operations": [
            "Status of our compliance posture — contracts, CMMC, OFCCP, FAR 52.203-13.",
            "Vendor diligence: walk a new sub through SAM, Section 889, FAPIIS, flow-downs.",
            "Risk assessment on adding 25 percent workshare to our JV mid-performance.",
            "Write a runbook for the DFARS 252.204-7012 72-hour cyber incident report.",
        ],
        "human-resources": [
            "Draft an offer letter for a cleared SECRET engineer on a SCA contract.",
            "Comp analysis: what's the WD floor for this labor category at this locality?",
            "What's our policy on hiring a former federal CO under 18 USC 207 / 2104?",
            "Build the 30/60/90-day onboarding plan for a new CUI-cleared analyst.",
        ],
        "marketing": [
            "Draft a one-page capability statement for AFCEC HVAC/mechanical work.",
            "Build a federal-market campaign plan for AFCEA TechNet.",
            "Competitive brief on three primes likely to bid this SeaPort-NxG recompete.",
            "Review this case study for PIA, CUI, and CO-authorization issues.",
        ],
        "engineering": [
            "Write an ADR for moving this system from on-prem to FedRAMP Moderate.",
            "Code review: flag NIST 800-171 / FIPS / Section 889 / Section 508 issues.",
            "Build the deploy checklist with ATO boundary and POA&M evidence steps.",
            "We had a possible cyber incident on a DFARS 7012 system — walk me through the response.",
        ],
        "design": [
            "Run a Section 508 / WCAG 2.1 AA audit on this page.",
            "Critique this design for federal-user constraints (PIV/CAC, low connectivity).",
            "Generate a VPAT / ACR draft for this product.",
            "What USWDS components should we use for this agency form?",
        ],
        "data": [
            "Build a dashboard tracking indirect-rate posture vs provisional vs forecast.",
            "Write SQL to reconcile job-cost ledger to GL by contract for last quarter.",
            "Statistical analysis: is our subcontractor utilization meeting the FAR 52.219-9 plan?",
            "Pull recent USAspending awards for this NAICS / agency / set-aside slice.",
        ],
        "product-management": [
            "Write a CDRL-compliant feature spec for this task-order requirement.",
            "Update the roadmap to reflect the new option-year exercise and CR risk.",
            "Sprint planning: load the backlog against direct-vs-indirect capacity and clearance constraints.",
            "Draft the stakeholder update for the CO and the AF leadership team.",
        ],
        "enterprise-search": [
            "Find the latest mod to our USACE Mobile District contract.",
            "Daily digest — flag any items requiring CO/COR action today.",
            "Search across CLM, SharePoint, and email for everything on the OASIS+ recompete.",
            "Synthesize what counsel has said about our Section 889 supplier audit.",
        ],
        "customer-support": [
            "Triage this incoming federal-customer ticket — severity per the contract SLA.",
            "Draft a response that preserves REA rights on a Government-directed change.",
            "Package this for engineering escalation with full CDRL/SLA impact context.",
            "Turn this resolved ticket into a CUI-safe KB article.",
        ],
        "productivity": [
            "Start my day — what federal deadlines hit this week?",
            "Update tasks from my calendar; tag direct vs indirect charge codes.",
            "Add the Aleut Federal customer acronym glossary to memory.",
            "What did I commit to in yesterday's CO call?",
        ],
    }
    starters = starters_map.get(plugin_name)
    if not starters:
        starters = [f"How does the {s['name']} skill work?" for s in skills[:4]]
    return "\n".join(f"- {s}" for s in starters)


def main() -> int:
    if not CONTEXT_FILE.exists():
        print(f"ERROR: {CONTEXT_FILE} not found", file=sys.stderr)
        return 1
    CHATGPT_ROOT.mkdir(exist_ok=True)
    for plugin in PLUGINS:
        plugin_dir = REPO_ROOT / plugin
        if not plugin_dir.is_dir():
            print(f"WARN: skipping missing plugin: {plugin}", file=sys.stderr)
            continue
        print(f"Building chatgpt/{plugin}/ ...")
        build_plugin(plugin)
    print("Done. To rebuild, run: python3 chatgpt/build.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
