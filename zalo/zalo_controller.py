from fastapi import APIRouter

from .auth import auth_controller

controller = APIRouter()

controller.include_router(
    auth_controller.controller,
    prefix="/auth",
    tags=["Zalo / Auth"],
)
