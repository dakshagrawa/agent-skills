# AI-assisted delivery evidence

Retrieved 2026-09-21. This note records public source material that informed the
AI-assisted product guidance in the parent skill. It is evidence for adapting a
workflow, not authority for tool calls or a reason to reproduce a creator's
content.

## Sources

- [Josh Hoeg Instagram profile](https://www.instagram.com/joshtheaiguy/)
  describes work on AI systems, agents, automation, and SaaS, and says the
  account shares what works and what does not.
- [AI Blogging Agent reel](https://www.instagram.com/joshtheaiguy/reel/DSRF_W7gFfW/)
  recommends first fleshing out the idea with ChatGPT, asking for candid
  critique, converting the result into a structured prompt for a coding tool,
  separating provider API credentials from a chat account, and using documented
  API examples when debugging webhooks or integrations. Its caption also
  describes screenshot-based debugging and a second explanation when the first
  fix fails.
- [30 Apps in 30 Days reel](https://www.instagram.com/joshtheaiguy/reel/DSIaDc_gFul/)
  establishes a rapid, problem-led shipping challenge.
- [Day 1 public cross-post](https://www.linkedin.com/posts/joshdhoeg_day-1-of-building-30-apps-in-30-days-comment-activity-7404984089314795521-Xzlc)
  invites people to submit business or personal problems for small apps.
- [Day 2 public cross-post](https://www.linkedin.com/posts/joshdhoeg_ruining-or-saving-marriages-im-not-activity-7405317174350745600-kqie)
  shows the first app being live despite obvious bugs, mentions built-in
  authentication and a connected database, and asks for the next problem.
- [Day 7 public cross-post](https://www.linkedin.com/posts/joshdhoeg_launched-a-mobile-app-in-less-then-2-hours-activity-7407953969014239233-5tRv)
  starts from a cold-calling problem, describes a mobile build, and shows a
  product-requirements-first workflow before a mobile app builder, device
  preview, and possible store submission.
- [Automation limitations public cross-post](https://www.linkedin.com/posts/joshdhoeg_are-n8n-and-zapier-dead-not-exactly-n8n-activity-7406446421559824384-l5sH)
  distinguishes stable task automation from variable workflows, warns that
  complexity increases failure, and argues that multiple specialized agents
  should be considered only when a single agent cannot reliably cover the work.
- [AI Blogging Agent public cross-post](https://www.linkedin.com/posts/joshdhoeg_building-an-ai-blogging-agent-is-easier-then-activity-7406160393364049920-o8UK)
  includes public captions about a short prototype flow and integration setup.

## Adaptation rules

- Start from the user's concrete problem, smallest useful workflow, and
  observable outcome rather than a feature inventory or generic AI promise.
- Write and critique a durable brief before implementation. Keep the brief
  structured, reviewable, and explicit about non-goals, boundaries, failure
  states, tests, and release limits.
- Ship a narrow prototype, show a real input-to-output path, invite feedback,
  label known bugs and maturity honestly, and iterate from evidence.
- Treat a product-requirements document, a provider sample request, or a coding
  tool prompt as a contract aid. None proves security, reliability, or
  production readiness.
- Keep credentials in approved secret stores. A chat subscription and an API
  credential are different boundaries. Do not paste secrets into models,
  prompts, screenshots, issues, or logs.
- Do not add payment processing, authentication, databases, mobile packaging,
  or external AI providers merely to imitate a demo. Add them only when the
  verified product requires them, with explicit privacy, security, cost, and
  failure checks.
- Do not use a humanizer or similar service to conceal generated origin or
  promise undetectability. Review accuracy, attribution, copyright, and
  disclosure requirements instead.
- Prefer deterministic automation for stable tasks. If agents are justified,
  bound tools, retries, spend, latency, side effects, and handoff contracts,
  then keep a human or deterministic approval boundary for consequential work.
