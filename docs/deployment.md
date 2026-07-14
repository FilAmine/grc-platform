# Deployment

## Current target: Docker Compose

`docker-compose.yml` is the reference deployment: `postgres`, `redis`, `backend`
(runs `alembic upgrade head` then `uvicorn`), `celery-worker`/`celery-beat`
(same image as `backend`, different `command:`, sharing its environment via
an `x-backend-env` YAML anchor), `frontend` (built into a static bundle,
served by nginx). This is suitable for a single-host deployment; it is
**not** a high-availability setup.

`celery-worker`/`celery-beat`'s `depends_on: backend` is a best-effort
ordering hint only, not a guarantee: `backend` has no healthcheck (only
`postgres`/`redis` do), so `depends_on` there just means "container
started," not "migrations finished" — a worker task could still race
`backend`'s `alembic upgrade head` on a cold start. Not solved here; would
need a real healthcheck on `backend` or a separate migration-completion
signal.

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

## Kubernetes

`k8s/` has a drafted set of plain manifests mirroring this file's Docker
Compose topology, and `helm/grc-platform/` templates the same design into
a proper Helm chart — see `k8s/README.md` and `helm/README.md` for the
full apply sequence, prerequisites, and what each deliberately doesn't
include (autoscaling, network policies, a real secrets-manager
integration). Both are now **schema-validated** — `kubectl kustomize`,
`helm lint`/`helm template`, and [`kubeconform`](https://github.com/yannh/kubeconform)
(real Kubernetes OpenAPI schemas, no cluster needed) all pass clean, 0
errors across every resource in both. **Neither has been applied to a
real cluster**, though — no live `kubectl apply`/`helm install`, no pods
actually scheduled. Schema validity doesn't catch everything a live apply
would (probe timing tuned for real startup time, a StorageClass that
exists in your actual cluster, real ingress-controller/cert-manager
interaction). See each directory's README for the exact commands run and
what a full apply would still need to confirm.

Both implement the three priorities this section used to list before they
were drafted: secrets moved into a Kubernetes Secret (still a stopgap, not
a real secrets-manager integration — see `k8s/secret.example.yaml`'s or
`helm/grc-platform/values.yaml`'s `secrets:` block header), migrations run
as a separate Job instead of in the app container's startup command (the
Helm chart does this as a proper `pre-install,pre-upgrade` hook, which
blocks the rest of the release until it succeeds — a genuine improvement
over the plain manifests' manual delete-then-apply-then-wait sequence),
and liveness/readiness probes on `/health`.

One related change needed regardless of which you use: `frontend/Dockerfile`
now accepts a `VITE_API_BASE_URL` build arg (default unchanged, so existing
Compose/local builds are unaffected) — the frontend bakes its API origin in
at build time, not container runtime, and had no way to point at a
non-`localhost` backend before this.

## Terraform (AWS)

`terraform/aws/` provisions the cloud infrastructure the Kubernetes
manifests/Helm chart need to run somewhere real: a VPC, an EKS cluster,
managed Postgres (RDS), managed Redis (ElastiCache), and two ECR
repositories. **AWS was picked as a default, not because anything else in
this repo specifies a cloud provider** — see `terraform/aws/README.md` for
that reasoning in full. `terraform init` (resolves the AWS provider and
both `terraform-aws-modules/vpc`/`terraform-aws-modules/eks` registry
modules cleanly) and `terraform validate` (real schema-level HCL
validation against the AWS provider) both now pass; `terraform plan` was
also attempted and fails exactly where expected — missing AWS credentials,
not a config bug — confirming this module is structurally sound right up
to the point a real AWS account becomes mandatory. **No AWS account,
credentials, cost, or real infrastructure were involved at any point.**
Also not attempted: Terraform state backend configuration (uses local
state as written), and a real secrets-manager wiring for the RDS master
password (a plain, `sensitive`-flagged variable today — still stored in
plaintext in Terraform state, same underlying gap the Kubernetes Secret
stopgaps have).

## Health checks

- Backend: `GET /health` → `{"status": "ok", "service": "<app_name>"}`. No
  database check is performed — it verifies the process is up and configured, not
  that the database is reachable.
- Postgres/Redis: `docker-compose.yml` defines container-level healthchecks
  (`pg_isready`, `redis-cli ping`) that gate the backend container's startup via
  `depends_on: condition: service_healthy`.
