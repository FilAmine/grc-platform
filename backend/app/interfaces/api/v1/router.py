from fastapi import APIRouter

from backend.app.modules.ai import api as ai
from backend.app.modules.assets import api as assets
from backend.app.modules.audits import api as audits
from backend.app.modules.auth import api as auth
from backend.app.modules.compliance import api as compliance
from backend.app.modules.controls import api as controls
from backend.app.modules.dashboard import api as dashboard
from backend.app.modules.documents import api as documents
from backend.app.modules.organizations import api as organizations
from backend.app.modules.permissions import api as permissions
from backend.app.modules.risks import api as risks
from backend.app.modules.roles import api as roles
from backend.app.modules.users import api as users

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
api_router.include_router(permissions.router, prefix="/permissions", tags=["permissions"])
api_router.include_router(organizations.router, prefix="/organizations", tags=["organizations"])
api_router.include_router(assets.router, prefix="/assets", tags=["assets"])
api_router.include_router(risks.router, prefix="/risks", tags=["risks"])
api_router.include_router(controls.router, prefix="/controls", tags=["controls"])
api_router.include_router(compliance.router, prefix="/compliance", tags=["compliance"])
api_router.include_router(audits.router, prefix="/audits", tags=["audits"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])

# Backward-compatible summary route for clients using the previous system namespace.
api_router.include_router(compliance.router, prefix="/system", tags=["system"])
