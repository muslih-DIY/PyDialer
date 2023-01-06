from fastapi.responses import HTMLResponse
from fastapi import Request
from PyDialer.frontend.base_route import router,templates

APP = 'home'

@router.get(f"/{APP}", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(f"/{APP}/home.html", {"request": request})

@router.get(f"/{APP}/login", response_class=HTMLResponse)
async def Login(request: Request):
    return templates.TemplateResponse(f"/{APP}/login.html", {"request": request})