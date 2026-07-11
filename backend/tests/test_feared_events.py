from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def _create_asset(client: TestClient, access_token: str, name: str = "prod-db") -> dict:
    response = client.post(
        "/api/v1/assets",
        headers=auth_headers(access_token),
        json={"name": name, "asset_type": "hardware", "owner": "Infra"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def test_feared_event_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="fe-org", email="admin@fe.example.com")
    headers = auth_headers(org["access_token"])
    asset = _create_asset(client, org["access_token"])

    feared_event = client.post(
        "/api/v1/feared-events",
        headers=headers,
        json={
            "title": "Loss of customer data confidentiality",
            "asset_id": asset["id"],
            "criterion": "confidentiality",
            "gravity": "critical",
        },
    )
    assert feared_event.status_code == 201, feared_event.text
    body = feared_event.json()
    assert body["asset_id"] == asset["id"]

    listed = client.get("/api/v1/feared-events", headers=headers).json()
    assert any(fe["id"] == body["id"] for fe in listed)


def test_feared_event_asset_id_is_required(client: TestClient) -> None:
    org = register_organization(client, slug="fe-required", email="admin@fe-required.example.com")
    headers = auth_headers(org["access_token"])

    response = client.post(
        "/api/v1/feared-events",
        headers=headers,
        json={"title": "No asset", "criterion": "integrity", "gravity": "low"},
    )
    assert response.status_code == 422


def test_feared_event_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="fe-a", email="admin@fe-a.example.com")
    org_b = register_organization(client, slug="fe-b", email="admin@fe-b.example.com")
    asset = _create_asset(client, org_a["access_token"])

    client.post(
        "/api/v1/feared-events",
        headers=auth_headers(org_a["access_token"]),
        json={"title": "Org A event", "asset_id": asset["id"], "criterion": "availability", "gravity": "medium"},
    )

    org_a_list = client.get("/api/v1/feared-events", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/feared-events", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_feared_event_asset_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="fe-cross-a", email="admin@fe-cross-a.example.com")
    org_b = register_organization(client, slug="fe-cross-b", email="admin@fe-cross-b.example.com")
    org_a_asset = _create_asset(client, org_a["access_token"])

    response = client.post(
        "/api/v1/feared-events",
        headers=auth_headers(org_b["access_token"]),
        json={
            "title": "Sneaky event",
            "asset_id": org_a_asset["id"],
            "criterion": "confidentiality",
            "gravity": "high",
        },
    )
    assert response.status_code == 404
