
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_asterisk_publications(ORMBaseModel):
	id:str 
	device_state:Optional[asnum.yesno_values] = asnum.yesno_values.
	mailbox_state:Optional[asnum.yesno_values] = asnum.yesno_values.
	mailboxstate_publish:Optional[str] = None
	device_state_filter:Optional[str] = None
	mailbox_state_filter:Optional[str] = None
	devicestate_publish:Optional[str] = None
