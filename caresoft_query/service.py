from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from netsuite.service import query_suiteql
from caresoft_query.dto import CustomerResponse, OrderBase

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


def get_orders_by_customer(customer_id: int) -> list:
    sql = ENVIRONMENT.get_template("get-orders-by-customer.sql.j2").render(
        customer_id=customer_id
    )
    data = query_suiteql(sql)

    return [OrderBase(id=row.get("id"), tranid=row.get("tranid")) for row in data]
