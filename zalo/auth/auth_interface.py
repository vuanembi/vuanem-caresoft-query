from typing import TypedDict


class AccessToken(TypedDict):
    access_token: str
    refresh_token: str
    expires_in: str
