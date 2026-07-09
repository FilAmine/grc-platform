# Development

## Adding a new module

Follow the pattern in `docs/architecture.md`. Concretely, for a module named
`widgets`:

1. `backend/app/modules/widgets/{__init__,models,service,repository,schemas,api}.py`
2. Domain dataclasses + enums + `Store` Protocol + service class in `service.py`
   (no SQLAlchemy/FastAPI imports here).
3. ORM model(s) in `models.py`, composing the mixins from `common/models.py` that
   apply (almost always `UUIDPKMixin` + `TimestampMixin`; add `TenantScopedMixin`
   if it's tenant-owned data, `SoftDeleteMixin` if it's a business object users
   can "delete", `AuditColumnsMixin` if you want who-created/updated tracking).
4. `SqlAlchemy*Repository` in `repository.py` implementing the `Store` Protocol,
   with a `to_<entity>()` mapper function converting the ORM row to the domain
   dataclass.
5. Pydantic schemas in `schemas.py`.
6. Router in `api.py` — thin, calls the service via `Depends()`.
7. Add a `get_widget_service()` factory to
   `backend/app/interfaces/api/dependencies.py`.
8. `import` the new model(s) into `backend/app/database/model_registry.py` (or
   Alembic autogenerate won't see the table).
9. Mount the router in `backend/app/interfaces/api/v1/router.py`.
10. Write an Alembic migration by hand (see any `202607*` migration for the
    pattern — this project hand-writes migrations rather than relying purely on
    `alembic revision --autogenerate`, partly because no Postgres instance was
    available to autogenerate against during initial development).
11. Add permission codes to `security/permissions.py` if the module needs its own
    RBAC gating, and wire them into the relevant system roles' tuples.
12. Tests in `backend/tests/test_widgets.py` — see `backend/tests/conftest.py`
    for the `client`/`db_session` fixtures and `register_organization()`/
    `auth_headers()` helpers.

## Running tests

```bash
pip install -r requirements.txt   # includes pytest/pytest-asyncio/pytest-cov
pytest backend/tests -q
pytest backend/tests -q --cov=backend/app --cov-report=term-missing
```

Tests run against an in-memory SQLite database (see `conftest.py::db_session`) with
`StaticPool` so the whole test suite shares one connection — no Docker/Postgres
required to run `pytest`. This means tests don't exercise Postgres-specific SQL;
the Alembic migrations themselves are validated separately (see below).

## Linting

```bash
ruff check backend
```

Config is in `pyproject.toml` under `[tool.ruff]`/`[tool.ruff.lint]`. Notable
choices: `line-length = 120`; `flake8-bugbear`'s `extend-immutable-calls` is
configured for FastAPI's `Depends()`/`Query()`/etc. so B008 doesn't false-positive
on the DI pattern used in every router; migration files are exempted from E501
(verbose `ForeignKeyConstraint` calls aren't improved by wrapping).

## Migrations

```bash
alembic upgrade head
alembic downgrade -1
alembic history
alembic upgrade head --sql   # offline SQL preview, no DB connection needed
```

`alembic upgrade head --sql` is useful for reviewing a migration's generated SQL
without a live database — every migration in this repo has been validated this
way against the `postgresql` dialect at minimum.

## Frontend

```bash
cd frontend
npm install
npm run dev          # Vite dev server, http://localhost:5173
npx tsc -b            # typecheck only
npm run build         # typecheck + production build
```

There is no ESLint config in this project yet (`npm run lint` will fail with "no
config found") — this predates the current session's changes and hasn't been
addressed.

## Local end-to-end testing without Docker

If Docker/Postgres genuinely isn't available, you can point `DATABASE_URL` at a
local SQLite file for manual UI testing — the ORM models use
`sqlalchemy.dialects.postgresql.UUID`/`JSON` types, which fall back to a working
generic implementation on SQLite. Create tables with
`Base.metadata.create_all(engine)` (Alembic's migrations use Postgres-specific DDL
like `postgresql.ENUM` and won't run against SQLite) and seed the permission
catalog/system roles the same way `conftest.py::db_session` does. This is a
manual-testing convenience, not a supported deployment target — always use
Postgres for anything beyond your own local UI smoke-testing.
