
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_inbound_publications(mixin.CRUDMixin,Model.BaseORM):
	id = Column('id',String(40),nullable=False)
	endpoint = Column('endpoint',String(40))
	event_asterisk-devicestate = Column('event_asterisk-devicestate',String(40))
	event_asterisk-mwi = Column('event_asterisk-mwi',String(40))
