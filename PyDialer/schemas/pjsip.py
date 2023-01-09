from typing import Optional
from pydantic import BaseModel, EmailStr
from .asterisk_enum import (
    pjsip_transport_protocol_values_v2,
    yesno_values,pjsip_transport_method_values
    )
from .base import ORMBaseModel
from . import asterisk_enum as asnum

class PjsipBaseSchem(BaseModel):
    id:str

class Transport(PjsipBaseSchem):
    bind:Optional[str] = '0.0.0.0:5060'
    protocol:pjsip_transport_protocol_values_v2 = pjsip_transport_protocol_values_v2.udp
    external_media_address:Optional[str]=None
    external_signaling_address:Optional[str]=None
    local_net:Optional[str]=None
    allow_reload:Optional[yesno_values]=yesno_values.no
    external_signaling_port:Optional[int]=5060
    method:Optional[pjsip_transport_method_values] = pjsip_transport_method_values.default

class DBTransport(ORMBaseModel,Transport):
    pass

class BasicEndpoint(PjsipBaseSchem):
    transport:Optional[str] = None
    context :Optional[str] = "agent-conf"
    allow :Optional[str] = 'ulaw,alaw,gsm,g726,g722,g723'
    disallow:Optional[str] = None
    callerid:Optional[str] = None
    dtmf_mode:Optional[asnum.pjsip_dtmf_mode_values_v3] = asnum.pjsip_dtmf_mode_values_v3.rfc4733
    direct_media:Optional[asnum.yesno_values] = asnum.yesno_values.yes
    rewrite_contact:Optional[asnum.yesno_values] = asnum.yesno_values.yes


class BasicUpdateEndpoint(BaseModel):
    transport:Optional[str] = None
    context :Optional[str] = "from-internal"
    allow :Optional[str] = 'ulaw,alaw,gsm,g726,g722,g723'
    callerid:Optional[str] = None
    dtmf_mode:Optional[str] ='rfc4733'
    direct_media:Optional[yesno_values] = yesno_values.yes

class DBEndpoints(ORMBaseModel,BasicEndpoint):
    pass
class BasicPsAuth(BaseModel):
    username : str
    password : str
    auth_type : Optional[str] = 'userpass'
    

class BasicPsAOR(BaseModel):
    contact : Optional[str] = ''
    max_contacts :Optional[int] = 1
    minimum_expiration : Optional[int] = 60
    remove_existing : yesno_values=yesno_values.yes
    qualify_frequency : Optional[int] =60


