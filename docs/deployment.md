# Deployment

## Current target: Docker Compose

`docker-compose.yml` is the reference deployment: `postgres`, `redis`, `backend`
(runs `alembic upgrade head` then `uvicorn`), `frontend` (built into a static
bundle, served by nginx). This is suitable for a single-host deployment; it is
**not** a high-availability setup.

Before deploying anywhere real:

1. Set a strong, unique `SECRET_KEY` — the default is intentionally a
   fail-a-review placeholder.
2. Point `DATABASE_URL` at a managed/backed-up Postgres instance, not the
   `postgres` container's local volume.
3. Set `BACKEND_CORS_ORIGINS` to your actual frontend origin(s), not localhost.
4. Set `AI_PROVIDER` and the matching credentials if you want real AI
   completions instead of the network-free `echo` default.
5. Put the frontend and backend behind TLS (a reverse proxy in front of both
   containers — nginx is already fronting the frontend's static files, but the
   backend container as shipped serves plain HTTP; terminate TLS in front of it).

## Rollout

```bash
docker compose pull   # if using published images rather than building locally
docker compose up -d --build
docker compose logs -f backend   # confirm `alembic upgrade head` succeeded before traffic
```

Migrations run automatically as part of the `backend` container's startup command
(`sh -c "alembic upgrade head && uvicorn ..."`). For a multi-instance deployment,
run the migration once (e.g. as a separate job/init container) rather than letting
every replica race to run it concurrently — Alembic doesn't currently guard against
concurrent `upgrade head` calls.

## Rollback

```bash
alembic downgrade -1     # revert the most recent migration
```

Every migration in this repo implements a real `downgrade()`, not a no-op — see
`docs/database.md` for the migration list. Application rollback is a matter of
redeploying the previous container image; there's no blue/green or canary
mechanism in the Compose setup.

## Future-ready, not yet implemented

The spec anticipates Kubernetes/Helm/Terraform as a future target. Nothing in this
repo assumes Docker Compose specifically — the `backend`/`frontend` Dockerfiles are
standard multi-stage builds that would work unmodified as a Kubernetes Deployment's
container image — but no Helm chart or Terraform module exists yet. Priorities for
that work, in order: externalize secrets (currently plain env vars) into a
secrets manager, run migrations as a Kubernetes Job/initContainer rather than in
the app container's startup command, and add liveness/readiness probes pointing at
`/health`.

## Health checks

- Backend: `GET /health` → `{"status": "ok", "service": "<app_name>"}`. No
  database check is performed — it verifies the process is up and configured, not
  that the database is reachable.
- Postgres/Redis: `docker-compose.yml` defines container-level healthchecks
  (`pg_isready`, `redis-cli ping`) that gate the backend container's startup via
  `depends_on: condition: service_healthy`.
