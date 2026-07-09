from __future__ import annotations

from uuid import UUID

from backend.app.modules.ai.models import (
    ChatMessageModel,
    ChatSessionModel,
    KnowledgeBaseDocumentModel,
    PromptTemplateModel,
)
from backend.app.modules.ai.service import (
    ChatMessage,
    ChatSession,
    KnowledgeBaseDocument,
    PromptTemplate,
)
from sqlalchemy import or_, select
from sqlalchemy.orm import Session


def to_prompt_template(model: PromptTemplateModel) -> PromptTemplate:
    return PromptTemplate(
        id=model.id,
        organization_id=model.organization_id,
        name=model.name,
        template_text=model.template_text,
        description=model.description,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_kb_document(model: KnowledgeBaseDocumentModel) -> KnowledgeBaseDocument:
    return KnowledgeBaseDocument(
        id=model.id,
        organization_id=model.organization_id,
        title=model.title,
        content=model.content,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_chat_session(model: ChatSessionModel) -> ChatSession:
    return ChatSession(
        id=model.id,
        organization_id=model.organization_id,
        user_id=model.user_id,
        title=model.title,
        created_at=model.created_at,
        updated_at=model.updated_at,
    )


def to_chat_message(model: ChatMessageModel) -> ChatMessage:
    return ChatMessage(
        id=model.id,
        session_id=model.session_id,
        role=model.role,
        content=model.content,
        created_at=model.created_at,
    )


class SqlAlchemyPromptRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def list(self, organization_id: UUID | None) -> list[PromptTemplate]:
        statement = select(PromptTemplateModel)
        if organization_id is not None:
            statement = statement.where(
                or_(
                    PromptTemplateModel.organization_id == organization_id,
                    PromptTemplateModel.organization_id.is_(None),
                )
            )
        else:
            statement = statement.where(PromptTemplateModel.organization_id.is_(None))
        rows = self._session.scalars(statement.order_by(PromptTemplateModel.name)).all()
        return [to_prompt_template(row) for row in rows]

    def create(
        self, organization_id: UUID | None, name: str, template_text: str, description: str
    ) -> PromptTemplate:
        model = PromptTemplateModel(
            organization_id=organization_id, name=name, template_text=template_text, description=description
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_prompt_template(model)


class SqlAlchemyKnowledgeBaseRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create(
        self, organization_id: UUID, title: str, content: str, embedding: list[float]
    ) -> KnowledgeBaseDocument:
        model = KnowledgeBaseDocumentModel(
            organization_id=organization_id, title=title, content=content, embedding=embedding
        )
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_kb_document(model)

    def list_with_embeddings(
        self, organization_id: UUID
    ) -> list[tuple[KnowledgeBaseDocument, list[float]]]:
        statement = select(KnowledgeBaseDocumentModel).where(
            KnowledgeBaseDocumentModel.organization_id == organization_id
        )
        rows = self._session.scalars(statement).all()
        return [(to_kb_document(row), row.embedding) for row in rows]


class SqlAlchemyChatRepository:
    def __init__(self, session: Session) -> None:
        self._session = session

    def create_session(self, organization_id: UUID, user_id: UUID, title: str) -> ChatSession:
        model = ChatSessionModel(organization_id=organization_id, user_id=user_id, title=title)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_chat_session(model)

    def get_session(self, session_id: UUID) -> ChatSession | None:
        model = self._session.get(ChatSessionModel, session_id)
        return to_chat_session(model) if model else None

    def list_sessions(self, organization_id: UUID, user_id: UUID) -> list[ChatSession]:
        statement = (
            select(ChatSessionModel)
            .where(ChatSessionModel.organization_id == organization_id, ChatSessionModel.user_id == user_id)
            .order_by(ChatSessionModel.created_at.desc())
        )
        rows = self._session.scalars(statement).all()
        return [to_chat_session(row) for row in rows]

    def add_message(self, session_id: UUID, role: str, content: str) -> ChatMessage:
        model = ChatMessageModel(session_id=session_id, role=role, content=content)
        self._session.add(model)
        self._session.commit()
        self._session.refresh(model)
        return to_chat_message(model)

    def list_messages(self, session_id: UUID) -> list[ChatMessage]:
        statement = (
            select(ChatMessageModel)
            .where(ChatMessageModel.session_id == session_id)
            .order_by(ChatMessageModel.created_at)
        )
        rows = self._session.scalars(statement).all()
        return [to_chat_message(row) for row in rows]
