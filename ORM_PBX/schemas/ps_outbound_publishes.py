
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_outbound_publishes(ORMBaseModel):
	id:str 
	max_auth_attempts:Optional[int] = None
	expiration:Optional[int] = None
	multi_user:Optional[asnum.yesno_values] = asnum.yesno_values.
	server_uri:Optional[str] = None
	from_uri:Optional[str] = None
	to_uri:Optional[str] = None
	event:Optional[str] = None
	transport:Optional[str] = None
	@body:Optional[str] = None
	@context:Optional[str] = None
	@exten:Optional[str] = None
	outbound_auth:Optional[str] = None
	outbound_proxy:Optional[str] = None
