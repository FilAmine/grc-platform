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
- **Rate limiting, security headers, dependency/SAST scanning**: Redis-backed
  rate limits on the unauthenticated auth endpoints, CSP/HSTS/X-Frame-Options
  etc. at the application (API) and nginx (SPA) levels, and `pip-audit`/
  `npm audit`/CodeQL wired into CI — see `docs/security.md` for thresholds,
  the fail-open/circuit-breaker design, CSP specifics, and which advisories
  are deliberately ignored and why.
- **Departments, threats, vulnerabilities**: a self-referential department
  hierarchy under an organization, a threat catalog, and a vulnerability
  register — each a standalone catalog/register module (list+create,
  tenant-scoped) matching how Risks/Assets work, not yet cross-linked to the
  risk register (that wiring is the separate EBIOS RM item below). See
  `docs/api.md` for the endpoints.
- **Incident management**: a standalone `Incident` entity with a real
  status workflow (`open` → `investigating` → `resolved` → `closed`, plus a
  `reopen` path) validated server-side by the same `StateMachine` the Audits
  module uses — illegal transitions 409. Not yet cross-linked to
  assets/threats/vulnerabilities (same "standalone first" reasoning as
  Departments/Threats/Vulnerabilities above). See `docs/api.md` for the
  endpoints.
- **EBIOS-RM-flavored risk linking**: `Risk` gained 4 optional,
  cross-tenant-validated FK fields — `asset_id`, `threat_id`,
  `vulnerability_id`, `feared_event_id` — plus a new standalone `FearedEvent`
  catalog (`asset_id` required, `criterion` = which CIA property is
  impacted, `gravity`). This is the structural linking
  `docs/roadmap.md` previously called out as missing ("asset-value /
  threat-source / feared-events structure"), **not** the full 5-workshop
  ANSSI EBIOS RM methodology: no risk-source/target-objective (SR/OV)
  pairing, no strategic/operational attack-path scenarios, no
  MITRE-ATT&CK-style technique modeling, no risk-treatment workflow. EBIOS
  RM's "business value" and "supporting asset" tiers are also deliberately
  conflated into the existing CMDB `Asset` — a stated simplification, not an
  oversight. Risk still has no `GET/{id}`, detail page, or update endpoint,
  so these links are settable at creation only; editing them later needs a
  future Risk detail page + `PATCH /risks/{id}`. See `docs/api.md` for the
  endpoints.
- **Tenant entity + generic Task module**: a real `Tenant` entity now exists
  above `Organization` (a nullable `organizations.tenant_id`), letting a
  platform operator group several existing orgs under one record. This does
  not touch the tenant-isolation boundary — `organization_id` is unaffected,
  and every existing module's scoping/RBAC/JWT-claim behavior is exactly as
  before. Note the resulting terminology overload, stated plainly rather
  than hidden: "tenant" now means two different things in this codebase —
  see `docs/database.md`'s `## Conventions` for the full disambiguation.
  `Tenant` has no frontend page (Organization management itself has none
  either — both are invisible, superuser-only backend concerns) and no RBAC
  permission codes (gated by a raw `is_superuser` check instead,
  deliberately, so the capability can never become delegable to a per-org
  role). Also added: a standalone, `StateMachine`-gated `Task` module
  (`open` → `in_progress` → `done`, plus `reopen`) — generic, not tied to
  any one module, unlike audit-scoped `corrective_actions`/`checklist_items`.
  See `docs/api.md` for the endpoints.
- **Vite major-version upgrade**: bumped to `vite@8.1.4` +
  `@vitejs/plugin-react@6.0.3`, fixing the `npm audit`-flagged `vite`/`esbuild`
  dev-tool advisories. Root cause of the previous failed attempt (see prior
  "Not done" text, now obsolete): `@mui/icons-material`'s `package.json` has
  no `exports` map, so a deep default import
  (`import Icon from '@mui/icons-material/X'`) resolves by plain file
  resolution straight to the package's **CJS** build
  (`@mui/icons-material/X.js`, `exports.default = ...`). Vite 8's bundler
  (Rolldown) fails to unwrap that CJS `.default` correctly for this import
  shape, so the imported binding is the whole CJS exports object instead of
  the component — every nav/page icon rendered as React's "type is invalid"
  crash. Fix: switched every icon import in the 21 affected files (51
  imports total) from the deep default form to a named import off the
  package barrel (`import { X as XIcon } from '@mui/icons-material'`), which
  resolves via the package's `module`/`types` fields to genuinely-ESM
  sources — no CJS interop involved. `sideEffects: false` in that package's
  `package.json` keeps this tree-shakeable, so the production bundle isn't
  pulling in the full ~2,000-icon set. Separately, `vite@8`/
  `@vitejs/plugin-react@6` also ship exports-only `package.json`s with no
  top-level `types` field, which TypeScript's legacy `moduleResolution:
  "Node"` can't resolve at all (it ignores the `exports` map entirely) —
  this only surfaced in CI, not locally, because a stale `.tsbuildinfo`
  incremental-build cache (gitignored, left over from before the bump) let
  local `tsc -b` skip re-validating `vite.config.ts` against the new
  package's types. Fixed by switching `moduleResolution` to `"Bundler"` in
  both `tsconfig.json` and `tsconfig.node.json` — the setting Vite projects
  are meant to use anyway. Verified via `tsc -b` (after deleting the stale
  `.tsbuildinfo` files to force a true from-scratch check), `npm run
  build`, and a live-browser console check (zero errors, including on the
  unauthenticated `/login` route, which is enough to exercise every
  statically-imported page/icon per `App.tsx`'s non-lazy imports).
- **Celery**: a real worker + beat process now exist (`celery-worker`/
  `celery-beat` in `docker-compose.yml`, both reusing the `backend` image
  with a different `command:`, sharing an `x-backend-env` anchor with
  `backend` to avoid tripling the environment block). One real scheduled
  task — `recompute_all_compliance_scores`
  (`backend/app/core/tasks.py`), nightly via Celery Beat
  (`crontab(hour=2, minute=0)` UTC), recomputing every `IN_PROGRESS`
  assessment's score across every organization. Deliberately scoped to
  `IN_PROGRESS` only — `COMPLETED` is meant to be a locked/final state
  (the state machine's explicit `reopen` transition signals this), so a
  scheduled recompute doesn't silently rewrite a "final" score. The other
  two candidate uses (async document/evidence file processing, scheduled
  notification digests) are still not built — no real upload pipeline or
  digest concept to hook into yet. `celery-worker`/`celery-beat`'s
  `depends_on: backend` is a best-effort ordering hint only, not a
  guarantee (`backend` has no healthcheck, so it just means "container
  started," not "migrations finished") — a real fix would need a
  healthcheck on `backend` or a separate migration-completion signal, not
  attempted here.

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
- **FastAPI/starlette major-version upgrade.** `pip-audit` (wired into CI, see
  `docs/security.md`) flags several `starlette` advisories only fixed in
  `starlette>=1.0.1`, which needs a FastAPI version many minors ahead of the
  `0.111.0` pinned here. Deliberately not bundled into the dependency-scanning
  CI work — it's a real upgrade with its own regression risk across every
  endpoint and DI-based dependency in this codebase, and deserves its own pass
  (bump, then re-run the full test suite plus a live-browser check of the
  docs/SSO/rate-limiting paths that touch middleware most directly).
- **Kubernetes/Helm/Terraform.** See `docs/deployment.md`.
- **Full EBIOS RM methodology.** The structural linking (asset/threat/
  vulnerability/feared-event) is done — see "Done" above — but the full
  5-workshop ANSSI methodology (risk-source/target-objective pairing,
  strategic/operational attack-path scenarios, MITRE-ATT&CK-style technique
  modeling, risk-treatment workflow) is not attempted and would be its own
  multi-week effort if ever pursued.

## Suggested next milestone

Frontend module coverage is complete (every backend module has a page), the
public-domain framework catalogs (NIST CSF, HIPAA, NIS2, DORA) are loaded, and
SSO (OIDC), rate limiting/security headers/dependency scanning,
departments/threats/vulnerabilities, incident management, EBIOS-RM-flavored
risk linking, the Tenant/Task modules, and a real Celery worker are all in.
The Vite major-version upgrade is now done too. What's left on this list is
either intentionally out of reach (licensed standards text — needs a
license, not a code change) or lower-priority infrastructure work (the
FastAPI/starlette upgrade, Kubernetes/Terraform, the full 5-workshop EBIOS
RM methodology). None of it blocks day-to-day use of what's already built;
pick based on which specific gap actually matters for your next deployment
target.
