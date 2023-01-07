
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class voicemail(ORMBaseModel):
	uniqueid:int 
	context:str 
	mailbox:str 
	password:str 
	stamp:Optional[datetime] = None
	attach:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	deletevoicemail:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	saycid:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	sendvoicemail:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	review:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	tempgreetwarn:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	operator:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	envelope:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	sayduration:Optional[int] = None
	forcename:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	forcegreetings:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	maxmsg:Optional[int] = None
	volgain:Optional[float] = None
	callback:Optional[str] = None
	dialout:Optional[str] = None
	exitcontext:Optional[str] = None
	imapport:Optional[str] = None
	imapflags:Optional[str] = None
	fullname:Optional[str] = None
	alias:Optional[str] = None
	email:Optional[str] = None
	pager:Optional[str] = None
	imapuser:Optional[str] = None
	attachfmt:Optional[str] = None
	serveremail:Optional[str] = None
	language:Optional[str] = None
	tz:Optional[str] = None
	imappassword:Optional[str] = None
	imapserver:Optional[str] = None
