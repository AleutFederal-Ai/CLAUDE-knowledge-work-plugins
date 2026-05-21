# code-review

> **What this skill does:** Review code changes for security, performance, and correctness. Trigger with a PR URL or diff, "review this before I merge", "is this code safe?", or when checking a change for N+1 queries, injection risks, missing edge cases, or error handling gaps.

# /code-review — Aleut Federal

> Aleut Federal company context lives in `ALEUT-FEDERAL-CONTEXT.md` (uploaded as `00-ALEUT-FEDERAL-CONTEXT.md`).

## Aleut Federal Context — Federal Code-Review Gates

In addition to standard security / performance / correctness checks, every code review on federal-contract code must verify:

- **No CUI / classified data in source** — code, comments, fixtures, sample data, logs.
- **No hardcoded secrets** — credentials, API keys, tokens, certificates.
- **FIPS 140-2/140-3 cryptography only** — no homegrown crypto; no non-validated libraries (e.g., no `MD5`, `SHA-1` for signing; only validated modules for AES/RSA/ECDSA).
- **NIST SP 800-53 control alignment** — changes affecting AC, AU, IA, SC controls require SSP / POA&M consideration.
- **Section 508 / WCAG 2.1 AA** — UI changes meet accessibility requirements (no images without alt text, semantic HTML, keyboard navigation, contrast).
- **Section 889 / supply chain** — no new dependencies from covered telecom entities; verify SBOM updates and SSDF attestation.
- **Logging** — adequate audit logging (NIST 800-53 AU controls); no PII / CUI in logs.
- **Data classification** — code handling CUI must be in a CUI-authorized repo / branch and protect data at rest and in transit per NIST 800-171.
- **License compliance** — no GPL contamination of work-for-hire deliverables where the customer expects unlimited or government-purpose rights (FAR 52.227-14 / DFARS 252.227-7013).
- **Configuration baseline** — changes to security-relevant configuration require ATO / change-control board awareness.

For any change implicating a security control, link the PR to the SSP control and POA&M item.

Review code changes with a structured lens on security, performance, correctness, and maintainability.

## Usage

```
/code-review <PR URL or file path>
```

Review the provided code changes: @$1

If no specific file or URL is provided, ask what to review.

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│ CODE REVIEW │
├─────────────────────────────────────────────────────────────────┤
│ STANDALONE (always works) │
│ ✓ Paste a diff, PR URL, or point to files │
│ ✓ Security audit (OWASP top 10, injection, auth) │
│ ✓ Performance review (N+1, memory leaks, complexity) │
│ ✓ Correctness (edge cases, error handling, race conditions) │
│ ✓ Style (naming, structure, readability) │
│ ✓ Actionable suggestions with code examples │
├─────────────────────────────────────────────────────────────────┤
│ SUPERCHARGED (when you connect your tools) │
│ + Source control: Pull PR diff automatically │
│ + Project tracker: Link findings to tickets │
│ + Knowledge base: Check against team coding standards │
└─────────────────────────────────────────────────────────────────┘
```

## Review Dimensions

### Security
- SQL injection, XSS, CSRF
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure deserialization
- Path traversal
- SSRF

### Performance
- N+1 queries
- Unnecessary memory allocations
- Algorithmic complexity (O(n²) in hot paths)
- Missing database indexes
- Unbounded queries or loops
- Resource leaks

### Correctness
- Edge cases (empty input, null, overflow)
- Race conditions and concurrency issues
- Error handling and propagation
- Off-by-one errors
- Type safety

### Maintainability
- Naming clarity
- Single responsibility
- Duplication
- Test coverage
- Documentation for non-obvious logic

## Output

```markdown
## Code Review: [PR title or file]

### Summary
[1-2 sentence overview of the changes and overall quality]

### Critical Issues
| # | File | Line | Issue | Severity |
|---|------|------|-------|----------|
| 1 | [file] | [line] | [description] | 🔴 Critical |

### Suggestions
| # | File | Line | Suggestion | Category |
|---|------|------|------------|----------|
| 1 | [file] | [line] | [description] | Performance |

### What Looks Good
- [Positive observations]

### Verdict
[Approve / Request Changes / Needs Discussion]
```

## If Connectors Available

If **~~source control** is connected:
- Pull the PR diff automatically from the URL
- Check CI status and test results

If **~~project tracker** is connected:
- Link findings to related tickets
- Verify the PR addresses the stated requirements

If **~~knowledge base** is connected:
- Check changes against team coding standards and style guides

## Tips

1. **Provide context** — "This is a hot path" or "This handles PII" helps me focus.
2. **Specify concerns** — "Focus on security" narrows the review.
3. **Include tests** — I'll check test coverage and quality too.
