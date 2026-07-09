from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_document_lifecycle_versioning_and_approval(client: TestClient) -> None:
    org = register_organization(client, slug="doc-org", email="admin@doc.example.com")
    headers = auth_headers(org["access_token"])

    document = client.post(
        "/api/v1/documents",
        headers=headers,
        json={
            "title": "Information Security Policy",
            "document_type": "policy",
            "owner": "CISO",
            "file_reference": "s3://bucket/isp-v1.pdf",
        },
    )
    assert document.status_code == 201
    document_id = document.json()["id"]
    assert document.json()["status"] == "draft"
    assert document.json()["published_version_id"] is None

    versions = client.get(f"/api/v1/documents/{document_id}/versions", headers=headers).json()
    assert len(versions) == 1
    version_id = versions[0]["id"]
    assert versions[0]["version_number"] == 1

    submit = client.post(f"/api/v1/documents/versions/{version_id}/submit-for-approval", headers=headers)
    assert submit.status_code == 200
    assert submit.json()["status"] == "pending_approval"

    approval = client.post(
        f"/api/v1/documents/versions/{version_id}/approval",
        headers=headers,
        json={"approve": True, "comment": "Looks good", "signature_reference": "docusign:env-123"},
    )
    assert approval.status_code == 200
    assert approval.json()["decision"] == "approved"

    published = client.get(f"/api/v1/documents/{document_id}", headers=headers).json()
    assert published["status"] == "published"
    assert published["published_version_id"] == version_id

    new_version = client.post(
        f"/api/v1/documents/{document_id}/versions",
        headers=headers,
        json={"file_reference": "s3://bucket/isp-v2.pdf", "change_summary": "Added remote work section"},
    )
    assert new_version.status_code == 201
    assert new_version.json()["version_number"] == 2

    archived = client.post(f"/api/v1/documents/{document_id}/archive", headers=headers)
    assert archived.status_code == 200
    assert archived.json()["status"] == "archived"


def test_approval_rejection_does_not_publish(client: TestClient) -> None:
    org = register_organization(client, slug="doc-org2", email="admin@doc2.example.com")
    headers = auth_headers(org["access_token"])

    document = client.post(
        "/api/v1/documents",
        headers=headers,
        json={"title": "Draft Procedure", "document_type": "procedure", "owner": "IT", "file_reference": "ref"},
    ).json()
    version_id = client.get(f"/api/v1/documents/{document['id']}/versions", headers=headers).json()[0]["id"]

    client.post(f"/api/v1/documents/versions/{version_id}/submit-for-approval", headers=headers)
    rejection = client.post(
        f"/api/v1/documents/versions/{version_id}/approval",
        headers=headers,
        json={"approve": False, "comment": "Needs rework"},
    )
    assert rejection.status_code == 200
    assert rejection.json()["decision"] == "rejected"

    document_after = client.get(f"/api/v1/documents/{document['id']}", headers=headers).json()
    assert document_after["status"] == "draft"
    assert document_after["published_version_id"] is None


def test_document_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="doc-a", email="admin@doc-a.example.com")
    org_b = register_organization(client, slug="doc-b", email="admin@doc-b.example.com")

    document = client.post(
        "/api/v1/documents",
        headers=auth_headers(org_a["access_token"]),
        json={"title": "Org A doc", "document_type": "policy", "owner": "xx", "file_reference": "ref"},
    ).json()

    response = client.get(f"/api/v1/documents/{document['id']}", headers=auth_headers(org_b["access_token"]))
    assert response.status_code == 404
