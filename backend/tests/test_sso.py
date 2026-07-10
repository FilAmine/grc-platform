from collections.abc import Generator
from urllib.parse import parse_qs, unquote, urlparse

import pytest
from backend.app.interfaces.api import dependencies as deps
from backend.app.modules.sso.oidc_client import OidcClaims, OidcError
from backend.app.security.tokens import create_sso_state_token, decode_access_token
from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


@pytest.fixture(autouse=True)
def _clear_oidc_client_override() -> Generator[None, None, None]:
    from backend.app.main import app

    try:
        yield
    finally:
        app.dependency_overrides.pop(deps.get_oidc_client, None)


class FakeOidcClient:
    """Swappable double for HttpxOidcClient -- returns canned claims for known
    codes instead of making real network calls. See oidc_client.py's module
    docstring for why this codebase tests external providers this way rather
    than mocking httpx."""

    def __init__(self, claims_by_code: dict[str, OidcClaims] | None = None) -> None:
        self._claims_by_code = claims_by_code or {}

    def build_authorization_url(self, issuer: str, client_id: str, redirect_uri: str, state: str) -> str:
        return f"{issuer}/authorize?client_id={client_id}&redirect_uri={redirect_uri}&state={state}"

    def exchange_code(
        self, issuer: str, client_id: str, client_secret: str, redirect_uri: str, code: str
    ) -> OidcClaims:
        if code not in self._claims_by_code:
            raise OidcError(f"unknown authorization code: {code}")
        return self._claims_by_code[code]


def _use_fake_oidc_client(claims_by_code: dict[str, OidcClaims] | None = None) -> None:
    from backend.app.main import app

    app.dependency_overrides[deps.get_oidc_client] = lambda: FakeOidcClient(claims_by_code)


def _organization_id(access_token: str) -> str:
    return decode_access_token(access_token)["org"]


CONNECTION_PAYLOAD = {
    "issuer": "https://idp.example.com",
    "client_id": "grc-platform",
    "client_secret": "super-secret-value",
    "default_role_id": None,
    "is_enabled": True,
}


def test_connection_crud_and_secret_never_leaks(client: TestClient) -> None:
    org = register_organization(client, slug="sso-crud", email="admin@sso-crud.example.com")
    headers = auth_headers(org["access_token"])

    assert client.get("/api/v1/sso/connection", headers=headers).json() is None

    created = client.put("/api/v1/sso/connection", headers=headers, json=CONNECTION_PAYLOAD)
    assert created.status_code == 200, created.text
    body = created.json()
    assert body["issuer"] == CONNECTION_PAYLOAD["issuer"]
    assert body["client_id"] == CONNECTION_PAYLOAD["client_id"]
    assert "client_secret" not in body

    fetched = client.get("/api/v1/sso/connection", headers=headers)
    assert fetched.status_code == 200
    assert "client_secret" not in fetched.json()
    assert fetched.json()["is_enabled"] is True

    updated = client.put(
        "/api/v1/sso/connection", headers=headers, json={**CONNECTION_PAYLOAD, "is_enabled": False}
    )
    assert updated.json()["is_enabled"] is False

    deleted = client.delete("/api/v1/sso/connection", headers=headers)
    assert deleted.status_code == 204
    assert client.get("/api/v1/sso/connection", headers=headers).json() is None


def test_connection_requires_sso_manage_permission(client: TestClient) -> None:
    org = register_organization(client, slug="sso-perm", email="admin@sso-perm.example.com")
    headers = auth_headers(org["access_token"])

    roles = client.get("/api/v1/roles", headers=headers).json()
    viewer_role = next(r for r in roles if r["name"] == "Viewer")

    invited = client.post(
        "/api/v1/users",
        headers=headers,
        json={"email": "viewer@sso-perm.example.com", "full_name": "Viewer User", "password": "SuperSecret123"},
    ).json()
    client.post(f"/api/v1/users/{invited['id']}/roles/{viewer_role['id']}", headers=headers)

    viewer_login = client.post(
        "/api/v1/auth/login",
        data={"username": "viewer@sso-perm.example.com", "password": "SuperSecret123"},
    ).json()
    viewer_headers = auth_headers(viewer_login["access_token"])

    response = client.put("/api/v1/sso/connection", headers=viewer_headers, json=CONNECTION_PAYLOAD)
    assert response.status_code == 403


def test_sso_login_redirects_when_configured(client: TestClient) -> None:
    org = register_organization(client, slug="sso-login", email="admin@sso-login.example.com")
    headers = auth_headers(org["access_token"])
    client.put("/api/v1/sso/connection", headers=headers, json=CONNECTION_PAYLOAD)
    _use_fake_oidc_client()

    response = client.get("/api/v1/auth/sso/sso-login/login", follow_redirects=False)
    assert response.status_code == 307
    location = response.headers["location"]
    assert location.startswith(f"{CONNECTION_PAYLOAD['issuer']}/authorize")
    query = parse_qs(urlparse(location).query)
    assert query["client_id"] == [CONNECTION_PAYLOAD["client_id"]]
    assert "state" in query


def test_sso_login_404_when_not_configured(client: TestClient) -> None:
    register_organization(client, slug="sso-unconfigured", email="admin@sso-unconfigured.example.com")
    response = client.get("/api/v1/auth/sso/sso-unconfigured/login", follow_redirects=False)
    assert response.status_code == 404


def test_sso_login_404_when_organization_unknown(client: TestClient) -> None:
    response = client.get("/api/v1/auth/sso/does-not-exist/login", follow_redirects=False)
    assert response.status_code == 404


def test_sso_callback_provisions_new_user_with_default_role(client: TestClient) -> None:
    org = register_organization(client, slug="sso-jit", email="admin@sso-jit.example.com")
    headers = auth_headers(org["access_token"])
    roles = client.get("/api/v1/roles", headers=headers).json()
    auditor_role = next(r for r in roles if r["name"] == "Auditor")

    client.put(
        "/api/v1/sso/connection",
        headers=headers,
        json={**CONNECTION_PAYLOAD, "default_role_id": auditor_role["id"]},
    )
    _use_fake_oidc_client(
        {"good-code": OidcClaims(email="newhire@sso-jit.example.com", name="New Hire")}
    )

    state = create_sso_state_token(_organization_id(org["access_token"]))
    response = client.get(
        f"/api/v1/auth/sso/callback?code=good-code&state={state}", follow_redirects=False
    )
    assert response.status_code == 307
    location = response.headers["location"]
    assert location.startswith("http://localhost:5173/sso/callback#")
    fragment = dict(pair.split("=", 1) for pair in location.split("#", 1)[1].split("&"))
    assert "access_token" in fragment and "refresh_token" in fragment

    me = client.get("/api/v1/auth/me", headers=auth_headers(fragment["access_token"]))
    assert me.status_code == 200
    me_body = me.json()
    assert me_body["email"] == "newhire@sso-jit.example.com"
    assert me_body["full_name"] == "New Hire"
    assert auditor_role["id"] in me_body["role_ids"]


def test_sso_callback_reuses_existing_user_on_second_login(client: TestClient) -> None:
    org = register_organization(client, slug="sso-reuse", email="admin@sso-reuse.example.com")
    headers = auth_headers(org["access_token"])
    client.put("/api/v1/sso/connection", headers=headers, json=CONNECTION_PAYLOAD)
    _use_fake_oidc_client({"code-1": OidcClaims(email="repeat@sso-reuse.example.com", name="Repeat User")})

    state = create_sso_state_token(_organization_id(org["access_token"]))
    first = client.get(f"/api/v1/auth/sso/callback?code=code-1&state={state}", follow_redirects=False)
    first_fragment = dict(
        pair.split("=", 1) for pair in first.headers["location"].split("#", 1)[1].split("&")
    )
    first_user_id = client.get(
        "/api/v1/auth/me", headers=auth_headers(first_fragment["access_token"])
    ).json()["id"]

    users_after_first = client.get("/api/v1/users", headers=headers).json()

    second = client.get(f"/api/v1/auth/sso/callback?code=code-1&state={state}", follow_redirects=False)
    second_fragment = dict(
        pair.split("=", 1) for pair in second.headers["location"].split("#", 1)[1].split("&")
    )
    second_user_id = client.get(
        "/api/v1/auth/me", headers=auth_headers(second_fragment["access_token"])
    ).json()["id"]

    assert first_user_id == second_user_id
    users_after_second = client.get("/api/v1/users", headers=headers).json()
    assert len(users_after_first) == len(users_after_second)


def test_sso_callback_rejects_invalid_state(client: TestClient) -> None:
    org = register_organization(client, slug="sso-badstate", email="admin@sso-badstate.example.com")
    headers = auth_headers(org["access_token"])
    client.put("/api/v1/sso/connection", headers=headers, json=CONNECTION_PAYLOAD)
    _use_fake_oidc_client({"good-code": OidcClaims(email="x@sso-badstate.example.com", name=None)})

    response = client.get(
        "/api/v1/auth/sso/callback?code=good-code&state=not-a-real-token", follow_redirects=False
    )
    assert response.status_code == 307
    location = response.headers["location"]
    assert "#error=" in location
    assert "access_token" not in location


def test_sso_callback_rejects_disabled_connection(client: TestClient) -> None:
    org = register_organization(client, slug="sso-disabled", email="admin@sso-disabled.example.com")
    headers = auth_headers(org["access_token"])
    client.put("/api/v1/sso/connection", headers=headers, json={**CONNECTION_PAYLOAD, "is_enabled": False})
    _use_fake_oidc_client({"good-code": OidcClaims(email="x@sso-disabled.example.com", name=None)})

    state = create_sso_state_token(_organization_id(org["access_token"]))
    response = client.get(
        f"/api/v1/auth/sso/callback?code=good-code&state={state}", follow_redirects=False
    )
    assert response.status_code == 307
    location = response.headers["location"]
    assert "#error=" in location
    assert unquote(location.split("#error=", 1)[1])
