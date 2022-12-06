from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.orm import relationship
from ..depends.db import Model,crud

class User(crud.CRUDMixin,Model.BaseORM):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=True)
    password = Column(String(256), nullable=True)
    email = Column(String, index=True, nullable=False)

    
    def __repr__(self) -> str:
        return f"<User {self.id} {self.username} {self.password} {self.email} {self.user_type}>"