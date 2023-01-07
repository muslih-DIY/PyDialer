
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class extensions(ORMBaseModel):
	id:int 
	priority:int 
	context:str 
	exten:str 
	app:str 
	appdata:str 
