from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.risk_treatments.service import RiskTreatmentDecision, RiskTreatmentResidualRisk
from pydantic import Field


class RiskTreatmentCreate(ReadSchema):
    strategic_scenario_id: UUID
    decision: RiskTreatmentDecision
    justification: str = Field(default="", max_length=4000)
    residual_risk_level: RiskTreatmentResidualRisk = RiskTreatmentResidualRisk.MEDIUM


class RiskTreatmentRead(ReadSchema):
    id: UUID
    organization_id: UUID
    strategic_scenario_id: UUID
    decision: RiskTreatmentDecision
    justification: str
    residual_risk_level: RiskTreatmentResidualRisk
    created_at: datetime
    updated_at: datetime
