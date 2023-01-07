
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class ps_transports(ORMBaseModel):
	id:str 
	external_signaling_port:Optional[int] = None
	method:Optional[asnum.pjsip_transport_method_values] = asnum.pjsip_transport_method_values.
	protocol:Optional[asnum.pjsip_transport_protocol_values_v2] = asnum.pjsip_transport_protocol_values_v2.
	require_client_cert:Optional[asnum.yesno_values] = asnum.yesno_values.
	verify_client:Optional[asnum.yesno_values] = asnum.yesno_values.
	verify_server:Optional[asnum.yesno_values] = asnum.yesno_values.
	async_operations:Optional[int] = None
	cos:Optional[int] = None
	allow_reload:Optional[asnum.yesno_values] = asnum.yesno_values.
	symmetric_transport:Optional[asnum.yesno_values] = asnum.yesno_values.
	allow_wildcard_certs:Optional[asnum.yesno_values] = asnum.yesno_values.
	tos:Optional[str] = None
	local_net:Optional[str] = None
	bind:Optional[str] = None
	ca_list_file:Optional[str] = None
	cert_file:Optional[str] = None
	cipher:Optional[str] = None
	domain:Optional[str] = None
	external_media_address:Optional[str] = None
	external_signaling_address:Optional[str] = None
	password:Optional[str] = None
	priv_key_file:Optional[str] = None
