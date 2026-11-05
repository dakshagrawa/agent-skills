# Repository scope and contribution placement

## Purpose

Maintain reusable, evidence-backed Hermes instructions for bringing software into production and operating it responsibly. Scope covers both web/app production readiness and the broader software lifecycle, including backend, infrastructure and non-web apps. Applicability must be explicit: a website checklist is not automatically appropriate for a CLI, native application, service or embedded product.

## In scope

- **Web and apps:** accessibility, real user flows, browser/runtime verification, mobile/native platform considerations, delivery and truthful product readiness.
- **Security and privacy:** threat modeling, authorization boundaries, dependency/supply-chain review, secrets handling and evidence-backed security checks. No promise of certification.
- **Testing and release qualification:** unit/integration/end-to-end acceptance, regression coverage, supported-platform checks and human gates where needed.
- **Deployment and change safety:** environment configuration, release gates, migrations, compatibility, deprecation, rollback plans and verification of the actual deployed artifact.
- **Performance and reliability:** measurement, profiling, resource/cost trade-offs, capacity, resilience and explicit success thresholds rather than unsupported optimization claims.
- **Operations:** logs/metrics/traces, SLOs, incident response, runbooks, backups, restore drills and ownership.
- **Backend and data systems:** API contracts, background work, concurrency/idempotency, storage, data lifecycle and safe schema changes.
- **Infrastructure:** reproducible configuration, networking, runtime/service supervision and access controls, with provider/platform limits and no invented deployment commands.
- **Non-web applications:** desktop/native/mobile apps, command-line tools and other software products with their own packaging, updates, permissions, offline and platform-specific acceptance requirements.

These are allowed subject areas, not shipped skills or an obligation to implement every category now.

## Decide where a change belongs

1. Inspect current skill contents, references, tests and open/closed issues/PRs. State the actual gap and the affected software/workflow; do not infer a gap from a missing category name.
2. **Extend the current skill** when a change belongs to its existing trigger and output contract. Keep `production-web-checklist` web-focused and preserve its package identity.
3. **Add a reference/template** for optional detail, citations or a repeated output format that would bloat the main instructions. Link it from the skill; do not accumulate per-video transcripts as standing rules.
4. **Add a separate skill** only for a distinct, reusable, independently callable workflow. Use `<skill-name>/SKILL.md` at the top level, a concise description and complete metadata, prerequisites, scope, procedure, pitfalls, verification and focused tests. Do not create empty category directories or speculative catalog rows.
5. **Open/update an issue** for unresolved research, uncertain scope or unimplemented proposals. Distinguish source observations, creator claims and independently supported requirements. Include rationale, exact proposed add-ons/placement, non-goals, risks and checkable acceptance criteria.
6. **No change** is valid when coverage already exists, evidence is weak, or a proposed practice is irrelevant or harmful. Link relevant upstream work instead of copying an entire installed skill catalog.

For reused work, retain original authorship and licensing; explain substantive adaptations. A local skill's existence is not permission to republish private content or silently relabel another author's work. Maintain a real catalog in the README and update it only when a skill actually exists.

## Out of scope

- Media Scout's bot/plugin/profile instructions, extraction machinery, review routing and generic media-to-GitHub helper: maintain them in `dakshagrawa/media-scout`.
- Unrelated productivity or social-media skills with no concrete software production-readiness purpose.
- Private profiles, credentials, raw submitted media/transcripts, conversations, approval receipts, machine-specific paths or identifying deployment configuration.
- A new custom runtime, deployment service, code generator or executable infrastructure simply to house instructions. Tool/dependency additions require separately reviewed scope; repository expansion is not a grant to install or run them.

## Review and authorization boundaries

Read-only investigation and drafting are separate from public issue/PR writes. Show the proposed public payload, preserve source attribution and privacy, and obtain the action-specific authorization required by the owner's workflow. Publishing instructions is not permission to install them, mutate production, change permissions, merge, deploy or purchase services. Keep native scanners and host approval gates intact.

Run focused and full offline contracts, verify supported platform assumptions, and document unexercised live behavior. Do not equate a passing checklist, green CI or a catalog entry with safe production deployment. Keep Media Scout and the original web skill independently understandable.
