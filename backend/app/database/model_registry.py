"""Central import point that registers every ORM model onto ``Base.metadata``.

Alembic's ``env.py`` imports this module for its side effects so that
``--autogenerate`` can see every table. Every module that defines SQLAlchemy
models must be imported here, otherwise migrations silently ignore it.
"""

from backend.app.modules.auth.models import RefreshTokenModel
from backend.app.modules.controls.models import ControlModel
from backend.app.modules.organizations.models import OrganizationModel
from backend.app.modules.permissions.models import PermissionModel
from backend.app.modules.risks.models import RiskModel
from backend.app.modules.roles.models import RoleModel, role_permissions
from backend.app.modules.users.models import UserModel, user_roles

__all__ = [
    "ControlModel",
    "OrganizationModel",
    "PermissionModel",
    "RefreshTokenModel",
    "RiskModel",
    "RoleModel",
    "UserModel",
    "role_permissions",
    "user_roles",
]
