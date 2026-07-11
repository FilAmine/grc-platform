from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def _create_asset(client: TestClient, access_token: str) -> dict:
    response = client.post(
        "/api/v1/assets",
        headers=auth_headers(access_token),
        json={"name": "prod-db", "asset_type": "hardware", "owner": "Infra"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def _create_threat(client: TestClient, access_token: str) -> dict:
    response = client.post(
        "/api/v1/threats",
        headers=auth_headers(access_token),
        json={"name": "Phishing", "category": "human"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def _create_vulnerability(client: TestClient, access_token: str) -> dict:
    response = client.post(
        "/api/v1/vulnerabilities",
        headers=auth_headers(access_token),
        json={"name": "Unpatched OpenSSL", "severity": "high"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def _create_feared_event(client: TestClient, access_token: str, asset_id: str) -> dict:
    response = client.post(
        "/api/v1/feared-events",
        headers=auth_headers(access_token),
        json={"title": "Data breach", "asset_id": asset_id, "criterion": "confidentiality", "gravity": "high"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def test_risk_create_without_links(client: TestClient) -> None:
    org = register_organization(client, slug="risk-no-links", email="admin@risk-no-links.example.com")
    headers = auth_headers(org["access_token"])

    risk = client.post(
        "/api/v1/risks",
        headers=headers,
        json={"title": "A risk", "description": "desc", "severity": "medium", "owner": "Owner"},
    )
    assert risk.status_code == 201, risk.text
    body = risk.json()
    assert body["asset_id"] is None
    assert body["threat_id"] is None
    assert body["vulnerability_id"] is None
    assert body["feared_event_id"] is None


def test_risk_create_with_all_links(client: TestClient) -> None:
    org = register_organization(client, slug="risk-links", email="admin@risk-links.example.com")
    token = org["access_token"]
    headers = auth_headers(token)

    asset = _create_asset(client, token)
    threat = _create_threat(client, token)
    vulnerability = _create_vulnerability(client, token)
    feared_event = _create_feared_event(client, token, asset["id"])

    risk = client.post(
        "/api/v1/risks",
        headers=headers,
        json={
            "title": "Linked risk",
            "description": "desc",
            "severity": "high",
            "owner": "Owner",
            "asset_id": asset["id"],
            "threat_id": threat["id"],
            "vulnerability_id": vulnerability["id"],
            "feared_event_id": feared_event["id"],
        },
    )
    assert risk.status_code == 201, risk.text
    body = risk.json()
    assert body["asset_id"] == asset["id"]
    assert body["threat_id"] == threat["id"]
    assert body["vulnerability_id"] == vulnerability["id"]
    assert body["feared_event_id"] == feared_event["id"]


def test_risk_asset_id_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="risk-cross-asset-a", email="admin@risk-cross-asset-a.example.com")
    org_b = register_organization(client, slug="risk-cross-asset-b", email="admin@risk-cross-asset-b.example.com")
    org_a_asset = _create_asset(client, org_a["access_token"])

    response = client.post(
        "/api/v1/risks",
        headers=auth_headers(org_b["access_token"]),
        json={
            "title": "Sneaky risk",
            "description": "desc",
            "severity": "low",
            "owner": "Owner",
            "asset_id": org_a_asset["id"],
        },
    )
    assert response.status_code == 404


def test_risk_threat_id_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="risk-cross-threat-a", email="admin@risk-cross-threat-a.example.com")
    org_b = register_organization(client, slug="risk-cross-threat-b", email="admin@risk-cross-threat-b.example.com")
    org_a_threat = _create_threat(client, org_a["access_token"])

    response = client.post(
        "/api/v1/risks",
        headers=auth_headers(org_b["access_token"]),
        json={
            "title": "Sneaky risk",
            "description": "desc",
            "severity": "low",
            "owner": "Owner",
            "threat_id": org_a_threat["id"],
        },
    )
    assert response.status_code == 404


def test_risk_vulnerability_id_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="risk-cross-vuln-a", email="admin@risk-cross-vuln-a.example.com")
    org_b = register_organization(client, slug="risk-cross-vuln-b", email="admin@risk-cross-vuln-b.example.com")
    org_a_vulnerability = _create_vulnerability(client, org_a["access_token"])

    response = client.post(
        "/api/v1/risks",
        headers=auth_headers(org_b["access_token"]),
        json={
            "title": "Sneaky risk",
            "description": "desc",
            "severity": "low",
            "owner": "Owner",
            "vulnerability_id": org_a_vulnerability["id"],
        },
    )
    assert response.status_code == 404


def test_risk_feared_event_id_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="risk-cross-fe-a", email="admin@risk-cross-fe-a.example.com")
    org_b = register_organization(client, slug="risk-cross-fe-b", email="admin@risk-cross-fe-b.example.com")
    org_a_asset = _create_asset(client, org_a["access_token"])
    org_a_feared_event = _create_feared_event(client, org_a["access_token"], org_a_asset["id"])

    response = client.post(
        "/api/v1/risks",
        headers=auth_headers(org_b["access_token"]),
        json={
            "title": "Sneaky risk",
            "description": "desc",
            "severity": "low",
            "owner": "Owner",
            "feared_event_id": org_a_feared_event["id"],
        },
    )
    assert response.status_code == 404
