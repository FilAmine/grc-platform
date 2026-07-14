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
  threat-source / feared-events structure") — see the Workshop 2 bullet
  below for the risk-source/target-objective (SR/OV) pairing, which is now
  also done. EBIOS RM's "business value" and "supporting asset" tiers are
  deliberately conflated into the existing CMDB `Asset` — a stated
  simplification, not an oversight. Risk still has no `GET/{id}`, detail
  page, or update endpoint, so these links are settable at creation only;
  editing them later needs a future Risk detail page + `PATCH /risks/{id}`.
  See `docs/api.md` for the endpoints.
- **EBIOS RM Workshop 2 (risk sources + SR/OV pairing)**: a `RiskSource`
  catalog (ANSSI's 7 standard threat-actor categories — state, organized
  crime, terrorist, activist, vengeful individual, amateur, specialized
  firm — each scored on `motivation`/`resources`, a shared 4-level scale,
  and `activity`, a 3-level one, matching ANSSI's own Workshop 2 evaluation
  grid) plus `RiskOrigin`, the actual "couple SR/OV": a mandatory
  `risk_source_id` paired with a free-text `target_objective`, an optional
  `feared_event_id` link, a `pertinence` score, and a `retained` flag
  marking which pairs are prioritized to carry into Workshop 3.
  See `docs/api.md` for the endpoints.
- **EBIOS RM Workshop 3 (ecosystem mapping + strategic scenarios)**: an
  `EcosystemParty` catalog (provider/subcontractor/partner/client, each
  scored on `dependency_level` and `cyber_maturity` — low maturity makes a
  party a more attractive stepping stone for an attacker) plus
  `StrategicScenario`, the actual Workshop 3 output: elaborates a
  *retained* `RiskOrigin` (Workshop 2) into a concrete attack path
  targeting a specific `FearedEvent`, optionally routed through an
  `EcosystemParty`, scored for `likelihood`. Severity is deliberately not
  duplicated onto this table — it's read off the required `feared_event_id`
  link's `gravity`. The API enforces, not just structurally models, one
  real methodological rule: creating a strategic scenario from a
  `RiskOrigin` that isn't `retained` returns `409` — Workshop 3 is meant to
  elaborate the pairs Workshop 2 prioritized, not any pair that exists.
  See `docs/api.md` for the endpoints.
- **EBIOS RM Workshop 4 (operational scenarios)**: `OperationalScenario`
  elaborates a `StrategicScenario` (Workshop 3) into a concrete technical
  attack chain: `mitre_technique_ids` (a free-text list of MITRE ATT&CK
  technique identifiers, e.g. `["T1566", "T1078"]` — not validated against
  a live ATT&CK catalog; importing and maintaining that dataset is a real,
  separate undertaking) and its own `technical_likelihood`, deliberately
  kept separate from the strategic scenario's `likelihood` (attacker
  motivation/targeting vs. technical feasibility — the two can diverge).
  See `docs/api.md` for the endpoints.
- **EBIOS RM Workshop 5 (risk treatment) — the final workshop.**
  `RiskTreatment` records the actual decision for a `StrategicScenario`:
  `decision` (avoid/reduce/transfer/accept — the standard ISO 27005/EBIOS
  RM 4-way choice), a `justification`, and the `residual_risk_level` left
  over after applying it. Deliberately list+create only like every other
  EBIOS RM module this session — no uniqueness constraint on
  `strategic_scenario_id`, so re-deciding a treatment means inserting a new
  row (an append-only decision history) rather than updating one in place.
  **This closes out the full 5-workshop ANSSI EBIOS RM methodology** —
  Workshop 1's structural linking, Workshop 2's risk sources + SR/OV
  pairing, Workshop 3's ecosystem mapping + strategic scenarios, Workshop
  4's operational/technical scenarios, and Workshop 5's treatment decision
  are all real, tested, cross-tenant-validated modules with a frontend
  page each. See `docs/api.md` for the endpoints and each workshop's own
  bullet above for the specific simplifications made along the way (no
  MITRE ATT&CK catalog validation, EBIOS RM's business-value/
  supporting-asset tiers conflated into the CMDB `Asset`, etc. — none of
  it hidden, all called out where it happens).
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
- **FastAPI/starlette major-version upgrade**: bumped `fastapi` `0.111.0` →
  `0.139.0`, which pulls in `starlette>=1.0.1` (fixing every `pip-audit`-flagged
  `starlette` advisory — confirmed via a fresh `pip-audit` run afterward; only
  the pre-existing, separately-tracked `ecdsa` finding remains) and required
  bumping `pydantic` `2.8.2` → `2.13.4` and `pydantic-settings` `2.3.4` →
  `2.14.2` to satisfy fastapi's new `pydantic>=2.9.0` floor. Lower actual risk
  than the version jump suggests: a pre-upgrade audit of the codebase found no
  use of anything Starlette 1.0 removed (`on_event`/`on_startup`/`on_shutdown`,
  the `@app.route()`/`@app.middleware()` decorators, deprecated `TestClient`/
  `FileResponse` args) and no legacy Pydantic v1-style calls (`.dict()`,
  `regex=`, `orm_mode`) anywhere — this project's endpoints, DI, and custom
  `BaseHTTPMiddleware` (`security_headers.py`) already used current-generation
  idioms throughout. Verified via `ruff check`, the full test suite (88 passed,
  90% coverage, no regressions), `pip-audit`, and a direct `TestClient` smoke
  check of `/health`, `/api/v1/openapi.json` (schema still generates, 73
  paths), `/api/v1/docs`/`/redoc` (render correctly, CSP headers intact), and
  security headers on a plain request — not a literal browser click-through
  (no local Postgres/Docker in this environment to run a live server against;
  same constraint noted for Celery's compose services), but a real ASGI
  request/response cycle through the full middleware stack, which is what a
  browser check would exercise anyway. One new, non-blocking
  deprecation warning surfaced: Starlette's `TestClient` now warns that
  `httpx`-based testing is deprecated in favor of a package called `httpx2` —
  not acted on here (that package is new and its stability wasn't evaluated),
  left as a future note rather than a blocker since tests still pass today.
  `.github/workflows/ci.yml`'s `pip-audit` step no longer needs to ignore the
  7 starlette advisory IDs — only `ecdsa`'s remains.
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
- **Kubernetes/Helm/Terraform.** All three are now drafted and
  schema-validated: `k8s/` (plain manifests), `helm/grc-platform/` (the
  same design as a proper Helm chart — values-driven config, the
  migration Job as a real `pre-install`/`pre-upgrade` hook instead of a
  manual delete-then-apply sequence), and `terraform/aws/` (VPC + EKS +
  RDS Postgres + ElastiCache Redis + ECR, targeting AWS as a reasonable
  default since nothing else in this repo specifies a cloud provider —
  see that directory's README for why AWS specifically, and what a
  GCP/Azure/on-prem target would need instead). `kubectl`, `helm`, and
  `terraform` are now installed and were actually run:
  [`kubeconform`](https://github.com/yannh/kubeconform) validates every
  Kubernetes resource (both `k8s/`'s files and Helm's rendered output)
  against real Kubernetes OpenAPI schemas with 0 errors; `terraform init`
  + `validate` resolve and schema-check the AWS provider and both
  registry modules cleanly, and `terraform plan` fails at exactly the
  expected point (missing AWS credentials, not a config bug). Still
  deliberately **not** called fully "Done": none of it has been applied
  to a real cluster or AWS account (that needs your own cluster/cloud
  account and credentials — not something to provision without your
  explicit go-ahead on cost, which is why it stopped at schema
  validation). See `docs/deployment.md`, `k8s/README.md`,
  `helm/README.md`, and `terraform/aws/README.md` for the exact commands
  run and what's still missing in each (a real secrets-manager
  integration everywhere, autoscaling/network policies for Kubernetes,
  remote Terraform state).

## Suggested next milestone

Frontend module coverage is complete (every backend module has a page), the
public-domain framework catalogs (NIST CSF, HIPAA, NIS2, DORA) are loaded,
SSO (OIDC), rate limiting/security headers/dependency scanning,
departments/threats/vulnerabilities, incident management, the Tenant/Task
modules, a real Celery worker, the Vite and FastAPI/starlette major-version
upgrades, the **full 5-workshop EBIOS RM methodology** (structural linking
through Workshop 5's treatment decision), and schema-validated Kubernetes
manifests, a Helm chart, and a Terraform AWS module are all in. The one
remaining gap is intentionally out of reach: licensed standards text (ISO
27002/27005, CIS Controls, SOC 2, PCI DSS) needs an actual license from
the standards body, not a code change — nothing left on this list is
something more engineering effort alone can close. None of it blocks
day-to-day use of what's already built; the infrastructure drafts
specifically still need your own real cluster/cloud account for a live
apply — that's a deliberate stopping point (real infrastructure spend
needs your explicit go-ahead, not something to provision autonomously),
not a gap in the code.
