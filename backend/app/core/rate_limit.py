"""Redis-backed fixed-window rate limiting.

A simple INCR + EXPIRE counter per (scope, client IP), not a sliding-window
or token-bucket algorithm -- deliberately the simplest thing that works,
matching this project's general preference for hand-rolled logic over new
dependencies where the built-in primitives (here, redis-py's INCR/EXPIRE)
already cover it.

Fails open: if Redis is unreachable, the request is allowed through and a
warning is logged, rather than making Redis a hard availability dependency
for login/auth. This also means the existing test suite (which never runs
against a real Redis) is unaffected by rate limiting being wired in --
requests just always pass through in that environment.

A small circuit breaker sits in front of the actual Redis call: after one
failure, further calls skip Redis entirely for a cooldown window instead of
each separately paying the connect-timeout cost. Confirmed this matters, not
just theoretical -- without it, the pytest suite (which calls
register_organization()/login helpers dozens of times, now hitting
rate-limited routes) went from ~5s to ~76s against an unreachable local
Redis, at roughly one full timeout per call. With the breaker it pays that
cost once per cooldown window, not once per request; this is also a more
sensible production behavior (don't hammer a known-down Redis under load).

`request.client.host` is used as the rate-limit key. There is no reverse
proxy in front of the backend in this project's docker-compose setup today,
so the client's real IP is what Starlette sees directly; if a proxy is added
later, this needs ProxyHeadersMiddleware (or equivalent trusted-hosts
handling) so `request.client.host` doesn't become the proxy's own IP for
every request, which would collapse everyone into one shared rate-limit
bucket. See docs/security.md's rate limiting section.
"""

import threading
import time

import structlog
from backend.app.interfaces.api.dependencies import get_redis
from fastapi import Depends, HTTPException, Request, status
from redis import Redis
from redis.exceptions import RedisError

logger = structlog.get_logger(__name__)

CIRCUIT_COOLDOWN_SECONDS = 5.0

_circuit_open_until = 0.0
_circuit_lock = threading.Lock()


def _circuit_is_open() -> bool:
    return time.monotonic() < _circuit_open_until


def _trip_circuit() -> None:
    global _circuit_open_until
    with _circuit_lock:
        _circuit_open_until = time.monotonic() + CIRCUIT_COOLDOWN_SECONDS


def rate_limit(scope: str, limit: int, window_seconds: int):
    def _dependency(request: Request, redis: Redis = Depends(get_redis)) -> None:
        if _circuit_is_open():
            return

        client_host = request.client.host if request.client else "unknown"
        key = f"rl:{scope}:{client_host}"
        try:
            current = redis.incr(key)
            if current == 1:
                redis.expire(key, window_seconds)
        except RedisError:
            logger.warning("rate_limit_redis_unavailable", scope=scope)
            _trip_circuit()
            return
        if current > limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="too many requests, please try again later",
                headers={"Retry-After": str(window_seconds)},
            )

    return _dependency
