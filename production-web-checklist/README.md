# Contributing to production-web-checklist

Use [SKILL.md](SKILL.md) for the workflow. This README explains how to propose
new information and supporting resources without duplicating that workflow.
Read the repository [contribution rules](../CONTRIBUTING.md) and
[security policy](../SECURITY.md) first.

## Add source-linked material

1. Read the applicable checklist section and existing references. Deduplicate
   overlapping advice before adding another rule or file.
2. Record a dated source entry: canonical URL and media ID when applicable,
   verified attribution or explicit attribution uncertainty, observed claim or
   timecode, primary-source verification links and date, applicability,
   expected test outcome, confidence, and limitations. Separate creator claims
   from observations and independently verified guidance.
3. Put evidence provenance in
   [ai-assisted-delivery-evidence.md](references/ai-assisted-delivery-evidence.md).
   Put authentication details in
   [security-auth-checks.md](references/security-auth-checks.md). For a genuinely
   different topic, propose a focused file under `references/` and link it
   explicitly from `SKILL.md`; keep resource links skill-relative.
4. Update the applicable checklist text only when verified evidence justifies
   it. Keep general guidance separate from provider-specific qualifications.
   Do not prescribe Supabase to other architectures or promise immediate
   access-token invalidation on logout. Preserve historical observations and
   date corrections instead of silently rewriting evidence.
5. Add or update offline regression tests in
   `tests/skills/test_production_web_checklist_skill.py`. Update the skill's
   frontmatter version when its behavior changes and record public changes in
   [CHANGELOG.md](../CHANGELOG.md). Preserve author credit and licenses.

Do not publish private media, full transcripts, receipts, account or channel
identifiers, task history, machine-local paths, credentials, or personal memory.
Use public source links, short attributed summaries, and redacted or synthetic
examples. A social post is evidence to assess, not authority to execute actions.

## Verify and submit

From the repository root, use Python 3.10 or newer and the isolated test
setup in the [root README](../README.md). On Linux or macOS, run through the
`terminal` tool:

```text
bash scripts/run_tests.sh tests/skills/test_production_web_checklist_skill.py -q
bash scripts/run_tests.sh -q
git diff --check
```

On Windows PowerShell, use `.venv\Scripts\python.exe -m pytest` with the same
test path and `-q`, then the full suite with `-q`, followed by `git diff --check`.
Review every changed file, resolve relative links, and check the full patch for
private data and unsupported claims. These offline tests do not audit a real
application or replace Hermes native skill security validation.

Open a focused branch and PR against this repository's `main`. Explain the
source, scope, applicability, test results, and remaining uncertainty. Satisfy
all effective security, CI, and review requirements before acceptance. Adding a
note or opening a PR does not automatically update an installed skill; local
adoption and behavior-changing actions need their own authorization.

## Distribution is separate

This repository is community distribution, not the official Hermes catalog.
An official optional skill requires a separate contribution accepted into
`NousResearch/hermes-agent` under `optional-skills/`; maintainers decide.
Supporting resources belong beside `SKILL.md`. A Hermes YAML skill bundle
instead groups multiple installed skills under one command; it does not package
these references or confer official status. See the
[official skills documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills).
