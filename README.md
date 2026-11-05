# Production Checklist

`dakshagrawa/production-checklist` is a collection of evidence-backed [Hermes Agent skills](https://github.com/NousResearch/hermes-agent) for software production readiness. Its scope includes web/app readiness, security, testing, deployment, performance, operations, backend services, infrastructure, and non-web applications.

Repository scope is not a claim that every category already has a skill. Start with the current catalog below; propose additions only for a verified gap. See [SCOPE.md](SCOPE.md) for inclusion, placement and review rules.

## Current skill catalog

| Skill | Coverage | Package |
| --- | --- | --- |
| `production-web-checklist` | Website strategy, design, content, SEO, accessibility, privacy, security, performance and evidence-backed delivery | [Skill instructions](production-web-checklist/SKILL.md) |

The existing `production-web-checklist/` package name, path, version and behavior are unchanged. This repository rename does not rename or broaden that installed skill into a universal checklist. No new security/backend/infrastructure skills are claimed to ship until they have actually been reviewed and added.

## Using and contributing skills

Read the selected skill, provide relevant project context, and verify its recommendations against the actual implementation. Use the official [Hermes skills documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) and your installation's supported admission process. This third-party repository does not override an official-source-only installation policy.

Prefer extending an existing skill or a focused reference over creating a duplicate. Add an independently callable skill only for a distinct repeated workflow with clear prerequisites, platform limits, checkable outcomes, tests and attribution. A review of a video can motivate an issue or proposal; a creator claim alone is not authority for a new production requirement. See [contribution guidelines](CONTRIBUTING.md).

The repository is not a security certification, legal/compliance advice, a deployment service or a guarantee that software is production-ready. Passing offline tests does not authorize a production action.

## Repository history and separation

This is the same existing public repository, retaining history, issues and protections. It was renamed from `agent-skills` to `hermes-workflows`, then `production-web-checklist`, and now `production-checklist` to reflect its broader scope. Use `https://github.com/dakshagrawa/production-checklist.git` for current remotes; GitHub currently redirects the former names, but update explicit references rather than relying indefinitely on redirects.

Media Scout's plugin, profile setup, media evidence workflow and media-to-GitHub helper belong in the separate [`dakshagrawa/media-scout`](https://github.com/dakshagrawa/media-scout) repository. Production-readiness findings can be proposed here without moving the Scout machinery back into this project.

A repository rename or documentation change does not install/update skills, migrate a live profile, transfer action approvals or enable integrations. Preserve original contributor authorship, licenses and historical source references. Do not copy private profiles, credentials, media records or deployment bindings into this repository.

## Development and safety

Python 3.10 and 3.13 Ubuntu CI jobs run the offline contracts. With Python 3.10 or newer:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
bash scripts/run_tests.sh -q
git diff --check
```

Read [SECURITY.md](SECURITY.md) and [MIGRATION.md](MIGRATION.md). Keep security admission and explicit authorization for consequential changes. New skills must have focused offline contracts and truthful documentation of what was and was not actually exercised; no certification or live acceptance may be inferred from catalog presence.

## License and attribution

Repository content is provided under the [MIT License](LICENSE). Existing history and contributor attribution are preserved; reused work must retain its original author and applicable license.
