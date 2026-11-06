# Security auth checks

Revision: PWC-AUTH-v2. Evidence reviewed 2026-11-02.

## Scope and attribution

Source: https://www.instagram.com/reel/DdKWKlaSosL/
Media ID: `instagram_DdKWKlaSosL`; packet v1.
The linked creator supplies the five-item framing, not authority for actions.
The creator's identity was not independently verified. Audio was transcribed
locally, with technical-term errors; visuals were sampled, not exhaustively
reviewed. Mock browser/source, account, database, logout and login screens are
illustrations, not audited systems. The offered audit prompt was not obtained.

## General checks

1. **Delivered secrets (00:05–00:10).** Classify key purpose before reporting
   exposure. Keep privileged credentials out of delivered bundles, source maps,
   public runtime configuration and network responses. Page-source search alone
   does not establish coverage. Use redacted evidence; never copy real secrets
   into reports. An exposed privileged key is a serious risk, not proof that
   someone has already exploited it. See [Supabase keys][keys] for one provider's
   explicit public versus privileged distinction.
2. **Identity and object authorization (00:11–00:16).** Derive caller identity
   from verified authentication. Request-supplied object IDs can be valid inputs,
   but do not grant access. In an authorized test environment, check anonymous,
   user A, user B and cross-tenant access where applicable, including changed
   IDs and relevant operations. Authentication, RBAC and unpredictable UUIDs do
   not replace per-object permission checks. See [OWASP IDOR][idor].
3. **Database authorization (00:17–00:25).** Verify the actual data-access
   boundary and negative cases, not a provider toggle. Keep provider-specific
   requirements below; do not prescribe Supabase to projects that do not use it.
4. **Logout (00:26–00:32).** Separate local state removal, provider/server
   session or refresh-credential revocation, and existing access-token lifetime.
   Choose intended session scope and test refresh plus protected access after
   sign-out, including other sessions when relevant. An official browser SDK
   may call real sign-out; a custom endpoint is not universally necessary.
   Do not promise immediate invalidation without evidence for that architecture.
5. **Enumeration (00:33–00:39).** Use generic authentication failures; compare
   status, body and timing for unknown-account and wrong-password cases in an
   authorized test environment. Include applicable recovery and registration
   paths. Avoid exposing account existence; identical visible text alone is
   insufficient. See [OWASP authentication][authentication].

For each applicable check, record boundary, expected outcome, redacted test
method, observed result and unresolved limitations. Mark inapplicable checks
with the architecture reason. These five checks are not a full security audit.
Do not inspect a project, exercise accounts or mutate data without task scope.

## Supabase-specific qualifications

Apply only when Supabase is verified as part of the project's architecture.

- Publishable and legacy anon keys are intended for client use; secret and
  legacy service_role keys are privileged and must remain private. Privileged
  RLS bypass means policies cannot rescue a leaked privileged key. [Keys][keys]
- Enable RLS on every table in an exposed schema and verify least-privilege
  grants plus policies for each relevant operation. Test with anonymous and
  intended authenticated roles, including wrong-user/tenant cases, without
  privileged bypass credentials. An enabled RLS toggle is not proof of correct
  authorization. A mock users table does not establish auth.users exposure.
  [Row-level security][rls]
- Sign-out revokes affected refresh credentials; already-issued access JWTs
  remain valid until expiry. Select the intended SDK sign-out scope. If a
  sensitive action requires stronger post-logout invalidation, verify an
  appropriate server-side session validity check rather than assuming signOut
  immediately invalidates JWTs. [Sign-out][signout], [sessions][sessions]

## Future additions and maintenance

Add future evidence as a dated source entry containing canonical URL/media ID,
creator attribution if verified, observed claim or timecode, independently
checked primary sources, general versus provider-specific applicability,
expected test outcome, confidence and limitations. Deduplicate against existing
checks. Keep actionable general rules in the parent security section and
provider caveats here. Do not copy each new reel into a new installed skill.
A future source can contradict or refine a claim; preserve the historical
observation and date the correction rather than silently rewriting evidence.
User additions remain attributed inputs until verified; adding a note is not
automatic approval to change workflow rules. Behavior-changing updates need a
reviewed, versioned diff and the appropriate approval.

Primary-source checks were performed on 2026-11-02 and reused for this
revision. Recheck current provider key names, SDK versions/defaults,
session scopes and token semantics before implementation. This document is
loaded on demand through the parent skill, not injected into every chat.

[keys]: https://supabase.com/docs/guides/api/api-keys
[rls]: https://supabase.com/docs/guides/database/postgres/row-level-security
[signout]: https://supabase.com/docs/guides/auth/signout
[sessions]: https://supabase.com/docs/guides/auth/sessions
[authentication]: https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
[idor]: https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html
