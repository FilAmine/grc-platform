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


def _create_risk_origin(client: TestClient, access_token: str, risk_source_id: str, retained: bool = True) -> dict:
    response = client.post(
        "/api/v1/risk-origins",
        headers=auth_headers(access_token),
        json={
            "risk_source_id": risk_source_id,
            "target_objective": "Extort a ransom",
            "retained": retained,
        },
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


def _create_ecosystem_party(client: TestClient, access_token: str, name: str = "Cloud host") -> dict:
    response = client.post(
        "/api/v1/ecosystem-parties",
        headers=auth_headers(access_token),
        json={"name": name, "category": "provider"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def _bootstrap_retained_origin(client: TestClient, access_token: str) -> tuple[dict, dict]:
    risk_source = _create_risk_source(client, access_token)
    risk_origin = _create_risk_origin(client, access_token, risk_source["id"], retained=True)
    asset = _create_asset(client, access_token)
    feared_event = _create_feared_event(client, access_token, asset["id"])
    return risk_origin, feared_event


def test_strategic_scenario_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="ss-org", email="admin@ss.example.com")
    access = org["access_token"]
    headers = auth_headers(access)
    risk_origin, feared_event = _bootstrap_retained_origin(client, access)

    scenario = client.post(
        "/api/v1/strategic-scenarios",
        headers=headers,
        json={
            "risk_origin_id": risk_origin["id"],
            "feared_event_id": feared_event["id"],
            "name": "Direct ransomware attack on production",
            "likelihood": "high",
        },
    )
    assert scenario.status_code == 201, scenario.text
    body = scenario.json()
    assert body["risk_origin_id"] == risk_origin["id"]
    assert body["feared_event_id"] == feared_event["id"]
    assert body["ecosystem_party_id"] is None

    listed = client.get("/api/v1/strategic-scenarios", headers=headers).json()
    assert any(s["id"] == body["id"] for s in listed)


def test_strategic_scenario_can_link_an_ecosystem_party(client: TestClient) -> None:
    org = register_organization(client, slug="ss-ecosystem", email="admin@ss-ecosystem.example.com")
    access = org["access_token"]
    risk_origin, feared_event = _bootstrap_retained_origin(client, access)
    ecosystem_party = _create_ecosystem_party(client, access)

    scenario = client.post(
        "/api/v1/strategic-scenarios",
        headers=auth_headers(access),
        json={
            "risk_origin_id": risk_origin["id"],
            "feared_event_id": feared_event["id"],
            "ecosystem_party_id": ecosystem_party["id"],
            "name": "Attack via compromised cloud host",
        },
    )
    assert scenario.status_code == 201, scenario.text
    assert scenario.json()["ecosystem_party_id"] == ecosystem_party["id"]


def test_strategic_scenario_requires_a_retained_risk_origin(client: TestClient) -> None:
    org = register_organization(client, slug="ss-not-retained", email="admin@ss-not-retained.example.com")
    access = org["access_token"]
    risk_source = _create_risk_source(client, access)
    risk_origin = _create_risk_origin(client, access, risk_source["id"], retained=False)
    asset = _create_asset(client, access)
    feared_event = _create_feared_event(client, access, asset["id"])

    scenario = client.post(
        "/api/v1/strategic-scenarios",
        headers=auth_headers(access),
        json={
            "risk_origin_id": risk_origin["id"],
            "feared_event_id": feared_event["id"],
            "name": "Should not be buildable yet",
        },
    )
    assert scenario.status_code == 409


def test_strategic_scenario_feared_event_id_is_required(client: TestClient) -> None:
    org = register_organization(client, slug="ss-required", email="admin@ss-required.example.com")
    access = org["access_token"]
    risk_source = _create_risk_source(client, access)
    risk_origin = _create_risk_origin(client, access, risk_source["id"])

    response = client.post(
        "/api/v1/strategic-scenarios",
        headers=auth_headers(access),
        json={"risk_origin_id": risk_origin["id"], "name": "No feared event"},
    )
    assert response.status_code == 422


def test_strategic_scenario_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="ss-a", email="admin@ss-a.example.com")
    org_b = register_organization(client, slug="ss-b", email="admin@ss-b.example.com")
    risk_origin, feared_event = _bootstrap_retained_origin(client, org_a["access_token"])

    client.post(
        "/api/v1/strategic-scenarios",
        headers=auth_headers(org_a["access_token"]),
        json={
            "risk_origin_id": risk_origin["id"],
            "feared_event_id": feared_event["id"],
            "name": "Org A scenario",
        },
    )

    org_a_list = client.get("/api/v1/strategic-scenarios", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/strategic-scenarios", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_strategic_scenario_risk_origin_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="ss-cross-a", email="admin@ss-cross-a.example.com")
    org_b = register_organization(client, slug="ss-cross-b", email="admin@ss-cross-b.example.com")
    risk_origin_a, _ = _bootstrap_retained_origin(client, org_a["access_token"])
    asset_b = _create_asset(client, org_b["access_token"])
    feared_event_b = _create_feared_event(client, org_b["access_token"], asset_b["id"])

    response = client.post(
        "/api/v1/strategic-scenarios",
        headers=auth_headers(org_b["access_token"]),
        json={
            "risk_origin_id": risk_origin_a["id"],
            "feared_event_id": feared_event_b["id"],
            "name": "Sneaky scenario",
        },
    )
    assert response.status_code == 404


def test_strategic_scenario_feared_event_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="ss-fe-cross-a", email="admin@ss-fe-cross-a.example.com")
    org_b = register_organization(client, slug="ss-fe-cross-b", email="admin@ss-fe-cross-b.example.com")
    _, feared_event_a = _bootstrap_retained_origin(client, org_a["access_token"])
    risk_source_b = _create_risk_source(client, org_b["access_token"])
    risk_origin_b = _create_risk_origin(client, org_b["access_token"], risk_source_b["id"])

    response = client.post(
        "/api/v1/strategic-scenarios",
        headers=auth_headers(org_b["access_token"]),
        json={
            "risk_origin_id": risk_origin_b["id"],
            "feared_event_id": feared_event_a["id"],
            "name": "Sneaky scenario",
        },
    )
    assert response.status_code == 404


def test_strategic_scenario_ecosystem_party_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="ss-ep-cross-a", email="admin@ss-ep-cross-a.example.com")
    org_b = register_organization(client, slug="ss-ep-cross-b", email="admin@ss-ep-cross-b.example.com")
    ecosystem_party_a = _create_ecosystem_party(client, org_a["access_token"])
    risk_origin_b, feared_event_b = _bootstrap_retained_origin(client, org_b["access_token"])

    response = client.post(
        "/api/v1/strategic-scenarios",
        headers=auth_headers(org_b["access_token"]),
        json={
            "risk_origin_id": risk_origin_b["id"],
            "feared_event_id": feared_event_b["id"],
            "ecosystem_party_id": ecosystem_party_a["id"],
            "name": "Sneaky scenario",
        },
    )
    assert response.status_code == 404
