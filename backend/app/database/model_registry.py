"""Central import point that registers every ORM model onto ``Base.metadata``.

Alembic's ``env.py`` imports this module for its side effects so that
``--autogenerate`` can see every table. Every module that defines SQLAlchemy
models must be imported here, otherwise migrations silently ignore it.
"""

from backend.app.modules.controls.models import ControlModel
from backend.app.modules.organizations.models import OrganizationModel
from backend.app.modules.risks.models import RiskModel

__all__ = [
    "ControlModel",
    "OrganizationModel",
    "RiskModel",
]
