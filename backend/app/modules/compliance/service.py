from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, date, datetime
from enum import StrEnum
from typing import Protocol
from uuid import UUID

from backend.app.modules.controls.service import Control, ControlStatus
from backend.app.modules.organizations.service import Organization
from backend.app.modules.risks.service import Risk, RiskStatus


class OrganizationReader(Protocol):
    def list_organizations(self) -> list[Organization]:
        raise NotImplementedError


class RiskReader(Protocol):
    def list_risks(self, organization_id: UUID | None = None) -> list[Risk]:
        raise NotImplementedError


class ControlReader(Protocol):
    def list_controls(self, organization_id: UUID | None = None) -> list[Control]:
        raise NotImplementedError


class AssessmentStatus(StrEnum):
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ARCHIVED = "archived"


class RequirementResultStatus(StrEnum):
    NOT_ASSESSED = "not_assessed"
    COMPLIANT = "compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NON_COMPLIANT = "non_compliant"
    NOT_APPLICABLE = "not_applicable"


@dataclass(frozen=True)
class ComplianceMetric:
    key: str
    value: int | str


class ComplianceService:
    def __init__(
        self,
        organizations: OrganizationReader,
        risks: RiskReader,
        controls: ControlReader,
    ) -> None:
        self._organizations = organizations
        self._risks = risks
        self._controls = controls

    def summary(self, organization_id: UUID) -> dict[str, int | str]:
        risk_items = self._risks.list_risks(organization_id)
        control_items = self._controls.list_controls(organization_id)
        open_risks = len([risk for risk in risk_items if risk.status != RiskStatus.CLOSED])
        active_controls = len(
            [control for control in control_items if control.status == ControlStatus.ACTIVE]
        )
        return {
            "organizations": 1,
            "risks_open": open_risks,
            "controls_active": active_controls,
            "posture": "attention_required" if open_risks else "healthy",
        }


# --- Framework catalog -------------------------------------------------------


@dataclass(frozen=True)
class Framework:
    id: UUID
    organization_id: UUID | None
    code: str
    name: str
    description: str
    is_system: bool
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class FrameworkVersion:
    id: UUID
    framework_id: UUID
    version: str
    published_at: date | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class Requirement:
    id: UUID
    framework_version_id: UUID
    category_id: UUID | None
    code: str
    title: str
    description: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class ControlMapping:
    id: UUID
    control_id: UUID
    requirement_id: UUID
    created_at: datetime


@dataclass(frozen=True)
class CreateFrameworkCommand:
    organization_id: UUID | None
    code: str
    name: str
    description: str = ""


@dataclass(frozen=True)
class CreateRequirementCommand:
    framework_version_id: UUID
    code: str
    title: str
    description: str = ""
    category_id: UUID | None = None


class RequirementReader(Protocol):
    def list_requirements(self, framework_version_id: UUID) -> list[Requirement]:
        raise NotImplementedError


class FrameworkStore(Protocol):
    def list(self, organization_id: UUID | None) -> list[Framework]:
        raise NotImplementedError

    def get_by_id(self, framework_id: UUID) -> Framework | None:
        raise NotImplementedError

    def create(self, organization_id: UUID | None, code: str, name: str, description: str) -> Framework:
        raise NotImplementedError

    def list_versions(self, framework_id: UUID) -> list[FrameworkVersion]:
        raise NotImplementedError

    def create_version(
        self, framework_id: UUID, version: str, published_at: date | None
    ) -> FrameworkVersion:
        raise NotImplementedError

    def list_requirements(self, framework_version_id: UUID) -> list[Requirement]:
        raise NotImplementedError

    def create_requirement(
        self,
        framework_version_id: UUID,
        category_id: UUID | None,
        code: str,
        title: str,
        description: str,
    ) -> Requirement:
        raise NotImplementedError


class FrameworkService:
    def __init__(self, frameworks: FrameworkStore) -> None:
        self._frameworks = frameworks

    def list_frameworks(self, organization_id: UUID | None) -> list[Framework]:
        return self._frameworks.list(organization_id)

    def get_framework(self, framework_id: UUID) -> Framework | None:
        return self._frameworks.get_by_id(framework_id)

    def create_framework(self, command: CreateFrameworkCommand) -> Framework:
        return self._frameworks.create(
            organization_id=command.organization_id,
            code=command.code,
            name=command.name,
            description=command.description,
        )

    def list_versions(self, framework_id: UUID) -> list[FrameworkVersion]:
        return self._frameworks.list_versions(framework_id)

    def create_version(
        self, framework_id: UUID, version: str, published_at: date | None
    ) -> FrameworkVersion:
        return self._frameworks.create_version(framework_id, version, published_at)

    def list_requirements(self, framework_version_id: UUID) -> list[Requirement]:
        return self._frameworks.list_requirements(framework_version_id)

    def create_requirement(self, command: CreateRequirementCommand) -> Requirement:
        return self._frameworks.create_requirement(
            framework_version_id=command.framework_version_id,
            category_id=command.category_id,
            code=command.code,
            title=command.title,
            description=command.description,
        )


class ControlMappingStore(Protocol):
    def create(self, control_id: UUID, requirement_id: UUID) -> ControlMapping:
        raise NotImplementedError

    def list_for_control(self, control_id: UUID) -> list[ControlMapping]:
        raise NotImplementedError

    def list_for_requirement(self, requirement_id: UUID) -> list[ControlMapping]:
        raise NotImplementedError


class ControlMappingService:
    def __init__(self, mappings: ControlMappingStore) -> None:
        self._mappings = mappings

    def map_control_to_requirement(self, control_id: UUID, requirement_id: UUID) -> ControlMapping:
        return self._mappings.create(control_id, requirement_id)

    def list_for_control(self, control_id: UUID) -> list[ControlMapping]:
        return self._mappings.list_for_control(control_id)

    def list_for_requirement(self, requirement_id: UUID) -> list[ControlMapping]:
        return self._mappings.list_for_requirement(requirement_id)


# --- Assessments --------------------------------------------------------------


@dataclass(frozen=True)
class Assessment:
    id: UUID
    organization_id: UUID
    framework_version_id: UUID
    name: str
    status: AssessmentStatus
    period_start: date | None
    period_end: date | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class AssessmentResult:
    id: UUID
    assessment_id: UUID
    requirement_id: UUID
    status: RequirementResultStatus
    notes: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class CreateAssessmentCommand:
    organization_id: UUID
    framework_version_id: UUID
    name: str
    period_start: date | None = None
    period_end: date | None = None
    created_by_id: UUID | None = None


class AssessmentStore(Protocol):
    def list(self, organization_id: UUID) -> list[Assessment]:
        raise NotImplementedError

    def get_by_id(self, assessment_id: UUID) -> Assessment | None:
        raise NotImplementedError

    def create(
        self,
        organization_id: UUID,
        framework_version_id: UUID,
        name: str,
        period_start: date | None,
        period_end: date | None,
        created_by_id: UUID | None,
    ) -> Assessment:
        raise NotImplementedError

    def list_results(self, assessment_id: UUID) -> list[AssessmentResult]:
        raise NotImplementedError

    def upsert_result(
        self, assessment_id: UUID, requirement_id: UUID, status: RequirementResultStatus, notes: str
    ) -> AssessmentResult:
        raise NotImplementedError

    def set_status(self, assessment_id: UUID, status: AssessmentStatus) -> Assessment:
        raise NotImplementedError


class AssessmentNotFoundError(Exception):
    pass


class AssessmentService:
    def __init__(self, assessments: AssessmentStore, requirements: RequirementReader) -> None:
        self._assessments = assessments
        self._requirements = requirements

    def list_assessments(self, organization_id: UUID) -> list[Assessment]:
        return self._assessments.list(organization_id)

    def get_assessment(self, assessment_id: UUID) -> Assessment | None:
        return self._assessments.get_by_id(assessment_id)

    def create_assessment(self, command: CreateAssessmentCommand) -> Assessment:
        assessment = self._assessments.create(
            organization_id=command.organization_id,
            framework_version_id=command.framework_version_id,
            name=command.name,
            period_start=command.period_start,
            period_end=command.period_end,
            created_by_id=command.created_by_id,
        )
        for requirement in self._requirements.list_requirements(command.framework_version_id):
            self._assessments.upsert_result(
                assessment.id, requirement.id, RequirementResultStatus.NOT_ASSESSED, ""
            )
        return assessment

    def list_results(self, assessment_id: UUID) -> list[AssessmentResult]:
        return self._assessments.list_results(assessment_id)

    def record_result(
        self, assessment_id: UUID, requirement_id: UUID, status: RequirementResultStatus, notes: str
    ) -> AssessmentResult:
        return self._assessments.upsert_result(assessment_id, requirement_id, status, notes)

    def set_status(self, assessment_id: UUID, status: AssessmentStatus) -> Assessment:
        return self._assessments.set_status(assessment_id, status)

    def compute_score(self, assessment_id: UUID) -> float:
        results = self._assessments.list_results(assessment_id)
        applicable = [r for r in results if r.status != RequirementResultStatus.NOT_APPLICABLE]
        if not applicable:
            return 0.0
        compliant = len([r for r in applicable if r.status == RequirementResultStatus.COMPLIANT])
        return round(100.0 * compliant / len(applicable), 2)


# --- Evidence -------------------------------------------------------------------


@dataclass(frozen=True)
class Evidence:
    id: UUID
    organization_id: UUID
    assessment_result_id: UUID | None
    control_id: UUID | None
    title: str
    description: str
    file_reference: str
    uploaded_by_id: UUID | None
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class AddEvidenceCommand:
    organization_id: UUID
    title: str
    file_reference: str
    description: str = ""
    assessment_result_id: UUID | None = None
    control_id: UUID | None = None
    uploaded_by_id: UUID | None = None


class EvidenceStore(Protocol):
    def create(
        self,
        organization_id: UUID,
        title: str,
        description: str,
        file_reference: str,
        assessment_result_id: UUID | None,
        control_id: UUID | None,
        uploaded_by_id: UUID | None,
    ) -> Evidence:
        raise NotImplementedError

    def list_for_result(self, assessment_result_id: UUID) -> list[Evidence]:
        raise NotImplementedError

    def list_for_control(self, control_id: UUID) -> list[Evidence]:
        raise NotImplementedError


class EvidenceService:
    def __init__(self, evidence: EvidenceStore) -> None:
        self._evidence = evidence

    def add_evidence(self, command: AddEvidenceCommand) -> Evidence:
        return self._evidence.create(
            organization_id=command.organization_id,
            title=command.title,
            description=command.description,
            file_reference=command.file_reference,
            assessment_result_id=command.assessment_result_id,
            control_id=command.control_id,
            uploaded_by_id=command.uploaded_by_id,
        )

    def list_for_result(self, assessment_result_id: UUID) -> list[Evidence]:
        return self._evidence.list_for_result(assessment_result_id)

    def list_for_control(self, control_id: UUID) -> list[Evidence]:
        return self._evidence.list_for_control(control_id)


# --- Compliance scoring ----------------------------------------------------------


@dataclass(frozen=True)
class ComplianceScore:
    id: UUID
    organization_id: UUID
    assessment_id: UUID
    framework_version_id: UUID
    score: float
    computed_at: datetime


class ComplianceScoreStore(Protocol):
    def create(
        self,
        organization_id: UUID,
        assessment_id: UUID,
        framework_version_id: UUID,
        score: float,
        computed_at: datetime,
    ) -> ComplianceScore:
        raise NotImplementedError

    def get_latest(self, assessment_id: UUID) -> ComplianceScore | None:
        raise NotImplementedError


class ComplianceScoringService:
    def __init__(self, assessments: AssessmentService, scores: ComplianceScoreStore) -> None:
        self._assessments = assessments
        self._scores = scores

    def compute_and_store(self, assessment: Assessment) -> ComplianceScore:
        value = self._assessments.compute_score(assessment.id)
        return self._scores.create(
            organization_id=assessment.organization_id,
            assessment_id=assessment.id,
            framework_version_id=assessment.framework_version_id,
            score=value,
            computed_at=datetime.now(UTC),
        )

    def get_latest(self, assessment_id: UUID) -> ComplianceScore | None:
        return self._scores.get_latest(assessment_id)
