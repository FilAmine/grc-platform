from datetime import UTC, datetime
from uuid import uuid4

from backend.app.modules.risk_sources.models import RiskSourceModel
from backend.app.modules.risk_sources.repository import SqlAlchemyRiskSourceRepository
from backend.app.modules.risk_sources.service import (
    RiskSourceActivity,
    RiskSourceCategory,
    RiskSourceLevel,
)
from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_risk_source_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="rs-org", email="admin@rs.example.com")
    headers = auth_headers(org["access_token"])

    risk_source = client.post(
        "/api/v1/risk-sources",
        headers=headers,
        json={
            "name": "State-sponsored APT group",
            "category": "state",
            "motivation": "very_high",
            "resources": "very_high",
            "activity": "high",
        },
    )
    assert risk_source.status_code == 201, risk_source.text
    body = risk_source.json()
    assert body["category"] == "state"
    assert body["motivation"] == "very_high"

    listed = client.get("/api/v1/risk-sources", headers=headers).json()
    assert any(rs["id"] == body["id"] for rs in listed)


def test_risk_source_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="rs-a", email="admin@rs-a.example.com")
    org_b = register_organization(client, slug="rs-b", email="admin@rs-b.example.com")

    client.post(
        "/api/v1/risk-sources",
        headers=auth_headers(org_a["access_token"]),
        json={"name": "Org A source", "category": "amateur"},
    )

    org_a_list = client.get("/api/v1/risk-sources", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/risk-sources", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_risk_source_repository_get_by_id(db_session: Session) -> None:
    repository = SqlAlchemyRiskSourceRepository(db_session)
    organization_id = uuid4()

    created = repository.create(
        organization_id=organization_id,
        name="Cyber-mercenary firm",
        category=RiskSourceCategory.SPECIALIZED_FIRM,
        description="",
        motivation=RiskSourceLevel.SIGNIFICANT,
        resources=RiskSourceLevel.SIGNIFICANT,
        activity=RiskSourceActivity.MEDIUM,
        created_by_id=None,
    )

    found = repository.get_by_id(created.id)
    assert found is not None
    assert found.id == created.id

    assert repository.get_by_id(uuid4()) is None

    model = db_session.get(RiskSourceModel, created.id)
    model.deleted_at = datetime.now(UTC)
    db_session.commit()
    assert repository.get_by_id(created.id) is None
