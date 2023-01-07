
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_subscription_persistence(ORMBaseModel):
	id:str 
	prune_on_boot:Optional[asnum.yesno_values] = asnum.yesno_values.
	src_port:Optional[int] = None
	local_port:Optional[int] = None
	cseq:Optional[int] = None
	expires:Optional[int] = None
	local_name:Optional[str] = None
	contact_uri:Optional[str] = None
	tag:Optional[str] = None
	packet:Optional[str] = None
	src_name:Optional[str] = None
	endpoint:Optional[str] = None
	transport_key:Optional[str] = None
