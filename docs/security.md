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
- **`is_superuser`** is a platform-operator flag, not assignable via the public
  API (no endpoint sets it after registration) — it's for direct database/ops use,
  e.g. the one Postgres operator managing the whole platform.

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

## Known gaps (tracked in `docs/roadmap.md`)

- **No MFA.** Login is single-factor (email + password).
- **No LDAP/Azure AD/OIDC/OAuth2 SSO.** The auth module is structured so an
  external identity provider could issue its own access tokens through the same
  `AIProvider`-style pluggable pattern used for AI providers, but nothing is wired.
- **No rate limiting** on `/auth/login` beyond the per-account lockout (a
  distributed attacker rotating source IPs isn't currently slowed by anything
  else). Redis is already a dependency and would be the natural backing store for
  this.
- **No security headers middleware** (CSP, HSTS, X-Frame-Options, etc.) — FastAPI's
  default response headers are used as-is. Typically added at the reverse-proxy
  layer (nginx, already in front of the frontend container) rather than in the
  app; the `infra/nginx/default.conf` does not yet set these.
- **No automated dependency/SAST scanning** wired into CI yet (e.g. `pip-audit`,
  `npm audit`, CodeQL) — `ruff` covers style/some correctness issues but not
  vulnerability scanning.
- **Electronic signatures**: `DocumentApproval.signature_reference` is a schema
  slot for an external e-signature provider's envelope ID — no provider is
  integrated, so "electronic signature ready" means the data model has somewhere
  to put it, not that signing actually happens.
