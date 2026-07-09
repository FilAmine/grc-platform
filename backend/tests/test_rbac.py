from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def _create_viewer_user(client: TestClient, admin_access_token: str, email: str) -> dict:
    create_response = client.post(
        "/api/v1/users",
        headers=auth_headers(admin_access_token),
        json={"email": email, "full_name": "Viewer User", "password": "ViewerSecret123"},
    )
    assert create_response.status_code == 201, create_response.text
    user = create_response.json()

    roles_response = client.get("/api/v1/roles", headers=auth_headers(admin_access_token))
    viewer_role = next(r for r in roles_response.json() if r["name"] == "Viewer")

    assign_response = client.post(
        f"/api/v1/users/{user['id']}/roles/{viewer_role['id']}",
        headers=auth_headers(admin_access_token),
    )
    assert assign_response.status_code == 204

    login_response = client.post(
        "/api/v1/auth/login", data={"username": email, "password": "ViewerSecret123"}
    )
    assert login_response.status_code == 200
    return login_response.json()


def test_viewer_role_can_read_but_not_manage_risks(client: TestClient) -> None:
    admin = register_organization(client, slug="rbac-org", email="admin@rbac.example.com")
    viewer_tokens = _create_viewer_user(client, admin["access_token"], "viewer@rbac.example.com")

    read_response = client.get("/api/v1/risks", headers=auth_headers(viewer_tokens["access_token"]))
    assert read_response.status_code == 200

    write_response = client.post(
        "/api/v1/risks",
        headers=auth_headers(viewer_tokens["access_token"]),
        json={"title": "x", "description": "y", "severity": "low", "owner": "z"},
    )
    assert write_response.status_code == 403


def test_viewer_cannot_manage_users(client: TestClient) -> None:
    admin = register_organization(client, slug="rbac-org2", email="admin@rbac2.example.com")
    viewer_tokens = _create_viewer_user(client, admin["access_token"], "viewer2@rbac2.example.com")

    response = client.post(
        "/api/v1/users",
        headers=auth_headers(viewer_tokens["access_token"]),
        json={"email": "new@rbac2.example.com", "full_name": "Someone", "password": "SomeSecret123"},
    )
    assert response.status_code == 403


def test_system_role_permissions_are_immutable(client: TestClient) -> None:
    admin = register_organization(client, slug="rbac-org3", email="admin@rbac3.example.com")
    roles_response = client.get("/api/v1/roles", headers=auth_headers(admin["access_token"]))
    admin_role = next(r for r in roles_response.json() if r["name"] == "Admin")

    response = client.put(
        f"/api/v1/roles/{admin_role['id']}/permissions",
        headers=auth_headers(admin["access_token"]),
        json={"permission_codes": []},
    )
    assert response.status_code == 403


def test_custom_role_permissions_can_be_updated(client: TestClient) -> None:
    admin = register_organization(client, slug="rbac-org4", email="admin@rbac4.example.com")
    create_response = client.post(
        "/api/v1/roles",
        headers=auth_headers(admin["access_token"]),
        json={"name": "Custom", "description": "custom role", "permission_codes": ["risks:read"]},
    )
    assert create_response.status_code == 201
    role = create_response.json()
    assert role["permission_codes"] == ["risks:read"]

    update_response = client.put(
        f"/api/v1/roles/{role['id']}/permissions",
        headers=auth_headers(admin["access_token"]),
        json={"permission_codes": ["risks:read", "risks:manage"]},
    )
    assert update_response.status_code == 200
    assert sorted(update_response.json()["permission_codes"]) == ["risks:manage", "risks:read"]
