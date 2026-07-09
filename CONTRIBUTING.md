# Contributing

## Before you start

Read `docs/architecture.md` for the module pattern and `docs/development.md` for
the concrete steps to add one. Following the existing pattern (domain logic in
`service.py` with zero framework imports, a `Store` Protocol implemented by
`repository.py`, thin `api.py` routers) matters more than any individual line of
code — it's what keeps 13+ modules consistent enough to navigate.

## Workflow

1. Branch from `main`.
2. Make your change, following the module pattern for new modules.
3. `ruff check backend` — must be clean (0 errors). CI enforces this.
4. `pytest backend/tests -q --cov=backend/app --cov-fail-under=80` — must pass.
   New modules/endpoints need real tests (a happy path + a cross-tenant isolation
   check is the minimum bar this codebase holds itself to — see any
   `test_tenant_isolation.py`-style test for the pattern).
5. If you added/changed a model, write the Alembic migration by hand (see
   `docs/development.md#migrations`) and validate it with
   `alembic upgrade head --sql` at minimum.
6. Frontend changes: `npx tsc -b` must pass; if you touch a page a human will
   click through, actually run `npm run dev` and check it in a browser — a green
   typecheck doesn't mean the feature works.
7. Open a PR. CI (`.github/workflows/ci.yml`) runs lint, migrations-against-Postgres,
   tests-with-coverage-gate, frontend typecheck+build, and Docker image builds.

## Commit style

Explain *why*, not *what* — the diff already shows what changed. If you're fixing
a bug you found incidentally while building something else, say so; it helps
future readers understand why an unrelated-looking line changed.

## Scope discipline

Don't bundle unrelated changes into one PR. If you notice something else that
needs fixing while working (dead code, a stale comment, a missing test), either
fix it in a small dedicated follow-up or flag it — don't let it balloon the PR
you're actually trying to get reviewed.
