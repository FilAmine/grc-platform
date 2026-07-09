from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID

from backend.app.modules.ai.providers import AIProvider, cosine_similarity

DEFAULT_SYSTEM_PROMPT = (
    "You are a GRC (Governance, Risk & Compliance) assistant. Answer using the "
    "provided context when relevant, and say when you are unsure."
)


@dataclass(frozen=True)
class PromptTemplate:
    id: UUID
    organization_id: UUID | None
    name: str
    template_text: str
    description: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class KnowledgeBaseDocument:
    id: UUID
    organization_id: UUID
    title: str
    content: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class ChatSession:
    id: UUID
    organization_id: UUID
    user_id: UUID
    title: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class ChatMessage:
    id: UUID
    session_id: UUID
    role: str
    content: str
    created_at: datetime


@dataclass(frozen=True)
class CreatePromptTemplateCommand:
    organization_id: UUID | None
    name: str
    template_text: str
    description: str = ""


class PromptStore(Protocol):
    def list(self, organization_id: UUID | None) -> list[PromptTemplate]:
        raise NotImplementedError

    def create(
        self, organization_id: UUID | None, name: str, template_text: str, description: str
    ) -> PromptTemplate:
        raise NotImplementedError


class PromptLibraryService:
    def __init__(self, prompts: PromptStore) -> None:
        self._prompts = prompts

    def list_templates(self, organization_id: UUID | None) -> list[PromptTemplate]:
        return self._prompts.list(organization_id)

    def create_template(self, command: CreatePromptTemplateCommand) -> PromptTemplate:
        return self._prompts.create(
            command.organization_id, command.name, command.template_text, command.description
        )


class KnowledgeBaseStore(Protocol):
    def create(
        self, organization_id: UUID, title: str, content: str, embedding: list[float]
    ) -> KnowledgeBaseDocument:
        raise NotImplementedError

    def list_with_embeddings(self, organization_id: UUID) -> list[tuple[KnowledgeBaseDocument, list[float]]]:
        raise NotImplementedError


class KnowledgeBaseService:
    def __init__(self, documents: KnowledgeBaseStore, provider: AIProvider) -> None:
        self._documents = documents
        self._provider = provider

    def add_document(self, organization_id: UUID, title: str, content: str) -> KnowledgeBaseDocument:
        embedding = self._provider.embed(content)
        return self._documents.create(organization_id, title, content, embedding)

    def search(self, organization_id: UUID, query: str, top_k: int = 3) -> list[KnowledgeBaseDocument]:
        query_embedding = self._provider.embed(query)
        scored = [
            (cosine_similarity(query_embedding, embedding), document)
            for document, embedding in self._documents.list_with_embeddings(organization_id)
        ]
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [document for _score, document in scored[:top_k]]


class ChatStore(Protocol):
    def create_session(self, organization_id: UUID, user_id: UUID, title: str) -> ChatSession:
        raise NotImplementedError

    def get_session(self, session_id: UUID) -> ChatSession | None:
        raise NotImplementedError

    def list_sessions(self, organization_id: UUID, user_id: UUID) -> list[ChatSession]:
        raise NotImplementedError

    def add_message(self, session_id: UUID, role: str, content: str) -> ChatMessage:
        raise NotImplementedError

    def list_messages(self, session_id: UUID) -> list[ChatMessage]:
        raise NotImplementedError


class ChatSessionNotFoundError(Exception):
    pass


class ChatService:
    def __init__(self, sessions: ChatStore, knowledge_base: KnowledgeBaseService, provider: AIProvider) -> None:
        self._sessions = sessions
        self._knowledge_base = knowledge_base
        self._provider = provider

    def create_session(self, organization_id: UUID, user_id: UUID, title: str) -> ChatSession:
        return self._sessions.create_session(organization_id, user_id, title)

    def list_sessions(self, organization_id: UUID, user_id: UUID) -> list[ChatSession]:
        return self._sessions.list_sessions(organization_id, user_id)

    def list_messages(self, session_id: UUID) -> list[ChatMessage]:
        return self._sessions.list_messages(session_id)

    def send_message(self, session_id: UUID, organization_id: UUID, content: str) -> ChatMessage:
        session = self._sessions.get_session(session_id)
        if session is None:
            raise ChatSessionNotFoundError("chat session not found")

        self._sessions.add_message(session_id, "user", content)
        history = self._sessions.list_messages(session_id)

        relevant_docs = self._knowledge_base.search(organization_id, content)
        system_prompt = DEFAULT_SYSTEM_PROMPT
        if relevant_docs:
            context = "\n\n".join(f"- {doc.title}: {doc.content}" for doc in relevant_docs)
            system_prompt = f"{DEFAULT_SYSTEM_PROMPT}\n\nRelevant context:\n{context}"

        reply_text = self._provider.chat(system_prompt, [(m.role, m.content) for m in history])
        return self._sessions.add_message(session_id, "assistant", reply_text)
