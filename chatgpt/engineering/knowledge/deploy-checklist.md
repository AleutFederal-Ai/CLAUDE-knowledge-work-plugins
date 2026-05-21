# deploy-checklist

> **What this skill does:** Pre-deployment verification checklist. Use when about to ship a release, deploying a change with database migrations or feature flags, verifying CI status and approvals before going to production, or documenting rollback triggers ahead of time.

# /deploy-checklist — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

## Aleut Federal Context — Federal Deployment Gates

In addition to standard pre-deploy verification, a federal-contract deploy must satisfy:

- **ATO scope check** — the change stays within the authorized boundary; if it changes the boundary (new component, new data flow, new external connection), the change is **significant** and requires ATO / AO action **before** deploy (NIST RMF Step 6).
- **Configuration management** — change ticket approved by the program CCB; baseline updated; SSP / SSPP delta noted.
- **POA&M alignment** — if the deploy closes a POA&M item, evidence captured for the next continuous-monitoring report.
- **Security scan results** — SAST/DAST/SCA/container scans clean (or risk-accepted) per the SSPP; SBOM regenerated and stored.
- **FIPS-validated crypto** in use; no new non-validated modules introduced.
- **No CUI / classified data** in deploy artifacts that move through unauthorized environments.
- **Section 508 regression test** for any UI changes.
- **CDRL impact** — does the deploy affect a contracted deliverable / SLA? Coordinate with the COR before changing observable behavior.
- **Customer-facing communication** — federal customers expect formal notice of changes affecting their experience; coordinate with the COR.
- **Rollback** — pre-staged; tested; rollback time meets contract availability SLA.
- **Records** — deployment record retained per the contract retention requirement (typically FAR 4.703).

Generate a pre-deployment checklist to verify readiness before shipping.

## Usage

```
/deploy-checklist $ARGUMENTS
```

## Output

```markdown
## Deploy Checklist: [Service/Release]
**Date:** [Date] | **Deployer:** [Name]

### Pre-Deploy
- [ ] All tests passing in CI
- [ ] Code reviewed and approved
- [ ] No known critical bugs in release
- [ ] Database migrations tested (if applicable)
- [ ] Feature flags configured (if applicable)
- [ ] Rollback plan documented
- [ ] On-call team notified

### Deploy
- [ ] Deploy to staging and verify
- [ ] Run smoke tests
- [ ] Deploy to production (canary if available)
- [ ] Monitor error rates and latency for 15 min
- [ ] Verify key user flows

### Post-Deploy
- [ ] Confirm metrics are nominal
- [ ] Update release notes / changelog
- [ ] Notify stakeholders
- [ ] Close related tickets

### Rollback Triggers
- Error rate exceeds [X]%
- P50 latency exceeds [X]ms
- [Critical user flow] fails
```

## Customization

Tell me about your deploy and I'll customize the checklist:
- "We use feature flags" → adds flag verification steps
- "This includes a database migration" → adds migration-specific checks
- "This is a breaking API change" → adds consumer notification steps

## If Connectors Available

If **~~source control** is connected:
- Pull the release diff and list of changes
- Verify all PRs are approved and merged

If **~~CI/CD** is connected:
- Check build and test status automatically
- Verify pipeline is green before deploy

If **~~monitoring** is connected:
- Pre-fill rollback trigger thresholds from current baselines
- Set up post-deploy metric watch

## Tips

1. **Run before every deploy** — Even routine ones. Checklists prevent "I forgot to..."
2. **Customize once, reuse** — Tell me your stack and I'll remember your deploy process.
3. **Include rollback criteria** — Decide when to roll back before you deploy, not during.
