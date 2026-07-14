from __future__ import annotations

from datetime import date, datetime
from uuid import UUID

from backend.app.modules.compliance.models import (
    AssessmentModel,
    AssessmentResultModel,
    ComplianceScoreModel,
    ControlMappingModel,
    EvidenceModel,
    FrameworkModel,
    FrameworkVersionModel,
    RequirementModel,
)
from backend.app.modules.compliance.service import (
    Assessment,
    AssessmentResult,
    AssessmentStatus,
    ComplianceScore,
    ControlMapping,
    Evidence,
    Framework,
    FrameworkVersion,
    Requirement,
    RequirementResultStatus,
)
from sqlalchemy import or_, select
from sqlalchemy.orm import Session


def to_framework(model: FrameworkModel) -> Framework:
    return Framework(
        id=model.id,
        organization_id=model.organization_id,
        code=model.code,
        name=model.name,
        description=model.description,
        is_system=model.is_system,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_framework_version(model: FrameworkVersionModel) -> FrameworkVersion:
    return FrameworkVersion(
        id=model.id,
        framework_id=model.framework_id,
        version=model.version,
        published_at=model.published_at,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_requirement(model: RequirementModel) -> Requirement:
    return Requirement(
        id=model.id,
        framework_version_id=model.framework_version_id,
        category_id=model.category_id,
        code=model.code,
        title=model.title,
        description=model.description,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_control_mapping(model: ControlMappingModel) -> ControlMapping:
    return ControlMapping(
        id=model.id,
        control_id=model.control_id,
        requirement_id=model.requirement_id,
        created_at=model.created_at,
    )


def to_assessment(model: AssessmentModel) -> Assessment:
    return Assessment(
        id=model.id,
        organization_id=model.organization_id,
        framework_version_id=model.framework_version_id,
        name=model.name,
        status=model.status,
        period_start=model.period_start,
        period_end=model.period_end,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_assessment_result(model: AssessmentResultModel) -> AssessmentResult:
    return AssessmentResult(
        id=model.id,
        assessment_id=model.assessment_id,
        requirement_id=model.requirement_id,
        status=model.status,
        notes=model.notes,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_evidence(model: EvidenceModel) -> Evidence:
    return Evidence(
        id=model.id,
        organization_id=model.organization_id,
        assessment_result_id=model.assessment_result_id,
        control_id=model.control_id,
        title=model.title,
        description=model.description,
        file_reference=model.file_reference,
        uploaded_by_id=model.uploaded_by_id,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_compliance_score(model: ComplianceScoreModel) -> ComplianceScore:
    return ComplianceScore(
        id=model.id,
        organization_id=model.organization_id,
        assessment_id=model.assessment_id,
        framework_version_id=model.framework_version_id,
        score=model.score,
        computed_at=model.computed_at,
    )


class SqlAlchemyFrameworkRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID | None) -> list[Framework]:
        statement = select(FrameworkModel)
        if organization_id is not None:
            statement = statement.where(
                or_(FrameworkModel.organization_id == organization_id, FrameworkModel.organization_id.is_(None))
            )
        else:
            statement = statement.where(FrameworkModel.organization_id.is_(None))
        statement = statement.order_by(FrameworkModel.name)
        rows = self._session.scalars(statement).all()
        return [to_framework(row) for row in rows]

    def get_by_id(self, framework_id: UUID) -> Framework | None:
        model = self._session.get(FrameworkModel, framework_id)
        return to_framework(model) if model else None

    def create(self, organization_id: UUID | None, code: str, name: str, description: str) -> Framework:
        model = FrameworkModel(
            organization_id=organization_id, code=code, name=name, description=description, is_system=False
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_framework(model)

    def list_versions(self, framework_id: UUID) -> list[FrameworkVersion]:
        statement = (
            select(FrameworkVersionModel)
            .where(FrameworkVersionModel.framework_id == framework_id)
            .order_by(FrameworkVersionModel.version)
        )
        rows = self._session.scalars(statement).all()
        return [to_framework_version(row) for row in rows]

    def get_version_by_id(self, framework_version_id: UUID) -> FrameworkVersion | None:
        model = self._session.get(FrameworkVersionModel, framework_version_id)
        return to_framework_version(model) if model else None

    def create_version(
        self, framework_id: UUID, version: str, published_at: date | None
    ) -> FrameworkVersion:
        model = FrameworkVersionModel(framework_id=framework_id, version=version, published_at=published_at)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_framework_version(model)

    def list_requirements(self, framework_version_id: UUID) -> list[Requirement]:
        statement = (
            select(RequirementModel)
            .where(RequirementModel.framework_version_id == framework_version_id)
            .order_by(RequirementModel.code)
        )
        rows = self._session.scalars(statement).all()
        return [to_requirement(row) for row in rows]

    def create_requirement(
        self,
        framework_version_id: UUID,
        category_id: UUID | None,
        code: str,
        title: str,
        description: str,
    ) -> Requirement:
        model = RequirementModel(
            framework_version_id=framework_version_id,
            category_id=category_id,
            code=code,
            title=title,
            description=description,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_requirement(model)


class SqlAlchemyControlMappingRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(self, control_id: UUID, requirement_id: UUID) -> ControlMapping:
        model = ControlMappingModel(control_id=control_id, requirement_id=requirement_id)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_control_mapping(model)

    def list_for_control(self, control_id: UUID) -> list[ControlMapping]:
        statement = select(ControlMappingModel).where(ControlMappingModel.control_id == control_id)
        rows = self._session.scalars(statement).all()
        return [to_control_mapping(row) for row in rows]

    def list_for_requirement(self, requirement_id: UUID) -> list[ControlMapping]:
        statement = select(ControlMappingModel).where(ControlMappingModel.requirement_id == requirement_id)
        rows = self._session.scalars(statement).all()
        return [to_control_mapping(row) for row in rows]


class SqlAlchemyAssessmentRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID) -> list[Assessment]:
        statement = (
            select(AssessmentModel)
            .where(AssessmentModel.organization_id == organization_id, AssessmentModel.deleted_at.is_(None))
            .order_by(AssessmentModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_assessment(row) for row in rows]

    def get_by_id(self, assessment_id: UUID) -> Assessment | None:
        model = self._session.get(AssessmentModel, assessment_id)
        if model is None or model.deleted_at is not None:
            return None
        return to_assessment(model)

    def create(
        self,
        organization_id: UUID,
        framework_version_id: UUID,
        name: str,
        period_start: date | None,
        period_end: date | None,
        created_by_id: UUID | None,
    ) -> Assessment:
        model = AssessmentModel(
            organization_id=organization_id,
            framework_version_id=framework_version_id,
            name=name,
            period_start=period_start,
            period_end=period_end,
            created_by_id=created_by_id,
            updated_by_id=created_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_assessment(model)

    def list_results(self, assessment_id: UUID) -> list[AssessmentResult]:
        statement = (
            select(AssessmentResultModel)
            .where(AssessmentResultModel.assessment_id == assessment_id)
            .order_by(AssessmentResultModel.created_at)
        )
        rows = self._session.scalars(statement).all()
        return [to_assessment_result(row) for row in rows]

    def upsert_result(
        self, assessment_id: UUID, requirement_id: UUID, status: RequirementResultStatus, notes: str
    ) -> AssessmentResult:
        statement = select(AssessmentResultModel).where(
            AssessmentResultModel.assessment_id == assessment_id,
            AssessmentResultModel.requirement_id == requirement_id,
        )
        model = self._session.scalars(statement).first()
        if model is None:
            model = AssessmentResultModel(
                assessment_id=assessment_id, requirement_id=requirement_id, status=status, notes=notes
            )
            self._session.add(model)
        else:
            model.status = status
            model.notes = notes
        self._session.commit()
        self._session.refresh(model)
        return to_assessment_result(model)

    def set_status(self, assessment_id: UUID, status: AssessmentStatus) -> Assessment:
        model = self._session.get(AssessmentModel, assessment_id)
        if model is None:
            raise ValueError("assessment not found")
        model.status = status
        self._session.commit()
        self._session.refresh(model)
        return to_assessment(model)


class SqlAlchemyEvidenceRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

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
        model = EvidenceModel(
            organization_id=organization_id,
            title=title,
            description=description,
            file_reference=file_reference,
            assessment_result_id=assessment_result_id,
            control_id=control_id,
            uploaded_by_id=uploaded_by_id,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_evidence(model)

    def list_for_result(self, assessment_result_id: UUID) -> list[Evidence]:
        statement = select(EvidenceModel).where(
            EvidenceModel.assessment_result_id == assessment_result_id, EvidenceModel.deleted_at.is_(None)
        )
        rows = self._session.scalars(statement).all()
        return [to_evidence(row) for row in rows]

    def list_for_control(self, control_id: UUID) -> list[Evidence]:
        statement = select(EvidenceModel).where(
            EvidenceModel.control_id == control_id, EvidenceModel.deleted_at.is_(None)
        )
        rows = self._session.scalars(statement).all()
        return [to_evidence(row) for row in rows]


class SqlAlchemyComplianceScoreRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(
        self,
        organization_id: UUID,
        assessment_id: UUID,
        framework_version_id: UUID,
        score: float,
        computed_at: datetime,
    ) -> ComplianceScore:
        model = ComplianceScoreModel(
            organization_id=organization_id,
            assessment_id=assessment_id,
            framework_version_id=framework_version_id,
            score=score,
            computed_at=computed_at,
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_compliance_score(model)

    def get_latest(self, assessment_id: UUID) -> ComplianceScore | None:
        statement = (
            select(ComplianceScoreModel)
            .where(ComplianceScoreModel.assessment_id == assessment_id)
            .order_by(ComplianceScoreModel.computed_at.desc())
        )
        model = self._session.scalars(statement).first()
        return to_compliance_score(model) if model else None
