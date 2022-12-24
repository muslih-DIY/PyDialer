from typing import List
from fastapi import APIRouter,Request,Form,Depends,Header,status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy import exc
from PyDialer.schemas.user import UserCreate,UserLogin,Users
from PyDialer.depends.db import get_db
from PyDialer.models import User
from PyDialer.exras.UserManager import (
    generate_token,get_token,validate_token,clear_user,validate_user,super_user_information)

import hashlib

#route
salt = 'Asteriskpystrix'
router = APIRouter(
    prefix="/account",
    tags=["accounts"]
    )


@router.post('/register', response_class=JSONResponse)
async def user_register(request: Request,user:UserCreate,depends=Depends(super_user_information)):
    try:
        user.password = hashlib.md5(':'.join([salt,user.password]).encode()).hexdigest()
        Userdb = User.create(**user.dict(),db=request.dbs)
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username is not avialiable'
            )
    return JSONResponse('OK')

@router.post('/login', response_class=JSONResponse)
async def login(request: Request,user:UserLogin,db=Depends(get_db)):
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
    request: Request,tkn=Header(),db=Depends(get_db)
    ):
    user = validate_token(tkn)
    if not user:
        return JSONResponse(status_code=403,content='Your Not Allowed, Wrong Auths')
    clear_user(user,tkn)
    return JSONResponse('Ok')

@router.post('/users', response_model=List[Users])
async def users_details(
    request: Request,db=Depends(get_db)
    ):
    users = User.get_all(db = db) 
    print(users[0])
    return [u.dict() for u in users]
