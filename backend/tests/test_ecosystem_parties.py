from datetime import UTC, datetime
from uuid import uuid4

from backend.app.modules.ecosystem_parties.models import EcosystemPartyModel
from backend.app.modules.ecosystem_parties.repository import SqlAlchemyEcosystemPartyRepository
from backend.app.modules.ecosystem_parties.service import EcosystemPartyCategory, EcosystemPartyLevel
from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def test_ecosystem_party_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="ep-org", email="admin@ep.example.com")
    headers = auth_headers(org["access_token"])

    ecosystem_party = client.post(
        "/api/v1/ecosystem-parties",
        headers=headers,
        json={
            "name": "Cloud hosting provider",
            "category": "provider",
            "dependency_level": "high",
            "cyber_maturity": "low",
        },
    )
    assert ecosystem_party.status_code == 201, ecosystem_party.text
    body = ecosystem_party.json()
    assert body["category"] == "provider"
    assert body["cyber_maturity"] == "low"

    listed = client.get("/api/v1/ecosystem-parties", headers=headers).json()
    assert any(ep["id"] == body["id"] for ep in listed)


def test_ecosystem_party_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="ep-a", email="admin@ep-a.example.com")
    org_b = register_organization(client, slug="ep-b", email="admin@ep-b.example.com")

    client.post(
        "/api/v1/ecosystem-parties",
        headers=auth_headers(org_a["access_token"]),
        json={"name": "Org A subcontractor", "category": "subcontractor"},
    )

    org_a_list = client.get("/api/v1/ecosystem-parties", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/ecosystem-parties", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_ecosystem_party_repository_get_by_id(db_session: Session) -> None:
    repository = SqlAlchemyEcosystemPartyRepository(db_session)
    organization_id = uuid4()

    created = repository.create(
        organization_id=organization_id,
        name="Payroll partner",
        category=EcosystemPartyCategory.PARTNER,
        description="",
        dependency_level=EcosystemPartyLevel.HIGH,
        cyber_maturity=EcosystemPartyLevel.MEDIUM,
        created_by_id=None,
    )

    found = repository.get_by_id(created.id)
    assert found is not None
    assert found.id == created.id

    assert repository.get_by_id(uuid4()) is None

    model = db_session.get(EcosystemPartyModel, created.id)
    model.deleted_at = datetime.now(UTC)
    db_session.commit()
    assert repository.get_by_id(created.id) is None
