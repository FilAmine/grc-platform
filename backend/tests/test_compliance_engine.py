from fastapi.testclient import TestClient

from backend.tests.conftest import auth_headers, register_organization


def _build_framework_with_requirements(client: TestClient, access_token: str) -> tuple[str, list[str]]:
    headers = auth_headers(access_token)
    framework = client.post(
        "/api/v1/compliance/frameworks",
        headers=headers,
        json={"code": "iso27001", "name": "ISO/IEC 27001", "description": "Information security"},
    ).json()

    version = client.post(
        f"/api/v1/compliance/frameworks/{framework['id']}/versions",
        headers=headers,
        json={"version": "2022"},
    ).json()

    requirement_ids = []
    for code, title in [("A.5.1", "Policies for information security"), ("A.8.1", "User endpoint devices")]:
        req = client.post(
            f"/api/v1/compliance/framework-versions/{version['id']}/requirements",
            headers=headers,
            json={"code": code, "title": title},
        ).json()
        requirement_ids.append(req["id"])

    return version["id"], requirement_ids


def test_framework_catalog_crud(client: TestClient) -> None:
    org = register_organization(client, slug="fw-org", email="admin@fw.example.com")
    headers = auth_headers(org["access_token"])

    framework = client.post(
        "/api/v1/compliance/frameworks",
        headers=headers,
        json={"code": "nist-csf", "name": "NIST CSF", "description": ""},
    )
    assert framework.status_code == 201
    framework_id = framework.json()["id"]

    listed = client.get("/api/v1/compliance/frameworks", headers=headers).json()
    assert any(f["id"] == framework_id for f in listed)


def test_assessment_lifecycle_and_scoring(client: TestClient) -> None:
    org = register_organization(client, slug="assess-org", email="admin@assess.example.com")
    access = org["access_token"]
    headers = auth_headers(access)

    version_id, (req1, req2) = _build_framework_with_requirements(client, access)

    assessment = client.post(
        "/api/v1/compliance/assessments",
        headers=headers,
        json={"framework_version_id": version_id, "name": "2026 ISO 27001 assessment"},
    )
    assert assessment.status_code == 201
    assessment_id = assessment.json()["id"]

    results = client.get(f"/api/v1/compliance/assessments/{assessment_id}/results", headers=headers).json()
    assert len(results) == 2
    assert all(r["status"] == "not_assessed" for r in results)

    r1 = client.put(
        f"/api/v1/compliance/assessments/{assessment_id}/results/{req1}",
        headers=headers,
        json={"status": "compliant", "notes": "policy in place"},
    )
    assert r1.status_code == 200
    assert r1.json()["status"] == "compliant"

    r2 = client.put(
        f"/api/v1/compliance/assessments/{assessment_id}/results/{req2}",
        headers=headers,
        json={"status": "non_compliant", "notes": "no MDM"},
    )
    assert r2.status_code == 200

    score_response = client.post(f"/api/v1/compliance/assessments/{assessment_id}/compute-score", headers=headers)
    assert score_response.status_code == 200
    assert score_response.json()["score"] == 50.0

    latest = client.get(f"/api/v1/compliance/assessments/{assessment_id}/score", headers=headers)
    assert latest.status_code == 200
    assert latest.json()["score"] == 50.0

    illegal_jump = client.patch(
        f"/api/v1/compliance/assessments/{assessment_id}/status",
        headers=headers,
        json={"status": "completed"},
    )
    assert illegal_jump.status_code == 409

    started = client.patch(
        f"/api/v1/compliance/assessments/{assessment_id}/status",
        headers=headers,
        json={"status": "in_progress"},
    )
    assert started.status_code == 200

    status_update = client.patch(
        f"/api/v1/compliance/assessments/{assessment_id}/status",
        headers=headers,
        json={"status": "completed"},
    )
    assert status_update.status_code == 200
    assert status_update.json()["status"] == "completed"


def test_control_mapping_and_evidence(client: TestClient) -> None:
    org = register_organization(client, slug="map-org", email="admin@map.example.com")
    access = org["access_token"]
    headers = auth_headers(access)

    version_id, (req1, _req2) = _build_framework_with_requirements(client, access)

    control = client.post(
        "/api/v1/controls",
        headers=headers,
        json={"name": "Endpoint MDM", "description": "Manage endpoints", "framework": "iso27001"},
    ).json()

    mapping = client.post(
        f"/api/v1/compliance/controls/{control['id']}/mappings/{req1}",
        headers=headers,
    )
    assert mapping.status_code == 201

    mappings = client.get(f"/api/v1/compliance/controls/{control['id']}/mappings", headers=headers).json()
    assert len(mappings) == 1

    evidence = client.post(
        "/api/v1/compliance/evidence",
        headers=headers,
        json={"title": "Policy PDF", "file_reference": "s3://bucket/policy.pdf", "control_id": control["id"]},
    )
    assert evidence.status_code == 201
    assert evidence.json()["control_id"] == control["id"]


def test_assessment_is_scoped_to_organization(client: TestClient) -> None:
    org_a = register_organization(client, slug="scope-a", email="admin@scope-a.example.com")
    org_b = register_organization(client, slug="scope-b", email="admin@scope-b.example.com")

    version_id, _ = _build_framework_with_requirements(client, org_a["access_token"])
    assessment = client.post(
        "/api/v1/compliance/assessments",
        headers=auth_headers(org_a["access_token"]),
        json={"framework_version_id": version_id, "name": "Org A assessment"},
    ).json()

    response = client.get(
        f"/api/v1/compliance/assessments/{assessment['id']}", headers=auth_headers(org_b["access_token"])
    )
    assert response.status_code == 404
