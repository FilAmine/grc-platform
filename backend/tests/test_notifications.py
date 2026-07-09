from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_document_approval_notifies_the_author(client: TestClient) -> None:
    org = register_organization(client, slug="notif-org", email="admin@notif.example.com")
    headers = auth_headers(org["access_token"])

    document = client.post(
        "/api/v1/documents",
        headers=headers,
        json={
            "title": "Data Retention Policy",
            "document_type": "policy",
            "owner": "Legal",
            "file_reference": "s3://bucket/drp.pdf",
        },
    ).json()
    version_id = client.get(f"/api/v1/documents/{document['id']}/versions", headers=headers).json()[0]["id"]

    client.post(f"/api/v1/documents/versions/{version_id}/submit-for-approval", headers=headers)
    client.post(
        f"/api/v1/documents/versions/{version_id}/approval",
        headers=headers,
        json={"approve": True, "comment": "ok"},
    )

    notifications = client.get("/api/v1/notifications", headers=headers).json()
    assert len(notifications) == 1
    assert notifications[0]["subject"] == "Document version approved"
    assert notifications[0]["read_at"] is None

    marked = client.post(f"/api/v1/notifications/{notifications[0]['id']}/read", headers=headers)
    assert marked.status_code == 200
    assert marked.json()["read_at"] is not None


def test_document_rejection_also_notifies(client: TestClient) -> None:
    org = register_organization(client, slug="notif-org2", email="admin@notif2.example.com")
    headers = auth_headers(org["access_token"])

    document = client.post(
        "/api/v1/documents",
        headers=headers,
        json={"title": "Draft Standard", "document_type": "standard", "owner": "IT", "file_reference": "ref"},
    ).json()
    version_id = client.get(f"/api/v1/documents/{document['id']}/versions", headers=headers).json()[0]["id"]

    client.post(f"/api/v1/documents/versions/{version_id}/submit-for-approval", headers=headers)
    client.post(
        f"/api/v1/documents/versions/{version_id}/approval",
        headers=headers,
        json={"approve": False, "comment": "needs work"},
    )

    notifications = client.get("/api/v1/notifications", headers=headers).json()
    assert len(notifications) == 1
    assert notifications[0]["subject"] == "Document version rejected"
