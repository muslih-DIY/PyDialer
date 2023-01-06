from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from PyDialer.routes import (
    user,Agent,pjsip,AgentManager
    )
from PyDialer import frontend
from PyDialer.frontend import templates
#Model.BaseORM.metadata.create_all(bind=session.engin)

app = FastAPI()
app.include_router(Agent.router)
app.include_router(user.router)
app.include_router(pjsip.router)
app.include_router(AgentManager.router)
app.include_router(frontend.router)
app.include_router(templates.router)

app.mount('/static',StaticFiles(directory="PyDialer/static"), name="static")

# @app.get("/login/", response_class=HTMLResponse)
# async def loginpage(request: Request):
    
#     return templates.TemplateResponse(name="index.html",context={"request": request})

# @app.get("/home/", response_class=HTMLResponse)
# async def homenpage(request: Request,endpoint: str):
    
#     return templates.TemplateResponse(name="agenthome.html",context={"request": request,"endpoint":endpoint})


    


