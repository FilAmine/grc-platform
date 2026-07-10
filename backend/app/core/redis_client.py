from backend.app.core.config import settings
from redis import Redis
from redis.backoff import NoBackoff
from redis.retry import Retry

# Short, explicit timeouts and zero retries: rate_limit.py's whole point is
# to fail open fast when Redis is unreachable. redis-py's defaults (no
# timeout at all, plus its own retry-on-timeout behavior) turn "fail open"
# into "fail open after several seconds of blocking on every single
# request" -- confirmed directly: an unreachable Redis with only the
# timeouts set (no retry override) took ~1s per call, roughly 2x the
# configured 0.5s, from one internal retry. With `retries=0` a failed call
# fails on the first attempt.
CONNECT_TIMEOUT_SECONDS = 0.2
SOCKET_TIMEOUT_SECONDS = 0.2


def get_redis() -> Redis:
    return Redis.from_url(
        settings.redis_url,
        decode_responses=True,
        socket_connect_timeout=CONNECT_TIMEOUT_SECONDS,
        socket_timeout=SOCKET_TIMEOUT_SECONDS,
        retry=Retry(NoBackoff(), retries=0),
        retry_on_timeout=False,
    )
