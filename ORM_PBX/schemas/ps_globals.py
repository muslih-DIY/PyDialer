
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_globals(ORMBaseModel):
	id:str 
	allow_sending_180_after_183:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	max_forwards:Optional[int] = None
	unidentified_request_prune_interval:Optional[int] = None
	mwi_tps_queue_high:Optional[int] = None
	mwi_tps_queue_low:Optional[int] = None
	mwi_disable_initial_unsolicited:Optional[asnum.yesno_values] = asnum.yesno_values.
	ignore_uri_user_options:Optional[asnum.yesno_values] = asnum.yesno_values.
	use_callerid_contact:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	send_contact_status_on_update_registration:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	taskprocessor_overload_trigger:Optional[asnum.pjsip_taskprocessor_overload_trigger_values] = asnum.pjsip_taskprocessor_overload_trigger_values.
	norefersub:Optional[asnum.ast_bool_values] = asnum.ast_bool_values.
	max_initial_qualify_time:Optional[int] = None
	keep_alive_interval:Optional[int] = None
	contact_expiration_check_interval:Optional[int] = None
	disable_multi_domain:Optional[asnum.yesno_values] = asnum.yesno_values.
	unidentified_request_count:Optional[int] = None
	unidentified_request_period:Optional[int] = None
	user_agent:Optional[str] = None
	default_outbound_endpoint:Optional[str] = None
	debug:Optional[str] = None
	endpoint_identifier_order:Optional[str] = None
	default_voicemail_extension:Optional[str] = None
	default_from_user:Optional[str] = None
	default_realm:Optional[str] = None
	regcontext:Optional[str] = None
