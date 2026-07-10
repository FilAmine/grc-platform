import hashlib
import secrets
from datetime import UTC, datetime, timedelta
from typing import Any

from backend.app.core.config import settings
from jose import JWTError, jwt
from passlib.context import CryptContext

ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


class InvalidTokenError(Exception):
    pass


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def create_access_token(
    subject: str, organization_id: str, expires_delta: timedelta | None = None
) -> str:
    expires_at = datetime.now(UTC) + (
        expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    )
    payload = {"sub": subject, "org": organization_id, "typ": "access", "exp": expires_at}
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict[str, Any]:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    except JWTError as exc:
        raise InvalidTokenError(str(exc)) from exc
    if payload.get("typ") != "access":
        raise InvalidTokenError("not an access token")
    return payload


def generate_refresh_token() -> str:
    return secrets.token_urlsafe(48)


def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def refresh_token_expiry() -> datetime:
    return datetime.now(UTC) + timedelta(days=settings.refresh_token_expire_days)


SSO_STATE_EXPIRE_MINUTES = 5


def create_sso_state_token(organization_id: str) -> str:
    """Short-lived, signed CSRF/correlation token for the OIDC redirect round-trip.

    No server-side storage needed: the organization id travels inside the
    signed JWT itself, so the callback can recover it without a lookup table
    for what is otherwise a purely ephemeral value.
    """
    expires_at = datetime.now(UTC) + timedelta(minutes=SSO_STATE_EXPIRE_MINUTES)
    payload = {"org": organization_id, "typ": "sso_state", "exp": expires_at}
    return jwt.encode(payload, settings.secret_key, algorithm=ALGORITHM)


def decode_sso_state_token(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
    except JWTError as exc:
        raise InvalidTokenError(str(exc)) from exc
    if payload.get("typ") != "sso_state":
        raise InvalidTokenError("not an sso_state token")
    return payload["org"]
