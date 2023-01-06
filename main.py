from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from caresoft_query.controller import controller as caresoft_query_controller

app = FastAPI(
    title="vuanem-caresoft-query",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(caresoft_query_controller)
