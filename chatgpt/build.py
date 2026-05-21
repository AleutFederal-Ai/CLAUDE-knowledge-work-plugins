#!/usr/bin/env python3
"""Build OpenAI Skill packages from the Claude plugin source.

Every skill in this repo lives canonically as <plugin>/skills/<name>/SKILL.md
(Claude plugin format). This script reads those, plus the company-wide
ALEUT-FEDERAL-CONTEXT.md, and emits a parallel chatgpt/ tree of native
OpenAI Skill packages (the format used by ChatGPT / Codex / Atlas / API
Skill installations).

The Claude and OpenAI skill specs are almost identical: both use SKILL.md
with YAML frontmatter (name, description) and a body. OpenAI adds:
  - agents/openai.yaml  - display metadata + products + invocation policy
  - assets/icon.svg     - icon for display surfaces
  - references/*.md     - optional reference docs the skill loads

This script:
  1. Wipes the existing chatgpt/<plugin>/ tree (preserving build.py and the
     hand-written README.md at chatgpt/ root).
  2. For each plugin: copies every <plugin>/skills/<name>/ to
     chatgpt/<plugin>/<name>/ with an agents/openai.yaml + icon added.
  3. Detects skill-name collisions across plugins and prefixes the conflicting
     ones with the plugin name (e.g. `pm-competitive-brief`).
  4. Generates a top-level chatgpt/aleut-federal-context/ Skill with
     allow_implicit_invocation: true so the AF company context auto-fires
     for AF-related questions.

Re-run after any SKILL.md or ALEUT-FEDERAL-CONTEXT.md edit:
    python3 chatgpt/build.py
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CONTEXT_FILE = REPO_ROOT / "ALEUT-FEDERAL-CONTEXT.md"
CHATGPT_ROOT = REPO_ROOT / "chatgpt"

# Plugins to export. Skip partner-built/* (third-party authors), the upstream
# small-business plugin (not AF-relevant), and cowork-plugin-management
# (Claude-only meta-plugin).
PLUGINS = [
    "aleut-enterprise",
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

# Generic AF icon (also reused from the SBA-ANC sample). Per-skill icons can
# be added later by replacing assets/icon.svg in a Skill folder; the script
# preserves a hand-edited icon if one already exists in the source plugin's
# skill directory (skills/<name>/assets/icon.svg).
DEFAULT_ICON = """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M3 13.5C3 12.1193 4.11929 11 5.5 11H9V21H5.5C4.11929 21 3 19.8807 3 18.5V13.5Z" fill="#FFD400"/>
<path d="M15 7H18.5C19.8807 7 21 8.11929 21 9.5V18.5C21 19.8807 19.8807 21 18.5 21H15V7Z" fill="#F75858"/>
<path d="M9 5.5C9 4.11929 10.1193 3 11.5 3H12.5C13.8807 3 15 4.11929 15 5.5V21H9V5.5Z" fill="#FFA43D"/>
</svg>
"""

OPENAI_YAML_TEMPLATE = """\
interface:
  display_name: {display_name}
  short_description: {short_description}
  icon_small: assets/icon.svg
  icon_large: assets/icon.svg
policy:
  products:
  - chatgpt
  - codex
  - api
  - atlas
  allow_implicit_invocation: {implicit}
"""


def parse_skill(skill_md_path: Path) -> dict:
    """Extract name, description, frontmatter, and body from a SKILL.md file."""
    text = skill_md_path.read_text()
    if not text.startswith("---"):
        return {
            "name": skill_md_path.parent.name,
            "description": "",
            "body": text,
        }
    end = text.index("---", 3)
    frontmatter = text[3:end]
    body = text[end + 3:].lstrip()

    name_match = re.search(r"^name:\s*(.+)$", frontmatter, re.MULTILINE)
    desc_match = re.search(
        r"^description:\s*(>-?|[|]-?)?\s*(.+(?:\n[ \t]+.+)*)",
        frontmatter,
        re.MULTILINE,
    )
    description = ""
    if desc_match:
        raw = desc_match.group(2)
        description = " ".join(line.strip() for line in raw.splitlines() if line.strip())

    return {
        "name": name_match.group(1).strip() if name_match else skill_md_path.parent.name,
        "description": description,
        "body": body,
    }


def normalize_body(body: str) -> str:
    """Adapt Claude-specific links to the OpenAI Skill context."""
    # ALEUT-FEDERAL-CONTEXT.md links → point at the companion implicit-invoke
    # Skill. The Skill renderer doesn't follow relative paths the same way
    # Claude does, so we describe rather than link.
    body = re.sub(
        r"\[ALEUT-FEDERAL-CONTEXT\.md\]\([^)]+\)",
        "the **aleut-federal-context** Skill (auto-invoked for AF-related questions)",
        body,
    )
    # Strip the "If you see unfamiliar placeholders..." sentence the Claude
    # skills include; CONNECTORS.md is a Claude convention.
    body = re.sub(
        r"\s*If you see unfamiliar placeholders or need to check which tools are connected, see \[CONNECTORS\.md\]\([^)]+\)\.",
        "",
        body,
    )
    body = re.sub(
        r"\[CONNECTORS\.md\]\([^)]+\)",
        "the plugin connector list (Claude-only; ChatGPT does not run MCP)",
        body,
    )
    body = re.sub(r"  +", " ", body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body


def first_sentence(text: str, max_len: int = 180) -> str:
    if not text:
        return ""
    match = re.search(r"^(.+?[.!?])(\s|$)", text)
    sentence = match.group(1) if match else text
    if len(sentence) > max_len:
        sentence = sentence[: max_len - 1].rsplit(" ", 1)[0] + "…"
    return sentence


def collect_skills() -> list[dict]:
    """Walk the source tree and collect every skill with its source paths."""
    skills = []
    for plugin in PLUGINS:
        plugin_dir = REPO_ROOT / plugin
        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir():
            continue
        for skill_dir in sorted(skills_dir.iterdir()):
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                continue
            parsed = parse_skill(skill_md)
            skills.append(
                {
                    "plugin": plugin,
                    "source_dir": skill_dir,
                    "source_name": parsed["name"],
                    "description": parsed["description"],
                    "body": parsed["body"],
                }
            )
    return skills


def resolve_output_names(skills: list[dict]) -> None:
    """Decide each skill's OpenAI Skill name. Prefix on collision with plugin."""
    counts = Counter(s["source_name"] for s in skills)
    for s in skills:
        if counts[s["source_name"]] > 1:
            # Two skills with the same source name (e.g. competitive-brief lives
            # in both sales and product-management). Disambiguate with the
            # plugin name, abbreviated when long.
            prefix = {
                "product-management": "pm",
                "human-resources": "hr",
                "enterprise-search": "es",
                "customer-support": "cs",
                "aleut-enterprise": "ae",
            }.get(s["plugin"], s["plugin"])
            s["openai_name"] = f"{prefix}-{s['source_name']}"
        else:
            s["openai_name"] = s["source_name"]


def write_skill_package(s: dict) -> None:
    """Write chatgpt/<plugin>/<openai_name>/ with SKILL.md + agents/ + assets/ + references/."""
    out_dir = CHATGPT_ROOT / s["plugin"] / s["openai_name"]
    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "agents").mkdir(parents=True)
    (out_dir / "assets").mkdir()

    # SKILL.md — rewrite frontmatter so `name:` matches the (possibly namespaced)
    # OpenAI Skill name. Body is the normalized Claude content.
    body = normalize_body(s["body"])
    skill_md = (
        f"---\n"
        f"name: {s['openai_name']}\n"
        f"description: {s['description']}\n"
        f"---\n\n"
        f"{body}".rstrip()
        + "\n"
    )
    (out_dir / "SKILL.md").write_text(skill_md)

    # agents/openai.yaml — display metadata + product targeting.
    display_name = s["source_name"].replace("-", " ").title()
    short_desc = first_sentence(s["description"]).replace('"', "'")
    yaml_text = OPENAI_YAML_TEMPLATE.format(
        display_name=display_name,
        short_description=short_desc,
        implicit="false",
    )
    # Reuse the source agents/openai.yaml if the source skill already provided
    # one (e.g. the user-imported sba-anc-source-guide).
    src_yaml = s["source_dir"] / "agents" / "openai.yaml"
    if src_yaml.exists():
        (out_dir / "agents" / "openai.yaml").write_text(src_yaml.read_text())
    else:
        (out_dir / "agents" / "openai.yaml").write_text(yaml_text)

    # assets/icon.svg — use the source icon if it exists, else the default.
    src_icon = s["source_dir"] / "assets" / "icon.svg"
    if src_icon.exists():
        shutil.copy(src_icon, out_dir / "assets" / "icon.svg")
    else:
        (out_dir / "assets" / "icon.svg").write_text(DEFAULT_ICON)

    # references/ — copy over any reference files from the source skill.
    src_refs = s["source_dir"] / "references"
    if src_refs.is_dir():
        dst_refs = out_dir / "references"
        dst_refs.mkdir()
        for ref in src_refs.iterdir():
            if ref.is_file():
                shutil.copy(ref, dst_refs / ref.name)


def write_implicit_context_skill() -> None:
    """Top-level aleut-federal-context Skill with implicit invocation enabled.

    Companion to every role Skill: auto-fires for AF-related questions so the
    company facts, regulatory framework, and hard constraints are loaded
    without an explicit invocation.
    """
    out_dir = CHATGPT_ROOT / "aleut-federal-context"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    (out_dir / "agents").mkdir(parents=True)
    (out_dir / "assets").mkdir()
    (out_dir / "references").mkdir()

    description = (
        "auto-load aleut federal company context (anc/8(a) status, far/dfars "
        "framework, sca/davis-bacon, cmmc 2.0, nist 800-171, far 52.203-13 "
        "mandatory disclosure, far 3.104 procurement integrity, hard "
        "constraints). use whenever a question involves aleut federal, our "
        "federal contracts, our 8(a) sole-source authority, our regulatory "
        "obligations, or our compliance posture. provides the company facts; "
        "other skills handle workflows."
    )

    skill_md = f"""---
name: aleut-federal-context
description: {description}
---

# Aleut Federal Context

> This Skill auto-loads for AF-related questions. The full company reference is in `references/aleut-federal-context.md`. Read that for facts; then defer to any active role Skill for workflow.

## Purpose

Anchor every AF-related answer in the authoritative company facts:

- Aleut Federal is a privately held subsidiary of **The Aleut Corporation**, an Alaska Native Corporation (ANC) established under ANCSA (43 U.S.C. § 1601 et seq.).
- Lines of business: **federal services** and **federal construction** to U.S. federal agencies.
- Special federal status: **SBA 8(a) Business Development Program** under the ANC rules (13 C.F.R. Part 124).
- Sole-source authority: civilian agencies — **unlimited dollar value**; DoD — **up to the current DoD sole-source threshold** (FAR 19.808-1; 13 C.F.R. § 124.506(b)).
- ANC subsidiaries are generally **not affiliated** with each other or the parent for SBA size purposes (13 C.F.R. § 121.103(b)(2)).

## Regulatory framework (load on demand from references/)

- **FAR / DFARS / agency supplements** — acquisition rules.
- **SBA 8(a) Program** — 13 C.F.R. Part 124; FAR Subpart 19.8.
- **SCA / Davis-Bacon / CWHSSA / Copeland / EO 14026** — labor.
- **Miller Act / EM 385-1-1 / OSHA 1926** — construction.
- **FAR Part 31 / CAS / DCAA** — cost accounting and audit.
- **DFARS 252.204-7012 / NIST 800-171 / CMMC 2.0 / FedRAMP** — cyber / CUI.
- **Section 889 / BAA / TAA / BABA** — supply chain.
- **FAR 52.203-13 / FCA / Anti-Kickback / PIA** — ethics and integrity.
- **OFCCP / VEVRAA / Section 503 / E-Verify** — equal employment.
- **ITAR / EAR** — export control.

## Hard constraints (apply to every answer)

1. **No legal advice.** AF skills assist with analysis and drafting; qualified counsel reviews before reliance.
2. **No source-selection-sensitive information** (FAR 3.104 / Procurement Integrity Act). Refuse if offered.
3. **No commitments outside the Contracting Officer.** Only the CO can change scope, price, period of performance, or T&Cs.
4. **No promises of award.** 8(a) sole-source eligibility is a tool, not a guarantee.
5. **Protect CUI / ITAR / classified.** Refuse to process in unauthorized environments.
6. **Section 889 hygiene.** Never suggest covered telecom from prohibited entities.
7. **Buy American / TAA / BABA hygiene.** Default to compliant origin on covered work.
8. **Mandatory disclosure (FAR 52.203-13).** Credible evidence of FCA / certain criminal violations / significant overpayment goes to General Counsel — never papered into routine outputs.

## How other Skills should use this Skill

When this Skill is active alongside a role Skill (legal, finance, sales, etc.), the role Skill drives the workflow; this Skill provides the facts and the hard-rule refusals. If a role Skill workflow would conflict with these constraints, this Skill's constraints win.

The full reference (NAICS codes, vehicle catalog, pipeline / BD sources, federal vocabulary) is in `references/aleut-federal-context.md`.
"""

    (out_dir / "SKILL.md").write_text(skill_md)

    # Copy the full company reference into the Skill's references/.
    shutil.copy(CONTEXT_FILE, out_dir / "references" / "aleut-federal-context.md")

    # agents/openai.yaml — IMPLICIT INVOCATION is the key flag here. This is
    # the only Skill in the bundle with implicit_invocation=true; everything
    # else is explicit-invoke-only.
    yaml_text = OPENAI_YAML_TEMPLATE.format(
        display_name="Aleut Federal Context",
        short_description="Auto-loads Aleut Federal's company facts, regulatory framework, and hard constraints for any AF-related question.",
        implicit="true",
    )
    (out_dir / "agents" / "openai.yaml").write_text(yaml_text)

    # Generic icon.
    (out_dir / "assets" / "icon.svg").write_text(DEFAULT_ICON)


def write_top_readme(skills: list[dict]) -> None:
    """Hand-curated README at the chatgpt/ root explaining the Skill layout."""
    by_plugin: dict[str, list[dict]] = {}
    for s in skills:
        by_plugin.setdefault(s["plugin"], []).append(s)

    plugin_rows = []
    for plugin in PLUGINS:
        skills_in = by_plugin.get(plugin, [])
        if not skills_in:
            continue
        plugin_rows.append(
            f"| `{plugin}/` | {len(skills_in)} | "
            + ", ".join(f"`{s['openai_name']}`" for s in skills_in)
            + " |"
        )

    readme = f"""# Aleut Federal — OpenAI Skills

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

{chr(10).join(plugin_rows)}

| | | |
|---|---|---|
| **Total** | {len(skills)} explicit-invoke Skills + 1 implicit-invoke context Skill | |

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
"""
    (CHATGPT_ROOT / "README.md").write_text(readme)


def main() -> int:
    if not CONTEXT_FILE.exists():
        print(f"ERROR: {CONTEXT_FILE} not found", file=sys.stderr)
        return 1

    CHATGPT_ROOT.mkdir(exist_ok=True)
    # Clean every plugin subdir + the implicit-context skill. Keep build.py.
    for entry in CHATGPT_ROOT.iterdir():
        if entry.name in {"build.py"}:
            continue
        if entry.is_dir():
            shutil.rmtree(entry)
        elif entry.is_file() and entry.name == "README.md":
            entry.unlink()

    skills = collect_skills()
    if not skills:
        print("ERROR: no skills found in source plugins", file=sys.stderr)
        return 1
    resolve_output_names(skills)

    # Sanity-check uniqueness after resolution.
    name_counts = Counter(s["openai_name"] for s in skills)
    dupes = {n: c for n, c in name_counts.items() if c > 1}
    if dupes:
        print(f"ERROR: duplicate OpenAI Skill names after resolution: {dupes}", file=sys.stderr)
        return 1

    for s in skills:
        write_skill_package(s)
    write_implicit_context_skill()
    write_top_readme(skills)

    print(f"Built {len(skills)} explicit-invoke Skills + 1 implicit-invoke context Skill.")
    print("To rebuild, run: python3 chatgpt/build.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
