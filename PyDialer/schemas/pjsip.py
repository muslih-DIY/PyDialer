from typing import Optional
from pydantic import BaseModel, EmailStr
from .asterisk_enum import (
    pjsip_transport_protocol_values_v2,
    yesno_values)


class PjsipBaseSchem(BaseModel):
    id:str

class Transport(PjsipBaseSchem):
    bind:Optional[str] = '0.0.0.0:5060'
    protocol:pjsip_transport_protocol_values_v2 = pjsip_transport_protocol_values_v2.udp
    external_media_address:Optional[str]=None
    external_signaling_address:Optional[str]=None


class BasicEndpoint(PjsipBaseSchem):
    transport:Optional[str] = None
    context :Optional[str] = "from-internal"
    allow :Optional[str] = 'ulaw,alaw,gsm,g726,g722,g723'
    callerid:Optional[str] = None
    dtmf_mode:Optional[str] ='rfc4733'

class BasicUpdateEndpoint(BaseModel):
    transport:Optional[str] = None
    context :Optional[str] = "from-internal"
    allow :Optional[str] = 'ulaw,alaw,gsm,g726,g722,g723'
    callerid:Optional[str] = None
    dtmf_mode:Optional[str] ='rfc4733'

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



