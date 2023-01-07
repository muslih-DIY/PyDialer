
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class musiconhold_entry(ORMBaseModel):
	position:int 
	name:str 
	entry:str 
