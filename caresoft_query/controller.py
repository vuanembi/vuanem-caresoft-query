from fastapi import APIRouter, status

from caresoft_query import dto, service

controller = APIRouter()

responses = {
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "NetSuite Error"},
}


@controller.get(
    "/query/customer/",
    response_model=list[dto.CustomerResponse],
    responses={**responses},  # type: ignore
    tags=["Customer"],
)
def get_customer(phone: str):
    return service.get_customer_by_phone(phone)


@controller.get(
    "/query/order/",
    response_model=list[dto.OrderBase],
    responses={**responses},  # type: ignore
    tags=["Sales Order"],
)
def get_orders(customer_id: int):
    return service.get_orders_by_customer(customer_id)


@controller.get(
    "/query/order/{id}",
    response_model=list[dto.Order],
    responses={**responses},  # type: ignore
    tags=["Sales Order"],
)
def get_order(id: int):
    return service.get_order_by_id(id)
