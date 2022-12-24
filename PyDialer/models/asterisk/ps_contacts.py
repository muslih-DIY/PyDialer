
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_contacts(mixin.CRUDMixin,Model.BaseORM):
	id = Column('id',String(255),primary_key=True)
	prune_on_boot = Column('prune_on_boot',Sql_yesno_values)
	expiration_time = Column('expiration_time',BigInteger)
	qualify_frequency = Column('qualify_frequency',Integer)
	qualify_timeout = Column('qualify_timeout',FLOAT)
	authenticate_qualify = Column('authenticate_qualify',Sql_yesno_values)
	via_port = Column('via_port',Integer)
	user_agent = Column('user_agent',String(255))
	call_id = Column('call_id',String(255))
	reg_server = Column('reg_server',String(255))
	endpoint = Column('endpoint',String(40))
	uri = Column('uri',String(511))
	via_addr = Column('via_addr',String(40))
	outbound_proxy = Column('outbound_proxy',String(40))
	path = Column('path',TEXT)
