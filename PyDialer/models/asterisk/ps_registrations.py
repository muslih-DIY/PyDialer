
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_registrations(mixin.CRUDMixin,Model.BaseORM):
	id = Column('id',String(40),primary_key=True)
	max_random_initial_delay = Column('max_random_initial_delay',Integer)
	auth_rejection_permanent = Column('auth_rejection_permanent',Sql_yesno_values)
	expiration = Column('expiration',Integer)
	max_retries = Column('max_retries',Integer)
	retry_interval = Column('retry_interval',Integer)
	forbidden_retry_interval = Column('forbidden_retry_interval',Integer)
	support_path = Column('support_path',Sql_yesno_values)
	fatal_retry_interval = Column('fatal_retry_interval',Integer)
	line = Column('line',Sql_yesno_values)
	support_outbound = Column('support_outbound',Sql_ast_bool_values)
	server_uri = Column('server_uri',String(255))
	client_uri = Column('client_uri',String(255))
	contact_user = Column('contact_user',String(40))
	transport = Column('transport',String(40))
	endpoint = Column('endpoint',String(40))
	outbound_auth = Column('outbound_auth',String(40))
	outbound_proxy = Column('outbound_proxy',String(40))
	contact_header_params = Column('contact_header_params',String(255))
