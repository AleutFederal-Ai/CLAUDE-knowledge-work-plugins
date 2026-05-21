# documentation

> **What this skill does:** Write and maintain technical documentation. Trigger with "write docs for", "document this", "create a README", "write a runbook", "onboarding guide", or when the user needs help with any form of technical writing — API docs, architecture docs, or operational runbooks.

# Technical Documentation — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

Write clear, maintainable technical documentation for federal-contract deliverables and internal use.

## Aleut Federal Context — Federal Documentation Categories

Federal contracts typically require a documented document set. Common categories and the authority that drives them:

- **System Security Plan (SSP)** — NIST SP 800-18 / 800-171 / 800-53.
- **Plan of Action & Milestones (POA&M)** — companion to SSP.
- **System Security and Privacy Plan (SSPP)** — RMF artifact.
- **Configuration Management Plan (CMP)** — NIST 800-128.
- **Incident Response Plan (IRP)** — NIST 800-61; DFARS 252.204-7012 alignment.
- **Contingency / Disaster Recovery Plan (CP / DRP)** — NIST 800-34.
- **Information System Continuous Monitoring (ISCM)** plan.
- **Privacy Impact Assessment (PIA)** — agency-specific (don't confuse with Procurement Integrity Act).
- **System / Subsystem Design Description (SSDD)** and **Software Design Description (SDD)** — DI-IPSC-81431 / -81435.
- **Software Test Plan (STP) and Report (STR)** — DI-IPSC-81438 / -81440.
- **Software Version Description (SVD)** — DI-IPSC-81442.
- **User manuals, operator manuals** — DI-SESS / DI-TMSS.
- **CDRL deliverables** — specific to the contract; format dictated by the DID.
- **Section 508 Voluntary Product Accessibility Template (VPAT) / ACR**.
- **SBOM** under EO 14028.

When writing any of these, follow the prescribed DID format (if applicable) exactly — non-conforming deliverables get rejected and show up in CPARS. Mark CUI properly; deliver only through agency-approved transmission channels.

## Document Types

### README
- What this is and why it exists
- Quick start (< 5 minutes to first success)
- Configuration and usage
- Contributing guide

### API Documentation
- Endpoint reference with request/response examples
- Authentication and error codes
- Rate limits and pagination
- SDK examples

### Runbook
- When to use this runbook
- Prerequisites and access needed
- Step-by-step procedure
- Rollback steps
- Escalation path

### Architecture Doc
- Context and goals
- High-level design with diagrams
- Key decisions and trade-offs
- Data flow and integration points

### Onboarding Guide
- Environment setup
- Key systems and how they connect
- Common tasks with walkthroughs
- Who to ask for what

## Principles

1. **Write for the reader** — Who is reading this and what do they need?
2. **Start with the most useful information** — Don't bury the lede
3. **Show, don't tell** — Code examples, commands, screenshots
4. **Keep it current** — Outdated docs are worse than no docs
5. **Link, don't duplicate** — Reference other docs instead of copying
