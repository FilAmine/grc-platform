# Security

## Authentication

- **Password hashing**: Argon2 (`passlib`, `argon2-cffi`), not bcrypt.
- **Access tokens**: JWT (HS256), short-lived (`ACCESS_TOKEN_EXPIRE_MINUTES`,
  default 30 min), signed with `SECRET_KEY`.
- **Refresh tokens**: opaque random tokens (`secrets.token_urlsafe(48)`), stored
  server-side only as a SHA-256 hash (`refresh_tokens.token_hash`) — a leaked
  database dump doesn't hand out live sessions. Refresh **rotates**: each use
  revokes the old token and issues a new one, so a stolen-then-reused refresh
  token is detectable (the legitimate holder's next refresh will fail).
  `REFRESH_TOKEN_EXPIRE_DAYS` defaults to 30.
- **Account lockout**: 5 consecutive failed logins locks the account for 15
  minutes (`modules/users/service.py`). Failed-attempt tracking is per-account,
  reset on successful login.
- **Password policy**: minimum 12 characters, at least one uppercase, one
  lowercase, one digit (`modules/users/schemas.py::validate_password_strength`),
  enforced both server-side (Pydantic validator) and client-side (Zod schema,
  same rules).

## Authorization (RBAC)

- Permission codes are `resource:action` strings (`risks:manage`,
  `documents:read`, ...), defined once in `security/permissions.py` — the single
  source of truth for both the seeded permission catalog and every
  `require_permission(code)` check.
- Four **system roles** (Admin, Manager, Auditor, Viewer) are shared read-only
  across every tenant (`roles.organization_id IS NULL`, `is_system=True`) and
  cannot have their permissions edited via the API (`RoleNotEditableError` → 403).
  Tenants can also create **custom roles** scoped to their own organization.
- `require_permission(code)` is a FastAPI dependency: superusers bypass the
  check entirely; everyone else must hold a role (system or custom) granting that
  permission code.
- **`is_superuser`** bypasses `require_permission` entirely, regardless of role
  assignment. It **is** settable via the public API: `POST /users` accepts an
  `is_superuser` flag, so anyone holding `users:manage` can grant it to a new
  user within their own organization (`modules/users/schemas.py::UserCreate`,
  `modules/users/api.py::create_user`) — there is no additional guard requiring
  platform-operator/direct-database access. Treat `users:manage` as
  superuser-equivalent when reasoning about blast radius.

## SSO / OIDC

- **Per-organization, not platform-wide.** Each org can optionally connect its
  own OIDC app registration (Azure AD, Okta, Google Workspace, or any
  standards-compliant IdP) via `PUT /sso/connection` (gated by `sso:manage`,
  admin-only by default — not granted to Manager/Auditor/Viewer). Password
  login keeps working for orgs that don't configure SSO; the two are not
  mutually exclusive.
- **Standard authorization-code flow**: `GET /auth/sso/{organization_slug}/login`
  redirects to the IdP's `authorization_endpoint` (discovered from
  `{issuer}/.well-known/openid-configuration`); `GET /auth/sso/callback`
  exchanges the code, verifies the returned `id_token`'s signature against the
  IdP's JWKS (`backend/app/modules/sso/oidc_client.py`), and redirects the
  browser to the SPA's `/sso/callback` route with a same-shape `TokenPair` as
  password login, carried in the URL fragment (not the query string, so it
  isn't logged server-side or sent via `Referer`).
- **CSRF/correlation via signed state, not server-side session storage**: the
  `state` parameter is a short-lived (5 min) signed JWT
  (`security/tokens.py::create_sso_state_token`) encoding the organization id
  — nothing to look up or expire out of a database table.
- **Just-in-time user provisioning**: the first successful SSO login for an
  email not yet in that org auto-creates the user, with a random
  `secrets.token_urlsafe(32)` password hash that is never communicated to
  anyone — that user can only ever authenticate via SSO, never the password
  form. An optional `default_role_id` on the connection is assigned to
  newly-provisioned users; existing users keep whatever roles they already
  have.
- **Known limitation: `client_secret` is stored in plaintext.** No
  KMS/envelope-encryption infrastructure exists in this codebase. Treat
  `sso_connections.client_secret` the same as any other plaintext secret in
  the database — encrypt at rest (or move to a real secrets manager) before
  storing real customer IdP credentials in a production deployment.
- **Not covered**: SAML and raw LDAP are different protocols and are not
  implemented — only OIDC. No MFA enforcement beyond whatever the connected
  IdP itself requires.

## Multi-tenant isolation

Every list/get across every module derives `organization_id` from the
authenticated user's JWT (`get_current_user`), never from a client-supplied query
parameter, path parameter, or request body field. `test_tenant_isolation.py`
exercises this directly: creating a risk in Org A and attempting to read it as Org
B's admin returns an empty list (for collection reads) or 404 (for direct-by-ID
reads), and a non-superuser cannot create a new `Organization` directly — only
via `/auth/register-organization`, which creates exactly one org + one admin user
atomically.

## Transport / headers

- CORS is configured via `BACKEND_CORS_ORIGINS` (comma-separated), restricted to
  known frontend origins — not `allow_origins=["*"]`.
- `SECRET_KEY` has a minimum length (16 chars) enforced by Pydantic and **must**
  be overridden in any non-local environment — the default
  (`change-me-in-production`) is intentionally named to fail a security review if
  left in place.

## Rate limiting

Redis-backed fixed-window counters (`INCR` + `EXPIRE`, `backend/app/core/rate_limit.py`)
applied to the unauthenticated/pre-auth `auth` endpoints, keyed by
`request.client.host`:

| Endpoint | Limit |
|---|---|
| `POST /auth/login` | 10 / 60s per IP |
| `POST /auth/register-organization` | 5 / 3600s per IP |
| `POST /auth/refresh` | 30 / 60s per IP (higher — legitimate 401-triggered auto-refresh) |
| `GET /auth/sso/{organization_slug}/login` | 20 / 60s per IP |
| `GET /auth/sso/callback` | 20 / 60s per IP |

Thresholds are hardcoded constants next to the routes they gate
(`modules/auth/api.py`), matching the existing
`MAX_FAILED_LOGIN_ATTEMPTS`/`LOCKOUT_MINUTES` precedent rather than new
`Settings` fields. This is on top of, not instead of, the per-account lockout
above — the lockout stops credential-stuffing a single account, the rate
limiter slows a distributed attacker rotating accounts or source IPs.

**Fails open**: if Redis is unreachable, the request is allowed through and a
warning is logged, rather than making Redis a hard availability dependency for
login/auth. A small circuit breaker skips Redis entirely for 5s after the
first failure, so an outage doesn't add a per-request connect-timeout to every
call.

**No reverse proxy sits in front of the backend** in this project's
docker-compose setup, so `request.client.host` is the real client IP as seen
directly by Starlette. If a proxy is ever added in front of the backend, this
needs `ProxyHeadersMiddleware` (or equivalent trusted-hosts handling) —
otherwise every request collapses into one shared rate-limit bucket keyed on
the proxy's own IP.

## Security headers

Set at the application level for the API (`backend/app/core/security_headers.py`,
a `BaseHTTPMiddleware` wired in `main.py`) and at the nginx level for the SPA
(`frontend/nginx.conf`, the file actually copied into the frontend Docker
image by `frontend/Dockerfile` — not `infra/nginx/default.conf`, which was an
unreferenced duplicate and has been removed). There is no reverse proxy in
front of the FastAPI backend, so these can't be assumed to come from a proxy
layer.

Both set: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`,
`Referrer-Policy: strict-origin-when-cross-origin`,
`Permissions-Policy: geolocation=(), microphone=(), camera=()`,
`Strict-Transport-Security: max-age=31536000; includeSubDomains` (safe to send
even over plain HTTP — browsers only enforce HSTS over HTTPS).

**CSP**: the API's default policy is strict (`default-src 'self';
frame-ancestors 'none'`), with a looser override specifically for
`/api/v1/docs` and `/api/v1/redoc` (FastAPI's built-in Swagger UI/ReDoc pages,
which load JS/CSS from `cdn.jsdelivr.net` and each embed an inline
bootstrap `<script>` — `'unsafe-inline'` is required there since FastAPI's
built-in docs routes have no nonce/hash wiring). The SPA's policy
(`default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline';
img-src 'self' data:; connect-src 'self' http://localhost:8000; frame-ancestors
'none'`) needs `style-src 'unsafe-inline'` for MUI's emotion runtime, which
injects `<style>` tags without a nonce — a known, deliberate compromise rather
than an oversight.

## Dependency and static-analysis scanning

CI runs `pip-audit -r requirements.txt` (backend), `npm audit --omit=dev
--audit-level=high` (frontend), and CodeQL (`python` + `javascript-typescript`,
on push/PR to `main` and weekly) — see `.github/workflows/ci.yml` and
`.github/workflows/codeql.yml`.

`pip-audit` ignores one advisory now (it used to ignore two — the `starlette`
group was fixed by bumping `fastapi` `0.111.0` → `0.139.0`, which pulls in
`starlette>=1.0.1`; see `docs/roadmap.md`):

- **`ecdsa` (`PYSEC-2026-1325`, Minerva timing attack)**: no fix exists upstream
  (the maintainers consider side-channel attacks out of scope for a pure-Python
  implementation) and the vulnerable code paths — `sign_digest()`, key
  generation, ECDH — are never exercised by this app: access/refresh tokens are
  always HS256 (`security/tokens.py`), and the SSO `id_token` verification path
  only ever does ECDSA/RSA *verification* (unaffected — see the advisory),
  never signing.

`python-jose`'s one remaining unfixed advisory (`PYSEC-2025-185`, a JWE
decompression-bomb DoS) isn't ignored in CI because it doesn't need to be: this
codebase never calls `jwe.decrypt` or otherwise touches JWE, only `jwt.encode`/
`jwt.decode` — the vulnerable function simply isn't reachable, so it doesn't
show up as a finding in the first place.

`npm audit` runs with `--omit=dev`. It used to flag `vite`/`esbuild`
(dev server/build-tool only, no production exposure); that's fixed now —
see `docs/roadmap.md` for the `vite@8` upgrade and the two follow-up issues
it took to actually ship (an `@mui/icons-material` CJS/ESM interop bug, and
a TypeScript `moduleResolution` setting). `--omit=dev` remains a real,
stated tradeoff regardless of what's currently flagged: it means a future
devDependency supply-chain compromise (a real category of past npm
incidents) wouldn't be caught by this CI gate — production dependencies are
scanned in full.

## Known gaps (tracked in `docs/roadmap.md`)

- **No MFA** beyond whatever an org's connected SSO identity provider itself
  enforces — password login remains single-factor.
- **No SAML or LDAP** — only OIDC is implemented (see the SSO/OIDC section
  above). `client_secret` is stored in plaintext, also noted above.
- **Electronic signatures**: `DocumentApproval.signature_reference` is a schema
  slot for an external e-signature provider's envelope ID — no provider is
  integrated, so "electronic signature ready" means the data model has somewhere
  to put it, not that signing actually happens.
