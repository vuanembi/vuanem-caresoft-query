import os

from redis import Redis

redis = Redis(
    host=os.getenv("REDIS_HOST", ""),
    port=6380,
    db=1,
    password=os.getenv("REDIS_PASSWORD"),
)
