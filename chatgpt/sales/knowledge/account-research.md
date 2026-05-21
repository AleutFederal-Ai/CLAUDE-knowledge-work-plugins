# account-research

> **What this skill does:** Research a federal agency, prime contractor, or specific federal contract for Aleut Federal capture. Works standalone with public sources (SAM.gov, USAspending, agency forecasts, FPDS), and is supercharged when GovWin / HigherGov / Bloomberg Gov / CRM is connected. Trigger with "research [agency]", "look up [prime]", "intel on [contract/solicitation]", "what's [agency] buying", or "who is the incumbent on [contract number]".

# Federal Account / Opportunity Research — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

Build a capture-ready picture of a federal customer, prime contractor, or specific opportunity. This skill works standalone with public federal data and gets richer when GovCon market-intel tools (GovWin / HigherGov / Bloomberg Gov / EZGovOpps) and the CRM are connected.

## What this skill researches

Sales targets in our world come in three flavors. Identify which the user is asking about:

1. **Agency / Sub-agency / Office** — e.g., "USACE Mobile District," "GSA FAS 2GIT," "DOE NNSA Production Office," "Air Force AFCEC Tyndall."
2. **Prime contractor** — for teaming, competitive intel, or recompete analysis. e.g., Leidos, SAIC, Booz Allen, Bechtel, KBR, AECOM, MOTS.
3. **Specific contract / vehicle / solicitation** — e.g., "F-101 award" notice, an IDIQ ceiling we want to sub under, a recompete coming up.

Ask which one if the user hasn't said.

## Sources (priority order)

Always start with authoritative federal sources before falling back to general web search.

| Source | What to pull |
|--------|--------------|
| **SAM.gov** | Active solicitations, sources sought, RFIs, awards (Contract Opportunities and Award Notices); entity registrations; exclusions |
| **USAspending.gov** | Historical award data — by agency, sub-agency, recipient, NAICS, PSC; ceiling vs obligated; subaward (FAR 4.14) reporting |
| **FPDS-NG** | Legacy view of contract actions; mods; vehicle codes |
| **DSBS (Dynamic Small Business Search)** | Capability narratives, certifications (8(a), HUBZone, WOSB), past performance |
| **agency forecasts** | DoD Annual Procurement Forecast (APFS), GSA forecast of contracting opportunities, VA, DHS, HHS, DOE, NASA, USAID forecasts |
| **eBuy** | GSA Schedule task orders |
| **DIBBS** | DLA solicitations |
| **PIEE / WAWF** | Awarded contract data, invoicing |
| **Federal Register** | Rule changes affecting the agency or program |
| **Agency websites** | Mission, organizational charts, strategic plans, IT modernization plans (CIO 10x), HCA / CCO names |
| **GAO / CRS** | Reports on the agency / program |
| **GovWin / HigherGov / Bloomberg Gov / EZGovOpps** | Aggregated forecasts, recompete probability, market analyses (if subscription connected) |
| **CPARS public summaries (when available)** | Past performance posture of primes |
| **Linkedin / agency press releases** | Key officials' backgrounds (apply PIA / 18 U.S.C. § 207 screen if hiring) |
| **Capability statements / press releases** | Prime competitor positioning |

## Workflow

### For agency research

1. **Mission and structure** — what does this agency do; sub-agencies and key offices; headcount; OCONUS posture.
2. **Budget posture** — current FY appropriation, request, and continuing resolution status; key program lines we touch (e.g., MILCON for construction; O&M for services).
3. **Contracting officers / HCAs / SCOs** — who runs procurement at the office level; identify the CO assigned to vehicles we hold or are pursuing.
4. **Forecast pulls** — pending opportunities by NAICS, PSC, and set-aside relevant to us; flag 8(a) sole-source candidates and small-business set-asides.
5. **Historical spend** (USAspending) — top vendors, NAICS distribution, set-aside utilization, average contract size, multi-year contract types.
6. **Vehicle alignment** — what GWACs / IDIQs / BPAs the agency uses for our type of work; whether we are on those vehicles or need to sub.
7. **Incumbent map** — for known recompetes, who has it, value, period of performance, CPARS history (where public), recompete probability.
8. **Pain points / priorities** — from agency strategic plans, OIG reports, GAO findings, news.
9. **Engagement plan** — industry days, RFI windows, sources-sought responses, agency conferences (e.g., SAME JETC, AFCEA TechNet, AFFIRM, FedTalks).

### For prime contractor research

1. **Overview** — size, focus, federal vs commercial mix.
2. **Key customers** — agencies they serve; share of revenue if known.
3. **Vehicles they hold** — GWACs / IDIQs / GSA Schedule; vehicles where we could partner.
4. **Past performance and CPARS** — public data; known program performance.
5. **Set-aside posture** — do they have small-business goals to meet under FAR 52.219-9? Are they a likely teaming partner where we provide a small-business component?
6. **Recent wins and losses** — last 24 months.
7. **Recompete exposure** — what contracts are up; what's their incumbency risk.
8. **Leadership and BD** — capture leads, BD reps; key offices.
9. **Teaming history with Aleut Federal** — from CRM if connected; any pending TAs/NDAs.
10. **Mentor-Protégé status** — are they an active SBA mentor; could a Mentor-Protégé arrangement help us?
11. **Compliance posture** — SAM status, FAPIIS entries, Section 889 representations.

### For a specific contract / solicitation

1. **Solicitation basics** — agency, sub-agency, CO, NAICS, PSC, set-aside, contract type, vehicle, estimated value, period of performance, place of performance.
2. **Sections L/M/H/C/J** — read in priority L→M→C; pull evaluation factors, sub-factors, weights; flag any pass/fail gates.
3. **Incumbent** — name, value, performance period, CPARS history (if available), recompete risk.
4. **Historical context** — was this work performed previously under a different vehicle/contract? Pull USAspending for prior award lineage.
5. **Vehicles** — is this on a contract we already hold? If sub-only, identify likely primes.
6. **Set-aside / size** — verify NAICS size standard and our eligibility; check whether 8(a) sole-source is an option for the customer (CO discretion + SBA acceptance).
7. **Competition landscape** — likely bidders; capture-management hypothesis.
8. **Compliance hot-spots** — DFARS 252.204-7012 / CMMC level required; Section 889 reps; Buy American / TAA / BABA on construction; SCA WD / Davis-Bacon WD; security clearances; place of performance OCONUS implications.
9. **Past performance fit** — our relevant references with size, recency, scope match.
10. **Capture strategy hypothesis** — bid / no-bid drivers; PPM (price-to-win) hypothesis; teaming requirements.

## Output Format

```markdown
## Federal Account Research: [Agency / Prime / Contract]

### Snapshot
- **Type**: [Agency / Prime / Contract]
- **Mission / Focus**: ...
- **Size**: budget (agency), revenue (prime), or value (contract)
- **Primary contracting offices**: ...
- **Set-aside / vehicle posture**: ...

### Key Findings
[3–5 bullets capture-ready]

### Forecast / Pipeline Items
| Title | Solicitation # | NAICS | Set-Aside | Estimated $ | PoP | Source |
|-------|----------------|-------|-----------|-------------|-----|--------|

### Top Incumbents / Vendors (USAspending, trailing 36 months)
| Vendor | Total Obligated | # Awards | Top NAICS | Set-Aside |

### Vehicle Map
- Vehicles in use:
- Vehicles we hold:
- Vehicles to consider:

### Engagement & Relationships
- CO / KO / SCO:
- COR / Program leads:
- Industry events:
- Aleut Federal prior interactions (CRM):

### Compliance Hotspots for Our Pursuits
- CUI / DFARS 7012 / CMMC level:
- SCA / Davis-Bacon WD:
- Section 889 considerations:
- Place of performance / clearances:

### Capture Strategy Hypothesis
[Bid/no-bid signals, teaming approach, set-aside angle, PPM bracket]

### Sources Consulted
- SAM.gov: ...
- USAspending: ...
- Agency forecast: ...
- Other: ...
```

## Hard Rules

- **No source-selection-sensitive information.** Do not seek, accept, or use any non-public source-selection information or contractor bid/proposal information (FAR 3.104 / Procurement Integrity Act).
- **No insider-cultivated agency contacts.** Engagement with federal officials must respect the agency's market research procedures (sources sought, industry days, RFIs, posted Q&A windows). Outside of those, exchanges are limited and gift rules (5 C.F.R. Part 2635) apply.
- **No promises of award** or implied endorsements by agency personnel.
- **Section 889 / SAM exclusions** — flag if a target prime or sub is excluded or has Section 889 issues.
- **Privileged information** — if research surfaces something that may implicate Procurement Integrity, FCA, or ethics, stop and route to GC.
