from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_task_create_and_list(client: TestClient) -> None:
    org = register_organization(client, slug="task-org", email="admin@task.example.com")
    headers = auth_headers(org["access_token"])

    task = client.post(
        "/api/v1/tasks",
        headers=headers,
        json={"title": "Rotate access keys", "assignee": "Security Team"},
    )
    assert task.status_code == 201, task.text
    body = task.json()
    assert body["status"] == "open"

    listed = client.get("/api/v1/tasks", headers=headers).json()
    assert any(t["id"] == body["id"] for t in listed)


def test_task_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="task-a", email="admin@task-a.example.com")
    org_b = register_organization(client, slug="task-b", email="admin@task-b.example.com")

    client.post(
        "/api/v1/tasks",
        headers=auth_headers(org_a["access_token"]),
        json={"title": "Org A task", "assignee": "Alice"},
    )

    org_a_list = client.get("/api/v1/tasks", headers=auth_headers(org_a["access_token"])).json()
    org_b_list = client.get("/api/v1/tasks", headers=auth_headers(org_b["access_token"])).json()

    assert len(org_a_list) == 1
    assert org_b_list == []


def test_task_get_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="task-get-a", email="admin@task-get-a.example.com")
    org_b = register_organization(client, slug="task-get-b", email="admin@task-get-b.example.com")

    task = client.post(
        "/api/v1/tasks",
        headers=auth_headers(org_a["access_token"]),
        json={"title": "Org A task", "assignee": "Alice"},
    ).json()

    response = client.get(f"/api/v1/tasks/{task['id']}", headers=auth_headers(org_b["access_token"]))
    assert response.status_code == 404


def test_task_status_workflow(client: TestClient) -> None:
    org = register_organization(client, slug="task-workflow", email="admin@task-w.example.com")
    headers = auth_headers(org["access_token"])

    task_id = client.post(
        "/api/v1/tasks",
        headers=headers,
        json={"title": "Patch servers", "assignee": "Ops"},
    ).json()["id"]

    illegal_jump = client.patch(
        f"/api/v1/tasks/{task_id}/status", headers=headers, json={"status": "done"}
    )
    assert illegal_jump.status_code == 409

    started = client.patch(
        f"/api/v1/tasks/{task_id}/status", headers=headers, json={"status": "in_progress"}
    )
    assert started.status_code == 200
    assert started.json()["status"] == "in_progress"

    completed = client.patch(
        f"/api/v1/tasks/{task_id}/status", headers=headers, json={"status": "done"}
    )
    assert completed.status_code == 200
    assert completed.json()["status"] == "done"

    illegal_from_done = client.patch(
        f"/api/v1/tasks/{task_id}/status", headers=headers, json={"status": "open"}
    )
    assert illegal_from_done.status_code == 409

    reopened = client.patch(
        f"/api/v1/tasks/{task_id}/status", headers=headers, json={"status": "in_progress"}
    )
    assert reopened.status_code == 200
    assert reopened.json()["status"] == "in_progress"
