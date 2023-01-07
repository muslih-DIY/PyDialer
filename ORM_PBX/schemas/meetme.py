
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class meetme(ORMBaseModel):
	bookid:int 
	members:int 
	confno:str 
	starttime:Optional[datetime] = None
	endtime:Optional[datetime] = None
	maxusers:Optional[int] = None
	adminpin:Optional[str] = None
	opts:Optional[str] = None
	adminopts:Optional[str] = None
	recordingfilename:Optional[str] = None
	recordingformat:Optional[str] = None
	pin:Optional[str] = None
