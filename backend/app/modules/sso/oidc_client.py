"""OIDC client abstraction.

Every provider-specific detail (discovery, token exchange, id_token
verification) lives here and nowhere else -- mirrors
``backend/app/modules/ai/providers.py``'s ``AIProvider`` Protocol. The rest
of the sso/auth modules only ever talk to the ``OidcClient`` Protocol, so
tests substitute a fake implementation via dependency override instead of
mocking HTTP calls (this codebase has no HTTP-mocking library installed, and
its other external-provider abstractions -- OpenAI/Azure OpenAI/Ollama --
follow the same "swap the whole client" testing approach rather than
mocking httpx directly).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from urllib.parse import urlencode

import httpx
from jose import JWTError, jwt


class OidcError(Exception):
    pass


@dataclass(frozen=True)
class OidcClaims:
    email: str
    name: str | None


class OidcClient(Protocol):
    def build_authorization_url(self, issuer: str, client_id: str, redirect_uri: str, state: str) -> str:
        raise NotImplementedError

    def exchange_code(
        self, issuer: str, client_id: str, client_secret: str, redirect_uri: str, code: str
    ) -> OidcClaims:
        raise NotImplementedError


class HttpxOidcClient:
    """Standard authorization-code-flow OIDC client. Discovery document,
    token endpoint, and JWKS-based id_token verification -- no assumptions
    beyond what every compliant IdP (Azure AD, Okta, Google Workspace, ...)
    exposes at ``{issuer}/.well-known/openid-configuration``."""

    TIMEOUT = 15.0

    def _request(self, method: str, url: str, **kwargs) -> httpx.Response:
        # httpx raises its own RequestError hierarchy (ConnectError,
        # TimeoutException, ...) for transport-level failures -- an
        # unreachable/misconfigured issuer URL is a normal, expected
        # misconfiguration for this feature (org admins hand-enter it), not
        # an unhandled-exception-worthy event, so it's mapped to OidcError
        # like every other failure mode here.
        try:
            return httpx.request(method, url, timeout=self.TIMEOUT, **kwargs)
        except httpx.RequestError as exc:
            raise OidcError(f"request to {url} failed: {exc}") from exc

    def _discovery(self, issuer: str) -> dict:
        response = self._request("GET", f"{issuer.rstrip('/')}/.well-known/openid-configuration")
        if response.status_code != 200:
            raise OidcError(f"OIDC discovery failed for issuer {issuer}: {response.status_code}")
        return response.json()

    def build_authorization_url(self, issuer: str, client_id: str, redirect_uri: str, state: str) -> str:
        discovery = self._discovery(issuer)
        params = {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": "openid email profile",
            "state": state,
        }
        return f"{discovery['authorization_endpoint']}?{urlencode(params)}"

    def exchange_code(
        self, issuer: str, client_id: str, client_secret: str, redirect_uri: str, code: str
    ) -> OidcClaims:
        discovery = self._discovery(issuer)
        token_response = self._request(
            "POST",
            discovery["token_endpoint"],
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": redirect_uri,
                "client_id": client_id,
                "client_secret": client_secret,
            },
        )
        if token_response.status_code != 200:
            raise OidcError(f"OIDC token exchange failed: {token_response.status_code} {token_response.text}")
        id_token = token_response.json().get("id_token")
        if not id_token:
            raise OidcError("OIDC token response did not include an id_token")

        claims = self._verify_id_token(id_token, discovery["jwks_uri"], client_id, issuer)
        email = claims.get("email")
        if not email:
            raise OidcError("id_token did not include an email claim")
        return OidcClaims(email=email, name=claims.get("name"))

    def _verify_id_token(self, id_token: str, jwks_uri: str, client_id: str, issuer: str) -> dict:
        try:
            header = jwt.get_unverified_header(id_token)
        except JWTError as exc:
            raise OidcError(f"invalid id_token header: {exc}") from exc

        jwks_response = self._request("GET", jwks_uri)
        if jwks_response.status_code != 200:
            raise OidcError(f"failed to fetch JWKS from {jwks_uri}: {jwks_response.status_code}")
        keys = jwks_response.json().get("keys", [])
        matching_key = next((key for key in keys if key.get("kid") == header.get("kid")), None)
        if matching_key is None:
            raise OidcError("no JWKS key matches id_token's kid")

        try:
            return jwt.decode(
                id_token,
                matching_key,
                algorithms=[header.get("alg", "RS256")],
                audience=client_id,
                issuer=issuer,
            )
        except JWTError as exc:
            raise OidcError(f"id_token verification failed: {exc}") from exc
