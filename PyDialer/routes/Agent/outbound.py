from fastapi import Request,Form
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel

from PyDialer.depends.asterisk import asterisk
from .base_route import router

class Agent(BaseModel):
    endpoint: str
    Number: str | None = None


@router.post("/login/", response_class=JSONResponse)
async def login(request: Request,Agent:Agent):
    print(Agent.endpoint)
    res = asterisk.Originate(
        channel=f'PJSIP/{Agent.endpoint}',
        callerid='"Call-Controller"<11111>',
        context='agent-conf',
        extension='123'#f'{Agent.endpoint}CONF'
        )
    print(res)
    return JSONResponse('OK')

@router.post("/dial/" , response_class=JSONResponse)
async def dialpage(request: Request,Agent:Agent):
    print(Agent.endpoint,Agent.Number)
    asterisk.Originate(channel=f'Local/{Agent.Number}@outbound-local',
        callerid=f'"Customer"<{Agent.Number}>',
        context='outbound-conf',
        extension=f'{Agent.endpoint}CONF')

    return JSONResponse('OK')