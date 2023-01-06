from fastapi import APIRouter

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

router = APIRouter(
    prefix="/template",
    tags=["frontend-template"]
    )


templates = Jinja2Templates('PyDialer/templates/pages')

@router.get("/pages/{page}", response_class=HTMLResponse)
async def index(request: Request,page:str):
    "show every pages in the template"
    return templates.TemplateResponse(f"{page}", {"request": request})