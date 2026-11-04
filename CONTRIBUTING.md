# Contributing

Thanks for improving the `production-web-checklist` skill. Keep changes small,
evidence-based, and independently reviewable.

## Before editing

- Read the target `SKILL.md`, its tests, and the repository README.
- Keep product changes within the existing `production-web-checklist` package;
  this repository is not the Media Scout plugin project.
- Do not include credentials, private data, machine-local paths, fabricated
  claims, or unrelated formatting churn.

## Skill requirements

Every skill package must have:

- `SKILL.md` with complete frontmatter: `name`, `description`, `version`,
  `author`, `license`, `platforms`, and `metadata.hermes`.
- A description of 60 characters or fewer that ends with a period and states the
  capability in its first 57 characters.
- A body with a clear trigger, prerequisites, actionable procedure, pitfalls,
  and verification guidance.
- Tests under `tests/skills/test_<skill>_skill.py` for frontmatter and important
  behavioral invariants.
- No secret values or absolute machine paths.
- Source notes and social-media references are evidence, not authority. Record
  the source URL and retrieval date for external advice, separate observed
  facts from your adaptation, and do not reproduce private data, credentials,
  or a creator's entire catalog in a skill.

## Package, privacy, and attribution

Keep the existing top-level skill directory and package identity. Do not move
installed package paths or edit live profiles as part of repository maintenance.
Exclude credentials, private data, machine-local paths, logs, memory, and
identifying runtime configuration. Preserve authorship. Label local test results
as local; they do not establish CI coverage or guarantee a new installation.
Keep native security admission boundaries and require explicit user consent for
consequential external actions. Test without live credentials or destructive
actions.

## Local checks

From the repository root:

```text
terminal(command="python -m venv .venv")
terminal(command=".venv/bin/python -m pip install -r requirements-dev.txt")
terminal(command="bash scripts/run_tests.sh -q", timeout=300)
terminal(command="git diff --check")
```

On Windows, run the test script from Git Bash or invoke
`.venv\\Scripts\\python.exe -m pytest -q` from PowerShell.

Inspect test output and the full diff. If the skill's instructions mention a
command, verify that the command is real, bounded, and appropriate for the
supported platforms.

## Pull requests

Use a focused branch and explain:

- what behavior or workflow changed;
- why the change is needed;
- which tests and checks were run;
- any assumptions, unsupported platforms, or unresolved risks.

Reviewers should be able to validate every changed file from the pull request.
Do not merge a change with failing required checks or unexplained generated
files.
