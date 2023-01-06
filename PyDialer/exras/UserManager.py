from fastapi import Header,Request,Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
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


async def current_user(request: Request,tkn=Header()):
    user = validate_token(tkn)
    if user and user.is_active:
        db:Session = request.db
        if user.reload(db):
            setattr(request,'User',user)
            return user
    raise HTTPException(status_code=403,detail='Your Not Allowed, Wrong Auths or Inactive account')
    

class have_role:
    """
    all : super, admin , etc..
    """
    def __init__(self,roles:list=['all']) -> None:
        self.roles = roles

    def __call__(self,user:User = Depends(current_user)):
        if not user.is_active:
            raise HTTPException(status_code=403, detail="User is inactive")
        if 'all' not in self.roles or user.is_superuser and 'super' in self.roles or user.role not in self.roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")


        