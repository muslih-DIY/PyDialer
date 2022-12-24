from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,BigInteger
from sqlalchemy.orm import relationship
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from .asterisk import ps_endpoints


class User(mixin.CRUDMixin,Model.BaseORM):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(127),nullable=False)
    username = Column(String(256),unique=True)
    password = Column(String(256))
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    endpoint = relationship("UserEndpoint", back_populates="user")

    def __repr__(self) -> str:
        return f"<User {self.id} {self.username} {self.email} {self.is_superuser}>"
