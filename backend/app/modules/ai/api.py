from uuid import UUID

from backend.app.interfaces.api.dependencies import (
    get_chat_service,
    get_current_user,
    get_knowledge_base_service,
    get_prompt_library_service,
    require_permission,
)
from backend.app.modules.ai.schemas import (
    ChatMessageCreate,
    ChatMessageRead,
    ChatSessionCreate,
    ChatSessionRead,
    KnowledgeBaseDocumentCreate,
    KnowledgeBaseDocumentRead,
    PromptTemplateCreate,
    PromptTemplateRead,
)
from backend.app.modules.ai.service import (
    ChatService,
    ChatSessionNotFoundError,
    CreatePromptTemplateCommand,
    KnowledgeBaseService,
    PromptLibraryService,
)
from backend.app.modules.users.service import User
from backend.app.security.permissions import AI_MANAGE, AI_USE
from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()


@router.get(
    "/prompts", response_model=list[PromptTemplateRead], dependencies=[Depends(require_permission(AI_USE))]
)
def list_prompt_templates(
    current_user: User = Depends(get_current_user),
    service: PromptLibraryService = Depends(get_prompt_library_service),
) -> list[PromptTemplateRead]:
    return [PromptTemplateRead.model_validate(p) for p in service.list_templates(current_user.organization_id)]


@router.post(
    "/prompts", response_model=PromptTemplateRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(AI_MANAGE))],
)
def create_prompt_template(
    payload: PromptTemplateCreate,
    current_user: User = Depends(get_current_user),
    service: PromptLibraryService = Depends(get_prompt_library_service),
) -> PromptTemplateRead:
    template = service.create_template(
        CreatePromptTemplateCommand(organization_id=current_user.organization_id, **payload.model_dump())
    )
    return PromptTemplateRead.model_validate(template)


@router.post(
    "/knowledge-base", response_model=KnowledgeBaseDocumentRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(AI_MANAGE))],
)
def add_knowledge_base_document(
    payload: KnowledgeBaseDocumentCreate,
    current_user: User = Depends(get_current_user),
    service: KnowledgeBaseService = Depends(get_knowledge_base_service),
) -> KnowledgeBaseDocumentRead:
    document = service.add_document(current_user.organization_id, payload.title, payload.content)
    return KnowledgeBaseDocumentRead.model_validate(document)


@router.get(
    "/chat/sessions", response_model=list[ChatSessionRead], dependencies=[Depends(require_permission(AI_USE))]
)
def list_chat_sessions(
    current_user: User = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
) -> list[ChatSessionRead]:
    return [
        ChatSessionRead.model_validate(s)
        for s in service.list_sessions(current_user.organization_id, current_user.id)
    ]


@router.post(
    "/chat/sessions", response_model=ChatSessionRead, status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(AI_USE))],
)
def create_chat_session(
    payload: ChatSessionCreate,
    current_user: User = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
) -> ChatSessionRead:
    session = service.create_session(current_user.organization_id, current_user.id, payload.title)
    return ChatSessionRead.model_validate(session)


@router.get(
    "/chat/sessions/{session_id}/messages", response_model=list[ChatMessageRead],
    dependencies=[Depends(require_permission(AI_USE))],
)
def list_chat_messages(
    session_id: UUID,
    service: ChatService = Depends(get_chat_service),
) -> list[ChatMessageRead]:
    return [ChatMessageRead.model_validate(m) for m in service.list_messages(session_id)]


@router.post(
    "/chat/sessions/{session_id}/messages", response_model=ChatMessageRead,
    dependencies=[Depends(require_permission(AI_USE))],
)
def send_chat_message(
    session_id: UUID,
    payload: ChatMessageCreate,
    current_user: User = Depends(get_current_user),
    service: ChatService = Depends(get_chat_service),
) -> ChatMessageRead:
    try:
        reply = service.send_message(session_id, current_user.organization_id, payload.content)
    except ChatSessionNotFoundError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc
    return ChatMessageRead.model_validate(reply)
