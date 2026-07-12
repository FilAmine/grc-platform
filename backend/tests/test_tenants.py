from backend.tests.conftest import auth_headers, promote_to_superuser, register_organization
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def _current_user_id(client: TestClient, access_token: str) -> str:
    return client.get("/api/v1/auth/me", headers=auth_headers(access_token)).json()["id"]


def test_non_superuser_cannot_list_or_create_tenants(client: TestClient) -> None:
    org = register_organization(client, slug="tenant-non-super", email="admin@tenant-non-super.example.com")
    headers = auth_headers(org["access_token"])

    assert client.get("/api/v1/tenants", headers=headers).status_code == 403
    create = client.post(
        "/api/v1/tenants", headers=headers, json={"name": "Acme Group", "slug": "acme-group"}
    )
    assert create.status_code == 403


def test_superuser_can_create_and_list_tenants(client: TestClient, db_session: Session) -> None:
    org = register_organization(client, slug="tenant-super", email="admin@tenant-super.example.com")
    token = org["access_token"]
    headers = auth_headers(token)
    promote_to_superuser(db_session, _current_user_id(client, token))

    created = client.post(
        "/api/v1/tenants", headers=headers, json={"name": "Acme Group", "slug": "acme-group"}
    )
    assert created.status_code == 201, created.text

    listed = client.get("/api/v1/tenants", headers=headers).json()
    assert any(t["slug"] == "acme-group" for t in listed)


def test_superuser_can_assign_and_clear_organization_tenant(client: TestClient, db_session: Session) -> None:
    org = register_organization(client, slug="tenant-assign", email="admin@tenant-assign.example.com")
    token = org["access_token"]
    headers = auth_headers(token)
    promote_to_superuser(db_session, _current_user_id(client, token))

    tenant = client.post(
        "/api/v1/tenants", headers=headers, json={"name": "Acme Group", "slug": "acme-group-2"}
    ).json()
    organization_id = client.get("/api/v1/auth/me", headers=headers).json()["organization_id"]

    assigned = client.patch(
        f"/api/v1/organizations/{organization_id}/tenant", headers=headers, json={"tenant_id": tenant["id"]}
    )
    assert assigned.status_code == 200, assigned.text
    assert assigned.json()["tenant_id"] == tenant["id"]

    cleared = client.patch(
        f"/api/v1/organizations/{organization_id}/tenant", headers=headers, json={"tenant_id": None}
    )
    assert cleared.status_code == 200
    assert cleared.json()["tenant_id"] is None


def test_assign_tenant_404s_on_unknown_tenant_id(client: TestClient, db_session: Session) -> None:
    org = register_organization(client, slug="tenant-unknown", email="admin@tenant-unknown.example.com")
    token = org["access_token"]
    headers = auth_headers(token)
    promote_to_superuser(db_session, _current_user_id(client, token))
    organization_id = client.get("/api/v1/auth/me", headers=headers).json()["organization_id"]

    response = client.patch(
        f"/api/v1/organizations/{organization_id}/tenant",
        headers=headers,
        json={"tenant_id": "00000000-0000-0000-0000-000000000000"},
    )
    assert response.status_code == 404


def test_non_superuser_cannot_assign_organization_tenant(client: TestClient) -> None:
    org = register_organization(client, slug="tenant-forbidden", email="admin@tenant-forbidden.example.com")
    headers = auth_headers(org["access_token"])
    organization_id = client.get("/api/v1/auth/me", headers=headers).json()["organization_id"]

    response = client.patch(
        f"/api/v1/organizations/{organization_id}/tenant", headers=headers, json={"tenant_id": None}
    )
    assert response.status_code == 403
