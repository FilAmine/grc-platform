"""The platform's controlled vocabulary of permission codes.

Codes are ``resource:action`` strings stored in the ``permissions`` table and
seeded by migration. Adding a new permission means adding it here *and* to the
seed data migration — this module is the single source of truth checked by
``require_permission`` dependencies.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class PermissionDef:
    code: str
    description: str


ORGANIZATIONS_READ = "organizations:read"
ORGANIZATIONS_MANAGE = "organizations:manage"
USERS_READ = "users:read"
USERS_MANAGE = "users:manage"
ROLES_MANAGE = "roles:manage"
RISKS_READ = "risks:read"
RISKS_MANAGE = "risks:manage"
CONTROLS_READ = "controls:read"
CONTROLS_MANAGE = "controls:manage"
COMPLIANCE_READ = "compliance:read"
FRAMEWORKS_MANAGE = "frameworks:manage"
ASSESSMENTS_READ = "assessments:read"
ASSESSMENTS_MANAGE = "assessments:manage"
EVIDENCE_MANAGE = "evidence:manage"
AUDITS_READ = "audits:read"
AUDITS_MANAGE = "audits:manage"
DOCUMENTS_READ = "documents:read"
DOCUMENTS_MANAGE = "documents:manage"
ASSETS_READ = "assets:read"
ASSETS_MANAGE = "assets:manage"

ALL_PERMISSIONS: tuple[PermissionDef, ...] = (
    PermissionDef(ORGANIZATIONS_READ, "View organization settings"),
    PermissionDef(ORGANIZATIONS_MANAGE, "Manage organization settings"),
    PermissionDef(USERS_READ, "View users"),
    PermissionDef(USERS_MANAGE, "Create, update, deactivate users"),
    PermissionDef(ROLES_MANAGE, "Create roles and assign permissions"),
    PermissionDef(RISKS_READ, "View the risk register"),
    PermissionDef(RISKS_MANAGE, "Create and update risks"),
    PermissionDef(CONTROLS_READ, "View controls"),
    PermissionDef(CONTROLS_MANAGE, "Create and update controls"),
    PermissionDef(COMPLIANCE_READ, "View compliance posture and scores"),
    PermissionDef(FRAMEWORKS_MANAGE, "Create custom frameworks, versions, and requirements"),
    PermissionDef(ASSESSMENTS_READ, "View assessments and their results"),
    PermissionDef(ASSESSMENTS_MANAGE, "Create assessments and record results"),
    PermissionDef(EVIDENCE_MANAGE, "Upload and attach evidence"),
    PermissionDef(AUDITS_READ, "View audits and findings"),
    PermissionDef(AUDITS_MANAGE, "Plan audits and record findings"),
    PermissionDef(DOCUMENTS_READ, "View policies and documents"),
    PermissionDef(DOCUMENTS_MANAGE, "Author and approve documents"),
    PermissionDef(ASSETS_READ, "View the CMDB"),
    PermissionDef(ASSETS_MANAGE, "Create and update CMDB assets"),
)

# Default role -> permission-code mapping seeded for every new organization.
SYSTEM_ROLES: dict[str, tuple[str, ...] | None] = {
    "Admin": None,  # None means "all permissions" — resolved at seed time.
    "Manager": (
        ORGANIZATIONS_READ,
        USERS_READ,
        RISKS_READ,
        RISKS_MANAGE,
        CONTROLS_READ,
        CONTROLS_MANAGE,
        COMPLIANCE_READ,
        ASSESSMENTS_READ,
        ASSESSMENTS_MANAGE,
        EVIDENCE_MANAGE,
        AUDITS_READ,
        AUDITS_MANAGE,
        DOCUMENTS_READ,
        DOCUMENTS_MANAGE,
        ASSETS_READ,
        ASSETS_MANAGE,
    ),
    "Auditor": (
        ORGANIZATIONS_READ,
        USERS_READ,
        RISKS_READ,
        CONTROLS_READ,
        COMPLIANCE_READ,
        ASSESSMENTS_READ,
        ASSESSMENTS_MANAGE,
        EVIDENCE_MANAGE,
        AUDITS_READ,
        AUDITS_MANAGE,
        DOCUMENTS_READ,
        ASSETS_READ,
    ),
    "Viewer": (
        ORGANIZATIONS_READ,
        RISKS_READ,
        CONTROLS_READ,
        COMPLIANCE_READ,
        ASSESSMENTS_READ,
        AUDITS_READ,
        DOCUMENTS_READ,
        ASSETS_READ,
    ),
}
