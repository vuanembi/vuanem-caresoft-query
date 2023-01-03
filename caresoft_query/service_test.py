from caresoft_query.service import get_customer_by_phone


def test_get_customer_by_phone():
    phone = "0773314403"
    result = get_customer_by_phone(phone)
    assert len(result) > 0
