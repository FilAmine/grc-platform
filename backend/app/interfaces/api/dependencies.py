from collections.abc import Generator
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.app.core.config import settings
from backend.app.database import get_db_session
from backend.app.modules.audits.repository import SqlAlchemyAuditRepository
from backend.app.modules.audits.service import AuditService
from backend.app.modules.auth.repository import SqlAlchemyRefreshTokenRepository
from backend.app.modules.auth.service import AuthService
from backend.app.modules.compliance.repository import (
    SqlAlchemyAssessmentRepository,
    SqlAlchemyComplianceScoreRepository,
    SqlAlchemyControlMappingRepository,
    SqlAlchemyEvidenceRepository,
    SqlAlchemyFrameworkRepository,
)
from backend.app.modules.compliance.service import (
    AssessmentService,
    ComplianceScoringService,
    ComplianceService,
    ControlMappingService,
    EvidenceService,
    FrameworkService,
)
from backend.app.modules.controls.repository import (
    SqlAlchemyControlRepository,
)
from backend.app.modules.controls.service import ControlService
from backend.app.modules.dashboard.service import DashboardService
from backend.app.modules.documents.repository import SqlAlchemyDocumentRepository
from backend.app.modules.documents.service import DocumentService
from backend.app.modules.organizations.repository import (
    SqlAlchemyOrganizationRepository,
)
from backend.app.modules.organizations.service import OrganizationService
from backend.app.modules.permissions.repository import SqlAlchemyPermissionRepository
from backend.app.modules.permissions.service import PermissionService
from backend.app.modules.risks.repository import (
    SqlAlchemyRiskRepository,
)
from backend.app.modules.risks.service import RiskService
from backend.app.modules.roles.repository import SqlAlchemyRoleRepository
from backend.app.modules.roles.service import RoleService
from backend.app.modules.users.repository import SqlAlchemyUserRepository
from backend.app.modules.users.service import User, UserService
from backend.app.security.tokens import InvalidTokenError, decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.api_v1_prefix}/auth/login")


def get_session() -> Generator[Session, None, None]:
    yield from get_db_session()


def get_organization_service(session: Session = Depends(get_session)) -> OrganizationService:
    return OrganizationService(SqlAlchemyOrganizationRepository(session))


def get_risk_service(session: Session = Depends(get_session)) -> RiskService:
    return RiskService(SqlAlchemyRiskRepository(session))


def get_control_service(session: Session = Depends(get_session)) -> ControlService:
    return ControlService(SqlAlchemyControlRepository(session))


def get_compliance_service(session: Session = Depends(get_session)) -> ComplianceService:
    organizations = OrganizationService(SqlAlchemyOrganizationRepository(session))
    risks = RiskService(SqlAlchemyRiskRepository(session))
    controls = ControlService(SqlAlchemyControlRepository(session))
    return ComplianceService(organizations=organizations, risks=risks, controls=controls)


def get_dashboard_service(
    compliance: ComplianceService = Depends(get_compliance_service),
) -> DashboardService:
    return DashboardService(compliance)


def get_framework_service(session: Session = Depends(get_session)) -> FrameworkService:
    return FrameworkService(SqlAlchemyFrameworkRepository(session))


def get_control_mapping_service(session: Session = Depends(get_session)) -> ControlMappingService:
    return ControlMappingService(SqlAlchemyControlMappingRepository(session))


def get_assessment_service(session: Session = Depends(get_session)) -> AssessmentService:
    return AssessmentService(
        SqlAlchemyAssessmentRepository(session), SqlAlchemyFrameworkRepository(session)
    )


def get_evidence_service(session: Session = Depends(get_session)) -> EvidenceService:
    return EvidenceService(SqlAlchemyEvidenceRepository(session))


def get_compliance_scoring_service(
    assessments: AssessmentService = Depends(get_assessment_service),
    session: Session = Depends(get_session),
) -> ComplianceScoringService:
    return ComplianceScoringService(assessments, SqlAlchemyComplianceScoreRepository(session))


def get_audit_service(session: Session = Depends(get_session)) -> AuditService:
    return AuditService(SqlAlchemyAuditRepository(session))


def get_document_service(session: Session = Depends(get_session)) -> DocumentService:
    return DocumentService(SqlAlchemyDocumentRepository(session))


def get_permission_service(session: Session = Depends(get_session)) -> PermissionService:
    return PermissionService(SqlAlchemyPermissionRepository(session))


def get_role_service(session: Session = Depends(get_session)) -> RoleService:
    return RoleService(SqlAlchemyRoleRepository(session))


def get_user_service(session: Session = Depends(get_session)) -> UserService:
    return UserService(SqlAlchemyUserRepository(session))


def get_auth_service(session: Session = Depends(get_session)) -> AuthService:
    return AuthService(
        organizations=get_organization_service(session),
        users=get_user_service(session),
        roles=get_role_service(session),
        refresh_tokens=SqlAlchemyRefreshTokenRepository(session),
    )


_CREDENTIALS_ERROR = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    user_service: UserService = Depends(get_user_service),
) -> User:
    try:
        payload = decode_access_token(token)
    except InvalidTokenError as exc:
        raise _CREDENTIALS_ERROR from exc
    subject = payload.get("sub")
    if subject is None:
        raise _CREDENTIALS_ERROR
    try:
        user_id = UUID(subject)
    except ValueError as exc:
        raise _CREDENTIALS_ERROR from exc
    user = user_service.get_user(user_id)
    if user is None or not user.is_active:
        raise _CREDENTIALS_ERROR
    return user


def require_permission(permission_code: str):
    def _dependency(
        current_user: User = Depends(get_current_user),
        user_service: UserService = Depends(get_user_service),
    ) -> User:
        if current_user.is_superuser:
            return current_user
        if not user_service.has_permission(current_user.id, permission_code):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"missing permission: {permission_code}",
            )
        return current_user

    return _dependency
