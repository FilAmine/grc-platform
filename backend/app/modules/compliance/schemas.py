from pydantic import BaseModel


class ComplianceSummary(BaseModel):
    organizations: int
    risks_open: int
    controls_active: int
    posture: str
