"""Security response headers.

There is no reverse proxy in front of the backend in this project's
docker-compose setup (the frontend's nginx only serves the SPA's static
files, on a different port) -- so headers that would normally be set at a
proxy layer have to be set here instead. See docs/security.md.
"""

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

_COMMON_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
    # Safe to always send: browsers only ever enforce HSTS over HTTPS, so
    # this is a no-op (not a footgun) when running plain HTTP locally.
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
}

# The default JSON-API policy is intentionally strict: no scripts, no
# styles, nothing but same-origin. Swagger UI and ReDoc (FastAPI's built-in
# /docs and /redoc HTML pages) need a materially looser policy -- they load
# JS/CSS from a CDN and both embed an inline <script> to bootstrap the UI,
# which 'unsafe-inline' is required for (no nonce/hash wiring exists for
# FastAPI's built-in docs routes).
_DEFAULT_CSP = "default-src 'self'; frame-ancestors 'none'"
_DOCS_CSP = (
    "default-src 'self'; "
    "script-src 'self' 'unsafe-inline' cdn.jsdelivr.net; "
    "style-src 'self' 'unsafe-inline' cdn.jsdelivr.net; "
    "img-src 'self' data: cdn.jsdelivr.net fastapi.tiangolo.com; "
    "connect-src 'self'; "
    "frame-ancestors 'none'"
)


def _is_docs_path(path: str, api_v1_prefix: str) -> bool:
    return path in (f"{api_v1_prefix}/docs", f"{api_v1_prefix}/redoc")


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, api_v1_prefix: str) -> None:
        super().__init__(app)
        self._api_v1_prefix = api_v1_prefix

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)
        for name, value in _COMMON_HEADERS.items():
            response.headers[name] = value
        response.headers["Content-Security-Policy"] = (
            _DOCS_CSP if _is_docs_path(request.url.path, self._api_v1_prefix) else _DEFAULT_CSP
        )
        return response
