
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class queues(ORMBaseModel):
	name:str 
	timeout:Optional[int] = None
	ringinuse:Optional[asnum.yesno_values] = asnum.yesno_values.
	announce_position_limit:Optional[int] = None
	setinterfacevar:Optional[asnum.yesno_values] = asnum.yesno_values.
	periodic_announce_frequency:Optional[int] = None
	relative_periodic_announce:Optional[asnum.yesno_values] = asnum.yesno_values.
	random_periodic_announce:Optional[asnum.yesno_values] = asnum.yesno_values.
	retry:Optional[int] = None
	wrapuptime:Optional[int] = None
	penaltymemberslimit:Optional[int] = None
	autofill:Optional[asnum.yesno_values] = asnum.yesno_values.
	setqueuevar:Optional[asnum.yesno_values] = asnum.yesno_values.
	autopause:Optional[asnum.queue_autopause_values] = asnum.queue_autopause_values.
	autopausedelay:Optional[int] = None
	autopausebusy:Optional[asnum.yesno_values] = asnum.yesno_values.
	autopauseunavail:Optional[asnum.yesno_values] = asnum.yesno_values.
	maxlen:Optional[int] = None
	servicelevel:Optional[int] = None
	strategy:Optional[asnum.queue_strategy_values] = asnum.queue_strategy_values.
	setqueueentryvar:Optional[asnum.yesno_values] = asnum.yesno_values.
	announce_frequency:Optional[int] = None
	reportholdtime:Optional[asnum.yesno_values] = asnum.yesno_values.
	memberdelay:Optional[int] = None
	weight:Optional[int] = None
	timeoutrestart:Optional[asnum.yesno_values] = asnum.yesno_values.
	announce_to_first_user:Optional[asnum.yesno_values] = asnum.yesno_values.
	min_announce_frequency:Optional[int] = None
	announce_round_seconds:Optional[int] = None
	timeoutpriority:Optional[str] = None
	musiconhold:Optional[str] = None
	announce:Optional[str] = None
	context:Optional[str] = None
	monitor_format:Optional[str] = None
	membermacro:Optional[str] = None
	membergosub:Optional[str] = None
	queue_youarenext:Optional[str] = None
	queue_thereare:Optional[str] = None
	queue_callswaiting:Optional[str] = None
	queue_quantity1:Optional[str] = None
	queue_quantity2:Optional[str] = None
	queue_holdtime:Optional[str] = None
	queue_minutes:Optional[str] = None
	queue_minute:Optional[str] = None
	queue_seconds:Optional[str] = None
	queue_thankyou:Optional[str] = None
	queue_callerannounce:Optional[str] = None
	queue_reporthold:Optional[str] = None
	announce_holdtime:Optional[str] = None
	announce_position:Optional[str] = None
	periodic_announce:Optional[str] = None
	monitor_type:Optional[str] = None
	joinempty:Optional[str] = None
	leavewhenempty:Optional[str] = None
	defaultrule:Optional[str] = None
