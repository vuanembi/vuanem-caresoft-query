from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return Jinja2Templates(
        directory=f"{Path(__file__).resolve().parent}/templates"
    ).TemplateResponse("index.html", {"request": request})
