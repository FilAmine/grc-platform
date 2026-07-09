# GRC Platform

A multi-tenant Governance, Risk & Compliance platform: JWT auth + RBAC, a
generic compliance engine (frameworks as data — ISO 27001, NIST CSF, SOC 2, and
others as catalog rows, not code), risk register, controls, audits, document
lifecycle/approval, CMDB, and an AI assistant with a provider-agnostic
chat/knowledge-base layer.

**Stack**: FastAPI + SQLAlchemy 2 + Alembic + PostgreSQL + Redis (backend);
React + TypeScript + Vite + MUI + TanStack Query + React Hook Form + Zod
(frontend); Docker Compose; GitHub Actions CI.

## Quick start

```bash
cp .env.example .env
cp frontend/.env.example frontend/.env
docker compose up --build
```

- Frontend: http://localhost:3000
- API docs: http://localhost:8000/api/v1/docs
- Health: http://localhost:8000/health

Then register your organization — see `docs/installation.md` for the manual
(non-Docker) setup and the registration request.

## Documentation

| Doc | Covers |
|---|---|
| [`docs/architecture.md`](docs/architecture.md) | Module pattern, multi-tenancy, the generic compliance engine, AI provider abstraction |
| [`docs/installation.md`](docs/installation.md) | Docker Compose and manual setup, first-login/registration, config reference |
| [`docs/development.md`](docs/development.md) | Adding a module, running tests/lint/migrations, frontend dev loop |
| [`docs/database.md`](docs/database.md) | Schema conventions, migration history, system/custom row pattern |
| [`docs/security.md`](docs/security.md) | Auth, RBAC, tenant isolation, known security gaps |
| [`docs/deployment.md`](docs/deployment.md) | Rollout, rollback, health checks, what's not production-hardened yet |
| [`docs/roadmap.md`](docs/roadmap.md) | Honest done/not-done accounting against the original spec |
| [`docs/api.md`](docs/api.md) | Every real endpoint, grouped by module |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Workflow and expectations for changes |

## Status

Backend: 14 modules, all with real (not stub) implementations — 40 tests, 89%
coverage, 0 ruff errors, migrations validated against a live Postgres service
container in CI. Frontend: auth flow + Dashboard/Risks/Controls pages built as a
reference pattern; most module UIs are not yet built (backend API is complete
and tested for all of them — see `docs/roadmap.md`).
