from typing import TypedDict


class SuiteQLResponse(TypedDict):
    hasMore: bool
    items: list[dict]
