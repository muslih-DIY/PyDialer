from fastapi import FastAPI,Request,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from asterisk_originates import originate


app = FastAPI()

app.mount('/static',StaticFiles(directory="static"), name="static")
templates = Jinja2Templates('templates')


@app.get("/login/", response_class=HTMLResponse)
async def loginpage(request: Request):
    
    return templates.TemplateResponse(name="index.html",context={"request": request})

@app.get("/home/", response_class=HTMLResponse)
async def homenpage(request: Request,endpoint: str):
    
    return templates.TemplateResponse(name="agenthome.html",context={"request": request,"endpoint":endpoint})


@app.post("/log-post/", response_class=HTMLResponse)
async def login(request: Request,endpoint: str):
    originate(endpoint=f'PJSIP/{endpoint}',callerid='"Call-Controller"<11111>',context='agent-conf',extension=f'{endpoint}CONF')
    return templates.TemplateResponse(name="agenthome.html",context={"request": request,"endpoint":endpoint})
    return RedirectResponse(f'/home/?endpoint={endpoint}' ,status_code=303)
    

@app.post("/dial/" , response_class=HTMLResponse)
async def dialpage(request: Request,agent: str = Form(),Number:str = Form()):
    print(agent,Number)
    originate(
        endpoint=f'Local/{Number}@outbound-local',
        callerid=f'"Customer"<{Number}>',
        context='outbound-conf',
        extension=f'{agent}CONF')

    return RedirectResponse(f'/home/?endpoint={agent}' ,status_code=303)

