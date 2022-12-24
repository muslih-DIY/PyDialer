
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class extensions(mixin.CRUDMixin,Model.BaseORM):
	id = Column('id',BigInteger,nullable=False)
	priority = Column('priority',Integer,nullable=False)
	context = Column('context',String(40),nullable=False)
	exten = Column('exten',String(40),nullable=False)
	app = Column('app',String(40),nullable=False)
	appdata = Column('appdata',String(256),nullable=False)
