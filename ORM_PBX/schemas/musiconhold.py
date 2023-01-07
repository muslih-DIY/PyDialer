
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class musiconhold(ORMBaseModel):
	name:str 
	mode:Optional[asnum.moh_mode_values] = asnum.moh_mode_values.
	stamp:Optional[datetime] = None
	application:Optional[str] = None
	sort:Optional[str] = None
	format:Optional[str] = None
	digit:Optional[str] = None
	directory:Optional[str] = None
