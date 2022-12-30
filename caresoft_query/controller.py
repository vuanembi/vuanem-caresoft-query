from fastapi import APIRouter

from caresoft_query.dto import CustomerResponse
from caresoft_query.service import get_user_by_phone

controller = APIRouter()


@controller.get(
    "/query/customer/{phone}",
    response_model=list[CustomerResponse],
)
def get_customer(phone: str):
    return get_user_by_phone(phone)
