# Architecture

## Backend: module-per-bounded-context

The backend is organized as one Python package per business capability under
`backend/app/modules/`, not by technical layer. Each module owns its full stack:

```
backend/app/modules/<name>/
  models.py       # SQLAlchemy ORM models
  service.py      # domain dataclasses, enums, Protocol "store" interfaces, and
                   # the service class that holds business logic (framework-free)
  repository.py   # ABC + SqlAlchemy implementation of the store Protocol
  schemas.py       # Pydantic request/response schemas
  api.py          # FastAPI router (thin: parses request, calls service, serializes response)
```

`service.py` never imports SQLAlchemy or FastAPI — it depends only on the `Store`
Protocol it defines, which `repository.py` implements. `api.py` wires a service to a
request via `Depends()` factories centralized in
[`backend/app/interfaces/api/dependencies.py`](../backend/app/interfaces/api/dependencies.py).
This keeps business logic testable without a database (swap in a fake `Store`) and
keeps routers free of persistence details.

Current modules: `auth`, `users`, `roles`, `permissions`, `organizations`,
`risks`, `controls`, `compliance` (the generic framework/assessment engine),
`audits`, `documents`, `assets`, `ai`, `notifications`, `dashboard`.

Cross-cutting code lives outside `modules/`:

- `common/models.py` — mixins every model composes from: `UUIDPKMixin`,
  `TenantScopedMixin` (adds `organization_id`), `SoftDeleteMixin` (`deleted_at`),
  `AuditColumnsMixin` (`created_by_id`/`updated_by_id`), `TimestampMixin`.
- `database/` — the SQLAlchemy `Base`/engine/session, and `model_registry.py`,
  which every module's `models.py` must be imported into so Alembic autogenerate
  and `Base.metadata` see the table.
- `security/` — password hashing, JWT issuance/verification, and
  `security/permissions.py`, the single source of truth for RBAC permission codes
  and the default system roles (seeded by migration `202607090001`).
- `workflow/state_machine.py` — a generic `StateMachine` used to validate status
  transitions (e.g. an audit can't jump straight from `planned` to `completed`);
  wired into `AuditService`, `AssessmentService`, and `DocumentService`.
- `interfaces/api/v1/router.py` — mounts every module's router under `/api/v1`.

## Multi-tenancy

`organizations` is the tenant root. Every tenant-owned table carries an
`organization_id` via `TenantScopedMixin`. The tenant boundary is enforced in the
API layer, never trusted from client input: `get_current_user` resolves the caller's
`organization_id` from their JWT, and every module's `list`/`get` methods filter by
it server-side. Global reference data (system roles, the framework catalog, system
prompt templates) uses `organization_id IS NULL` and a matching `is_system` flag;
tenants can also create their own private rows in the same tables (custom roles,
custom frameworks, custom prompt templates) — see `docs/database.md`.

## The generic compliance engine

`modules/compliance` deliberately has no ISO27001-specific code. The schema is:

```
Framework -> FrameworkVersion -> ControlCategory / Requirement
Control <-(ControlMapping)-> Requirement
Assessment -> AssessmentResult -> Evidence
                                -> ComplianceScore (computed)
```

Supporting a new standard means inserting `Framework`/`FrameworkVersion`/
`Requirement` rows (via the API or a data migration), not writing code. Creating an
`Assessment` auto-populates one `AssessmentResult` per requirement in that
framework version; `compute-score` derives a 0–100 score from the compliant/
applicable ratio.

## Request flow

1. FastAPI route parses/validates the request body against a Pydantic schema.
2. A `Depends()` factory in `interfaces/api/dependencies.py` builds the service,
   injecting a `SqlAlchemy*Repository` bound to the request's DB session.
3. `get_current_user` decodes the JWT and loads the `User`; `require_permission(code)`
   additionally checks the user's roles carry that permission (or `is_superuser`).
4. The service executes domain logic against the repository's `Store` Protocol.
5. The repository's SQLAlchemy implementation persists/queries and maps ORM rows
   back to the module's frozen dataclass.
6. The route validates the dataclass into a Pydantic response schema.

## AI provider abstraction

`modules/ai/providers.py` is the only file that knows about OpenAI, Azure OpenAI,
or Ollama specifics. Everything else depends on the `AIProvider` Protocol
(`chat`, `embed`). `get_ai_provider(settings)` picks a provider from
`settings.ai_provider`, defaulting to `EchoProvider` — a deterministic, network-free
implementation — so the platform runs with zero AI credentials configured.
Knowledge-base documents are embedded and retrieved via a linear cosine-similarity
scan over a JSON-encoded float array column (works on any SQL backend); swapping in
pgvector later only touches `KnowledgeBaseRepository`.

## Frontend

Vite + React + TypeScript + MUI + TanStack Query + React Router + React Hook Form +
Zod. `AuthContext` wraps a TanStack Query "me" query with token persistence
(localStorage) and an axios interceptor that transparently refreshes on 401.
`RequireAuth`/`RedirectIfAuthenticated` are route guards. Only the Dashboard, Risks,
and Controls pages are built as a reference pattern — see `docs/roadmap.md` for the
remaining module UIs.

## Infrastructure

- PostgreSQL 16, Redis 7, Docker Compose for local parity.
- Alembic owns schema migrations — see `docs/database.md`.
- Structured logging via `structlog`.
- Celery is a declared dependency for future async job processing (e.g. long-running
  scans, scheduled compliance score recomputation) but no worker/task is wired yet —
  see `docs/roadmap.md`.
