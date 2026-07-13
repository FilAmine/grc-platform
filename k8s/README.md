# Kubernetes manifests

Plain manifests (no Helm), mirroring `docker-compose.yml`'s service topology.
Addresses the three priorities `docs/deployment.md` stated for this work:
externalized secrets (`secret.example.yaml`, still a stopgap — see its own
header), migrations as a Job instead of the backend container's startup
command (`migration-job.yaml`), and liveness/readiness probes on `/health`
(`backend-deployment.yaml`).

## Status: drafted, not verified against a real cluster

No `kubectl`, `helm`, or Kubernetes cluster is available in the environment
these were written in, so nothing here has been applied, rendered, or
schema-validated against a real API server — the only check performed was
parsing every file with a plain YAML parser to catch syntax errors. Treat
this as a solid starting draft, not a tested deployment artifact: run
`kubectl apply --dry-run=server -k k8s/` (or equivalent) against a real
cluster before trusting it, and expect to fix at least minor issues (exact
probe timings, resource requests/limits for your actual traffic, storage
class names for the PVCs in `postgres.yaml`/`redis.yaml`, which aren't set
here and will fall back to your cluster's default StorageClass).

## Before applying anything

1. **Build and push real images**, replacing every
   `ghcr.io/your-org/grc-backend:latest` / `grc-frontend:latest` placeholder
   across these files with your actual registry path and a real tag (not
   `latest` — pin a digest or a git-SHA tag so rollouts are reproducible).

   ```bash
   docker build -f backend/Dockerfile -t <registry>/grc-backend:<tag> .
   docker push <registry>/grc-backend:<tag>

   # The frontend bakes its API URL in at build time (see frontend/Dockerfile
   # and frontend/nginx.conf's comment) -- pass the real backend origin here,
   # matching ingress.yaml's api.grc.example.com host:
   docker build -f frontend/Dockerfile \
     --build-arg VITE_API_BASE_URL=https://api.grc.example.com/api/v1 \
     -t <registry>/grc-frontend:<tag> frontend
   docker push <registry>/grc-frontend:<tag>
   ```

2. **Set up secrets.** Copy `secret.example.yaml` to `secret.yaml` (gitignored),
   fill in real values, apply it directly (it's excluded from
   `kustomization.yaml` on purpose):

   ```bash
   cp k8s/secret.example.yaml k8s/secret.yaml
   # edit k8s/secret.yaml with real values
   kubectl apply -f k8s/secret.yaml
   ```

   This is a real Kubernetes Secret (base64-at-rest, not encrypted, unless
   your cluster has encryption-at-rest enabled for the Secret resource
   type) — swap it for a real secrets manager before this matters for
   production. See `secret.example.yaml`'s header for why that's not
   drafted here.

3. **Update the placeholder domains.** `grc.example.com` / `api.grc.example.com`
   appear in `ingress.yaml` and `configmap.yaml`'s `BACKEND_CORS_ORIGINS`/
   `BACKEND_BASE_URL`/`FRONTEND_BASE_URL` — replace all of them with your
   real domains, consistently (a mismatch here breaks CORS or the SSO/OIDC
   redirect_uri construction in `backend/app/core/config.py`).

## Apply order

```bash
kubectl apply -k k8s/                      # namespace, configmap, postgres,
                                            # redis, backend, celery, frontend,
                                            # ingress
kubectl apply -f k8s/secret.yaml           # see step 2 above

# Migrations: delete-then-apply-then-wait, since a Job's spec is immutable
# and this needs to re-run on every deploy that includes a new migration.
kubectl delete job/migrate -n grc-platform --ignore-not-found
kubectl apply -f k8s/migration-job.yaml
kubectl wait --for=condition=complete job/migrate -n grc-platform --timeout=120s
```

Run the migration step before the first rollout reaches real traffic, and
again on every subsequent deploy that includes a migration — a CI/CD
pipeline is the natural place to script this sequence rather than running it
by hand each time.

## What's deliberately not here

- **A Helm chart / Terraform** — now drafted separately, see
  `helm/grc-platform/` and `terraform/aws/` (both with their own
  unverified-status disclaimers). These plain manifests are still the
  simplest option if you don't need Helm's templating or values-driven
  config.
- **HorizontalPodAutoscalers**, **NetworkPolicies**, **PodDisruptionBudgets** —
  none are provisioned. Reasonable next additions once this is actually
  running somewhere, but speculative without real traffic/capacity data.
- **A real secrets-manager integration** — see `secret.example.yaml`'s header.
- **StorageClass selection** for the `postgres.yaml`/`redis.yaml` PVCs —
  left to your cluster's default; pin one explicitly if that default isn't
  what you want for a database volume.
