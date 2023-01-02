from fastapi import APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="",
    tags=["frontend"]
    )

router.mount('/static',StaticFiles(directory="PyDialer/static"), name="static")

templates = Jinja2Templates('PyDialer/templates')
