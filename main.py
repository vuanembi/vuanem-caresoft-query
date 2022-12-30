from pathlib import Path
import json
from jinja2 import Template
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from caresoft_query.service import get_user_by_phone

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return Jinja2Templates(
        directory=f"{Path(__file__).resolve().parent}/templates"
    ).TemplateResponse("index.html", {"request": request})


@app.get("/query/customer/{phone}", response_class=HTMLResponse)
def get_customer(request: Request, phone:str):
    response = get_user_by_phone(phone) 
    return templates.TemplateResponse("info.html", {"request": request, "res": response})
