from fastapi import HTTPException
from furl import furl
import httpx

from .auth_interface import AccessToken
from .auth_repository import (
    AUTHORIZATION_URL,
    exchange_code_for_token,
    get_access_token,
    get_refresh_token,
    store_access_token,
    store_refresh_token,
    refresh_access_token,
)
from settings import settings


def create_authorization_url():
    return furl(
        AUTHORIZATION_URL,
        {
            "app_id": settings.ZALO_CLIENT_ID,
            "redirect_uri": f"{settings.APP_URL}/zalo/auth/callback",
        },
    ).url


def authorization_callback(code: str):
    token: AccessToken = exchange_code_for_token(code)

    store_access_token(token["access_token"], int(token["expires_in"]))
    store_refresh_token(token["refresh_token"])

    return token


def create_zalo_client():
    access_token = get_access_token()

    if not access_token:
        refresh_token = get_refresh_token()

        if not refresh_token:
            raise HTTPException(500, "refresh token expired")

        access_token = refresh_access_token(refresh_token)

    return httpx.Client(headers={"access_token": access_token})
