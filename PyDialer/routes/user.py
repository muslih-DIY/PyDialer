from typing import List
from fastapi import APIRouter,Request,Depends,Header,status
from sqlalchemy.orm.session import Session
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy import exc
from PyDialer.schemas.user import UserLogin
from PyDialer.models import User
from PyDialer.exras.UserManager import (
    get_token,validate_token,clear_user,validate_user)

import hashlib

#route
salt = 'Asteriskpystrix'
router = APIRouter(
    prefix="/account",
    tags=["accounts"]
    )



@router.post('/login', response_class=JSONResponse)
async def login(request: Request,user:UserLogin):
    db:Session = request.db
    user.password = hashlib.md5(':'.join([salt,user.password]).encode()).hexdigest()
    Userdb =  User.get_filter_by(db=db,username=user.username).first()
    if not Userdb:
        return JSONResponse(status_code=403,content='Your Not Allowed, Wrong Auths')
    if user.password == Userdb.password :
        tkn = validate_user(Userdb) or get_token(Userdb)
        return JSONResponse(tkn)
    return JSONResponse(status_code=403,content='Your Not Allowed, Wrong Auths')

@router.post('/logout', response_class=JSONResponse)
async def logout(
    request: Request,tkn=Header()
    ):
    db:Session = request.db
    user = validate_token(tkn)
    if not user:
        return JSONResponse(status_code=403,content='Your Not Allowed, Wrong Auths')
    clear_user(user,tkn)
    return JSONResponse('Ok')