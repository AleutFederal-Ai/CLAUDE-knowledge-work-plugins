---
name: user-access-provisioning
description: Provision, modify, and deprovision user accounts and access for Aleut Federal — joiner / mover / leaver workflow across AF systems and federal-customer environments. Includes E-Verify confirmation, clearance verification, CUI-environment enrollment, PIV / CAC issuance / revocation, MFA enrollment, role-based access (RBAC), least-privilege enforcement, and immediate account disable on termination or clearance loss.
argument-hint: "<joiner | mover | leaver | access-change> <employee>"
---

# /user-access-provisioning — Aleut Federal CIO Shop

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md).

Joiner / Mover / Leaver workflow for AF user accounts and access, with the federal-contractor gates baked in.

## Aleut Federal Context — Federal-Contractor Access Controls

Federal-contractor access has obligations commercial JML does not:

- **E-Verify** (FAR 52.222-54) — work authorization confirmed in the federal E-Verify system within 3 business days of hire, before access provisioning.
- **Security clearance verification** — for cleared roles, current clearance level confirmed via DCSA / agency security office before account creation in any cleared environment.
- **CUI environment enrollment** — for roles handling CUI (DFARS 252.204-7012), access requires SSP acknowledgment + NIST 800-171 training completion + authorized environment account.
- **PIV / CAC** — for federal-customer system access, federal-issued credential; AF's role is sponsoring/coordinating, not issuing.
- **Citizenship** — verified for roles with ITAR-controlled data access.
- **Continuous evaluation** — clearance-relevant changes (financial, foreign contact, drug, criminal) must be reported; affects ongoing access.
- **NIST 800-171 3.1.x access controls** — least privilege, role-based access, separation of duties.
- **Account audit trail** — every provision / modify / deprovision logged for NIST 800-53 AU-2 / DFARS 7012 auditability.
- **Immediate disable on termination** — clearance loss, voluntary or involuntary termination, suspension for cause — all trigger immediate disable, even before the formal offboarding.

## Workflow

### Joiner

1. **Pre-start checks** (HR coordinates; IT executes when go signal received):
   - I-9 + E-Verify queries complete.
   - Background check cleared.
   - For cleared roles: clearance verified via DCSA; SF-86 or passback confirmed.
   - For CUI-handling roles: SSP acknowledgment signed, NIST 800-171 training complete.
   - Code of Business Ethics acknowledgment (FAR 52.203-13).
   - Drug screen passed (FAR 52.223-6).

2. **Day 1 provisioning** — based on role, contract assignment, and clearance level:
   - AD / Entra account with role-based group membership.
   - M365 / Google Workspace mailbox.
   - MFA enrollment (FIDO2 / authenticator app; no SMS).
   - SSO assignments matched to role.
   - VPN access if needed; locked to authorized geographies.
   - PIV/CAC sponsor request submitted to the federal customer (for cleared / federal-system roles).
   - CUI-authorized environment account (when applicable).
   - Charge codes loaded into timekeeping system.
   - Software licenses per role.

3. **Day 5 verification:**
   - Confirm new hire can perform role tasks.
   - Confirm timekeeping working (DFARS 252.242-7006(c)(6) daily total time accounting).
   - Confirm training assignments enrolled (ethics, cybersecurity awareness, contract-specific).

### Mover (role / contract / clearance change)

1. Identify new role, contract assignment, and required access changes.
2. **Revoke** access no longer needed (least-privilege enforcement).
3. **Add** access needed for the new role.
4. **Clearance changes:** if upgrading, run additional vetting; if losing clearance, revoke cleared-environment access immediately.
5. **Contract reassignment:** update charge codes; if moving off a CUI contract, evaluate CUI environment access.
6. **OCONUS / locality change:** update geographic access controls.

### Leaver (termination — voluntary or involuntary)

1. **Immediate (concurrent with notice):**
   - Disable AD / Entra account (do not delete; preserve for audit).
   - Disable all SSO sessions; revoke all active tokens / API keys.
   - Disable VPN / remote access.
   - Revoke PIV/CAC sponsorship; notify federal customer to revoke if applicable.
   - Disable email forwarding to external addresses (legal hold may apply).
   - Disable mobile device profiles; remote-wipe AF-managed devices.
   - For cleared personnel: notify FSO; FSO debriefs clearance.

2. **Within 24 hours:**
   - Inventory and recover AF-issued hardware.
   - Inventory and recover CAC / PIV / smartcards.
   - Identify shared accounts / passwords the leaver had access to; rotate.
   - Preserve mailbox and OneDrive / SharePoint for the retention period (FAR 4.703 minimum; longer for cleared / CUI environments).

3. **Within 7 days:**
   - Final offboarding ticket: confirm all access disabled; clearance debriefed; hardware returned; mailbox archived.
   - For-cause terminations: coordinate with GC and HR; preserve communications under legal hold.
   - **Mandatory-disclosure check (FAR 52.203-13):** if the termination relates to fraud / criminal / significant overpayment evidence, route to GC.

### Access Change (no role move)

For one-off access changes (project assignment, temporary elevation):
- Justification documented.
- Approver per the role's access matrix.
- Time-bounded where appropriate (auto-expire).
- Logged for audit.

## Hard Rules

- **Never provision access before E-Verify and background check complete.**
- **Never provision cleared-environment access without verified active clearance** at the required level.
- **Never provision CUI-environment access without SSP acknowledgment and training completion.**
- **Never delete an account.** Disable, preserve for audit per FAR 4.703.
- **Never leave an offboarded account enabled overnight.** Immediate disable, even when full inventory recovery takes longer.
- **Always coordinate cleared-personnel offboarding with the FSO.**
- **Always coordinate for-cause terminations with HR + GC** before any system changes that could affect a litigation hold.
- **Section 889 / supply chain:** never enroll an offboarded account into a successor system that uses prohibited covered telecom.

## Output Format

```markdown
## Access Action: [Joiner / Mover / Leaver / Access Change] — [Employee]

**Effective:** [date/time]
**Owner:** [requestor]
**Approver:** [role]
**Status:** [In Progress / Complete]

### Pre-Action Gates (Joiner / Mover)
- [ ] I-9 + E-Verify (joiner)
- [ ] Background check (joiner)
- [ ] Clearance verified (cleared role)
- [ ] SSP + NIST 800-171 training (CUI role)
- [ ] Ethics acknowledgment (joiner)
- [ ] Drug screen (joiner)

### Access Provisioned / Modified / Revoked
| System | Role / Group | Action | Status |

### Hardware
| Item | Action | Status |

### Special Items
- PIV/CAC sponsorship request: [...]
- FSO notification (cleared): [...]
- Mailbox / OneDrive retention: [...]
- Legal hold (for-cause): [...]
- Mandatory-disclosure trigger (FAR 52.203-13): [None / Routed to GC]
```
