
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_systems(ORMBaseModel):
	id:str 
	disable_rport:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	timer_t1:Optional[int] = None
	timer_b:Optional[int] = None
	compact_headers:Optional[asnum.yesno_values] = asnum.yesno_values.
	threadpool_initial_size:Optional[int] = None
	threadpool_auto_increment:Optional[int] = None
	threadpool_idle_timeout:Optional[int] = None
	threadpool_max_size:Optional[int] = None
	disable_tcp_switch:Optional[asnum.yesno_values] = asnum.yesno_values.
	follow_early_media_fork:Optional[asnum.yesno_values] = asnum.yesno_values.
	accept_multiple_sdp_answers:Optional[asnum.yesno_values] = asnum.yesno_values.
