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
| `202607100001` | Real requirement rows for NIST CSF 2.0 (14), HIPAA Security Rule (13), NIS2 (6), and DORA (5) — see the note below on why these four and not the rest of the catalog |

**Note on permission seeding**: `202607090001`'s seed step imports
`security.permissions.ALL_PERMISSIONS`/`SYSTEM_ROLES` at *migration run time*, not
at the time the file was written — so a fresh `alembic upgrade head` always seeds
whatever permission codes exist in that module today. Once this migration has
actually run against a database, though, it won't run again: any permission code
added to `security/permissions.py` *after* a database has been migrated needs its
own follow-up migration to insert the delta. This hasn't bitten anyone yet because
no environment has been deployed from this codebase, but it will the first time a
new permission is added post-launch.

**Note on `user_roles`/`role_permissions`**: both are plain many-to-many join
tables (composite PK on the two FK columns, no extra columns of their own) —
`users` has no `role_id`/`roles` column, and neither does `roles` carry a
`permission_ids` column. The API's `UserRead.role_ids` field (see `docs/api.md`)
is derived from `user_roles` at read time via the ORM relationship; it isn't a
stored/denormalized column, so there's nothing to keep in sync on writes.

**Note on `202607100001` (which frameworks got real requirement text, and
why)**: of the 10 catalog frameworks, only NIST CSF, HIPAA, NIS2, and DORA
got real requirement rows. ISO 27001/27002/27005, CIS Controls, SOC 2, and
PCI DSS remain catalog-only (name/code/version, zero requirement rows) —
those are commercially licensed standards sold by their standards bodies
(ISO, PCI SSC, AICPA, CIS), and this project has no rights to reproduce their
official requirement text, even paraphrased. NIST CSF 2.0 and the HIPAA
Security Rule (45 CFR Part 164) are US federal government works and are in
the public domain (17 U.S.C. § 105); NIS2 and DORA are EU legislation, and
the loaded rows paraphrase the legal obligations rather than quoting the
directive/regulation text. The migration's data lives in
`REQUIREMENTS_BY_FRAMEWORK` in
`backend/migrations/versions/202607100001_public_domain_requirement_catalogs.py`
— add rows there (and a follow-up migration, per the pattern below) for any
future public-domain framework content; don't add rows for the licensed
standards without first confirming a license actually permits it.

## Known gaps

- **ISO 27001 still only has 4 illustrative requirements** (Annex
  A.5.1/A.5.7/A.8.1/A.8.8) as a worked example of the generic engine, and
  ISO 27002/27005, CIS Controls, SOC 2, and PCI DSS have zero requirement
  rows at all — see the `202607100001` note above for why (commercial
  licensing, not a schema or code limitation). Loading more ISO content, or
  any content for the other licensed standards, requires either a license
  from the relevant standards body or a switch to a different source
  framework that's actually public domain.
- Migrations have been validated with `alembic upgrade head --sql` (offline SQL
  generation against the `postgresql` dialect) and exercised structurally via the
  test suite's SQLite fixtures, but have **not** been run against a live Postgres
  instance in this environment (no Docker available). The CI workflow
  (`.github/workflows/ci.yml`) runs them for real against a Postgres service
  container on every push.
