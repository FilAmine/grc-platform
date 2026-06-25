from fastapi import APIRouter

from backend.app.interfaces.api.v1.routes import controls, organizations, risks, system

api_router = APIRouter()
api_router.include_router(system.router, prefix="/system", tags=["system"])
api_router.include_router(organizations.router, prefix="/organizations", tags=["organizations"])
api_router.include_router(risks.router, prefix="/risks", tags=["risks"])
api_router.include_router(controls.router, prefix="/controls", tags=["controls"])
