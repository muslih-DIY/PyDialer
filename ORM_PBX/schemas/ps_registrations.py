
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_registrations(ORMBaseModel):
	id:str 
	max_random_initial_delay:Optional[int] = None
	auth_rejection_permanent:Optional[asnum.yesno_values] = asnum.yesno_values.
	expiration:Optional[int] = None
	max_retries:Optional[int] = None
	retry_interval:Optional[int] = None
	forbidden_retry_interval:Optional[int] = None
	support_path:Optional[asnum.yesno_values] = asnum.yesno_values.
	fatal_retry_interval:Optional[int] = None
	line:Optional[asnum.yesno_values] = asnum.yesno_values.
	support_outbound:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	server_uri:Optional[str] = None
	client_uri:Optional[str] = None
	contact_user:Optional[str] = None
	transport:Optional[str] = None
	endpoint:Optional[str] = None
	outbound_auth:Optional[str] = None
	outbound_proxy:Optional[str] = None
	contact_header_params:Optional[str] = None
