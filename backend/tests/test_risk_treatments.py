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


def test_risk_treatment_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="rt-org", email="admin@rt.example.com")
    access = org["access_token"]
    headers = auth_headers(access)
    strategic_scenario = _create_strategic_scenario(client, access)

    risk_treatment = client.post(
        "/api/v1/risk-treatments",
        headers=headers,
        json={
            "strategic_scenario_id": strategic_scenario["id"],
            "decision": "reduce",
            "justification": "Deploy EDR and enforce MFA on all remote access",
            "residual_risk_level": "medium",
        },
    )
    assert risk_treatment.status_code == 201, risk_treatment.text
    body = risk_treatment.json()
    assert body["strategic_scenario_id"] == strategic_scenario["id"]
    assert body["decision"] == "reduce"
    assert body["residual_risk_level"] == "medium"

    listed = client.get("/api/v1/risk-treatments", headers=headers).json()
    assert any(rt["id"] == body["id"] for rt in listed)


def test_risk_treatment_allows_multiple_decisions_per_scenario(client: TestClient) -> None:
    org = register_organization(client, slug="rt-multi", email="admin@rt-multi.example.com")
    access = org["access_token"]
    strategic_scenario = _create_strategic_scenario(client, access)

    first = client.post(
        "/api/v1/risk-treatments",
        headers=auth_headers(access),
        json={"strategic_scenario_id": strategic_scenario["id"], "decision": "accept"},
    )
    assert first.status_code == 201, first.text

    second = client.post(
        "/api/v1/risk-treatments",
        headers=auth_headers(access),
        json={
            "strategic_scenario_id": strategic_scenario["id"],
            "decision": "reduce",
            "justification": "Revised after a new control was implemented",
        },
    )
    assert second.status_code == 201, second.text

    listed = client.get("/api/v1/risk-treatments", headers=auth_headers(access)).json()
    assert len(listed) == 2


def test_risk_treatment_decision_is_required(client: TestClient) -> None:
    org = register_organization(client, slug="rt-required", email="admin@rt-required.example.com")
    access = org["access_token"]
    strategic_scenario = _create_strategic_scenario(client, access)

    response = client.post(
        "/api/v1/risk-treatments",
        headers=auth_headers(access),
        json={"strategic_scenario_id": strategic_scenario["id"]},
    )
    assert response.status_code == 422


def test_risk_treatment_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="rt-a", email="admin@rt-a.example.com")
    org_b = register_organization(client, slug="rt-b", email="admin@rt-b.example.com")
    strategic_scenario = _create_strategic_scenario(client, org_a["access_token"])

    client.post(
        "/api/v1/risk-treatments",
        headers=auth_headers(org_a["access_token"]),
        json={"strategic_scenario_id": strategic_scenario["id"], "decision": "accept"},
    )

    org_a_list = client.get("/api/v1/risk-treatments", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/risk-treatments", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_risk_treatment_strategic_scenario_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="rt-cross-a", email="admin@rt-cross-a.example.com")
    org_b = register_organization(client, slug="rt-cross-b", email="admin@rt-cross-b.example.com")
    strategic_scenario_a = _create_strategic_scenario(client, org_a["access_token"])

    response = client.post(
        "/api/v1/risk-treatments",
        headers=auth_headers(org_b["access_token"]),
        json={"strategic_scenario_id": strategic_scenario_a["id"], "decision": "accept"},
    )
    assert response.status_code == 404
