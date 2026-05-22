from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

redis_client = Redis.from_url("redis://localhost:6379/0")
storage = RedisStorage(redis=redis_client)
