from fastapi import APIRouter,Request,Form
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel
from ..depends.asterisk import asterisk


router = APIRouter(
    prefix="/account",
    tags=["accounts"]
    )

router.post('/register', response_class=JSONResponse)
async def user_register(request: Request):
    return JSONResponse('OK')