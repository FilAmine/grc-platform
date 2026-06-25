# GRC Platform

Production-ready bootstrap for a Governance, Risk, and Compliance platform using FastAPI, React, PostgreSQL, SQLAlchemy, Alembic, Redis, Docker, and Material UI.

## Architecture

The backend follows Clean Architecture:

- `domain`: business entities and repository contracts.
- `application`: use cases and DTOs.
- `infrastructure`: database, cache, repositories, external adapters.
- `interfaces`: FastAPI routes, dependencies, and schemas.
- `core`: configuration, security, logging, and cross-cutting concerns.

The frontend is a Vite React TypeScript application using Material UI, React Router, TanStack Query, and Axios.

## Quick Start

1. Copy environment defaults:

```bash
cp .env.example .env
cp frontend/.env.example frontend/.env
```

2. Start the stack:

```bash
docker compose up --build
```

3. Open:

- Frontend: http://localhost:3000
- API docs: http://localhost:8000/api/v1/docs
- Health: http://localhost:8000/health

## Backend Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
alembic upgrade head
uvicorn backend.app.main:app --reload
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
alembic upgrade head
uvicorn backend.app.main:app --reload
```

## Frontend Development

```bash
cd frontend
npm install
npm run dev
```

## Useful Commands

```bash
pytest
ruff check .
mypy backend
alembic revision --autogenerate -m "describe change"
alembic upgrade head
```

## Default Modules

- Organizations
- Risks
- Controls
- Compliance health checks

These are intentionally small but complete enough to demonstrate conventions for database models, repositories, use cases, API schemas, and UI composition.
