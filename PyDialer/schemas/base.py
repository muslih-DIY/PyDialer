from typing import Optional,List
from pydantic import BaseModel

class ORMBaseModel(BaseModel):
    class Config:
        orm_mode =True

class Integerid(BaseModel):
    id : int

class StringId(BaseModel):
    id : str