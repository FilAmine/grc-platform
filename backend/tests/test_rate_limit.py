from collections.abc import Generator

import pytest
from backend.app.core import rate_limit as rate_limit_module
from backend.app.core.rate_limit import rate_limit
from fastapi import HTTPException
from redis.exceptions import ConnectionError as RedisConnectionError
from starlette.requests import Request


class FakeRedis:
    """Tracks per-key counters like real INCR/EXPIRE, or raises like a
    down Redis would -- the same swap-the-whole-client testing approach used
    for FakeOidcClient (see test_sso.py), not httpx/redis-level mocking."""

    def __init__(self, fail: bool = False) -> None:
        self.counters: dict[str, int] = {}
        self.incr_calls = 0
        self._fail = fail

    def incr(self, key: str) -> int:
        self.incr_calls += 1
        if self._fail:
            raise RedisConnectionError("simulated redis outage")
        self.counters[key] = self.counters.get(key, 0) + 1
        return self.counters[key]

    def expire(self, key: str, seconds: int) -> None:
        pass


def _make_request(client_host: str) -> Request:
    return Request(scope={"type": "http", "client": (client_host, 12345), "headers": []})


@pytest.fixture(autouse=True)
def _reset_circuit_breaker() -> Generator[None, None, None]:
    rate_limit_module._circuit_open_until = 0.0
    yield
    rate_limit_module._circuit_open_until = 0.0


def test_allows_up_to_limit_then_rejects() -> None:
    fake = FakeRedis()
    dependency = rate_limit("test-scope", limit=3, window_seconds=60)
    request = _make_request("1.1.1.1")

    for _ in range(3):
        dependency(request, redis=fake)  # type: ignore[arg-type]

    with pytest.raises(HTTPException) as exc_info:
        dependency(request, redis=fake)  # type: ignore[arg-type]
    assert exc_info.value.status_code == 429
    assert exc_info.value.headers["Retry-After"] == "60"


def test_fails_open_when_redis_unavailable() -> None:
    fake = FakeRedis(fail=True)
    dependency = rate_limit("test-scope", limit=1, window_seconds=60)
    request = _make_request("2.2.2.2")

    # Would be request #1 and #2 against a limit of 1 -- both must pass
    # through uninterrupted since Redis is "down".
    dependency(request, redis=fake)  # type: ignore[arg-type]
    dependency(request, redis=fake)  # type: ignore[arg-type]


def test_different_hosts_get_independent_counters() -> None:
    fake = FakeRedis()
    dependency = rate_limit("test-scope", limit=1, window_seconds=60)

    dependency(_make_request("3.3.3.1"), redis=fake)  # type: ignore[arg-type]
    with pytest.raises(HTTPException):
        dependency(_make_request("3.3.3.1"), redis=fake)  # type: ignore[arg-type]

    # A different host is a separate counter, not affected by the first host
    # having already hit its limit.
    dependency(_make_request("3.3.3.2"), redis=fake)  # type: ignore[arg-type]


def test_circuit_breaker_skips_redis_after_a_failure() -> None:
    fake = FakeRedis(fail=True)
    dependency = rate_limit("test-scope", limit=1, window_seconds=60)
    request = _make_request("4.4.4.4")

    dependency(request, redis=fake)  # type: ignore[arg-type]  # trips the circuit
    assert fake.incr_calls == 1

    # While the circuit is open, further calls must not even attempt to
    # reach Redis -- this is the whole point of the breaker (see
    # rate_limit.py's module docstring for why: without it, every call to a
    # down Redis separately pays the connect-timeout cost).
    dependency(request, redis=fake)  # type: ignore[arg-type]
    assert fake.incr_calls == 1
