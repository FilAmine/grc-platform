from fastapi.testclient import TestClient

from backend.tests.conftest import auth_headers, register_organization


def test_asset_crud_and_lifecycle(client: TestClient) -> None:
    org = register_organization(client, slug="cmdb-org", email="admin@cmdb.example.com")
    headers = auth_headers(org["access_token"])

    asset = client.post(
        "/api/v1/assets",
        headers=headers,
        json={
            "name": "prod-db-01",
            "asset_type": "hardware",
            "owner": "Infra Team",
            "supplier": "Dell",
            "confidentiality": "high",
            "integrity": "high",
            "availability": "high",
        },
    )
    assert asset.status_code == 201
    body = asset.json()
    assert body["lifecycle_stage"] == "planned"
    assert body["confidentiality"] == "high"
    asset_id = body["id"]

    listed = client.get("/api/v1/assets", headers=headers).json()
    assert any(a["id"] == asset_id for a in listed)

    updated = client.patch(
        f"/api/v1/assets/{asset_id}/lifecycle", headers=headers, json={"lifecycle_stage": "in_use"}
    )
    assert updated.status_code == 200
    assert updated.json()["lifecycle_stage"] == "in_use"


def test_asset_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="cmdb-a", email="admin@cmdb-a.example.com")
    org_b = register_organization(client, slug="cmdb-b", email="admin@cmdb-b.example.com")

    asset = client.post(
        "/api/v1/assets",
        headers=auth_headers(org_a["access_token"]),
        json={"name": "org-a-asset", "asset_type": "software", "owner": "IT"},
    ).json()

    response = client.get(f"/api/v1/assets/{asset['id']}", headers=auth_headers(org_b["access_token"]))
    assert response.status_code == 404
