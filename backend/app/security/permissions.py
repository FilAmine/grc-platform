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
AI_USE = "ai:use"
AI_MANAGE = "ai:manage"
SSO_MANAGE = "sso:manage"
DEPARTMENTS_READ = "departments:read"
DEPARTMENTS_MANAGE = "departments:manage"
THREATS_READ = "threats:read"
THREATS_MANAGE = "threats:manage"
VULNERABILITIES_READ = "vulnerabilities:read"
VULNERABILITIES_MANAGE = "vulnerabilities:manage"
INCIDENTS_READ = "incidents:read"
INCIDENTS_MANAGE = "incidents:manage"
FEARED_EVENTS_READ = "feared_events:read"
FEARED_EVENTS_MANAGE = "feared_events:manage"
TASKS_READ = "tasks:read"
TASKS_MANAGE = "tasks:manage"
RISK_SOURCES_READ = "risk_sources:read"
RISK_SOURCES_MANAGE = "risk_sources:manage"
RISK_ORIGINS_READ = "risk_origins:read"
RISK_ORIGINS_MANAGE = "risk_origins:manage"
ECOSYSTEM_PARTIES_READ = "ecosystem_parties:read"
ECOSYSTEM_PARTIES_MANAGE = "ecosystem_parties:manage"
STRATEGIC_SCENARIOS_READ = "strategic_scenarios:read"
STRATEGIC_SCENARIOS_MANAGE = "strategic_scenarios:manage"
OPERATIONAL_SCENARIOS_READ = "operational_scenarios:read"
OPERATIONAL_SCENARIOS_MANAGE = "operational_scenarios:manage"
RISK_TREATMENTS_READ = "risk_treatments:read"
RISK_TREATMENTS_MANAGE = "risk_treatments:manage"

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
    PermissionDef(AI_USE, "Use the AI chat assistant and prompt library"),
    PermissionDef(AI_MANAGE, "Manage prompt templates and the AI knowledge base"),
    PermissionDef(SSO_MANAGE, "Configure the organization's SSO (OIDC) connection"),
    PermissionDef(DEPARTMENTS_READ, "View the department hierarchy"),
    PermissionDef(DEPARTMENTS_MANAGE, "Create departments"),
    PermissionDef(THREATS_READ, "View the threat catalog"),
    PermissionDef(THREATS_MANAGE, "Create threats"),
    PermissionDef(VULNERABILITIES_READ, "View the vulnerability register"),
    PermissionDef(VULNERABILITIES_MANAGE, "Create vulnerabilities"),
    PermissionDef(INCIDENTS_READ, "View incidents"),
    PermissionDef(INCIDENTS_MANAGE, "Create incidents and change their status"),
    PermissionDef(FEARED_EVENTS_READ, "View feared events"),
    PermissionDef(FEARED_EVENTS_MANAGE, "Create feared events"),
    PermissionDef(TASKS_READ, "View tasks"),
    PermissionDef(TASKS_MANAGE, "Create tasks and change their status"),
    PermissionDef(RISK_SOURCES_READ, "View the EBIOS RM risk source catalog"),
    PermissionDef(RISK_SOURCES_MANAGE, "Create risk sources"),
    PermissionDef(RISK_ORIGINS_READ, "View EBIOS RM risk origin (SR/OV) pairs"),
    PermissionDef(RISK_ORIGINS_MANAGE, "Create and prioritize risk origin (SR/OV) pairs"),
    PermissionDef(ECOSYSTEM_PARTIES_READ, "View the EBIOS RM ecosystem party catalog"),
    PermissionDef(ECOSYSTEM_PARTIES_MANAGE, "Create ecosystem parties"),
    PermissionDef(STRATEGIC_SCENARIOS_READ, "View EBIOS RM strategic scenarios"),
    PermissionDef(STRATEGIC_SCENARIOS_MANAGE, "Create strategic scenarios"),
    PermissionDef(OPERATIONAL_SCENARIOS_READ, "View EBIOS RM operational scenarios"),
    PermissionDef(OPERATIONAL_SCENARIOS_MANAGE, "Create operational scenarios"),
    PermissionDef(RISK_TREATMENTS_READ, "View EBIOS RM risk treatment decisions"),
    PermissionDef(RISK_TREATMENTS_MANAGE, "Record risk treatment decisions"),
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
        AI_USE,
        AI_MANAGE,
        DEPARTMENTS_READ,
        DEPARTMENTS_MANAGE,
        THREATS_READ,
        THREATS_MANAGE,
        VULNERABILITIES_READ,
        VULNERABILITIES_MANAGE,
        INCIDENTS_READ,
        INCIDENTS_MANAGE,
        FEARED_EVENTS_READ,
        FEARED_EVENTS_MANAGE,
        TASKS_READ,
        TASKS_MANAGE,
        RISK_SOURCES_READ,
        RISK_SOURCES_MANAGE,
        RISK_ORIGINS_READ,
        RISK_ORIGINS_MANAGE,
        ECOSYSTEM_PARTIES_READ,
        ECOSYSTEM_PARTIES_MANAGE,
        STRATEGIC_SCENARIOS_READ,
        STRATEGIC_SCENARIOS_MANAGE,
        OPERATIONAL_SCENARIOS_READ,
        OPERATIONAL_SCENARIOS_MANAGE,
        RISK_TREATMENTS_READ,
        RISK_TREATMENTS_MANAGE,
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
        AI_USE,
        DEPARTMENTS_READ,
        THREATS_READ,
        VULNERABILITIES_READ,
        INCIDENTS_READ,
        FEARED_EVENTS_READ,
        TASKS_READ,
        RISK_SOURCES_READ,
        RISK_ORIGINS_READ,
        ECOSYSTEM_PARTIES_READ,
        STRATEGIC_SCENARIOS_READ,
        OPERATIONAL_SCENARIOS_READ,
        RISK_TREATMENTS_READ,
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
        AI_USE,
        DEPARTMENTS_READ,
        THREATS_READ,
        VULNERABILITIES_READ,
        INCIDENTS_READ,
        FEARED_EVENTS_READ,
        TASKS_READ,
        RISK_SOURCES_READ,
        RISK_ORIGINS_READ,
        ECOSYSTEM_PARTIES_READ,
        STRATEGIC_SCENARIOS_READ,
        OPERATIONAL_SCENARIOS_READ,
        RISK_TREATMENTS_READ,
    ),
}
