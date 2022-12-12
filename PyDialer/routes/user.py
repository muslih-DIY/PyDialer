from fastapi import APIRouter,Request,Form,Depends
from fastapi.responses import HTMLResponse,JSONResponse
from pydantic import BaseModel
from ..schemas.user import UserCreate,UserLogin
from ..depends.db import get_db,Session
from .. import models
import hashlib
#route
salt = 'Asteriskpystrix'
router = APIRouter(
    prefix="/account",
    tags=["accounts"]
    )

@router.post('/register', response_class=JSONResponse)
async def user_register(request: Request,User:UserCreate,db=Depends(get_db)):
    User.password = hashlib.md5(':'.join([salt,User.password]).encode()).hexdigest()
    Userdb = models.User.create(**User.dict(),db=db)
    return JSONResponse('OK')

@router.post('/login', response_class=JSONResponse)
async def login(request: Request,User:UserLogin,db=Depends(get_db)):
    User.password = hashlib.md5(':'.join([salt,User.password]).encode()).hexdigest()
    Userdb =  models.User.get_filter_by(db=db,username=User.username).first()
    if User.password == Userdb.password :
        return JSONResponse('OK')
    return JSONResponse(status_code=403,content='Your Not Allowed, Wrong Auths')