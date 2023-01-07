from fastapi.responses import HTMLResponse
from fastapi import Request
from PyDialer.frontend.base_route import router,templates,host,async_request
from PyDialer.routes import admin
import requests
APP = 'admin'

@router.get(f"/{APP}", response_class=HTMLResponse)
async def adminhome(request: Request):
    return templates.TemplateResponse(f"/{APP}/home.html", {"request": request})

@router.get(f"/{APP}"+"/{model}", response_class=HTMLResponse)
async def model_read(request: Request,model:str):
    url = host+f'admin/{model}'
    print(url)
    models = await async_request.get(url)
    model_list = models.json()
    print(model_list)
    return templates.TemplateResponse(f"/{APP}/user.html", {"request": request,"users":model_list})

@router.get(f"/{APP}"+"/pjsip/{model}", response_class=HTMLResponse)
async def pj_model_read(request: Request,model:str):
    url = host+f'pjsip/{model}'
    print(url)
    response = await async_request.get(url)
    model_list=[]
    if response.status_code==200:
        model_list = response.json()

    return templates.TemplateResponse(f"/{APP}/user.html", {"request": request,"users":model_list})