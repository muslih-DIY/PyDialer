
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_transports(mixin.CRUDMixin,Model.BaseORM):
	external_signaling_port = Column('external_signaling_port',Integer)
	method = Column('method',Sql_pjsip_transport_method_values)
	protocol = Column('protocol',Sql_pjsip_transport_protocol_values_v2)
	require_client_cert = Column('require_client_cert',Sql_yesno_values)
	verify_client = Column('verify_client',Sql_yesno_values)
	verify_server = Column('verify_server',Sql_yesno_values)
	async_operations = Column('async_operations',Integer)
	cos = Column('cos',Integer)
	allow_reload = Column('allow_reload',Sql_yesno_values)
	symmetric_transport = Column('symmetric_transport',Sql_yesno_values)
	allow_wildcard_certs = Column('allow_wildcard_certs',Sql_yesno_values)
	tos = Column('tos',String(10))
	local_net = Column('local_net',String(40))
	bind = Column('bind',String(40))
	ca_list_file = Column('ca_list_file',String(200))
	cert_file = Column('cert_file',String(200))
	cipher = Column('cipher',String(200))
	domain = Column('domain',String(40))
	external_media_address = Column('external_media_address',String(40))
	external_signaling_address = Column('external_signaling_address',String(40))
	id = Column('id',String(40),nullable=False)
	password = Column('password',String(40))
	priv_key_file = Column('priv_key_file',String(200))
