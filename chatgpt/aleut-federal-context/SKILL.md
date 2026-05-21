---
name: aleut-federal-context
description: auto-load aleut federal company context (anc/8(a) status, far/dfars framework, sca/davis-bacon, cmmc 2.0, nist 800-171, far 52.203-13 mandatory disclosure, far 3.104 procurement integrity, hard constraints). use whenever a question involves aleut federal, our federal contracts, our 8(a) sole-source authority, our regulatory obligations, or our compliance posture. provides the company facts; other skills handle workflows.
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
