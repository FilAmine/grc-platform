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
| `202607100002` | Adds the `sso:manage` permission and grants it to the global `Admin` system role — the first real (idempotent, find-or-create) instance of the permission-seeding follow-up-migration pattern described below |
| `202607100003` | `sso_connections` (per-organization OIDC configuration) |
| `202607110001` | `departments` (self-referential hierarchy), `threats`, `vulnerabilities`; seeds the 6 new permission codes and grants them to the 4 global system roles — the second real instance of the idempotent permission-seeding pattern `202607100002` established |
| `202607120001` | `incidents` (with a `resolved_at` column driven by a real status-workflow state machine, unlike the other catalog/register tables); seeds 2 new permission codes and grants them — the third instance of the idempotent permission-seeding pattern |

**Note on permission seeding**: `202607090001`'s seed step imports
`security.permissions.ALL_PERMISSIONS`/`SYSTEM_ROLES` at *migration run time*, not
at the time the file was written — so a fresh `alembic upgrade head` always seeds
whatever permission codes exist in that module today. Once this migration has
actually run against a database, though, it won't run again: any permission code
added to `security/permissions.py` *after* a database has been migrated needs its
own follow-up migration to insert the delta. `202607100002` (adding `sso:manage`)
is the first real instance of this — and it's a genuine trap either way: a blind
`INSERT` there hits a duplicate-key error on any database that was migrated
*fresh* after `sso:manage` was added to the source file (because `202607090001`'s
dynamic seed already picked it up), while skipping the insert entirely would
leave it missing on any database migrated *before* that point. The fix is to
make the follow-up migration idempotent (find-or-create for both the permission
row and the role grant), not to special-case which scenario you think you're in
— confirmed by actually hitting the duplicate-key error against a real local
Postgres instance while developing `202607100002`, not just reasoned about.
Any future new permission should follow the same idempotent pattern.

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
- Every migration is validated with `alembic upgrade head --sql` (offline SQL
  generation against the `postgresql` dialect) before being committed, and the
  CI workflow (`.github/workflows/ci.yml`) runs them for real against a
  Postgres service container on every push. Several migrations (including
  `202607100001`–`202607100003`) have additionally been exercised by hand
  against a real local Postgres instance (portable binaries, no Docker) during
  development — full up/down/up round-trips, not just the offline preview —
  since offline mode can't catch everything: it's how the `create_type=False`
  ENUM bug (see `202606250001`'s note) and a non-portable multi-argument
  `.where()` in `202607100002`'s original draft were both actually found.
- **`sso_connections.client_secret` is plaintext** — see `docs/security.md`'s
  SSO/OIDC section for the same caveat from the API/security angle.
