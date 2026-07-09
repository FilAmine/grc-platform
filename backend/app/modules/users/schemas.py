import re
from datetime import datetime
from uuid import UUID

from backend.app.common.schemas import ReadSchema
from pydantic import EmailStr, Field, field_validator

PASSWORD_MIN_LENGTH = 12


def validate_password_strength(password: str) -> str:
    if len(password) < PASSWORD_MIN_LENGTH:
        raise ValueError(f"password must be at least {PASSWORD_MIN_LENGTH} characters")
    if not re.search(r"[a-z]", password):
        raise ValueError("password must contain a lowercase letter")
    if not re.search(r"[A-Z]", password):
        raise ValueError("password must contain an uppercase letter")
    if not re.search(r"\d", password):
        raise ValueError("password must contain a digit")
    return password


class UserCreate(ReadSchema):
    email: EmailStr
    full_name: str = Field(min_length=2, max_length=255)
    password: str = Field(min_length=PASSWORD_MIN_LENGTH, max_length=128)
    is_superuser: bool = False

    @field_validator("password")
    @classmethod
    def _check_password(cls, value: str) -> str:
        return validate_password_strength(value)


class UserUpdate(ReadSchema):
    full_name: str | None = Field(default=None, min_length=2, max_length=255)
    is_active: bool | None = None


class UserRead(ReadSchema):
    id: UUID
    organization_id: UUID
    email: str
    full_name: str
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
