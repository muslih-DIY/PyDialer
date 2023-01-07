
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class queue_members(ORMBaseModel):
	uniqueid:int 
	interface:str 
	queue_name:str 
	ringinuse:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	penalty:Optional[int] = None
	paused:Optional[int] = None
	wrapuptime:Optional[int] = None
	membername:Optional[str] = None
	state_interface:Optional[str] = None
