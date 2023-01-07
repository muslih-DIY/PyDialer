from fastapi import APIRouter

from fastapi.templating import Jinja2Templates
from functools import wraps
import httpx,asyncio

router = APIRouter(
    prefix="/view",
    tags=["frontend"]
    )

host = 'http://localhost:8000/'
templates = Jinja2Templates('PyDialer/templates')


class async_request:

    async def get(*args,**kwargs):
        async with httpx.AsyncClient() as client:
            resp = await client.get(*args,**kwargs) 
            return resp


    async def post(*args,**kwargs):
        async with httpx.AsyncClient() as client:
            resp = await client.post(*args,**kwargs)
            
            return resp
