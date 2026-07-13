from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from backend.app.modules.ecosystem_parties.service import EcosystemPartyCategory, EcosystemPartyLevel
from pydantic import Field


class EcosystemPartyCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=255)
    category: EcosystemPartyCategory
    description: str = Field(default="", max_length=4000)
    dependency_level: EcosystemPartyLevel = EcosystemPartyLevel.MEDIUM
    cyber_maturity: EcosystemPartyLevel = EcosystemPartyLevel.MEDIUM


class EcosystemPartyRead(ReadSchema):
    id: UUID
    organization_id: UUID
    name: str
    description: str
    category: EcosystemPartyCategory
    dependency_level: EcosystemPartyLevel
    cyber_maturity: EcosystemPartyLevel
    created_at: datetime
    updated_at: datetime
