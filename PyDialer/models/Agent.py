from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.models import User,ps_endpoints

class UserEndpoint(mixin.CRUDMixin,Model.BaseORM):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id',ondelete="CASCADE"))
    user = relationship('User')
    endpoint_id = Column(String(40),ForeignKey('ps_endpoints.id',ondelete="CASCADE"),unique=True)
    endpoint = relationship('ps_endpoints')