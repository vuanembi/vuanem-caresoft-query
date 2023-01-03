from fastapi import APIRouter

from caresoft_query import dto, service

controller = APIRouter()


@controller.get("/query/customer/", response_model=list[dto.CustomerResponse])
def get_customer(phone: str):
    return service.get_customer_by_phone(phone)


@controller.get("/query/order/", response_model=list[dto.OrderBase])
def get_orders(customer_id: int):
    return service.get_orders_by_customer(customer_id)
