from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def _create_risk_source(client: TestClient, access_token: str, name: str = "Ransomware gang") -> dict:
    response = client.post(
        "/api/v1/risk-sources",
        headers=auth_headers(access_token),
        json={"name": name, "category": "organized_crime"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def _create_risk_origin(client: TestClient, access_token: str, risk_source_id: str) -> dict:
    response = client.post(
        "/api/v1/risk-origins",
        headers=auth_headers(access_token),
        json={"risk_source_id": risk_source_id, "target_objective": "Extort a ransom", "retained": True},
    )
    assert response.status_code == 201, response.text
    return response.json()


def _create_asset(client: TestClient, access_token: str, name: str = "prod-db") -> dict:
    response = client.post(
        "/api/v1/assets",
        headers=auth_headers(access_token),
        json={"name": name, "asset_type": "hardware", "owner": "Infra"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def _create_feared_event(client: TestClient, access_token: str, asset_id: str) -> dict:
    response = client.post(
        "/api/v1/feared-events",
        headers=auth_headers(access_token),
        json={
            "title": "Loss of availability",
            "asset_id": asset_id,
            "criterion": "availability",
            "gravity": "high",
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


def _create_strategic_scenario(client: TestClient, access_token: str) -> dict:
    risk_source = _create_risk_source(client, access_token)
    risk_origin = _create_risk_origin(client, access_token, risk_source["id"])
    asset = _create_asset(client, access_token)
    feared_event = _create_feared_event(client, access_token, asset["id"])

    response = client.post(
        "/api/v1/strategic-scenarios",
        headers=auth_headers(access_token),
        json={
            "risk_origin_id": risk_origin["id"],
            "feared_event_id": feared_event["id"],
            "name": "Direct ransomware attack",
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


def test_operational_scenario_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="os-org", email="admin@os.example.com")
    access = org["access_token"]
    headers = auth_headers(access)
    strategic_scenario = _create_strategic_scenario(client, access)

    operational_scenario = client.post(
        "/api/v1/operational-scenarios",
        headers=headers,
        json={
            "strategic_scenario_id": strategic_scenario["id"],
            "name": "Phishing -> RDP lateral move -> ransomware deploy",
            "mitre_technique_ids": ["T1566", "T1021", "T1486"],
            "technical_likelihood": "high",
        },
    )
    assert operational_scenario.status_code == 201, operational_scenario.text
    body = operational_scenario.json()
    assert body["strategic_scenario_id"] == strategic_scenario["id"]
    assert body["mitre_technique_ids"] == ["T1566", "T1021", "T1486"]
    assert body["technical_likelihood"] == "high"

    listed = client.get("/api/v1/operational-scenarios", headers=headers).json()
    assert any(o["id"] == body["id"] for o in listed)


def test_operational_scenario_defaults_mitre_technique_ids_to_empty_list(client: TestClient) -> None:
    org = register_organization(client, slug="os-defaults", email="admin@os-defaults.example.com")
    access = org["access_token"]
    strategic_scenario = _create_strategic_scenario(client, access)

    response = client.post(
        "/api/v1/operational-scenarios",
        headers=auth_headers(access),
        json={"strategic_scenario_id": strategic_scenario["id"], "name": "Undetailed scenario"},
    )
    assert response.status_code == 201, response.text
    body = response.json()
    assert body["mitre_technique_ids"] == []
    assert body["technical_likelihood"] == "medium"


def test_operational_scenario_strategic_scenario_id_is_required(client: TestClient) -> None:
    org = register_organization(client, slug="os-required", email="admin@os-required.example.com")

    response = client.post(
        "/api/v1/operational-scenarios",
        headers=auth_headers(org["access_token"]),
        json={"name": "No strategic scenario"},
    )
    assert response.status_code == 422


def test_operational_scenario_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="os-a", email="admin@os-a.example.com")
    org_b = register_organization(client, slug="os-b", email="admin@os-b.example.com")
    strategic_scenario = _create_strategic_scenario(client, org_a["access_token"])

    client.post(
        "/api/v1/operational-scenarios",
        headers=auth_headers(org_a["access_token"]),
        json={"strategic_scenario_id": strategic_scenario["id"], "name": "Org A scenario"},
    )

    org_a_list = client.get("/api/v1/operational-scenarios", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/operational-scenarios", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_operational_scenario_strategic_scenario_cannot_reference_another_organization(
    client: TestClient,
) -> None:
    org_a = register_organization(client, slug="os-cross-a", email="admin@os-cross-a.example.com")
    org_b = register_organization(client, slug="os-cross-b", email="admin@os-cross-b.example.com")
    strategic_scenario_a = _create_strategic_scenario(client, org_a["access_token"])

    response = client.post(
        "/api/v1/operational-scenarios",
        headers=auth_headers(org_b["access_token"]),
        json={"strategic_scenario_id": strategic_scenario_a["id"], "name": "Sneaky scenario"},
    )
    assert response.status_code == 404
