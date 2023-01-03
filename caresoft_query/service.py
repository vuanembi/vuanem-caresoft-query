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
            name=row.get("lastname"),
            email=row.get("email"),
            phone=row.get("phone"),
            customer_id=row.get("id"),
            date_of_birth=row.get("custentity_dob"),
            loyalty_points=row.get("custentity_tei_loyaltyremainingpointval"),
            loyalty_group=row.get("name"),
        )
        for row in data
    ]


def get_orders_by_customer(customer_id: int) -> list:
    sql = ENVIRONMENT.get_template("get-orders-by-customer.sql.j2").render(
        customer_id=customer_id
    )
    data = query_suiteql(sql)

    return [OrderBase(id=row.get("id"), tranid=row.get("tranid")) for row in data]
