from datetime import datetime
from uuid import UUID

from pydantic import Field

from backend.app.common.schemas import ReadSchema


class PromptTemplateCreate(ReadSchema):
    name: str = Field(min_length=2, max_length=255)
    template_text: str = Field(min_length=1, max_length=8000)
    description: str = Field(default="", max_length=2000)


class PromptTemplateRead(ReadSchema):
    id: UUID
    organization_id: UUID | None
    name: str
    template_text: str
    description: str
    created_at: datetime
    updated_at: datetime


class KnowledgeBaseDocumentCreate(ReadSchema):
    title: str = Field(min_length=2, max_length=255)
    content: str = Field(min_length=1, max_length=20000)


class KnowledgeBaseDocumentRead(ReadSchema):
    id: UUID
    organization_id: UUID
    title: str
    content: str
    created_at: datetime
    updated_at: datetime


class ChatSessionCreate(ReadSchema):
    title: str = Field(default="New chat", max_length=255)


class ChatSessionRead(ReadSchema):
    id: UUID
    organization_id: UUID
    user_id: UUID
    title: str
    created_at: datetime
    updated_at: datetime


class ChatMessageCreate(ReadSchema):
    content: str = Field(min_length=1, max_length=8000)


class ChatMessageRead(ReadSchema):
    id: UUID
    session_id: UUID
    role: str
    content: str
    created_at: datetime
