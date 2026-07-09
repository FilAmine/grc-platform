from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_register_organization_returns_tokens(client: TestClient) -> None:
    tokens = register_organization(client)
    assert tokens["token_type"] == "bearer"  # noqa: S105
    assert tokens["access_token"]
    assert tokens["refresh_token"]


def test_register_organization_rejects_duplicate_email(client: TestClient) -> None:
    register_organization(client, slug="acme", email="dup@example.com")
    response = client.post(
        "/api/v1/auth/register-organization",
        json={
            "organization_name": "Other",
            "organization_slug": "other",
            "admin_email": "dup@example.com",
            "admin_full_name": "Someone Else",
            "admin_password": "SuperSecret123",
        },
    )
    assert response.status_code == 409


def test_login_success(client: TestClient) -> None:
    register_organization(client, email="login@example.com")
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "login@example.com", "password": "SuperSecret123"},
    )
    assert response.status_code == 200
    assert response.json()["access_token"]


def test_login_wrong_password_rejected(client: TestClient) -> None:
    register_organization(client, email="wrong@example.com")
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "wrong@example.com", "password": "not-the-password"},
    )
    assert response.status_code == 401


def test_account_locks_after_max_failed_attempts(client: TestClient) -> None:
    register_organization(client, email="lockout@example.com")
    for _ in range(5):
        client.post(
            "/api/v1/auth/login",
            data={"username": "lockout@example.com", "password": "wrong"},
        )
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "lockout@example.com", "password": "SuperSecret123"},
    )
    assert response.status_code == 401


def test_me_requires_bearer_token(client: TestClient) -> None:
    response = client.get("/api/v1/auth/me")
    assert response.status_code == 401


def test_me_returns_current_user(client: TestClient) -> None:
    tokens = register_organization(client, email="me@example.com")
    response = client.get("/api/v1/auth/me", headers=auth_headers(tokens["access_token"]))
    assert response.status_code == 200
    assert response.json()["email"] == "me@example.com"


def test_refresh_rotates_token_and_old_one_is_dead(client: TestClient) -> None:
    tokens = register_organization(client, email="refresh@example.com")
    response = client.post("/api/v1/auth/refresh", json={"refresh_token": tokens["refresh_token"]})
    assert response.status_code == 200
    new_tokens = response.json()
    assert new_tokens["refresh_token"] != tokens["refresh_token"]

    reuse_response = client.post("/api/v1/auth/refresh", json={"refresh_token": tokens["refresh_token"]})
    assert reuse_response.status_code == 401


def test_logout_revokes_refresh_token(client: TestClient) -> None:
    tokens = register_organization(client, email="logout@example.com")
    logout_response = client.post("/api/v1/auth/logout", json={"refresh_token": tokens["refresh_token"]})
    assert logout_response.status_code == 204

    refresh_response = client.post("/api/v1/auth/refresh", json={"refresh_token": tokens["refresh_token"]})
    assert refresh_response.status_code == 401
