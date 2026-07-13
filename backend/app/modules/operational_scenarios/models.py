from uuid import UUID as PyUUID

from backend.app.common.models import (
    AuditColumnsMixin,
    SoftDeleteMixin,
    TenantScopedMixin,
    TimestampMixin,
    UUIDPKMixin,
)
from backend.app.database import Base
from backend.app.modules.operational_scenarios.service import OperationalScenarioLikelihood
from sqlalchemy import JSON, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column


class OperationalScenarioModel(
    UUIDPKMixin, TenantScopedMixin, TimestampMixin, SoftDeleteMixin, AuditColumnsMixin, Base
):
    __tablename__ = "operational_scenarios"

    # RESTRICT, not SET NULL: an operational scenario *is* the technical
    # elaboration of a specific strategic scenario -- same reasoning as
    # strategic_scenarios.risk_origin_id.
    strategic_scenario_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True),
        ForeignKey("strategic_scenarios.id", ondelete="RESTRICT"),
        index=True,
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")
    # Plain JSON list of free-text identifiers, not a Postgres-specific ARRAY
    # column -- runs against any SQL backend (SQLite in tests, Postgres in
    # prod), same reasoning as KnowledgeBaseDocumentModel.embedding.
    mitre_technique_ids: Mapped[list[str]] = mapped_column(JSON, nullable=False, default=list)
    technical_likelihood: Mapped[OperationalScenarioLikelihood] = mapped_column(
        Enum(OperationalScenarioLikelihood), default=OperationalScenarioLikelihood.MEDIUM, nullable=False
    )
