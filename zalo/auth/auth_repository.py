from typing import Optional
from datetime import timedelta

import httpx

from settings import settings
from .auth_interface import AccessToken
from redis_module import redis

ACCESS_TOKEN_KEY = "zalo:access-token"
REFRESH_TOKEN_KEY = "zalo:refresh-token"

AUTHORIZATION_URL = "https://oauth.zaloapp.com/v4/oa/permission"
TOKEN_URL = "https://oauth.zaloapp.com/v4/oa/access_token"


def get_key(key: str):
    def _get() -> Optional[str]:
        bytes_ = redis.get(key)
        return bytes_.decode("utf-8") if bytes_ else None

    return _get


get_access_token, get_refresh_token = [
    get_key(key) for key in [ACCESS_TOKEN_KEY, REFRESH_TOKEN_KEY]
]


def store_access_token(data: str, expires_in: int):
    redis.set(ACCESS_TOKEN_KEY, data, ex=expires_in)


def store_refresh_token(data: str):
    redis.set(REFRESH_TOKEN_KEY, data, ex=timedelta(days=30 * 3))


def exchange_code_for_token(code: str) -> AccessToken:
    response = httpx.request(
        method="POST",
        url=TOKEN_URL,
        headers={
            "content-type": "application/x-www-form-urlencoded",
            "secret_key": settings.ZALO_CLIENT_SECRET,
        },
        data={
            "code": code,
            "app_id": settings.ZALO_CLIENT_ID,
            "grant_type": "authorization_code",
        },
    )

    response.raise_for_status()

    return response.json()


def refresh_access_token(refresh_token: str):
    response = httpx.request(
        method="POST",
        url=TOKEN_URL,
        headers={
            "content-type": "application/x-www-form-urlencoded",
            "secret_key": settings.ZALO_CLIENT_SECRET,
        },
        data={
            "refresh_token": refresh_token,
            "app_id": settings.ZALO_CLIENT_ID,
            "grant_type": "refresh_token",
        },
    )

    response.raise_for_status()

    return response.json()
