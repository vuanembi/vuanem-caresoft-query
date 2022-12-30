from netsuite.service import run_suiteql_query, netsuite_session
from jinja2 import Environment, FileSystemLoader

from caresoft_query.dto import CustomerResponse

ENVIRONMENT = Environment(loader=FileSystemLoader("./caresoft_query/templates"))


def get_user_by_phone(phone: str) -> list:
    sql = ENVIRONMENT.get_template("get_by_phone.sql.j2").render(phone=phone)
    with netsuite_session() as session:
        data = run_suiteql_query(session, sql)
    return [
        CustomerResponse(
            name=row.get("lastname"),
            email=row.get("email"),
            phone=row.get("phone"),
            date_of_birth=row.get("custentity_dob"),
            loyalty_points=row.get("custentity_tei_loyaltyremainingpointval"),
            loyalty_group=row.get("name"),
        )
        for row in data
    ]
