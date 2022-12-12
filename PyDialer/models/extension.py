from sqlalchemy import Column,Integer,String,Boolean,BigInteger,UniqueConstraint
 
from enum import Enum
from ..crud import mixin
from ..depends.db import Model


class extensions(mixin.CRUDMixin,Model.BaseORM):
    id = Column(BigInteger,primary_key=True, index=True) 
    context = Column(String(40))  
    exten = Column(String(40))  
    priority = Column(Integer) 
    app = Column(String(40))  
    appdata = Column(String(256)) 
    __table_args__ = (UniqueConstraint('context','exten','priority', name='cont_ext_pr_unq'),
                     )