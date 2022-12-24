from typing import Optional
from pydantic import BaseModel, EmailStr

#schame

class UserBase(BaseModel):
    username : Optional[str]
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
    id : Optional[int] = None
    
    class Config:
        orm_mode =True

class User(UserDBBase):
    pass