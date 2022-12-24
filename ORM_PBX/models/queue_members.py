
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class queue_members(mixin.CRUDMixin,Model.BaseORM):
	ringinuse = Column('ringinuse',Sql_ast_bool_values)
	penalty = Column('penalty',Integer)
	paused = Column('paused',Integer)
	uniqueid = Column('uniqueid',Integer,nullable=False)
	wrapuptime = Column('wrapuptime',Integer)
	interface = Column('interface',String(80),nullable=False)
	membername = Column('membername',String(80))
	state_interface = Column('state_interface',String(80))
	queue_name = Column('queue_name',String(80),nullable=False)
