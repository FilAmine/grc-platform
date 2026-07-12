"""Central import point that registers every ORM model onto ``Base.metadata``.

Alembic's ``env.py`` imports this module for its side effects so that
``--autogenerate`` can see every table. Every module that defines SQLAlchemy
models must be imported here, otherwise migrations silently ignore it.
"""

from backend.app.modules.ai.models import (
    ChatMessageModel,
    ChatSessionModel,
    KnowledgeBaseDocumentModel,
    PromptTemplateModel,
)
from backend.app.modules.assets.models import AssetModel
from backend.app.modules.audits.models import (
    AuditModel,
    ChecklistItemModel,
    CorrectiveActionModel,
    FindingModel,
)
from backend.app.modules.auth.models import RefreshTokenModel
from backend.app.modules.compliance.models import (
    AssessmentModel,
    AssessmentResultModel,
    ComplianceScoreModel,
    ControlCategoryModel,
    ControlMappingModel,
    EvidenceModel,
    FrameworkModel,
    FrameworkVersionModel,
    RequirementModel,
)
from backend.app.modules.controls.models import ControlModel
from backend.app.modules.departments.models import DepartmentModel
from backend.app.modules.documents.models import (
    DocumentApprovalModel,
    DocumentModel,
    DocumentVersionModel,
)
from backend.app.modules.feared_events.models import FearedEventModel
from backend.app.modules.incidents.models import IncidentModel
from backend.app.modules.notifications.models import NotificationModel
from backend.app.modules.organizations.models import OrganizationModel
from backend.app.modules.permissions.models import PermissionModel
from backend.app.modules.risks.models import RiskModel
from backend.app.modules.roles.models import RoleModel, role_permissions
from backend.app.modules.sso.models import SsoConnectionModel
from backend.app.modules.tasks.models import TaskModel
from backend.app.modules.tenants.models import TenantModel
from backend.app.modules.threats.models import ThreatModel
from backend.app.modules.users.models import UserModel, user_roles
from backend.app.modules.vulnerabilities.models import VulnerabilityModel

__all__ = [
    "AssessmentModel",
    "AssessmentResultModel",
    "AssetModel",
    "AuditModel",
    "ChatMessageModel",
    "ChatSessionModel",
    "ChecklistItemModel",
    "ComplianceScoreModel",
    "CorrectiveActionModel",
    "DepartmentModel",
    "DocumentApprovalModel",
    "DocumentModel",
    "DocumentVersionModel",
    "FindingModel",
    "ControlCategoryModel",
    "ControlMappingModel",
    "ControlModel",
    "EvidenceModel",
    "FearedEventModel",
    "FrameworkModel",
    "FrameworkVersionModel",
    "IncidentModel",
    "KnowledgeBaseDocumentModel",
    "NotificationModel",
    "OrganizationModel",
    "PromptTemplateModel",
    "PermissionModel",
    "RefreshTokenModel",
    "RequirementModel",
    "RiskModel",
    "RoleModel",
    "SsoConnectionModel",
    "TaskModel",
    "TenantModel",
    "ThreatModel",
    "UserModel",
    "VulnerabilityModel",
    "role_permissions",
    "user_roles",
]
