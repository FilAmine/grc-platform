# Database

PostgreSQL 16. Every migration lives in `backend/migrations/versions/`, applied in
order by Alembic. Run `alembic upgrade head` (or let the `backend` container do it
on startup — see `docker-compose.yml`).

## Conventions

- **UUID primary keys** everywhere (`UUIDPKMixin`), generated client-side
  (`uuid4()`) rather than by the database, so application code can reference an
  entity's ID before the row is committed.
- **Soft delete** (`SoftDeleteMixin` → `deleted_at`) on tenant-owned business
  objects (organizations, risks, controls, users, assessments, documents, assets,
  evidence). Rows are never hard-deleted; repositories filter
  `deleted_at IS NULL` on every read. Association/history tables (audit findings,
  chat messages, refresh tokens, etc.) don't soft-delete — they're immutable
  records, not editable business objects.
- **Audit columns** (`AuditColumnsMixin` → `created_by_id`/`updated_by_id`,
  nullable FKs to `users.id`) on most business tables. Nullable because the very
  first user of a tenant (created during self-service registration) has no prior
  actor to reference, and system-seeded rows (frameworks, permissions, system
  roles) have no user at all.
- **Tenant scoping** (`TenantScopedMixin` → `organization_id`, FK to
  `organizations.id`) on every tenant-owned table. `organizations` itself has no
  `organization_id` — it *is* the tenant root.
- **Naming convention**: `Base.metadata` has an explicit naming convention
  (`ix_<table>_<cols>`, `fk_<table>_<cols>_<ref_table>`, `pk_<table>`,
  `uq_<table>_<cols>`) so constraint names are deterministic and migrations don't
  depend on driver-generated names.

## System vs. custom rows (the recurring `organization_id IS NULL` pattern)

Three tables — `roles`, `frameworks`, `prompt_templates` — support both
platform-wide "system" rows (`organization_id IS NULL`, `is_system=True`, seeded by
migration, read-only via the API) and tenant-private "custom" rows
(`organization_id` set, `is_system=False`, created via the API). Repository `list()`
methods for these tables return `WHERE organization_id = :tenant OR organization_id
IS NULL` — every tenant sees the shared catalog plus their own private rows.

## Circular foreign keys

Two tables reference each other:

- `organizations.created_by_id`/`updated_by_id` → `users.id`
- `users.organization_id` → `organizations.id`

and similarly `documents.published_version_id` → `document_versions.id` while
`document_versions.document_id` → `documents.id`.

Migrations resolve this by creating the first table's audit/reference columns as
plain nullable UUID columns (no FK constraint), creating the second table, then
adding the FK constraint via `op.create_foreign_key` once both tables exist. See
migration `202607090001_auth_rbac_and_tenancy.py` and
`202607090004_documents.py`.

## Migration history

| Revision | Adds |
|---|---|
| `202606250001` | `organizations`, `risks`, `controls` (original bootstrap) |
| `202607090001` | `users`, `permissions`, `roles`, `role_permissions`, `user_roles`, `refresh_tokens`; retrofits `deleted_at`/audit columns onto the three original tables; seeds the permission catalog + system roles |
| `202607090002` | Generic compliance engine: `frameworks`, `framework_versions`, `control_categories`, `requirements`, `control_mappings`, `assessments`, `assessment_results`, `evidence`, `compliance_scores`; seeds the framework catalog (ISO 27001/27002/27005, NIST CSF, NIS2, DORA, CIS Controls, SOC 2, PCI DSS, HIPAA) and 4 real ISO 27001:2022 Annex A requirements as a worked example |
| `202607090003` | `audits`, `checklist_items`, `findings`, `corrective_actions` |
| `202607090004` | `documents`, `document_versions`, `document_approvals` |
| `202607090005` | `assets` (CMDB) |
| `202607090006` | `prompt_templates`, `knowledge_base_documents`, `chat_sessions`, `chat_messages` |
| `202607090007` | `notifications` |

**Note on permission seeding**: `202607090001`'s seed step imports
`security.permissions.ALL_PERMISSIONS`/`SYSTEM_ROLES` at *migration run time*, not
at the time the file was written — so a fresh `alembic upgrade head` always seeds
whatever permission codes exist in that module today. Once this migration has
actually run against a database, though, it won't run again: any permission code
added to `security/permissions.py` *after* a database has been migrated needs its
own follow-up migration to insert the delta. This hasn't bitten anyone yet because
no environment has been deployed from this codebase, but it will the first time a
new permission is added post-launch.

## Known gaps

- **Only 4 real requirements are loaded** (ISO 27001:2022, Annex A.5.1/A.5.7/A.8.1/A.8.8),
  as a working example of the generic engine. Loading full official requirement
  text for every catalog entry is a data-loading exercise (and in several cases —
  PCI DSS, HIPAA — involves licensed/restricted content), not a schema or code
  change.
- Migrations have been validated with `alembic upgrade head --sql` (offline SQL
  generation against the `postgresql` dialect) and exercised structurally via the
  test suite's SQLite fixtures, but have **not** been run against a live Postgres
  instance in this environment (no Docker available). The CI workflow
  (`.github/workflows/ci.yml`) runs them for real against a Postgres service
  container on every push.
