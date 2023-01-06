from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,BigInteger,ARRAY
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
    group = relationship('Groups',secondary = 'usergroup')
    def __repr__(self) -> str:
        return f"<User {self.id} {self.username} {self.email} {self.group}>"


class Groups(mixin.CRUDMixin,Model.BaseORM):
    id = Column(Integer, primary_key=True)
    name = Column(String(127),nullable=False,unique=True)
    permissions = Column(ARRAY(String))
    user = relationship('User',secondary='usergroup',viewonly=True)

class UserGroup(mixin.CRUDMixin,Model.BaseORM):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id',ondelete="CASCADE"),nullable=False,primary_key = True)
    group_id = Column(Integer,ForeignKey('groups.id',ondelete="CASCADE"),nullable=False,primary_key = True)
