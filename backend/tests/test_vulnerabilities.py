from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_vulnerability_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="vuln-org", email="admin@vuln.example.com")
    headers = auth_headers(org["access_token"])

    vulnerability = client.post(
        "/api/v1/vulnerabilities",
        headers=headers,
        json={"name": "Unpatched OpenSSL", "severity": "critical"},
    )
    assert vulnerability.status_code == 201, vulnerability.text
    body = vulnerability.json()
    assert body["severity"] == "critical"
    assert body["status"] == "open"

    listed = client.get("/api/v1/vulnerabilities", headers=headers).json()
    assert any(v["id"] == body["id"] for v in listed)


def test_vulnerability_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="vuln-a", email="admin@vuln-a.example.com")
    org_b = register_organization(client, slug="vuln-b", email="admin@vuln-b.example.com")

    client.post(
        "/api/v1/vulnerabilities",
        headers=auth_headers(org_a["access_token"]),
        json={"name": "Org A vulnerability", "severity": "low"},
    )

    org_a_list = client.get("/api/v1/vulnerabilities", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/vulnerabilities", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []
