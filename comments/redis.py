from redis.asyncio import Redis
from comments.config import settings


async def get_redis():
    redis_client = Redis(
        host=settings.REDIS_HOST, port=settings.REDIS_PORT, decode_responses=True
    )
    try:
        yield redis_client
    finally:
        await redis_client.close()
