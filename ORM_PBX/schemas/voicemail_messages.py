
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class voicemail_messages(ORMBaseModel):
	msgnum:int 
	dir:str 
	origtime:Optional[int] = None
	duration:Optional[int] = None
	recording:Optional[str] = None
	flag:Optional[str] = None
	category:Optional[str] = None
	mailboxuser:Optional[str] = None
	mailboxcontext:Optional[str] = None
	msg_id:Optional[str] = None
	context:Optional[str] = None
	macrocontext:Optional[str] = None
	callerid:Optional[str] = None
