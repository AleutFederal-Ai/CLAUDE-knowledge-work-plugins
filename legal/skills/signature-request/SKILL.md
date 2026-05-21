---
name: signature-request
description: Prepare and route a document for e-signature — run a pre-signature checklist, configure signing order, and send for execution. Use when a contract is finalized and ready to sign, when verifying entity names, exhibits, and signature blocks before sending, or when setting up an envelope with sequential or parallel signers.
argument-hint: "<document or contract to send>"
---

# /signature-request -- E-Signature Routing (Aleut Federal)

> Aleut Federal company context lives in [ALEUT-FEDERAL-CONTEXT.md](../../../ALEUT-FEDERAL-CONTEXT.md). If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Aleut Federal Context — Signature Authority and Federal Documents

- **Federal prime contracts and mods (SF 1449, SF 33, SF 30, DD 1155):** signed by the Contracting Officer on the Government side. On our side, only authorized officers may sign — verify against the current **Delegation of Authority** matrix (typically CEO / President / contracts director with named dollar thresholds and contract-type limits).
- **Teaming Agreements / Joint Venture Agreements:** for 8(a) JVs, ensure the **managing venturer's** authorized signatory signs first; SBA approval may be required prior to award and may need to be attached.
- **Subcontracts:** require purchase-order / subcontract-administrator sign-off plus the authorized officer; flow-downs exhibit must be attached.
- **Reps and Certs (FAR 52.204-8 annual reps, SAM.gov):** only an authorized official may certify; preserve provenance (date, IP, signer identity).
- **Wage Determinations (SCA / Davis-Bacon):** the WD revision in effect at contract execution governs; the executed WD must be attached and posted at the worksite.
- **Bond forms (Miller Act SF 25 / SF 25A):** signed by surety + authorized officer; deliver originals to CO; verify Treasury Listing 570 acceptability.

Bright lines:

- **No backdating.** Effective dates must reflect actual signature dates.
- **No simultaneous-execution shortcuts on federal mods.** A mod requires the CO's signature first or per the mod's effective-date language.
- **No CUI / source-selection information** in signature envelopes routed through non-authorized e-signature tenants.

Prepare a document for electronic signature — verify completeness, set signing order, and route for execution.

**Important**: This command assists with legal workflows but does not provide legal advice. Verify documents are in final form before sending for signature.

## Usage

```
/signature-request $ARGUMENTS
```

Prepare for signature: @$1

## Workflow

### Step 1: Accept the Document

Accept the document in any format:
- **File upload**: PDF, DOCX
- **URL**: Link to a document in ~~cloud storage or ~~CLM
- **Reference**: "The Acme Corp MSA we finalized yesterday"

### Step 2: Pre-Signature Checklist

Before routing for signature, verify:

```markdown
## Pre-Signature Checklist

- [ ] Document is in final, agreed form (no open redlines)
- [ ] All exhibits and schedules are attached
- [ ] Correct legal entity names on signature blocks
- [ ] Dates are correct or left blank for execution date
- [ ] Signature blocks match the authorized signers
- [ ] Any required internal approvals have been obtained
- [ ] Document has been reviewed by appropriate counsel
```

### Step 3: Configure Signing

Gather signing details:
- **Signers**: Who needs to sign? (names, emails, titles)
- **Signing order**: Sequential or parallel?
- **Internal approval**: Does anyone need to approve before the counterparty signs?
- **CC recipients**: Who should receive a copy of the executed document?

### Step 4: Route for Signature

**If ~~e-signature is connected:**
- Create the signature envelope/request
- Set signing fields and order
- Add any required initials or date fields
- Send for signature

**If not connected:**
- Generate a signing instruction document
- Provide the document formatted for wet signature or manual e-sign
- List all signers with contact information

## Output

```markdown
## Signature Request: [Document Title]

### Document Details
- **Type**: [MSA / NDA / SOW / Amendment / etc.]
- **Parties**: [Party A] and [Party B]
- **Pages**: [X]

### Pre-Signature Check: [PASS / ISSUES FOUND]
[List any issues that need attention before sending]

### Signing Configuration
| Order | Signer | Email | Role |
|-------|--------|-------|------|
| 1 | [Name] | [email] | [Party A Authorized Signatory] |
| 2 | [Name] | [email] | [Party B Authorized Signatory] |

### CC Recipients
- [Name] — [email]

### Status
[Sent for signature / Ready to send / Issues to resolve first]

### Next Steps
- [What to expect after sending]
- [Expected turnaround time]
- [Follow-up if not signed within X days]
```

## Tips

1. **Check entity names carefully** — The most common signing error is incorrect legal entity names.
2. **Verify authority** — Make sure each signer is authorized to bind their organization.
3. **Keep a copy** — Executed copies should be filed in ~~cloud storage or ~~CLM immediately after execution.
