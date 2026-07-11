from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_threat_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="threat-org", email="admin@threat.example.com")
    headers = auth_headers(org["access_token"])

    threat = client.post(
        "/api/v1/threats",
        headers=headers,
        json={"name": "Phishing", "category": "human", "likelihood": "high"},
    )
    assert threat.status_code == 201, threat.text
    body = threat.json()
    assert body["category"] == "human"
    assert body["likelihood"] == "high"

    listed = client.get("/api/v1/threats", headers=headers).json()
    assert any(t["id"] == body["id"] for t in listed)


def test_threat_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="threat-a", email="admin@threat-a.example.com")
    org_b = register_organization(client, slug="threat-b", email="admin@threat-b.example.com")

    client.post(
        "/api/v1/threats",
        headers=auth_headers(org_a["access_token"]),
        json={"name": "Org A threat", "category": "technical"},
    )

    org_a_list = client.get("/api/v1/threats", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/threats", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []
