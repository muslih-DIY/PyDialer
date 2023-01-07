
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_endpoint_id_ips(ORMBaseModel):
	id:str 
	srv_lookups:Optional[asnum.yesno_values] = asnum.yesno_values.
	endpoint:Optional[str] = None
	match:Optional[str] = None
	match_header:Optional[str] = None
