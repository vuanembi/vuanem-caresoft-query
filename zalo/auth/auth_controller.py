from fastapi import APIRouter, status
from fastapi.responses import JSONResponse, RedirectResponse

from .auth_service import create_authorization_url, authorization_callback

controller = APIRouter()


@controller.get("/authorize")
def redirect_authorize():
    return RedirectResponse(
        url=create_authorization_url(),
        status_code=status.HTTP_308_PERMANENT_REDIRECT,
    )


@controller.get("/callback")
def callback(code: str):
    return JSONResponse(authorization_callback(code))
