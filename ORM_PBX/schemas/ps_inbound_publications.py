
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_inbound_publications(ORMBaseModel):
	id:str 
	endpoint:Optional[str] = None
	event_asterisk-devicestate:Optional[str] = None
	event_asterisk-mwi:Optional[str] = None
