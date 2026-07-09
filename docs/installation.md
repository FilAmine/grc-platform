# Installation

## Option 1: Docker Compose (recommended)

Requires Docker and Docker Compose.

```bash
cp .env.example .env
cp frontend/.env.example frontend/.env
docker compose up --build
```

This starts PostgreSQL, Redis, the backend (running `alembic upgrade head` on
startup, then `uvicorn`), and the frontend (built and served via nginx).

- Frontend: http://localhost:3000
- API + interactive docs: http://localhost:8000/api/v1/docs
- Health check: http://localhost:8000/health

## Option 2: Manual (backend + frontend separately)

You'll need Python 3.12, Node.js 20+, and a running PostgreSQL 16 instance
(update `DATABASE_URL` in `.env` to point at it — see `docker-compose.yml`
for a one-off Postgres container if you don't have one).

### Backend

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
alembic upgrade head
uvicorn backend.app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## First login: creating your organization

There's no seed data for a demo tenant — the platform is multi-tenant from the
first request. Create your organization (and its Admin user) via:

```bash
curl -X POST http://localhost:8000/api/v1/auth/register-organization \
  -H "Content-Type: application/json" \
  -d '{
    "organization_name": "Acme Corp",
    "organization_slug": "acme-corp",
    "admin_email": "admin@acme.example.com",
    "admin_full_name": "Ada Admin",
    "admin_password": "SuperSecret123"
  }'
```

or use the "Create one" link on the frontend's login page. The response contains
an `access_token`/`refresh_token` pair; the frontend handles this for you.

## Configuration reference

See `.env.example` for every recognized environment variable. Notable ones:

| Variable | Default | Purpose |
|---|---|---|
| `SECRET_KEY` | `change-me-in-production` | JWT signing key — **override this** outside local dev |
| `DATABASE_URL` | (Postgres, see `.env.example`) | SQLAlchemy connection string |
| `BACKEND_CORS_ORIGINS` | `http://localhost:3000,http://localhost:5173` | comma-separated allowed frontend origins |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | JWT access token lifetime |
| `REFRESH_TOKEN_EXPIRE_DAYS` | `30` | Refresh token lifetime |
| `AI_PROVIDER` | `echo` | `echo` (no network, default), `openai`, `azure_openai`, or `ollama` — see `docs/architecture.md#ai-provider-abstraction` |
