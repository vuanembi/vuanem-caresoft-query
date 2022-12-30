import json
import os
from oauthlib.oauth1 import SIGNATURE_HMAC_SHA256
from requests_oauthlib import OAuth1Session


def netsuite_session() -> OAuth1Session:
    return OAuth1Session(
        client_key=os.getenv("CONSUMER_KEY"),
        client_secret=os.getenv("CONSUMER_SECRET"),
        resource_owner_key=os.getenv("ACCESS_TOKEN"),
        resource_owner_secret=os.getenv("TOKEN_SECRET"),
        realm=os.getenv("ACCOUNT_ID"),
        signature_method=SIGNATURE_HMAC_SHA256,
    )


def run_suiteql_query(session: OAuth1Session, sql: str) -> list[dict]:
    account_id = os.getenv("ACCOUNT_ID")
    headers = {"Prefer": "transient", "Content-Type": "application/json"}
    with session.request(
        method="POST",
        url=f"https://{account_id}.suitetalk.api.netsuite.com/services/rest/query/v1/suiteql",
        params={"limit": 1000, "offset": 0},
        json={"q": sql},
        headers=headers,
    ) as r:
        response_json = json.loads(r.text)
        items = response_json["items"]
        return items
