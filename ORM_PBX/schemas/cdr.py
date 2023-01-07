
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class cdr(ORMBaseModel):
	sequence:Optional[int] = None
	start:Optional[datetime] = None
	answer:Optional[datetime] = None
	end:Optional[datetime] = None
	duration:Optional[int] = None
	billsec:Optional[int] = None
	dstchannel:Optional[str] = None
	lastapp:Optional[str] = None
	lastdata:Optional[str] = None
	userfield:Optional[str] = None
	uniqueid:Optional[str] = None
	linkedid:Optional[str] = None
	peeraccount:Optional[str] = None
	accountcode:Optional[str] = None
	disposition:Optional[str] = None
	amaflags:Optional[str] = None
	src:Optional[str] = None
	dst:Optional[str] = None
	dcontext:Optional[str] = None
	clid:Optional[str] = None
	channel:Optional[str] = None
