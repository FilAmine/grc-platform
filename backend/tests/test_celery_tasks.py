from backend.app.core.tasks import _recompute_all_compliance_scores
from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session


def _build_framework_with_requirement(client: TestClient, access_token: str) -> tuple[str, str]:
    headers = auth_headers(access_token)
    framework = client.post(
        "/api/v1/compliance/frameworks",
        headers=headers,
        json={"code": "iso27001", "name": "ISO/IEC 27001", "description": ""},
    ).json()
    version = client.post(
        f"/api/v1/compliance/frameworks/{framework['id']}/versions",
        headers=headers,
        json={"version": "2022"},
    ).json()
    requirement = client.post(
        f"/api/v1/compliance/framework-versions/{version['id']}/requirements",
        headers=headers,
        json={"code": "A.5.1", "title": "Policies for information security"},
    ).json()
    return version["id"], requirement["id"]


def test_recompute_scores_for_in_progress_assessment(client: TestClient, db_session: Session) -> None:
    org = register_organization(client, slug="celery-in-progress", email="admin@celery-ip.example.com")
    access = org["access_token"]
    headers = auth_headers(access)
    version_id, requirement_id = _build_framework_with_requirement(client, access)

    assessment_id = client.post(
        "/api/v1/compliance/assessments",
        headers=headers,
        json={"framework_version_id": version_id, "name": "In-progress assessment"},
    ).json()["id"]

    client.put(
        f"/api/v1/compliance/assessments/{assessment_id}/results/{requirement_id}",
        headers=headers,
        json={"status": "compliant", "notes": ""},
    )
    client.patch(
        f"/api/v1/compliance/assessments/{assessment_id}/status", headers=headers, json={"status": "in_progress"}
    )

    before = client.get(f"/api/v1/compliance/assessments/{assessment_id}/score", headers=headers)
    assert before.status_code == 200
    assert before.json() is None

    recomputed = _recompute_all_compliance_scores(db_session)
    assert recomputed == 1

    latest = client.get(f"/api/v1/compliance/assessments/{assessment_id}/score", headers=headers)
    assert latest.status_code == 200
    assert latest.json()["score"] == 100.0


def test_recompute_skips_draft_assessment(client: TestClient, db_session: Session) -> None:
    org = register_organization(client, slug="celery-draft", email="admin@celery-draft.example.com")
    access = org["access_token"]
    headers = auth_headers(access)
    version_id, _ = _build_framework_with_requirement(client, access)

    assessment_id = client.post(
        "/api/v1/compliance/assessments",
        headers=headers,
        json={"framework_version_id": version_id, "name": "Draft assessment"},
    ).json()["id"]

    recomputed = _recompute_all_compliance_scores(db_session)
    assert recomputed == 0

    after = client.get(f"/api/v1/compliance/assessments/{assessment_id}/score", headers=headers)
    assert after.status_code == 200
    assert after.json() is None
