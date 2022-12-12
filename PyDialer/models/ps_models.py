from sqlalchemy import Column,Integer,String,UniqueConstraint
from ..crud import mixin
from ..depends.db import Model
from PyDialer.schemas.pjsip import Transport
class ps_transports(mixin.CRUDMixin[Transport],Model.BaseORM):
    id = Column(String(40),primary_key=True, index=True) 
    async_operations = Column(Integer)  
    bind = Column(String(40))  
    ca_list_file = Column(String(200))  
    cert_file = Column(String(200))  
    cipher = Column(String(200))  
    domain = Column(String(40))  
    external_media_address = Column(String(40))  
    external_signaling_address = Column(String(40))  
    external_signaling_port  = Column(Integer) 
    method = Column(String(40))  
    local_net = Column(String(40))  
    password = Column(String(40))  
    priv_key_file = Column(String(200))  
    protocol = Column(String(40))   
    require_client_cert = Column(String(40))   
    verify_client = Column(String(40))  
    verifiy_server = Column(String(40))   
    tos = Column(String(40))  
    cos = Column(String(40))  

    __table_args__ = (UniqueConstraint('bind','protocol', name='protocol_bind_unq'),
                     )

    def __str__(self) -> str:
        return self.id
    def __repr__(self) -> str:
        return f"<{self.id}>"