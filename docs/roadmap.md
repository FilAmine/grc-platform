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
  ComplianceScore — genuinely framework-agnostic, seeded with the standards named
  in the spec as catalog entries (see `docs/database.md` for exactly which
  requirement text is real vs. a placeholder catalog row).
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

## Not done — biggest gaps first

- **SSO / enterprise identity.** No LDAP, Azure AD, OIDC, or OAuth2 integration.
  No MFA. The auth module's structure (a pluggable provider behind a narrow
  interface, as done for AI providers) would extend naturally to this, but
  nothing is wired.
- **Full framework requirement catalogs.** Only 4 illustrative ISO 27001:2022
  requirements are loaded; the other 9 seeded frameworks have no requirement rows
  yet. This is a data-loading task (and for PCI DSS/HIPAA, involves
  licensed/restricted source text), not a code change — the engine itself is
  generic and tested.
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
- **Rate limiting, security headers middleware, dependency/SAST scanning in
  CI.** See `docs/security.md` for the full list.
- **Kubernetes/Helm/Terraform.** See `docs/deployment.md`.
- **EBIOS RM.** Named in the spec as "prepare for"; the current risk model
  (severity/status/owner) doesn't yet have the asset-value / threat-source /
  feared-events structure EBIOS RM assessments need.

## Suggested next milestone

Frontend module coverage is now complete (every backend module has a page).
The highest-leverage next steps are backend-side: loading full framework
requirement catalogs beyond the 4 illustrative ISO 27001:2022 rows, and SSO /
enterprise identity, both listed above.
