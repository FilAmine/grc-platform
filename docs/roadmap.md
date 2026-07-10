# Roadmap

An honest accounting against the original spec, so nobody has to re-derive what's
real by reading every module. "Done" means: real persistence, a tested API, and
(where applicable) a UI — not just a stub file.

## Done

- **Multi-tenant foundation**: JWT auth, Argon2 password hashing, rotating
  refresh tokens, account lockout, full RBAC (system + custom roles,
  permission-code based), tenant isolation enforced server-side and covered by
  cross-tenant isolation tests.
- **Generic compliance engine**: Framework/FrameworkVersion/Requirement/
  ControlCategory/ControlMapping/Assessment/AssessmentResult/Evidence/
  ComplianceScore — genuinely framework-agnostic, seeded with the standards
  named in the spec as catalog entries, with real requirement text loaded for
  the public-domain ones (NIST CSF, HIPAA, NIS2, DORA) and an illustrative
  ISO 27001 sample (see `docs/database.md` for exactly which frameworks have
  real requirement text vs. catalog-only entries, and why).
- **Risk register, controls, audits** (planning/checklists/findings/corrective
  actions/report), **documents** (versioning + approval workflow, e-signature
  slot but no provider), **assets/CMDB** (CIA classification, lifecycle stages),
  **ai** (provider abstraction, RAG-lite knowledge base, chat, prompt library),
  **notifications** (one real trigger: document approval decisions).
- **Workflow engine**: a real, reusable `StateMachine` validating status
  transitions, used by audits/assessments/documents.
- **Frontend**: auth flow (register/login/refresh/logout) end-to-end, protected
  routing, and a page for every module — Dashboard, Risks, Controls, Audits,
  Documents, Assets/CMDB, Compliance assessments, RBAC admin (users/roles), AI
  chat (with prompt library and knowledge-base seeding), and a notifications
  inbox.
- **CI**: lint (ruff, 0 errors), test (pytest, 89% coverage, `--cov-fail-under=80`
  gate), migrations exercised against a real Postgres service container,
  frontend typecheck + build, Docker image builds — all on every push/PR.
- **SSO (OIDC)**: per-organization connections (an org optionally connects its
  own Azure AD/Okta/Google Workspace/any OIDC IdP), standard
  authorization-code flow with JWKS-verified `id_token`s, just-in-time user
  provisioning with an optional default role, and an admin settings page to
  configure it — see `docs/security.md`'s SSO/OIDC section for the full design
  and its known limitations (OIDC only, no SAML/LDAP; `client_secret` stored
  in plaintext).

## Not done — biggest gaps first

- **Framework requirement catalogs are only loaded for the public-domain
  frameworks.** NIST CSF 2.0 (14 requirements), the HIPAA Security Rule (13),
  NIS2 (6), and DORA (5) have real requirement text — those sources are US
  federal government works or EU legislation, freely reproducible/paraphrasable.
  ISO 27001 still only has 4 illustrative Annex A entries as a worked example,
  and ISO 27002/27005, CIS Controls, SOC 2, and PCI DSS have zero requirement
  rows: those are commercially licensed standards this project has no rights
  to reproduce, even paraphrased, without a license from ISO/PCI SSC/AICPA/CIS.
  See `docs/database.md` for the full rationale and the migration to extend if
  a license is ever obtained.
- **Departments, tenants-as-distinct-from-organizations, threats,
  vulnerabilities, incidents, generic tasks-as-a-module.** The spec's module list
  names these separately; this build treats `organizations` as the tenant root
  (no separate `tenants` entity), doesn't yet have a `departments` hierarchy
  under an org, and the risk register doesn't yet have separate Threat/
  Vulnerability catalog entities (EBIOS RM readiness) or an incident-management
  module. `corrective_actions`/`checklist_items` cover audit-scoped follow-up
  items but there's no cross-module generic "Task" entity yet.
- **Celery.** Declared as a dependency; no worker process, no task, no
  `docker-compose.yml` service for it. Candidate real uses once needed:
  recomputing compliance scores on a schedule, async document/evidence file
  processing, scheduled notification digests.
- **Dependency/SAST scanning in CI** (e.g. `pip-audit`, `npm audit`, CodeQL) —
  `ruff` covers style/some correctness issues but not vulnerability scanning.
  Rate limiting and security headers middleware are done; see
  `docs/security.md`.
- **Kubernetes/Helm/Terraform.** See `docs/deployment.md`.
- **EBIOS RM.** Named in the spec as "prepare for"; the current risk model
  (severity/status/owner) doesn't yet have the asset-value / threat-source /
  feared-events structure EBIOS RM assessments need.

## Suggested next milestone

Frontend module coverage is complete (every backend module has a page), the
public-domain framework catalogs (NIST CSF, HIPAA, NIS2, DORA) are loaded, and
SSO (OIDC) is in. What's left on this list is either intentionally out of
reach (licensed standards text — needs a license, not a code change) or
lower-priority infrastructure work (Celery, rate limiting, security headers,
dependency/SAST scanning, Kubernetes/Terraform, EBIOS RM, the
departments/threats/vulnerabilities/incidents module gaps). None of it blocks
day-to-day use of what's already built; pick based on which specific gap
actually matters for your next deployment target.
