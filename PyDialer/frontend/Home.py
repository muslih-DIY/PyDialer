from fastapi.responses import HTMLResponse
from fastapi import Request,Form
from PyDialer.frontend.base_route import router,templates

APP = 'home'

@router.get(f"/{APP}", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(f"/{APP}/home.html", {"request": request})

@router.get(f"/{APP}/login", response_class=HTMLResponse)
async def Login(request: Request,username: str = Form(), password: str = Form()):
    
    return templates.TemplateResponse(f"/{APP}/login.html", {"request": request})