
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class musiconhold(mixin.CRUDMixin,Model.BaseORM):
	mode = Column('mode',Sql_moh_mode_values)
	stamp = Column('stamp',TIMESTAMP(False))
	application = Column('application',String(255))
	name = Column('name',String(80),nullable=False)
	sort = Column('sort',String(10))
	format = Column('format',String(10))
	digit = Column('digit',String(1))
	directory = Column('directory',String(255))
