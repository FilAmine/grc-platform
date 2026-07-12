from backend.app.modules.ai import api as ai
from backend.app.modules.assets import api as assets
from backend.app.modules.audits import api as audits
from backend.app.modules.auth import api as auth
from backend.app.modules.compliance import api as compliance
from backend.app.modules.controls import api as controls
from backend.app.modules.dashboard import api as dashboard
from backend.app.modules.departments import api as departments
from backend.app.modules.documents import api as documents
from backend.app.modules.feared_events import api as feared_events
from backend.app.modules.incidents import api as incidents
from backend.app.modules.notifications import api as notifications
from backend.app.modules.organizations import api as organizations
from backend.app.modules.permissions import api as permissions
from backend.app.modules.risks import api as risks
from backend.app.modules.roles import api as roles
from backend.app.modules.sso import api as sso
from backend.app.modules.tasks import api as tasks
from backend.app.modules.tenants import api as tenants
from backend.app.modules.threats import api as threats
from backend.app.modules.users import api as users
from backend.app.modules.vulnerabilities import api as vulnerabilities
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])
api_router.include_router(permissions.router, prefix="/permissions", tags=["permissions"])
api_router.include_router(organizations.router, prefix="/organizations", tags=["organizations"])
api_router.include_router(tenants.router, prefix="/tenants", tags=["tenants"])
api_router.include_router(assets.router, prefix="/assets", tags=["assets"])
api_router.include_router(risks.router, prefix="/risks", tags=["risks"])
api_router.include_router(controls.router, prefix="/controls", tags=["controls"])
api_router.include_router(departments.router, prefix="/departments", tags=["departments"])
api_router.include_router(threats.router, prefix="/threats", tags=["threats"])
api_router.include_router(
    vulnerabilities.router, prefix="/vulnerabilities", tags=["vulnerabilities"]
)
api_router.include_router(feared_events.router, prefix="/feared-events", tags=["feared-events"])
api_router.include_router(compliance.router, prefix="/compliance", tags=["compliance"])
api_router.include_router(audits.router, prefix="/audits", tags=["audits"])
api_router.include_router(incidents.router, prefix="/incidents", tags=["incidents"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
api_router.include_router(documents.router, prefix="/documents", tags=["documents"])
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
api_router.include_router(notifications.router, prefix="/notifications", tags=["notifications"])
api_router.include_router(sso.router, prefix="/sso", tags=["sso"])

# Backward-compatible alias for clients using the previous system namespace.
# Deliberately just the one route, not the whole compliance router -- that
# router has since grown far beyond a summary endpoint (frameworks, assessments,
# evidence, ...), none of which the old /system namespace ever exposed.
legacy_system_router = APIRouter()
for route in compliance.router.routes:
    if getattr(route, "path", None) == "/summary":
        legacy_system_router.routes.append(route)
api_router.include_router(legacy_system_router, prefix="/system", tags=["system"])
