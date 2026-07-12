from collections.abc import Generator
from uuid import UUID

import pytest
from backend.app.database import (
    Base,
    model_registry,  # noqa: F401  (registers all ORM models)
)
from backend.app.interfaces.api import dependencies as deps
from backend.app.main import app
from backend.app.modules.permissions.models import PermissionModel
from backend.app.modules.roles.models import RoleModel
from backend.app.modules.users.models import UserModel
from backend.app.security.permissions import ALL_PERMISSIONS, SYSTEM_ROLES
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool


@pytest.fixture()
def db_session() -> Generator[Session, None, None]:
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    TestSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, expire_on_commit=False)

    permission_objs = [PermissionModel(code=p.code, description=p.description) for p in ALL_PERMISSIONS]
    by_code = {p.code: p for p in permission_objs}
    seed_session = TestSessionLocal()
    seed_session.add_all(permission_objs)
    seed_session.flush()
    for role_name, codes in SYSTEM_ROLES.items():
        granted = list(by_code.values()) if codes is None else [by_code[c] for c in codes]
        seed_session.add(
            RoleModel(
                organization_id=None,
                name=role_name,
                description=f"System role: {role_name}",
                is_system=True,
                permissions=granted,
            )
        )
    seed_session.commit()
    seed_session.close()

    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()
        engine.dispose()


@pytest.fixture()
def client(db_session: Session) -> Generator[TestClient, None, None]:
    def override_get_session() -> Generator[Session, None, None]:
        yield db_session

    app.dependency_overrides[deps.get_session] = override_get_session
    try:
        yield TestClient(app)
    finally:
        app.dependency_overrides.pop(deps.get_session, None)


def register_organization(client: TestClient, *, slug: str = "acme", email: str = "admin@acme.example.com") -> dict:
    response = client.post(
        "/api/v1/auth/register-organization",
        json={
            "organization_name": slug.capitalize(),
            "organization_slug": slug,
            "admin_email": email,
            "admin_full_name": "Admin User",
            "admin_password": "SuperSecret123",
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


def auth_headers(access_token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {access_token}"}


def promote_to_superuser(db_session: Session, user_id: UUID | str) -> None:
    """There is no API path, seed script, or existing test that produces an
    `is_superuser=True` user -- every superuser-gated path today (see
    `test_non_superuser_cannot_create_organization_directly`) is only tested
    on its negative branch. This flips the flag directly on the row, via the
    same `db_session` fixture the `client` fixture is already wired to, so
    tests for `Tenant`/`PATCH /organizations/{id}/tenant` can exercise the
    positive path too."""
    if isinstance(user_id, str):
        user_id = UUID(user_id)
    user = db_session.get(UserModel, user_id)
    assert user is not None
    user.is_superuser = True
    db_session.commit()
