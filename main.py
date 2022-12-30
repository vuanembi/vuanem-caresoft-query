from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from caresoft_query.controller import controller as caresoft_query_controller
from caresoft_query.service import get_user_by_phone

app = FastAPI()

app.include_router(caresoft_query_controller)

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return Jinja2Templates(
        directory=f"{Path(__file__).resolve().parent}/templates"
    ).TemplateResponse("index.html", {"request": request})

