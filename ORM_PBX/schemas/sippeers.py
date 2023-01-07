
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class sippeers(ORMBaseModel):
	id:int 
	name:str 
	supportpath:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	port:Optional[int] = None
	regseconds:Optional[int] = None
	lastms:Optional[int] = None
	type:Optional[asnum.type_values] = asnum.type_values.
	transport:Optional[asnum.sip_transport_values] = asnum.sip_transport_values.
	dtmfmode:Optional[asnum.sip_dtmfmode_values] = asnum.sip_dtmfmode_values.
	directmedia:Optional[asnum.sip_directmedia_values_v2] = asnum.sip_directmedia_values_v2.
	trustrpid:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	progressinband:Optional[asnum.sip_progressinband_values] = asnum.sip_progressinband_values.
	promiscredir:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	useclientcode:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	callcounter:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	busylevel:Optional[int] = None
	allowoverlap:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	allowsubscribe:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	videosupport:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	maxcallbitrate:Optional[int] = None
	rfc2833compensate:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	session-timers:Optional[asnum.sip_session_timers_values] = asnum.sip_session_timers_values.
	session-expires:Optional[int] = None
	session-minse:Optional[int] = None
	session-refresher:Optional[asnum.sip_session_refresher_values] = asnum.sip_session_refresher_values.
	rtptimeout:Optional[int] = None
	rtpholdtimeout:Optional[int] = None
	sendrpid:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	timert1:Optional[int] = None
	timerb:Optional[int] = None
	qualifyfreq:Optional[int] = None
	constantssrc:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	usereqphone:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	textsupport:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	faxdetect:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	buggymwi:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	callingpres:Optional[asnum.sip_callingpres_values] = asnum.sip_callingpres_values.
	hasvoicemail:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	subscribemwi:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	autoframing:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	rtpkeepalive:Optional[int] = None
	call-limit:Optional[int] = None
	g726nonstandard:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	ignoresdpversion:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	allowtransfer:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	dynamic:Optional[asnum.yes_no_values] = asnum.yes_no_values.
	ipaddr:Optional[str] = None
	contactdeny:Optional[str] = None
	mohinterpret:Optional[str] = None
	defaultuser:Optional[str] = None
	fullcontact:Optional[str] = None
	regserver:Optional[str] = None
	useragent:Optional[str] = None
	mohsuggest:Optional[str] = None
	host:Optional[str] = None
	t38pt_usertpsource:Optional[str] = None
	context:Optional[str] = None
	permit:Optional[str] = None
	deny:Optional[str] = None
	secret:Optional[str] = None
	md5secret:Optional[str] = None
	remotesecret:Optional[str] = None
	regexten:Optional[str] = None
	fromdomain:Optional[str] = None
	fromuser:Optional[str] = None
	nat:Optional[str] = None
	callgroup:Optional[str] = None
	pickupgroup:Optional[str] = None
	language:Optional[str] = None
	disallow:Optional[str] = None
	allow:Optional[str] = None
	insecure:Optional[str] = None
	qualify:Optional[str] = None
	defaultip:Optional[str] = None
	parkinglot:Optional[str] = None
	vmexten:Optional[str] = None
	accountcode:Optional[str] = None
	setvar:Optional[str] = None
	callerid:Optional[str] = None
	amaflags:Optional[str] = None
	auth:Optional[str] = None
	outboundproxy:Optional[str] = None
	callbackextension:Optional[str] = None
	fullname:Optional[str] = None
	trunkname:Optional[str] = None
	cid_number:Optional[str] = None
	path:Optional[str] = None
	mailbox:Optional[str] = None
	contactpermit:Optional[str] = None
