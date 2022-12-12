from typing import Optional
from pydantic import BaseModel, EmailStr


class BasicPJModel(BaseModel):
    id:str

class Transport(BasicPJModel):
    bind:Optional[str] = '0.0.0.0:5060'
    protocol:Optional[str] = 'udp'
    external_media_address:Optional[str]=None
    external_signaling_address:Optional[str]=None


class BasicEndpoint(BaseModel):
    id:str
    transport:Optional[str] = None
    context :Optional[str] = "from-internal"
    allow :Optional[str] = 'ulaw,alaw,gsm,g726,g722,g723'
    callerid:Optional[str] = None 
    dtmf_mode:Optional[str] ='rfc4733'

class BasicPsAuth(BaseModel):
    password : str
    auth_type : Optional[str] = 'userpass'
    username : Optional[str] = None

class BasicPsAOR(BaseModel):
    contact : Optional[str] = ''
    max_contacts :Optional[int] = 1
    minimum_expiration : Optional[int] = 60
    remove_existing : Optional[str] ='yes'
    qualify_frequency : Optional[int] =60
