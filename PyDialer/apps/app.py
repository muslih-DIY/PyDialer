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
async def login(request: Request):
    
    return templates.TemplateResponse(name="index.html",context={"request": request})

@app.get("/home/", response_class=HTMLResponse)
async def home(request: Request,endpoint: str):
    originate(endpoint=endpoint,callerid='"Call-Controller"<11111>',context='test-conf',extension=f'{endpoint}CONF')
    return templates.TemplateResponse(name="agenthome.html",context={"request": request,"endpoint":endpoint})

@app.post("/dial/" , response_class=HTMLResponse)
async def home(request: Request,agent: str = Form(),Number:str = Form()):
    print(agent,Number)
    originate(endpoint=Number,callerid=f'"OnlineMagic"<{11111}>',context='test-conf',extension=f'{agent}CONF')
    return RedirectResponse(f'/home/?endpoint={agent}')

