from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_department_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="dept-org", email="admin@dept.example.com")
    headers = auth_headers(org["access_token"])

    department = client.post(
        "/api/v1/departments",
        headers=headers,
        json={"name": "Engineering", "description": "Builds the product"},
    )
    assert department.status_code == 201, department.text
    body = department.json()
    assert body["parent_department_id"] is None

    listed = client.get("/api/v1/departments", headers=headers).json()
    assert any(d["id"] == body["id"] for d in listed)


def test_department_hierarchy_via_parent_id(client: TestClient) -> None:
    org = register_organization(client, slug="dept-hierarchy", email="admin@dept-h.example.com")
    headers = auth_headers(org["access_token"])

    parent = client.post(
        "/api/v1/departments", headers=headers, json={"name": "Engineering"}
    ).json()
    child = client.post(
        "/api/v1/departments",
        headers=headers,
        json={"name": "Platform Team", "parent_department_id": parent["id"]},
    )
    assert child.status_code == 201, child.text
    assert child.json()["parent_department_id"] == parent["id"]


def test_department_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="dept-a", email="admin@dept-a.example.com")
    org_b = register_organization(client, slug="dept-b", email="admin@dept-b.example.com")

    client.post(
        "/api/v1/departments",
        headers=auth_headers(org_a["access_token"]),
        json={"name": "Org A department"},
    )

    org_a_list = client.get("/api/v1/departments", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/departments", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_department_parent_cannot_reference_another_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="dept-cross-a", email="admin@dept-cross-a.example.com")
    org_b = register_organization(client, slug="dept-cross-b", email="admin@dept-cross-b.example.com")

    org_a_department = client.post(
        "/api/v1/departments",
        headers=auth_headers(org_a["access_token"]),
        json={"name": "Org A department"},
    ).json()

    response = client.post(
        "/api/v1/departments",
        headers=auth_headers(org_b["access_token"]),
        json={"name": "Sneaky child", "parent_department_id": org_a_department["id"]},
    )
    assert response.status_code == 404
