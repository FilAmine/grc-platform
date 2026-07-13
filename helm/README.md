# Helm chart

Templates `k8s/`'s plain-manifest design (see that directory's own README
for the underlying topology and status) into a proper Helm chart. Same
status disclaimer applies here too: **not applied to or validated against
a real cluster** — no `helm` binary was available where this was written,
so nothing here has been `helm template`d, `helm lint`ed, or
`helm install --dry-run`ed. Treat it as a solid draft, not a tested
deployment artifact.

## What Helm gets you over the plain `k8s/` manifests

- **Values-driven config** instead of hand-editing placeholder domains/image
  tags across a dozen files — see `values.yaml`.
- **The migration Job is a proper `pre-install,pre-upgrade` hook**
  (`templates/migration-job.yaml`), so `helm install`/`helm upgrade` blocks
  on it automatically and fails the whole release if it fails, rather than
  needing the manual `kubectl delete job/migrate && kubectl apply && kubectl wait`
  sequence `k8s/README.md` documents.
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

Run `--dry-run --debug` first on a real cluster before trusting this, per
the unverified-status disclaimer above.

## What's deliberately not here

Same list `k8s/README.md` gives, unchanged by moving to Helm:
HorizontalPodAutoscalers, NetworkPolicies, PodDisruptionBudgets, a real
secrets-manager integration, explicit StorageClass selection. Also not
attempted: chart tests (`helm test`), a `NOTES.txt` post-install banner, or
publishing this to a chart repository — all reasonable next additions once
this is actually running somewhere.
