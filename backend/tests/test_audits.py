from fastapi.testclient import TestClient

from backend.tests.conftest import auth_headers, register_organization


def test_audit_lifecycle_findings_and_corrective_actions(client: TestClient) -> None:
    org = register_organization(client, slug="audit-org", email="admin@audit.example.com")
    headers = auth_headers(org["access_token"])

    audit = client.post(
        "/api/v1/audits",
        headers=headers,
        json={"title": "Q3 Internal Audit", "scope": "Access control", "lead_auditor": "Jane Auditor"},
    )
    assert audit.status_code == 201
    audit_id = audit.json()["id"]
    assert audit.json()["status"] == "planned"

    item = client.post(
        f"/api/v1/audits/{audit_id}/checklist-items",
        headers=headers,
        json={"description": "Verify MFA is enforced for all admins"},
    )
    assert item.status_code == 201
    item_id = item.json()["id"]

    updated_item = client.put(
        f"/api/v1/audits/checklist-items/{item_id}/status",
        headers=headers,
        json={"status": "done", "notes": "Confirmed via IdP config"},
    )
    assert updated_item.status_code == 200
    assert updated_item.json()["status"] == "done"

    finding = client.post(
        f"/api/v1/audits/{audit_id}/findings",
        headers=headers,
        json={
            "title": "Shared admin account in use",
            "description": "One admin account is shared by three engineers",
            "severity": "major",
            "checklist_item_id": item_id,
        },
    )
    assert finding.status_code == 201
    finding_id = finding.json()["id"]

    action = client.post(
        f"/api/v1/audits/findings/{finding_id}/corrective-actions",
        headers=headers,
        json={"description": "Provision individual admin accounts", "owner": "IT Team"},
    )
    assert action.status_code == 201
    action_id = action.json()["id"]
    assert action.json()["status"] == "open"

    completed = client.patch(
        f"/api/v1/audits/corrective-actions/{action_id}/status",
        headers=headers,
        json={"status": "done"},
    )
    assert completed.status_code == 200
    assert completed.json()["status"] == "done"
    assert completed.json()["completed_at"] is not None

    report = client.get(f"/api/v1/audits/{audit_id}/report", headers=headers)
    assert report.status_code == 200
    body = report.json()
    assert body["checklist_total"] == 1
    assert body["checklist_done"] == 1
    assert body["findings_by_severity"] == {"major": 1}
    assert body["corrective_actions_total"] == 1
    assert body["corrective_actions_done"] == 1

    illegal_jump = client.patch(
        f"/api/v1/audits/{audit_id}/status", headers=headers, json={"status": "completed"}
    )
    assert illegal_jump.status_code == 409

    started = client.patch(
        f"/api/v1/audits/{audit_id}/status", headers=headers, json={"status": "in_progress"}
    )
    assert started.status_code == 200
    assert started.json()["status"] == "in_progress"

    status_update = client.patch(
        f"/api/v1/audits/{audit_id}/status", headers=headers, json={"status": "completed"}
    )
    assert status_update.status_code == 200
    assert status_update.json()["status"] == "completed"


def test_audit_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="audit-a", email="admin@audit-a.example.com")
    org_b = register_organization(client, slug="audit-b", email="admin@audit-b.example.com")

    audit = client.post(
        "/api/v1/audits",
        headers=auth_headers(org_a["access_token"]),
        json={"title": "Org A audit", "scope": "x", "lead_auditor": "Someone"},
    ).json()

    response = client.get(f"/api/v1/audits/{audit['id']}", headers=auth_headers(org_b["access_token"]))
    assert response.status_code == 404
