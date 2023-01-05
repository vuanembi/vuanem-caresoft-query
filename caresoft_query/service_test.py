from caresoft_query.service import (
    get_customer_by_phone,
    get_orders_by_customer,
    get_order_by_id,
)


def test_get_customer_by_phone():
    phone = "0773314403"
    result = get_customer_by_phone(phone)
    assert len(result) > 0


def test_get_orders_by_customer():
    phone = 599656
    result = get_orders_by_customer(phone)
    assert len(result) > 0


def test_get_orders_by_id():
    id = 9020111
    result = get_order_by_id(id)
    assert len(result) > 0
