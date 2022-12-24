
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class musiconhold_entry(mixin.CRUDMixin,Model.BaseORM):
	position = Column('position',Integer,nullable=False)
	name = Column('name',String(80),nullable=False)
	entry = Column('entry',String(1024),nullable=False)
