from typing import Optional,List
from pydantic import BaseModel, EmailStr
from .pjsip import PjsipBaseSchem
from .base import ORMBaseModel
#schame

class AgentBase(BaseModel):
    endpoint_id : str
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username : str
    name : str
    is_active:bool= True    
    email : Optional[EmailStr] = None
    endpoint: Optional[List[AgentBase]] = []
    group : Optional[List[int]] = [0] ## should create a group of default privilage 

class UserLogin(BaseModel):
    username : str
    password : str 

class UserCreate(UserBase):
    password : str 

class PasswordUpdate(UserLogin):
    new_password : str
    repeat_password : str


class UserUpdate(UserBase):
    id : int




class UserDBBase(UserBase):
    id : int
    is_superuser:bool=False    
    endpoint: Optional[List[AgentBase]] = []
    class Config:
        orm_mode =True

class Users(UserDBBase):
    pass

####   Group creation

class GroupsCreate(BaseModel):
    name : str
    permissions: Optional[List[str]] = []

class GroupsUpdate(BaseModel):
    id:int
    name : Optional[str] = None
    permissions: Optional[List[str]] = []

class DBGroup(GroupsCreate,ORMBaseModel):
    id : int