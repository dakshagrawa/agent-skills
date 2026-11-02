# Hermes Workflows

Reusable skills and portable native-workflow templates for
[Hermes Agent](https://github.com/NousResearch/hermes-agent).

Formerly `dakshagrawa/agent-skills`: same repository and history, broader scope.
Existing skill paths are unchanged. See [migration notes](MIGRATION.md).

## Choose a package

| Package | Purpose |
| --- | --- |
| [production-web-checklist](production-web-checklist/SKILL.md) | Evidence-based website design, accessibility, SEO, security and release review |
| [media-evidence-library](media-evidence-library/SKILL.md) | Capture, deduplicate, review and recall source-backed media evidence |
| [Media Scout workflow](workflows/media-scout/README.md) | Native intake/reviewer profiles, automatic review under consent, learning notes and qualified retention |
| [Optional naming patch](patches/media-thread-naming/README.md) | Base-specific native Discord Instagram-ID naming; not an upstream release or auto-installer |

The [Media Scout diagram](workflows/media-scout/workflow.html) is a self-contained
HTML artifact: download it and open locally. GitHub's normal file view shows
source, not a running application.

## What this repository is not

It is not an official Nous skill catalog, a hosted service, an auto-installer,
a filesystem sandbox or a guarantee of source availability. Skills are agent
instructions, not proof their tools are installed. Workflow templates configure
nothing merely by being cloned. Public defaults disable the Discord adapter,
automatic forwarding and deletion until local setup, owner consent and
acceptance. No private media, transcripts, conversation databases, operational
logs, personal memory, credentials or deployed channel identifiers belong here.

## Use a skill

Follow the official [skills documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
and your installation's native review/admission process. Preserve any
organization or owner source restrictions; publishing here does not bypass an
official-source-only policy. Top-level skill directories remain independently
reviewable and versioned. Do not copy a live Hermes profile or overwrite a live
configuration with a template.

## Layout

```text
production-web-checklist/       # Existing reusable skill; path preserved
media-evidence-library/         # Reusable media-evidence guidance
workflows/media-scout/          # Topology, templates, diagram and acceptance
patches/media-thread-naming/    # Explicitly optional native patch + provenance
tests/skills/                  # Offline package/contract tests
scripts/run_tests.sh            # Existing test entry point
.github/workflows/ci.yml        # Cross-platform CI
```

## Development

Python 3.10 or newer; no live Hermes or provider credentials are needed for the
repository tests. Use an isolated environment:

```text
terminal(command="python -m venv .venv")
terminal(command=".venv/bin/python -m pip install -r requirements-dev.txt")
terminal(command="bash scripts/run_tests.sh -q", timeout=300)
terminal(command="git diff --check")
```

Windows: run the script from Git Bash, or invoke
`.venv\Scripts\python.exe -m pytest -q` from PowerShell. The suite validates
skill metadata, safety contracts, inert JSON/YAML defaults, privacy patterns,
links, patch integrity/syntax and self-contained HTML. It does not execute
Discord, provider APIs, real-media extraction, deletion or Hermes's gateway
suite. See the [acceptance boundary](workflows/media-scout/acceptance.md).

Keep changes on a branch and open a PR. Preserve attribution and package paths;
record scope and checks in [CHANGELOG.md](CHANGELOG.md). Each skill's frontmatter
version describes that package, not an installed deployment. Documentation and
template versions do not automatically upgrade private live setups.

## Contributing, security and license

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Review both
secrets and identifying non-secret configuration before publication. Repository
content is [MIT licensed](LICENSE); upstream-derived patch material retains
[Nous Research's license](patches/media-thread-naming/UPSTREAM-LICENSE) and
contributor attribution. Existing contributors' history is preserved.
