import time

from authlib.integrations.httpx_client import OAuth1Client
from fastapi import HTTPException

from settings import settings
from netsuite.interface import SuiteQLResponse


def create_client() -> OAuth1Client:
    return OAuth1Client(
        client_id=settings.NS_CONSUMER_KEY,
        client_secret=settings.NS_CONSUMER_SECRET,
        token=settings.NS_ACCESS_TOKEN,
        token_secret=settings.NS_TOKEN_SECRET,
        realm=settings.NS_ACCOUNT_ID,
        force_include_body=True,
        base_url=settings.NS_SUITETALK_URL,
    )


def query_suiteql(sql: str) -> list[dict]:
    limit = 1000

    def _request(client: OAuth1Client, offset: int = 0):
        response = client.request(
            method="POST",
            url="/query/v1/suiteql",
            headers={"Prefer": "transient", "Content-Type": "application/json"},
            params={"limit": limit, "offset": offset},
            json={"q": sql},
        )

        if response.status_code == 200:
            data: SuiteQLResponse = response.json()

            return (
                data["items"] + _request(client, offset + limit)
                if data["hasMore"]
                else data["items"]
            )
        elif response.status_code == 429:
            time.sleep(5)
            return _request(client, offset)
        else:
            print(response)
            raise HTTPException(status_code=500, detail="NetSuite Error")

    with create_client() as client:
        return _request(client)
