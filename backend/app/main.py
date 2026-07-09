from backend.app.core.config import settings
from backend.app.core.logging import configure_logging
from backend.app.interfaces.api.v1.router import api_router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(
        title=settings.app_name,
        version="0.1.0",
        docs_url=f"{settings.api_v1_prefix}/docs",
        redoc_url=f"{settings.api_v1_prefix}/redoc",
        openapi_url=f"{settings.api_v1_prefix}/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", tags=["system"])
    def health() -> dict[str, str]:
        return {"status": "ok", "service": settings.app_name}

    app.include_router(api_router, prefix=settings.api_v1_prefix)
    return app


app = create_app()
