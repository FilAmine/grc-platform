from backend.app.interfaces.api.dependencies import (
    get_current_user,
    get_ecosystem_party_service,
    require_permission,
)
from backend.app.modules.ecosystem_parties.schemas import EcosystemPartyCreate, EcosystemPartyRead
from backend.app.modules.ecosystem_parties.service import (
    CreateEcosystemPartyCommand,
    EcosystemPartyService,
)
from backend.app.modules.users.service import User
from backend.app.security.permissions import ECOSYSTEM_PARTIES_MANAGE, ECOSYSTEM_PARTIES_READ
from fastapi import APIRouter, Depends, status

router = APIRouter()


@router.get(
    "",
    response_model=list[EcosystemPartyRead],
    dependencies=[Depends(require_permission(ECOSYSTEM_PARTIES_READ))],
)
def list_ecosystem_parties(
    current_user: User = Depends(get_current_user),
    service: EcosystemPartyService = Depends(get_ecosystem_party_service),
) -> list[EcosystemPartyRead]:
    return [
        EcosystemPartyRead.model_validate(item)
        for item in service.list_ecosystem_parties(current_user.organization_id)
    ]


@router.post(
    "",
    response_model=EcosystemPartyRead,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(require_permission(ECOSYSTEM_PARTIES_MANAGE))],
)
def create_ecosystem_party(
    payload: EcosystemPartyCreate,
    current_user: User = Depends(get_current_user),
    service: EcosystemPartyService = Depends(get_ecosystem_party_service),
) -> EcosystemPartyRead:
    ecosystem_party = service.create_ecosystem_party(
        CreateEcosystemPartyCommand(
            organization_id=current_user.organization_id,
            created_by_id=current_user.id,
            **payload.model_dump(),
        )
    )
    return EcosystemPartyRead.model_validate(ecosystem_party)
