import json
from pydantic import BaseModel
import os
from oauthlib.oauth1 import SIGNATURE_HMAC_SHA256
from requests_oauthlib import OAuth1Session


class Customer(BaseModel):
    name: str
    phone: str
    email: str
    date_of_birth: str
    loyalty_points: float
    loyalty_group: str


def parse_suiteql_response(response):
    response_json = json.loads(response.text)
    items = response_json["items"]
    _list = []
    for item in items:
        name = item.get('lastname'),
        phone = item.get('phone'), 
        email = item.get('email'), 
        date_of_birth = item.get('custentity_dob'),
        loyalty_point = item.get('custentity_tei_loyaltyremainingpointval'),
        loyalty_group = item.get('name')
        _dict = {
            "name": name,
            "phone": phone,
            "email": email,
            "date_of_birth": date_of_birth,
            "loyalty_point":loyalty_point,
            "loyalty_group": loyalty_group
        }
        _list.append(_dict)
    return _list


def netsuite_session() -> OAuth1Session:
    return OAuth1Session(
        client_key=os.getenv("CONSUMER_KEY"),
        client_secret=os.getenv("CONSUMER_SECRET"),
        resource_owner_key=os.getenv("ACCESS_TOKEN"),
        resource_owner_secret=os.getenv("TOKEN_SECRET"),
        realm=os.getenv("ACCOUNT_ID"),
        signature_method=SIGNATURE_HMAC_SHA256,
    )


def run_suiteql_query(session: OAuth1Session, sql: str):
    account_id = os.getenv("ACCOUNT_ID")
    headers = {"Prefer": "transient", "Content-Type": "application/json"}
    with session.request(
        method="POST",
        url=f"https://{account_id}.suitetalk.api.netsuite.com/services/rest/query/v1/suiteql",
        params={"limit": 1000, "offset": 0},
        json={"q": sql},
        headers=headers,
    ) as r:
        return parse_suiteql_response(r)


def get_user_by_phone(phone: str):
    sql = f"""
        SELECT 
            Customer.lastName, 
            Customer.email, 
            Customer.phone, 
            Customer.custentity_dob, 
            Customer.custentity_tei_loyaltyremainingpointval,
            CUSTOMRECORD_TBT_LOYALTY_CUST_GRP.name  
        FROM Customer 
            LEFT JOIN CUSTOMRECORD_TBT_LOYALTY_CUST_GRP 
            ON Customer.custentity_tbt_loyalty_grp = CUSTOMRECORD_TBT_LOYALTY_CUST_GRP.id
        WHERE Customer.phone = '{phone}'
    """
    return run_suiteql_query(netsuite_session(), sql)
