# Production Web Checklist

`dakshagrawa/production-web-checklist` is the public home of one focused, reusable [Hermes Agent skill](https://github.com/NousResearch/hermes-agent) for planning, building, reviewing, and preparing websites for release.

## Use the skill

Read [`production-web-checklist/SKILL.md`](production-web-checklist/SKILL.md), provide relevant project context, and verify its recommendations against the implementation. It covers strategy, design, content, SEO, accessibility, privacy, security, performance, and evidence-backed delivery. It is not legal advice, a security certification, a website generator, or a guarantee of search performance.

Install and review it using the official [Hermes skills documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills) and your installation's native process. The top-level `production-web-checklist/` package path is intentionally preserved.

## Repository history and project split

This repository retains the original public repository's history and existing issues/protection; it was renamed from `hermes-workflows` to `production-web-checklist`. The source project was `dakshagrawa/hermes-workflows` (formerly `dakshagrawa/agent-skills`), where this skill lived alongside a separate Media Scout project. Media Scout and its supporting assets now live in [`dakshagrawa/media-scout`](https://github.com/dakshagrawa/media-scout). The split does not replace this repository or its history.

The Media Scout repository's filtered Git history necessarily has different commit IDs; that is a history-filtering consequence, not replaced authorship. Original author and date attribution is preserved there, and its required package tags are retained for upgrade tests. Historical entries below describe what happened in the source project and are labelled accordingly; they do not imply those components remain here.

Neither repository publication nor a renamed slug automatically migrates, updates, or enables any installed skill or deployment. Review and update your own references explicitly. Do not copy live profiles, credentials, private data, or deployed configuration.

## Development and safety

Python 3.10 and 3.13 Ubuntu CI jobs run the repository checks. Run locally with Python 3.10 or newer:

```bash
python -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
bash scripts/run_tests.sh -q
git diff --check
```

Tests are offline contracts, not proof that a user's environment or website is safe. Read [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [MIGRATION.md](MIGRATION.md) before contributing or changing references. Keep native security admission boundaries and explicit user consent for consequential actions; public instructions do not authorize external side effects.

## License and attribution

Repository content is provided under the [MIT License](LICENSE). Existing history and contributor attribution are preserved.
