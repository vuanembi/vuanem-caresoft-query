from fastapi import FastAPI

from caresoft_query.controller import controller as caresoft_query_controller

app = FastAPI(
    title="vuanem-caresoft-query",
)

app.include_router(caresoft_query_controller)
