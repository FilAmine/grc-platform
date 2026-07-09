from uuid import UUID as PyUUID

from sqlalchemy import JSON, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID as PGUUID
from sqlalchemy.orm import Mapped, mapped_column

from backend.app.common.models import TenantScopedMixin, TimestampMixin, UUIDPKMixin
from backend.app.database import Base


class PromptTemplateModel(UUIDPKMixin, TimestampMixin, Base):
    """System templates (``organization_id`` NULL) ship with the platform; tenants
    can also define their own, mirroring the Role/Framework system/custom split."""

    __tablename__ = "prompt_templates"

    organization_id: Mapped[PyUUID | None] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("organizations.id", ondelete="CASCADE"), nullable=True, index=True
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    template_text: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False, default="")


class KnowledgeBaseDocumentModel(UUIDPKMixin, TenantScopedMixin, TimestampMixin, Base):
    """``embedding`` is stored as a plain JSON float array so this runs against any
    SQL backend (SQLite in tests, Postgres in prod) without a vector extension.
    At CMDB/KB scale a linear cosine-similarity scan is fine; swapping in pgvector
    later only touches this model and KnowledgeBaseRepository."""

    __tablename__ = "knowledge_base_documents"

    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    embedding: Mapped[list[float]] = mapped_column(JSON, nullable=False)


class ChatSessionModel(UUIDPKMixin, TenantScopedMixin, TimestampMixin, Base):
    __tablename__ = "chat_sessions"

    user_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False, default="New chat")


class ChatMessageModel(UUIDPKMixin, TimestampMixin, Base):
    __tablename__ = "chat_messages"

    session_id: Mapped[PyUUID] = mapped_column(
        PGUUID(as_uuid=True), ForeignKey("chat_sessions.id", ondelete="CASCADE"), index=True, nullable=False
    )
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
