from backend.app.core.config import settings
from redis import Redis


def get_redis() -> Redis:
    return Redis.from_url(settings.redis_url, decode_responses=True)
