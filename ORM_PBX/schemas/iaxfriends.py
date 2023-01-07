
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class iaxfriends(ORMBaseModel):
	id:int 
	name:str 
	transfer:Optional[asnum.iax_transfer_values] = asnum.iax_transfer_values.
	jitterbuffer:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	forcejitterbuffer:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	port:Optional[int] = None
	sendani:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	regseconds:Optional[int] = None
	trunk:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	qualifysmoothing:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	type:Optional[asnum.type_values] = asnum.type_values.
	maxauthreq:Optional[int] = None
	requirecalltoken:Optional[asnum.iax_requirecalltoken_values] = asnum.iax_requirecalltoken_values.
	adsi:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	encryption:Optional[asnum.iax_encryption_values] = asnum.iax_encryption_values.
	accountcode:Optional[str] = None
	mohinterpret:Optional[str] = None
	mohsuggest:Optional[str] = None
	inkeys:Optional[str] = None
	outkeys:Optional[str] = None
	language:Optional[str] = None
	callerid:Optional[str] = None
	cid_number:Optional[str] = None
	fullname:Optional[str] = None
	auth:Optional[str] = None
	disallow:Optional[str] = None
	allow:Optional[str] = None
	codecpriority:Optional[str] = None
	qualify:Optional[str] = None
	qualifyfreqok:Optional[str] = None
	qualifyfreqnotok:Optional[str] = None
	timezone:Optional[str] = None
	amaflags:Optional[str] = None
	setvar:Optional[str] = None
	username:Optional[str] = None
	mailbox:Optional[str] = None
	secret:Optional[str] = None
	dbsecret:Optional[str] = None
	context:Optional[str] = None
	regcontext:Optional[str] = None
	host:Optional[str] = None
	ipaddr:Optional[str] = None
	defaultip:Optional[str] = None
	sourceaddress:Optional[str] = None
	mask:Optional[str] = None
	regexten:Optional[str] = None
