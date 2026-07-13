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


def test_risk_origin_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="ro-org", email="admin@ro.example.com")
    headers = auth_headers(org["access_token"])
    risk_source = _create_risk_source(client, org["access_token"])

    risk_origin = client.post(
        "/api/v1/risk-origins",
        headers=headers,
        json={
            "risk_source_id": risk_source["id"],
            "target_objective": "Extort a ransom by encrypting production data",
            "pertinence": "high",
            "retained": True,
        },
    )
    assert risk_origin.status_code == 201, risk_origin.text
    body = risk_origin.json()
    assert body["risk_source_id"] == risk_source["id"]
    assert body["retained"] is True

    listed = client.get("/api/v1/risk-origins", headers=headers).json()
    assert any(ro["id"] == body["id"] for ro in listed)


def test_risk_origin_can_link_a_feared_event(client: TestClient) -> None:
    org = register_organization(client, slug="ro-fe", email="admin@ro-fe.example.com")
    access = org["access_token"]
    risk_source = _create_risk_source(client, access)
    asset = _create_asset(client, access)
    feared_event = _create_feared_event(client, access, asset["id"])

    risk_origin = client.post(
        "/api/v1/risk-origins",
        headers=auth_headers(access),
        json={
            "risk_source_id": risk_source["id"],
            "target_objective": "Disrupt operations",
            "feared_event_id": feared_event["id"],
        },
    )
    assert risk_origin.status_code == 201, risk_origin.text
    assert risk_origin.json()["feared_event_id"] == feared_event["id"]


def test_risk_origin_risk_source_id_is_required(client: TestClient) -> None:
    org = register_organization(client, slug="ro-required", email="admin@ro-required.example.com")

    response = client.post(
        "/api/v1/risk-origins",
        headers=auth_headers(org["access_token"]),
        json={"target_objective": "No source"},
    )
    assert response.status_code == 422


def test_risk_origin_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="ro-a", email="admin@ro-a.example.com")
    org_b = register_organization(client, slug="ro-b", email="admin@ro-b.example.com")
    risk_source = _create_risk_source(client, org_a["access_token"])

    client.post(
        "/api/v1/risk-origins",
        headers=auth_headers(org_a["access_token"]),
        json={"risk_source_id": risk_source["id"], "target_objective": "Org A objective"},
    )

    org_a_list = client.get("/api/v1/risk-origins", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/risk-origins", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_risk_origin_risk_source_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="ro-cross-a", email="admin@ro-cross-a.example.com")
    org_b = register_organization(client, slug="ro-cross-b", email="admin@ro-cross-b.example.com")
    org_a_risk_source = _create_risk_source(client, org_a["access_token"])

    response = client.post(
        "/api/v1/risk-origins",
        headers=auth_headers(org_b["access_token"]),
        json={"risk_source_id": org_a_risk_source["id"], "target_objective": "Sneaky objective"},
    )
    assert response.status_code == 404


def test_risk_origin_feared_event_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="ro-fe-cross-a", email="admin@ro-fe-cross-a.example.com")
    org_b = register_organization(client, slug="ro-fe-cross-b", email="admin@ro-fe-cross-b.example.com")
    asset_a = _create_asset(client, org_a["access_token"])
    feared_event_a = _create_feared_event(client, org_a["access_token"], asset_a["id"])
    risk_source_b = _create_risk_source(client, org_b["access_token"])

    response = client.post(
        "/api/v1/risk-origins",
        headers=auth_headers(org_b["access_token"]),
        json={
            "risk_source_id": risk_source_b["id"],
            "target_objective": "Sneaky objective",
            "feared_event_id": feared_event_a["id"],
        },
    )
    assert response.status_code == 404
