
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_auths(ORMBaseModel):
	id:str 
	nonce_lifetime:Optional[int] = None
	auth_type:Optional[asnum.pjsip_auth_type_values_v2] = asnum.pjsip_auth_type_values_v2.
	password:Optional[str] = None
	realm:Optional[str] = None
	username:Optional[str] = None
	refresh_token:Optional[str] = None
	oauth_clientid:Optional[str] = None
	oauth_secret:Optional[str] = None
	md5_cred:Optional[str] = None
