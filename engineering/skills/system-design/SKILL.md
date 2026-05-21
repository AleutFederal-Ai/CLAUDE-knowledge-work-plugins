---
name: system-design
description: Design systems, services, and architectures. Trigger with "design a system for", "how should we architect", "system design for", "what's the right architecture for", or when the user needs help with API design, data modeling, or service boundaries.
---

# System Design — Aleut Federal

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). See the `architecture` skill for ADR-specific federal context.

Help design systems and evaluate architectural decisions for federal-contract work.

## Aleut Federal Context — Federal System-Design Inputs

Every design choice is constrained by the contract. Always start by collecting:

- **FIPS 199 impact level** (Low / Moderate / High) for confidentiality, integrity, availability.
- **Hosting authority** — on-prem, FedRAMP Moderate/High cloud, DoD IL2/IL4/IL5/IL6.
- **Data classes** — public, FOUO, CUI category (e.g., CUI//SP-CTI, CUI//PRVCY), classified.
- **User population** — public, federal employees, contractors, foreign nationals (affects ITAR/EAR).
- **Authentication** — PIV / CAC / FIDO2; agency SSO?
- **Logging / audit** — NIST 800-53 AU controls; agency retention requirements.
- **Availability target** — SLA in the contract; affects multi-AZ / multi-region cost.
- **Network boundary** — does it cross a federal network boundary (TIC / SASE)?
- **Cryptographic mandates** — FIPS 140-2/140-3; agency PKI integration.
- **Section 508 / accessibility** for any UI.
- **Records retention** — per the contract.

The design must produce a system that can earn (or inherit) an ATO at the required impact level on the required platform.

## Framework

### 1. Requirements Gathering
- Functional requirements (what it does)
- Non-functional requirements (scale, latency, availability, cost)
- Constraints (team size, timeline, existing tech stack)

### 2. High-Level Design
- Component diagram
- Data flow
- API contracts
- Storage choices

### 3. Deep Dive
- Data model design
- API endpoint design (REST, GraphQL, gRPC)
- Caching strategy
- Queue/event design
- Error handling and retry logic

### 4. Scale and Reliability
- Load estimation
- Horizontal vs. vertical scaling
- Failover and redundancy
- Monitoring and alerting

### 5. Trade-off Analysis
- Every decision has trade-offs. Make them explicit.
- Consider: complexity, cost, team familiarity, time to market, maintainability

## Output

Produce clear, structured design documents with diagrams (ASCII or described), explicit assumptions, and trade-off analysis. Always identify what you'd revisit as the system grows.
