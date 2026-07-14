# Helm chart

Templates `k8s/`'s plain-manifest design (see that directory's own README
for the underlying topology and status) into a proper Helm chart.

## Status: actually installed and verified on a real (local) cluster

Updated twice now. First pass: `helm lint`/`helm template` plus
[`kubeconform`](https://github.com/yannh/kubeconform) schema validation,
all clean — but that never *executes* a release, so it couldn't catch
ordering bugs. Second pass: Docker Desktop + a local
[`kind`](https://kind.sigs.k8s.io/) cluster (free, no AWS account) let this
chart actually be `helm install`ed for real, and it caught a real bug the
static checks never could have:

**The migration Job was originally a `pre-install,pre-upgrade` hook.**
Helm fires `pre-install` hooks *before* creating any of the chart's
regular resources — not just Postgres, but the ConfigMap and Secret the
Job's `envFrom` depends on too. The first live install failed immediately:
`CreateContainerConfigError: configmap "...-config" not found`. Fixed by
moving the hook to `post-install,post-upgrade` and adding a
`wait-for-postgres` initContainer (a plain TCP-reachability retry loop
using the already-injected `DATABASE_URL`, no extra tooling needed) so the
migration doesn't race a Postgres pod that's created but not yet ready —
see `templates/migration-job.yaml`'s header comment for the full story.

After the fix, a real `helm install` against the local `kind` cluster
(locally built `grc-backend:local`/`grc-frontend:local` images, loaded via
`kind load docker-image`, `ingress.enabled=false` since `kind` has no
ingress controller) succeeded end to end and was verified live:

- All 6 pods (backend, celery-worker, celery-beat, frontend, postgres,
  redis) reached `Running`/`1/1 Ready`.
- The migration Job actually ran `alembic upgrade head` against the real
  Postgres pod — confirmed by `psql`-ing in and checking `alembic_version`
  (`202607180001`, the true head) and `\dt` (every table, including all 5
  EBIOS RM workshops' tables, genuinely present).
- `kubectl port-forward` to the backend Service and a real `curl` got
  `{"status":"ok","service":"GRC Platform"}` from `/health`, `200` from
  `/api/v1/openapi.json`, and `200` with the real page title from the
  frontend Service.

The test release and cluster were torn down afterward
(`helm uninstall` + `kind delete cluster`) — nothing was left running.
**Still not exercised**: a real ingress controller/cert-manager
interaction (this test disabled ingress entirely, since `kind` has none by
default), and anything at real-world scale/traffic. If you want to
reproduce this yourself: `kind create cluster`, build+`kind load
docker-image` the two images, then `helm install` with `ingress.enabled:
false` and real `secrets.secretKey`/`secrets.postgresPassword` values.

## What Helm gets you over the plain `k8s/` manifests

- **Values-driven config** instead of hand-editing placeholder domains/image
  tags across a dozen files — see `values.yaml`.
- **The migration Job is a proper `post-install,post-upgrade` hook**
  (`templates/migration-job.yaml`) with its own Postgres-readiness wait,
  so `helm install`/`helm upgrade` blocks on it automatically and fails the
  whole release if it fails, rather than needing the manual
  `kubectl delete job/migrate && kubectl apply && kubectl wait` sequence
  `k8s/README.md` documents.
- **Release-scoped resource names** (`{{ .Release.Name }}-grc-platform-*`),
  so multiple releases (e.g. staging + prod, or two customers) can coexist
  in one cluster without name collisions — the plain manifests use fixed
  names and can't do this.

## Before installing anything

Same three prerequisites `k8s/README.md` lists, adapted for Helm:

1. **Build and push real images** (see `k8s/README.md`'s exact commands —
   identical here, just referenced via `values.yaml`'s `backend.image`/
   `frontend.image`).
2. **Set real secrets.** Don't edit `values.yaml`'s `secrets:` block
   in place. Create a separate, gitignored `values-secret.yaml`:

   ```yaml
   secrets:
     secretKey: "<a real 32+ byte random value>"
     postgresPassword: "<a real password>"
     openaiApiKey: "<if using AI_PROVIDER=openai>"
   ```

   and pass it at install time (see below). This is still a plaintext
   Kubernetes Secret at the end of the day (base64-at-rest, not
   encrypted) — see `values.yaml`'s header and `k8s/secret.example.yaml`
   for why a real secrets-manager integration is a separate, undone piece
   of work.
3. **Set real domains** in `values.yaml`'s `ingress:` and `config:` blocks
   (`grc.example.com`/`api.grc.example.com` placeholders), consistently —
   a mismatch breaks CORS or the SSO/OIDC `redirect_uri` construction.

## Install

```bash
helm install grc-platform ./helm/grc-platform \
  --namespace grc-platform --create-namespace \
  -f values-secret.yaml \
  --set backend.image.tag=<your-tag> \
  --set frontend.image.tag=<your-tag>

# Later, to roll out a new version or config change:
helm upgrade grc-platform ./helm/grc-platform \
  --namespace grc-platform \
  -f values-secret.yaml \
  --set backend.image.tag=<new-tag>
```

Run `--dry-run --debug` first against your real target cluster before
trusting this — a local `kind` cluster confirmed the chart installs
cleanly (see the status section above), but every cluster's ingress
controller, StorageClass defaults, and available AZs/capacity differ.

## What's deliberately not here

Same list `k8s/README.md` gives, unchanged by moving to Helm:
HorizontalPodAutoscalers, NetworkPolicies, PodDisruptionBudgets, a real
secrets-manager integration, explicit StorageClass selection. Also not
attempted: chart tests (`helm test`), a `NOTES.txt` post-install banner, or
publishing this to a chart repository — all reasonable next additions once
this is actually running somewhere.
