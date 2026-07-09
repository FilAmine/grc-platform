from pydantic import EmailStr, Field, field_validator

from backend.app.common.schemas import ReadSchema
from backend.app.modules.users.schemas import validate_password_strength


class RegisterOrganizationRequest(ReadSchema):
    organization_name: str = Field(min_length=2, max_length=255)
    organization_slug: str = Field(min_length=2, max_length=100, pattern=r"^[a-z0-9-]+$")
    admin_email: EmailStr
    admin_full_name: str = Field(min_length=2, max_length=255)
    admin_password: str = Field(min_length=12, max_length=128)

    @field_validator("admin_password")
    @classmethod
    def _check_password(cls, value: str) -> str:
        return validate_password_strength(value)


class RefreshRequest(ReadSchema):
    refresh_token: str


class TokenResponse(ReadSchema):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
