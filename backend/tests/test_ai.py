from backend.tests.conftest import auth_headers, register_organization
from fastapi.testclient import TestClient


def test_prompt_library_crud(client: TestClient) -> None:
    org = register_organization(client, slug="ai-org", email="admin@ai.example.com")
    headers = auth_headers(org["access_token"])

    created = client.post(
        "/api/v1/ai/prompts",
        headers=headers,
        json={"name": "Risk summary", "template_text": "Summarize this risk: {{risk}}"},
    )
    assert created.status_code == 201

    listed = client.get("/api/v1/ai/prompts", headers=headers).json()
    assert any(p["name"] == "Risk summary" for p in listed)


def test_chat_with_rag_uses_knowledge_base_context(client: TestClient) -> None:
    org = register_organization(client, slug="ai-org2", email="admin@ai2.example.com")
    headers = auth_headers(org["access_token"])

    kb = client.post(
        "/api/v1/ai/knowledge-base",
        headers=headers,
        json={"title": "Password Policy", "content": "Passwords must be at least 12 characters."},
    )
    assert kb.status_code == 201

    session = client.post("/api/v1/ai/chat/sessions", headers=headers, json={"title": "Q&A"})
    assert session.status_code == 201
    session_id = session.json()["id"]

    reply = client.post(
        f"/api/v1/ai/chat/sessions/{session_id}/messages",
        headers=headers,
        json={"content": "What is the password policy?"},
    )
    assert reply.status_code == 200
    assert reply.json()["role"] == "assistant"
    assert "echo" in reply.json()["content"]

    messages = client.get(f"/api/v1/ai/chat/sessions/{session_id}/messages", headers=headers).json()
    assert len(messages) == 2
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"


def test_chat_session_not_found(client: TestClient) -> None:
    org = register_organization(client, slug="ai-org3", email="admin@ai3.example.com")
    headers = auth_headers(org["access_token"])

    import uuid

    response = client.post(
        f"/api/v1/ai/chat/sessions/{uuid.uuid4()}/messages", headers=headers, json={"content": "hi"}
    )
    assert response.status_code == 404
