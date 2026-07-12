# API

Base path: `/api/v1`. Interactive OpenAPI docs (Swagger) at `/api/v1/docs`,
ReDoc at `/api/v1/redoc`, raw schema at `/api/v1/openapi.json`.

All endpoints except `/health`, `/auth/register-organization`, `/auth/login`,
and the two SSO redirect endpoints (`/auth/sso/{organization_slug}/login`,
`/auth/sso/callback` — there's no bearer token to send yet at that point in the
flow) require a `Bearer` access token (`Authorization: Bearer <token>`) and are
scoped to the caller's organization server-side — none of them accept a
client-supplied tenant ID. Most also require a specific RBAC permission code
(see `docs/security.md`); the OpenAPI docs show each endpoint's requirement.

## Auth

| Method | Path | Notes |
|---|---|---|
| POST | `/auth/register-organization` | Creates an organization + its Admin user atomically; returns tokens |
| POST | `/auth/login` | OAuth2 password form (`username`=email, `password`) |
| POST | `/auth/refresh` | Rotates the refresh token, returns a new pair |
| POST | `/auth/logout` | Revokes a refresh token |
| GET | `/auth/me` | Current user |
| GET | `/auth/sso/{organization_slug}/login` | Unauthenticated. 307-redirects to the org's configured IdP, or 404 if none is configured/enabled, or 502 if the IdP is unreachable |
| GET | `/auth/sso/callback` | Unauthenticated. Exchanges the authorization code, then 307-redirects to `{frontend_base_url}/sso/callback#access_token=...&refresh_token=...` (or `#error=...`) |

## Users, roles, permissions

| Method | Path |
|---|---|
| GET/POST | `/users` |
| GET/PATCH | `/users/{user_id}` |
| POST/DELETE | `/users/{user_id}/roles/{role_id}` |
| GET/POST | `/roles` |
| PUT | `/roles/{role_id}/permissions` |
| GET | `/permissions` |

`UserRead` includes `role_ids: UUID[]` — the role IDs currently assigned to
that user, derived from the `user_roles` join table (not a stored column).
There's no endpoint that returns "roles for user X" separately; this field is
the only way to read a user's role assignments, so cross-reference it against
`GET /roles` to resolve names/permissions client-side.

## Organizations

| Method | Path | Notes |
|---|---|---|
| GET | `/organizations` | Returns the caller's own org (or all, if superuser) |
| POST | `/organizations` | Superuser-only; regular signup goes through `/auth/register-organization` |
| PATCH | `/organizations/{id}/tenant` | Superuser-only; assigns/clears the org's `tenant_id` (404 if the given `tenant_id` doesn't exist) |

## Tenants

| Method | Path | Notes |
|---|---|---|
| GET/POST | `/tenants` | Superuser-only (raw `is_superuser` check, not `require_permission` — see `docs/database.md` for why) |

An optional grouping *above* `Organization` (e.g. a holding company with
several subsidiary orgs) — not the tenant-isolation boundary, which remains
`organization_id`. See `docs/database.md` for the full disambiguation. No
frontend page — Organization management itself has none either.

## Risks / Controls

| Method | Path |
|---|---|
| GET/POST | `/risks` |

`RiskCreate`/`RiskRead` include 4 optional EBIOS-RM-flavored link fields:
`asset_id`, `threat_id`, `vulnerability_id`, `feared_event_id` — each
validated cross-tenant on `POST` (404 if the referenced row belongs to
another organization). Settable at creation only: Risk has no `GET/{id}`,
detail page, or update endpoint, so these links can't be edited after a risk
is created. See `## Feared Events` below and `docs/roadmap.md`'s EBIOS RM
entry for the full picture.
| GET/POST | `/controls` |

## Compliance (generic framework engine)

| Method | Path |
|---|---|
| GET | `/compliance/summary` |
| GET/POST | `/compliance/frameworks` |
| GET/POST | `/compliance/frameworks/{framework_id}/versions` |
| GET/POST | `/compliance/framework-versions/{framework_version_id}/requirements` |
| POST | `/compliance/controls/{control_id}/mappings/{requirement_id}` |
| GET | `/compliance/controls/{control_id}/mappings` |
| GET/POST | `/compliance/assessments` |
| GET | `/compliance/assessments/{assessment_id}` |
| PATCH | `/compliance/assessments/{assessment_id}/status` |
| GET | `/compliance/assessments/{assessment_id}/results` |
| PUT | `/compliance/assessments/{assessment_id}/results/{requirement_id}` |
| POST | `/compliance/assessments/{assessment_id}/compute-score` |
| GET | `/compliance/assessments/{assessment_id}/score` |
| POST | `/compliance/evidence` |
| GET | `/compliance/assessments/results/{assessment_result_id}/evidence` |

`GET /system/summary` is a backward-compatible alias for `/compliance/summary`
only — it does not re-expose the rest of the compliance API.

## Audits

| Method | Path |
|---|---|
| GET/POST | `/audits` |
| GET | `/audits/{audit_id}` |
| PATCH | `/audits/{audit_id}/status` |
| GET | `/audits/{audit_id}/report` |
| GET/POST | `/audits/{audit_id}/checklist-items` |
| PUT | `/audits/checklist-items/{item_id}/status` |
| GET/POST | `/audits/{audit_id}/findings` |
| PATCH | `/audits/findings/{finding_id}/status` |
| GET/POST | `/audits/findings/{finding_id}/corrective-actions` |
| PATCH | `/audits/corrective-actions/{action_id}/status` |

## Documents

| Method | Path |
|---|---|
| GET/POST | `/documents` |
| GET | `/documents/{document_id}` |
| POST | `/documents/{document_id}/archive` |
| GET/POST | `/documents/{document_id}/versions` |
| POST | `/documents/versions/{version_id}/submit-for-approval` |
| POST | `/documents/versions/{version_id}/approval` |
| GET | `/documents/versions/{version_id}/approvals` |

## Assets (CMDB)

| Method | Path |
|---|---|
| GET/POST | `/assets` |
| GET | `/assets/{asset_id}` |
| PATCH | `/assets/{asset_id}/lifecycle` |

## Departments

| Method | Path |
|---|---|
| GET/POST | `/departments` |

A flat list, ordered by `created_at`; the `parent_department_id` on each row
forms a hierarchy. There's no server-side tree endpoint — the frontend walks
`parent_department_id` client-side to render indentation. `POST` 404s if
`parent_department_id` doesn't reference a department in the caller's own
organization.

## Threats

| Method | Path |
|---|---|
| GET/POST | `/threats` |

A standalone threat catalog — not yet cross-linked to the risk register (see
`docs/roadmap.md`'s EBIOS RM item).

## Vulnerabilities

| Method | Path |
|---|---|
| GET/POST | `/vulnerabilities` |

A standalone vulnerability register — same not-yet-cross-linked caveat as
Threats above.

## Incidents

| Method | Path |
|---|---|
| GET/POST | `/incidents` |
| GET | `/incidents/{incident_id}` |
| PATCH | `/incidents/{incident_id}/status` |

Unlike Departments/Threats/Vulnerabilities, Incidents has a real status
workflow (`open` → `investigating` → `resolved` → `closed`, with a `reopen`
path back from `resolved` to `investigating`) validated server-side by the
same `StateMachine` the Audits module uses — an illegal transition returns
`409`. `resolved_at` is set when status becomes `resolved` and cleared again
on `reopen`. Standalone, not yet cross-linked to assets/threats/
vulnerabilities.

## Feared Events

| Method | Path |
|---|---|
| GET/POST | `/feared-events` |

An undesirable event impacting an asset's confidentiality, integrity, or
availability — EBIOS RM's "feared event" (événement redouté), with
"business value" and "supporting asset" deliberately conflated into the
existing CMDB `Asset` (see `docs/roadmap.md`). `asset_id` is **required**
(unlike Risk's 4 optional link fields) and validated cross-tenant on `POST`.

## Tasks

| Method | Path |
|---|---|
| GET/POST | `/tasks` |
| GET | `/tasks/{task_id}` |
| PATCH | `/tasks/{task_id}/status` |

A generic, standalone follow-up item, not tied to any one module (unlike
`corrective_actions`/`checklist_items`, which are audit-scoped). Same real
`StateMachine` status workflow as Audits/Incidents (`open` →
`in_progress` → `done`, with a `reopen` path back from `done` to
`in_progress`) — an illegal transition returns `409`.

## AI

| Method | Path |
|---|---|
| GET/POST | `/ai/prompts` |
| POST | `/ai/knowledge-base` |
| GET/POST | `/ai/chat/sessions` |
| GET/POST | `/ai/chat/sessions/{session_id}/messages` |

## Notifications

| Method | Path |
|---|---|
| GET | `/notifications` |
| POST | `/notifications/{notification_id}/read` |

## SSO (per-organization OIDC connection)

| Method | Path |
|---|---|
| GET/PUT/DELETE | `/sso/connection` |

Requires `sso:manage` (admin-only by default). `SsoConnectionRead` never
includes `client_secret` — same `hashed_password`-style omission pattern as
`UserRead`. See `docs/security.md`'s SSO/OIDC section for the full flow these
endpoints participate in.

## Dashboard

| Method | Path |
|---|---|
| GET | `/dashboard/summary` |
