---
name: process-optimization
description: Analyze and improve business processes. Trigger with "this process is slow", "how can we improve", "streamline this workflow", "too many steps", "bottleneck", or when the user describes an inefficient process they want to fix.
---

# Process Optimization — Aleut Federal

> Aleut Federal company context lives in the **aleut-federal-context** Skill (auto-invoked for AF-related questions).

Analyze existing processes and recommend improvements, with awareness of the federal-contractor environment.

## Aleut Federal Context — Constraints on "Optimization"

Many commercial "optimizations" are not permissible for a federal contractor:

- Cannot bypass FAR/DFARS clause obligations (e.g., skip competitive sub procurement when FAR 52.244-2 or our CPSR requires it).
- Cannot skip approvals required by the CO (FAR 52.243-x changes; FAR 52.245-x property).
- Cannot lower the FAR 31.205 cost-allowability bar to widen margin.
- Cannot relax NIST 800-171 / CMMC controls below the contract requirement.
- Cannot reduce SCA / Davis-Bacon compliance for efficiency.
- Cannot reduce documentation that DCAA / DCMA / IPA needs.

Optimizations that ARE valuable:
- Reducing cycle time on internal approvals while preserving required control points.
- Automating evidence collection for compliance.
- Consolidating indirect-cost pools where consistent with CAS and disclosure statement.
- Streamlining timekeeping with controls preserving daily-total-time accounting.
- Improving subcontractor onboarding to clear FAR/DFARS gates faster.

Run a "compliance impact" check before recommending any process change.

## Analysis Framework

### 1. Map Current State
- Document every step, decision point, and handoff
- Identify who does what and how long each step takes
- Note manual steps, approvals, and waiting times

### 2. Identify Waste
- **Waiting**: Time spent in queues or waiting for approvals
- **Rework**: Steps that fail and need to be redone
- **Handoffs**: Each handoff is a potential point of failure or delay
- **Over-processing**: Steps that add no value
- **Manual work**: Tasks that could be automated

### 3. Design Future State
- Eliminate unnecessary steps
- Automate where possible
- Reduce handoffs
- Parallelize independent steps
- Add checkpoints (not gates)

### 4. Measure Impact
- Time saved per cycle
- Error rate reduction
- Cost savings
- Employee satisfaction improvement

## Output

Produce a before/after process comparison with specific improvement recommendations, estimated impact, and an implementation plan.
