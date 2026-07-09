from uuid import UUID

from backend.app.interfaces.api.dependencies import (
    get_assessment_service,
    get_compliance_scoring_service,
    get_compliance_service,
    get_control_mapping_service,
    get_current_user,
    get_evidence_service,
    get_framework_service,
    require_permission,
)
from backend.app.modules.compliance.schemas import (
    AssessmentCreate,
    AssessmentRead,
    AssessmentResultRead,
    AssessmentResultUpdate,
    AssessmentStatusUpdate,
    ComplianceScoreRead,
    ComplianceSummary,
    ControlMappingRead,
    EvidenceCreate,
    EvidenceRead,
    FrameworkCreate,
    FrameworkRead,
    FrameworkVersionCreate,
    FrameworkVersionRead,
    RequirementCreate,
    RequirementRead,
)
from backend.app.modules.compliance.service import (
    AddEvidenceCommand,
    AssessmentService,
    ComplianceScoringService,
    ComplianceService,
    ControlMappingService,
    CreateAssessmentCommand,
    CreateFrameworkCommand,
    CreateRequirementCommand,
    FrameworkService,
)
from backend.app.modules.users.service import User
from backend.app.security.permissions import (
    ASSESSMENTS_MANAGE,
    ASSESSMENTS_READ,
    COMPLIANCE_READ,
    EVIDENCE_MANAGE,
    FRAMEWORKS_MANAGE,
)
from backend.app.workflow.state_machine import IllegalTransitionError
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get(
    "/summary",
    response_model=ComplianceSummary,
    dependencies=[Depends(require_permission(COMPLIANCE_READ))],
)
def compliance_summary(
    current_user: User = Depends(get_current_user),
    service: ComplianceService = Depends(get_compliance_service),
) -> ComplianceSummary:
    return ComplianceSummary.model_validate(service.summary(current_user.organization_id))


# --- Framework catalog --------------------------------------------------------


@router.get(
    "/frameworks",
    response_model=list[FrameworkRead],
    dependencies=[Depends(require_permission(COMPLIANCE_READ))],
)
def list_frameworks(
    current_user: User = Depends(get_current_user),
    service: FrameworkService = Depends(get_framework_service),
) -> list[FrameworkRead]:
    return [FrameworkRead.model_validate(f) for f in service.list_frameworks(current_user.organization_id)]


@router.post(
    "/frameworks",
    response_model=FrameworkRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(FRAMEWORKS_MANAGE))],
)
def create_framework(
    payload: FrameworkCreate,
    current_user: User = Depends(get_current_user),
    service: FrameworkService = Depends(get_framework_service),
) -> FrameworkRead:
    framework = service.create_framework(
        CreateFrameworkCommand(organization_id=current_user.organization_id, **payload.model_dump())
    )
    return FrameworkRead.model_validate(framework)


@router.get(
    "/frameworks/{framework_id}/versions",
    response_model=list[FrameworkVersionRead],
    dependencies=[Depends(require_permission(COMPLIANCE_READ))],
)
def list_framework_versions(
    framework_id: UUID,
    service: FrameworkService = Depends(get_framework_service),
) -> list[FrameworkVersionRead]:
    return [FrameworkVersionRead.model_validate(v) for v in service.list_versions(framework_id)]


@router.post(
    "/frameworks/{framework_id}/versions",
    response_model=FrameworkVersionRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(FRAMEWORKS_MANAGE))],
)
def create_framework_version(
    framework_id: UUID,
    payload: FrameworkVersionCreate,
    service: FrameworkService = Depends(get_framework_service),
) -> FrameworkVersionRead:
    version = service.create_version(framework_id, payload.version, payload.published_at)
    return FrameworkVersionRead.model_validate(version)


@router.get(
    "/framework-versions/{framework_version_id}/requirements",
    response_model=list[RequirementRead],
    dependencies=[Depends(require_permission(COMPLIANCE_READ))],
)
def list_requirements(
    framework_version_id: UUID,
    service: FrameworkService = Depends(get_framework_service),
) -> list[RequirementRead]:
    return [RequirementRead.model_validate(r) for r in service.list_requirements(framework_version_id)]


@router.post(
    "/framework-versions/{framework_version_id}/requirements",
    response_model=RequirementRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(FRAMEWORKS_MANAGE))],
)
def create_requirement(
    framework_version_id: UUID,
    payload: RequirementCreate,
    service: FrameworkService = Depends(get_framework_service),
) -> RequirementRead:
    requirement = service.create_requirement(
        CreateRequirementCommand(framework_version_id=framework_version_id, **payload.model_dump())
    )
    return RequirementRead.model_validate(requirement)


# --- Control <-> requirement mappings ------------------------------------------


@router.post(
    "/controls/{control_id}/mappings/{requirement_id}",
    response_model=ControlMappingRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(FRAMEWORKS_MANAGE))],
)
def map_control_to_requirement(
    control_id: UUID,
    requirement_id: UUID,
    service: ControlMappingService = Depends(get_control_mapping_service),
) -> ControlMappingRead:
    mapping = service.map_control_to_requirement(control_id, requirement_id)
    return ControlMappingRead.model_validate(mapping)


@router.get(
    "/controls/{control_id}/mappings",
    response_model=list[ControlMappingRead],
    dependencies=[Depends(require_permission(COMPLIANCE_READ))],
)
def list_mappings_for_control(
    control_id: UUID,
    service: ControlMappingService = Depends(get_control_mapping_service),
) -> list[ControlMappingRead]:
    return [ControlMappingRead.model_validate(m) for m in service.list_for_control(control_id)]


# --- Assessments ----------------------------------------------------------------


@router.get(
    "/assessments",
    response_model=list[AssessmentRead],
    dependencies=[Depends(require_permission(ASSESSMENTS_READ))],
)
def list_assessments(
    current_user: User = Depends(get_current_user),
    service: AssessmentService = Depends(get_assessment_service),
) -> list[AssessmentRead]:
    return [AssessmentRead.model_validate(a) for a in service.list_assessments(current_user.organization_id)]


@router.post(
    "/assessments",
    response_model=AssessmentRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(ASSESSMENTS_MANAGE))],
)
def create_assessment(
    payload: AssessmentCreate,
    current_user: User = Depends(get_current_user),
    service: AssessmentService = Depends(get_assessment_service),
) -> AssessmentRead:
    assessment = service.create_assessment(
        CreateAssessmentCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return AssessmentRead.model_validate(assessment)


def _get_owned_assessment(
    assessment_id: UUID, current_user: User, service: AssessmentService
) -> AssessmentRead:
    assessment = service.get_assessment(assessment_id)
    if assessment is None or assessment.organization_id != current_user.organization_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="assessment not found")
    return assessment


@router.get(
    "/assessments/{assessment_id}",
    response_model=AssessmentRead,
    dependencies=[Depends(require_permission(ASSESSMENTS_READ))],
)
def get_assessment(
    assessment_id: UUID,
    current_user: User = Depends(get_current_user),
    service: AssessmentService = Depends(get_assessment_service),
) -> AssessmentRead:
    return AssessmentRead.model_validate(_get_owned_assessment(assessment_id, current_user, service))


@router.patch(
    "/assessments/{assessment_id}/status",
    response_model=AssessmentRead,
    dependencies=[Depends(require_permission(ASSESSMENTS_MANAGE))],
)
def update_assessment_status(
    assessment_id: UUID,
    payload: AssessmentStatusUpdate,
    current_user: User = Depends(get_current_user),
    service: AssessmentService = Depends(get_assessment_service),
) -> AssessmentRead:
    _get_owned_assessment(assessment_id, current_user, service)
    try:
        assessment = service.set_status(assessment_id, payload.status)
    except IllegalTransitionError as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(exc)) from exc
    return AssessmentRead.model_validate(assessment)


@router.get(
    "/assessments/{assessment_id}/results",
    response_model=list[AssessmentResultRead],
    dependencies=[Depends(require_permission(ASSESSMENTS_READ))],
)
def list_assessment_results(
    assessment_id: UUID,
    current_user: User = Depends(get_current_user),
    service: AssessmentService = Depends(get_assessment_service),
) -> list[AssessmentResultRead]:
    _get_owned_assessment(assessment_id, current_user, service)
    return [AssessmentResultRead.model_validate(r) for r in service.list_results(assessment_id)]


@router.put(
    "/assessments/{assessment_id}/results/{requirement_id}",
    response_model=AssessmentResultRead,
    dependencies=[Depends(require_permission(ASSESSMENTS_MANAGE))],
)
def record_assessment_result(
    assessment_id: UUID,
    requirement_id: UUID,
    payload: AssessmentResultUpdate,
    current_user: User = Depends(get_current_user),
    service: AssessmentService = Depends(get_assessment_service),
) -> AssessmentResultRead:
    _get_owned_assessment(assessment_id, current_user, service)
    result = service.record_result(assessment_id, requirement_id, payload.status, payload.notes)
    return AssessmentResultRead.model_validate(result)


@router.post(
    "/assessments/{assessment_id}/compute-score",
    response_model=ComplianceScoreRead,
    dependencies=[Depends(require_permission(ASSESSMENTS_MANAGE))],
)
def compute_assessment_score(
    assessment_id: UUID,
    current_user: User = Depends(get_current_user),
    assessments: AssessmentService = Depends(get_assessment_service),
    scoring: ComplianceScoringService = Depends(get_compliance_scoring_service),
) -> ComplianceScoreRead:
    assessment = _get_owned_assessment(assessment_id, current_user, assessments)
    score = scoring.compute_and_store(assessment)
    return ComplianceScoreRead.model_validate(score)


@router.get(
    "/assessments/{assessment_id}/score",
    response_model=ComplianceScoreRead | None,
    dependencies=[Depends(require_permission(ASSESSMENTS_READ))],
)
def get_latest_assessment_score(
    assessment_id: UUID,
    current_user: User = Depends(get_current_user),
    assessments: AssessmentService = Depends(get_assessment_service),
    scoring: ComplianceScoringService = Depends(get_compliance_scoring_service),
) -> ComplianceScoreRead | None:
    _get_owned_assessment(assessment_id, current_user, assessments)
    score = scoring.get_latest(assessment_id)
    return ComplianceScoreRead.model_validate(score) if score else None


# --- Evidence -------------------------------------------------------------------


@router.post(
    "/evidence",
    response_model=EvidenceRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(EVIDENCE_MANAGE))],
)
def add_evidence(
    payload: EvidenceCreate,
    current_user: User = Depends(get_current_user),
    service=Depends(get_evidence_service),
) -> EvidenceRead:
    evidence = service.add_evidence(
        AddEvidenceCommand(
            organization_id=current_user.organization_id,
            uploaded_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return EvidenceRead.model_validate(evidence)


@router.get(
    "/assessments/results/{assessment_result_id}/evidence",
    response_model=list[EvidenceRead],
    dependencies=[Depends(require_permission(ASSESSMENTS_READ))],
)
def list_evidence_for_result(
    assessment_result_id: UUID,
    service=Depends(get_evidence_service),
) -> list[EvidenceRead]:
    return [EvidenceRead.model_validate(e) for e in service.list_for_result(assessment_result_id)]
