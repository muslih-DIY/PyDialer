from fastapi import Header,Request

from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from PyDialer.depends.db import get_db
from PyDialer.depends.secrets import generate_token
from PyDialer.models import User

token_user = {}
user_token = {}

def get_token(user:User):
    global tokens
    tkn = generate_token(user.username,user.id)
    token_user[tkn]=user
    user_token[user.id]=tkn
    return tkn

def clear_user(user,tkn):
    del token_user[tkn]
    del user_token[user.id]

def validate_token(tkn) -> User:
    global token_user
    account:User() = token_user.get(tkn,None)
    return account

def validate_user(user):
    global user_token
    tkn = user_token.get(user.id,'')
    return tkn


async def user_information(request: Request,tkn=Header()):
    user = validate_token(tkn)
    if user:
        db:Session = next(get_db()) 
        if user.reload(db):
            setattr(request,'User',user)
            setattr(request,'dbs',db)
            return user,db
    raise HTTPException(status_code=403,detail='Your Not Allowed, Wrong Auths')
    

async def super_user_information(request: Request,tkn=Header()):
    user = validate_token(tkn)
    db:Session = next(get_db())
    if user and user.reload(db) and user.is_superuser:
        setattr(request,'dbs',db)
        setattr(request,'User',user)
        return user,db
    raise HTTPException(status_code=403,detail='Your Not Allowed')
    
