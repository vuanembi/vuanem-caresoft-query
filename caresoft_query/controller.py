from fastapi import APIRouter

from caresoft_query.dto import CustomerResponse, OrderByCustomer
from caresoft_query.service import get_customer_by_phone
from caresoft_query.service import get_orders_by_customer

controller = APIRouter()


@controller.get("/query/customer/", response_model=list[CustomerResponse])
def get_customer(phone: str):
    return get_customer_by_phone(phone)

@controller.get("/query/order/", response_model=list[OrderByCustomer])
def get_orders(customer_id: str):
    return get_orders_by_customer(customer_id)