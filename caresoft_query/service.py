from operator import itemgetter
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from netsuite.service import query_suiteql
from caresoft_query.dto import CustomerResponse, OrderBase, Order, Item
from itertools import groupby

ENVIRONMENT = Environment(loader=FileSystemLoader(f"{Path(__file__).parent}/templates"))


def get_customer_by_phone(phone: str) -> list:
    sql = ENVIRONMENT.get_template("get-customer-by-phone.sql.j2").render(phone=phone)

    data = query_suiteql(sql)

    return [
        CustomerResponse(
            date_of_birth=row.get("custentity_dob"),
            email=row.get("email"),
            id=row.get("id"),
            loyalty_group=row.get("loyalty_group_name"),
            loyalty_points=row.get("loyalty_points"),
            name=row.get("lastname"),
            phone=row.get("phone"),
        )
        for row in data
    ]


def get_orders_by_customer(customer_id: int) -> list[OrderBase]:
    sql = ENVIRONMENT.get_template("get-orders-by-customer.sql.j2").render(
        customer_id=customer_id
    )
    data = query_suiteql(sql)

    return [
        OrderBase(
            id=row.get("id"),
            tranid=row.get("tranid"),
        )
        for row in data
    ]


def get_order_by_id(id: int) -> list[Order]:
    sql = ENVIRONMENT.get_template("get-order-by-id.sql.j2").render(id=id)

    data = query_suiteql(sql)

    group_key = itemgetter("id", "tranid", "trandate")

    sorted_data = sorted(data, key=group_key)  # type: ignore

    return [
        Order(
            id=group[0],
            tranid=group[1],
            trandate=group[2],
            items=[
                Item(
                    sku=value.get("itemid"),
                    quantity=value.get("quantity"),
                    amount=value.get("netamount"),
                )
                for value in values
            ],
        )
        for group, values in groupby(sorted_data, key=group_key)  # type: ignore
    ]
