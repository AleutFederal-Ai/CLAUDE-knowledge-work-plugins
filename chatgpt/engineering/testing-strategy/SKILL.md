---
name: testing-strategy
description: Design test strategies and test plans. Trigger with "how should we test", "test strategy for", "write tests for", "test plan", "what tests do we need", or when the user needs help with testing approaches, coverage, or test architecture.
---

# Testing Strategy — Aleut Federal

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Design effective testing strategies for federal-contract systems balancing coverage, speed, maintenance, and the contracted Software Test Plan (STP) / Software Test Report (STR) deliverables.

## Aleut Federal Context — Federal Testing Layers

In addition to the standard testing pyramid, federal systems usually require:

- **Security testing** — SAST, DAST, SCA, container image scans; results feed POA&M / ATO. Cadence per the SSPP.
- **Section 508 / accessibility** automated and manual testing for any UI.
- **STIG / SCAP scans** where DoD STIG applicability is required.
- **FIPS validation evidence** — testing confirms the cryptographic module in use is the validated one (CMVP certificate).
- **Penetration testing** — periodic; aligned to the AO's risk-based requirements (typically annual at Moderate, more frequent at High).
- **Continuous monitoring** — automated control assessments per ISCM plan.
- **STP/STR deliverables** — formal test plan and report per DI-IPSC-81438 / -81440 (or agency equivalent); test cases mapped to PWS requirements and CDRL deliverables.
- **Test data** — never use production CUI; create synthetic or scrubbed datasets.

Test results feed the CPARS narrative and the next continuous-monitoring submission to the AO.

## Testing Pyramid

```
 / E2E \ Few, slow, high confidence
 / Integration \ Some, medium speed
 / Unit Tests \ Many, fast, focused
```

## Strategy by Component Type

- **API endpoints**: Unit tests for business logic, integration tests for HTTP layer, contract tests for consumers
- **Data pipelines**: Input validation, transformation correctness, idempotency tests
- **Frontend**: Component tests, interaction tests, visual regression, accessibility
- **Infrastructure**: Smoke tests, chaos engineering, load tests

## What to Cover

Focus on: business-critical paths, error handling, edge cases, security boundaries, data integrity.

Skip: trivial getters/setters, framework code, one-off scripts.

## Output

Produce a test plan with: what to test, test type for each area, coverage targets, and example test cases. Identify gaps in existing coverage.
