
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_subscription_persistence(mixin.CRUDMixin,Model.BaseORM):
	prune_on_boot = Column('prune_on_boot',Sql_yesno_values)
	src_port = Column('src_port',Integer)
	local_port = Column('local_port',Integer)
	cseq = Column('cseq',Integer)
	expires = Column('expires',Integer)
	local_name = Column('local_name',String(128))
	id = Column('id',String(40),nullable=False)
	contact_uri = Column('contact_uri',String(256))
	tag = Column('tag',String(128))
	packet = Column('packet',String(2048))
	src_name = Column('src_name',String(128))
	endpoint = Column('endpoint',String(40))
	transport_key = Column('transport_key',String(64))
