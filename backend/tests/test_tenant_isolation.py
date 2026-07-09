from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def _create_risk(client: TestClient, access_token: str, title: str = "A risk") -> dict:
    response = client.post(
        "/api/v1/risks",
        headers=auth_headers(access_token),
        json={"title": title, "description": "desc", "severity": "high", "owner": "Owner"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def test_unauthenticated_requests_are_rejected(client: TestClient) -> None:
    assert client.get("/api/v1/risks").status_code == 401
    assert client.get("/api/v1/controls").status_code == 401
    assert client.get("/api/v1/organizations").status_code == 401


def test_risk_created_in_org_is_scoped_to_that_org(client: TestClient) -> None:
    org_a = register_organization(client, slug="org-a", email="admin@org-a.example.com")
    org_b = register_organization(client, slug="org-b", email="admin@org-b.example.com")

    risk = _create_risk(client, org_a["access_token"], "Org A risk")
    assert risk["organization_id"]

    org_a_list = client.get("/api/v1/risks", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/risks", headers=auth_headers(org_b["access_token"])).json()

    assert any(r["id"] == risk["id"] for r in org_a_list)
    assert all(r["id"] != risk["id"] for r in org_b_list)
    assert org_b_list == []


def test_organization_client_cannot_pick_a_different_tenant(client: TestClient) -> None:
    org_a = register_organization(client, slug="org-a2", email="admin@org-a2.example.com")
    org_b = register_organization(client, slug="org-b2", email="admin@org-b2.example.com")

    other_org_id = client.get("/api/v1/auth/me", headers=auth_headers(org_b["access_token"])).json()[
        "organization_id"
    ]

    # RiskCreate no longer accepts organization_id at all; even if a client tries to
    # smuggle one in the body it must be ignored because the server derives the
    # tenant from the authenticated user, not from client input.
    response = client.post(
        "/api/v1/risks",
        headers=auth_headers(org_a["access_token"]),
        json={
            "organization_id": other_org_id,
            "title": "Attempted cross-tenant write",
            "description": "desc",
            "severity": "low",
            "owner": "Attacker",
        },
    )
    assert response.status_code == 201
    created = response.json()
    assert created["organization_id"] != other_org_id


def test_regular_user_only_sees_own_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="org-a3", email="admin@org-a3.example.com")
    register_organization(client, slug="org-b3", email="admin@org-b3.example.com")

    visible = client.get("/api/v1/organizations", headers=auth_headers(org_a["access_token"])).json()
    assert len(visible) == 1
    assert visible[0]["slug"] == "org-a3"


def test_non_superuser_cannot_create_organization_directly(client: TestClient) -> None:
    org_a = register_organization(client, slug="org-a4", email="admin@org-a4.example.com")
    response = client.post(
        "/api/v1/organizations",
        headers=auth_headers(org_a["access_token"]),
        json={"name": "Sneaky Co", "slug": "sneaky-co"},
    )
    assert response.status_code == 403
