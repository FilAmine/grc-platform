from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_incident_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="incident-org", email="admin@incident.example.com")
    headers = auth_headers(org["access_token"])

    incident = client.post(
        "/api/v1/incidents",
        headers=headers,
        json={"title": "Suspicious login", "severity": "high", "reported_by": "Security Team"},
    )
    assert incident.status_code == 201, incident.text
    body = incident.json()
    assert body["status"] == "open"
    assert body["resolved_at"] is None

    listed = client.get("/api/v1/incidents", headers=headers).json()
    assert any(i["id"] == body["id"] for i in listed)


def test_incident_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="incident-a", email="admin@incident-a.example.com")
    org_b = register_organization(client, slug="incident-b", email="admin@incident-b.example.com")

    client.post(
        "/api/v1/incidents",
        headers=auth_headers(org_a["access_token"]),
        json={"title": "Org A incident", "severity": "low", "reported_by": "Alice"},
    )

    org_a_list = client.get("/api/v1/incidents", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/incidents", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_incident_get_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="incident-get-a", email="admin@incident-get-a.example.com")
    org_b = register_organization(client, slug="incident-get-b", email="admin@incident-get-b.example.com")

    incident = client.post(
        "/api/v1/incidents",
        headers=auth_headers(org_a["access_token"]),
        json={"title": "Org A incident", "severity": "low", "reported_by": "Alice"},
    ).json()

    response = client.get(
        f"/api/v1/incidents/{incident['id']}", headers=auth_headers(org_b["access_token"])
    )
    assert response.status_code == 404


def test_incident_status_workflow(client: TestClient) -> None:
    org = register_organization(client, slug="incident-workflow", email="admin@incident-w.example.com")
    headers = auth_headers(org["access_token"])

    incident_id = client.post(
        "/api/v1/incidents",
        headers=headers,
        json={"title": "Data exfiltration attempt", "severity": "critical", "reported_by": "SOC"},
    ).json()["id"]

    illegal_jump = client.patch(
        f"/api/v1/incidents/{incident_id}/status", headers=headers, json={"status": "resolved"}
    )
    assert illegal_jump.status_code == 409

    investigating = client.patch(
        f"/api/v1/incidents/{incident_id}/status", headers=headers, json={"status": "investigating"}
    )
    assert investigating.status_code == 200
    assert investigating.json()["status"] == "investigating"
    assert investigating.json()["resolved_at"] is None

    resolved = client.patch(
        f"/api/v1/incidents/{incident_id}/status", headers=headers, json={"status": "resolved"}
    )
    assert resolved.status_code == 200
    assert resolved.json()["status"] == "resolved"
    assert resolved.json()["resolved_at"] is not None

    # Reopening must clear resolved_at, not leave it stale -- this is the
    # regression test for the completed_at-staleness bug found in
    # AuditRepository.set_corrective_action_status (see the migration/service
    # docstrings for why this repository unconditionally assigns instead).
    reopened = client.patch(
        f"/api/v1/incidents/{incident_id}/status", headers=headers, json={"status": "investigating"}
    )
    assert reopened.status_code == 200
    assert reopened.json()["status"] == "investigating"
    assert reopened.json()["resolved_at"] is None

    resolved_again = client.patch(
        f"/api/v1/incidents/{incident_id}/status", headers=headers, json={"status": "resolved"}
    )
    assert resolved_again.status_code == 200

    closed = client.patch(
        f"/api/v1/incidents/{incident_id}/status", headers=headers, json={"status": "closed"}
    )
    assert closed.status_code == 200
    assert closed.json()["status"] == "closed"

    illegal_from_closed = client.patch(
        f"/api/v1/incidents/{incident_id}/status", headers=headers, json={"status": "investigating"}
    )
    assert illegal_from_closed.status_code == 409
