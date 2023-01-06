from operator import itemgetter
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from collections import defaultdict

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
    data = sorted(data, key=itemgetter("tranid", "trandate"))
    result = defaultdict(list)
    i = 0
    tran_id = []
    for key, value in groupby(data, key=itemgetter("tranid", "trandate")):
        result[i].append(list(value))
        tran_id.append(key)
        i = i + 1
    kq = list[Order]
    kq = []
    for a in range(i):
        t = result[a]
        res = list[Item]
        res = [
            Item(
                sku=x.get("itemid"),
                quantity=x.get("quantity"),
                amount=x.get("netamount"),
            )
            for x in t[0]
        ]
        tr = tran_id[a]
        kq.append(Order(id=id, tranid=tr[0], trandate=tr[1], items=res))
    return kq
