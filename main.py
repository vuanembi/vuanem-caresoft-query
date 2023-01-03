from fastapi import FastAPI

from caresoft_query.controller import controller as caresoft_query_controller

app = FastAPI()

app.include_router(caresoft_query_controller)
