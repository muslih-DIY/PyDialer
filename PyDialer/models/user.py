from sqlalchemy import Column,Integer,String,Boolean
from ..crud import mixin
from ..depends.db import Model

class User(mixin.CRUDMixin,Model.BaseORM):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=True)
    password = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)
    is_superuser = Column(Boolean, default=False)
    
    def __repr__(self) -> str:
        return f"<User {self.id} {self.username} {self.email} {self.is_superuser}>"