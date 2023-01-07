
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_aors(ORMBaseModel):
	id:str 
	remove_unavailable:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	qualify_frequency:Optional[int] = None
	authenticate_qualify:Optional[asnum.yesno_values] = asnum.yesno_values.
	maximum_expiration:Optional[int] = None
	support_path:Optional[asnum.yesno_values] = asnum.yesno_values.
	qualify_timeout:Optional[float] = None
	default_expiration:Optional[int] = None
	max_contacts:Optional[int] = None
	minimum_expiration:Optional[int] = None
	remove_existing:Optional[asnum.yesno_values] = asnum.yesno_values.
	contact:Optional[str] = None
	mailboxes:Optional[str] = None
	outbound_proxy:Optional[str] = None
	voicemail_extension:Optional[str] = None
