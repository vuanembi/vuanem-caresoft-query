from fastapi import APIRouter, status

from caresoft_query import dto, service

controller = APIRouter(tags=["Customer"])

responses = {
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "NetSuite Error"},
}


@controller.get(
    "/query/customer/",
    response_model=list[dto.CustomerResponse],
    responses={**responses},  # type: ignore
)
def get_customer_by_phone(phone: str):
    return service.get_customer_by_phone(phone)
