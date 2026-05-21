# tech-debt

> **What this skill does:** Identify, categorize, and prioritize technical debt. Trigger with "tech debt", "technical debt audit", "what should we refactor", "code health", or when the user asks about code quality, refactoring priorities, or maintenance backlog.

# Tech Debt Management — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

Systematically identify, categorize, and prioritize technical debt across federal-contract systems.

## Aleut Federal Context — Federal Tech-Debt Categories

Tech debt on federal systems carries regulatory teeth in addition to engineering cost:

- **Security-control debt** — gaps against NIST 800-53 / 800-171 baseline; reflected in POA&M items with target completion dates. Aging POA&M items are an ATO risk.
- **CMMC posture debt** — controls below the contract's required level; affects eligibility for new task orders and DoD contract awards.
- **Cryptography debt** — non-FIPS-validated modules, deprecated algorithms (MD5, SHA-1 for signing, RC4, 3DES).
- **Supply-chain debt** — outdated SBOM, unaddressed CVEs, Section 889 supplier in the dependency chain.
- **Accessibility debt** — Section 508 / WCAG 2.1 AA gaps; affects whether the system is acceptable to federal users.
- **Documentation debt** — out-of-date SSP, SDD, CMP, IRP, DRP, CDRL deliverables.
- **Configuration baseline drift** — config that has diverged from the approved baseline; CCB attention required.
- **Funding category** — most tech-debt remediation on a federal contract is billable only if in scope; out-of-scope remediation may need CO mod or run on overhead.

Prioritize by ATO risk + customer-visible impact, not just engineering pain.

## Categories

| Type | Examples | Risk |
|------|----------|------|
| **Code debt** | Duplicated logic, poor abstractions, magic numbers | Bugs, slow development |
| **Architecture debt** | Monolith that should be split, wrong data store | Scaling limits |
| **Test debt** | Low coverage, flaky tests, missing integration tests | Regressions ship |
| **Dependency debt** | Outdated libraries, unmaintained dependencies | Security vulns |
| **Documentation debt** | Missing runbooks, outdated READMEs, tribal knowledge | Onboarding pain |
| **Infrastructure debt** | Manual deploys, no monitoring, no IaC | Incidents, slow recovery |

## Prioritization Framework

Score each item on:
- **Impact**: How much does it slow the team down? (1-5)
- **Risk**: What happens if we don't fix it? (1-5)
- **Effort**: How hard is the fix? (1-5, inverted — lower effort = higher priority)

Priority = (Impact + Risk) x (6 - Effort)

## Output

Produce a prioritized list with estimated effort, business justification for each item, and a phased remediation plan that can be done alongside feature work.
