from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from PyDialer import outbound,user,endpoints
from PyDialer.depends.db import Model,session

#Model.BaseORM.metadata.create_all(bind=session.engin)

app = FastAPI()
app.include_router(outbound.router)

app.mount('/static',StaticFiles(directory="PyDialer/static"), name="static")
templates = Jinja2Templates('PyDialer/templates')


@app.get("/login/", response_class=HTMLResponse)
async def loginpage(request: Request):
    
    return templates.TemplateResponse(name="index.html",context={"request": request})

@app.get("/home/", response_class=HTMLResponse)
async def homenpage(request: Request,endpoint: str):
    
    return templates.TemplateResponse(name="agenthome.html",context={"request": request,"endpoint":endpoint})


    


