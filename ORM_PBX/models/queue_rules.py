
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class queue_rules(mixin.CRUDMixin,Model.BaseORM):
	rule_name = Column('rule_name',String(80),nullable=False)
	time = Column('time',String(32),nullable=False)
	min_penalty = Column('min_penalty',String(32),nullable=False)
	max_penalty = Column('max_penalty',String(32),nullable=False)
