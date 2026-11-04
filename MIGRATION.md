# Repository split and compatibility

This repository retains the existing Git history, issues, and protection of the source public repository. Its GitHub slug is now `dakshagrawa/production-web-checklist`; the one existing skill remains at `production-web-checklist/SKILL.md`. Update explicit remotes and bookmarks to `https://github.com/dakshagrawa/production-web-checklist.git` when updating a legacy checkout.

The source repository was `dakshagrawa/hermes-workflows` (formerly `dakshagrawa/agent-skills`). The separate Media Scout plugin and supporting assets now live in [dakshagrawa/media-scout](https://github.com/dakshagrawa/media-scout). Its filtered history has different commit IDs by design; original author/date attribution is retained. This repository's history is not filtered or replaced.

No installed skill, profile, live configuration, channel credential, or private data is migrated or automatically updated by the repository split or slug rename. A repository/package version is not a deployed policy version. Review your deployment and perform any desired updates through Hermes's supported native processes; do not copy private data or assume old Media Scout workflows auto-migrate.
