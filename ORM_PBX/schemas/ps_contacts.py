
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_contacts(ORMBaseModel):
	id:str 
	prune_on_boot:Optional[asnum.yesno_values] = asnum.yesno_values.
	expiration_time:Optional[int] = None
	qualify_frequency:Optional[int] = None
	qualify_timeout:Optional[float] = None
	authenticate_qualify:Optional[asnum.yesno_values] = asnum.yesno_values.
	via_port:Optional[int] = None
	user_agent:Optional[str] = None
	call_id:Optional[str] = None
	reg_server:Optional[str] = None
	endpoint:Optional[str] = None
	uri:Optional[str] = None
	via_addr:Optional[str] = None
	outbound_proxy:Optional[str] = None
	path:Optional[str] = None
