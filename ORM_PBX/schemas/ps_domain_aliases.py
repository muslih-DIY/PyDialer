
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_domain_aliases(ORMBaseModel):
	id:str 
	domain:Optional[str] = None
