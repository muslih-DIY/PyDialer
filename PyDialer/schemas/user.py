from typing import Optional
from pydantic import BaseModel, EmailStr
from .pjsip import PjsipBaseSchem
#schame

class UserBase(BaseModel):
    username : str
    name : str
    email : Optional[EmailStr] = None

class UserLogin(BaseModel):
    username : str
    password : str 

class UserCreate(UserBase):
    password : str 

class PasswordUpdate(UserBase):
    password : str 
    new_password : str
    repeat_password : str


class UserUpdate(UserBase):
    pass

class UserDBBase(UserBase):
    id : int
    is_superuser:bool=False
    is_active:bool= True
    endpoint:Optional[list[str]]= None
    class Config:
        orm_mode =True

class Users(UserDBBase):
    pass