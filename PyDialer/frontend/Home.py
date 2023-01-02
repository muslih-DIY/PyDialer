from fastapi.responses import HTMLResponse
from fastapi import Request
from PyDialer.frontend.base_route import router,templates


@router.get("/home", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("Home.html", {"request": request})