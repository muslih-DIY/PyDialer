
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_outbound_publishes(mixin.CRUDMixin,Model.BaseORM):
	max_auth_attempts = Column('max_auth_attempts',Integer)
	expiration = Column('expiration',Integer)
	multi_user = Column('multi_user',Sql_yesno_values)
	server_uri = Column('server_uri',String(256))
	from_uri = Column('from_uri',String(256))
	to_uri = Column('to_uri',String(256))
	event = Column('event',String(40))
	transport = Column('transport',String(40))
	@body = Column('@body',String(40))
	@context = Column('@context',String(256))
	id = Column('id',String(40),nullable=False)
	@exten = Column('@exten',String(256))
	outbound_auth = Column('outbound_auth',String(40))
	outbound_proxy = Column('outbound_proxy',String(256))
