
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_resource_list(ORMBaseModel):
	id:str 
	full_state:Optional[asnum.yesno_values] = asnum.yesno_values.
	notification_batch_interval:Optional[int] = None
	resource_display_name:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	list_item:Optional[str] = None
	event:Optional[str] = None
