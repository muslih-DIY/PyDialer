
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_globals(mixin.CRUDMixin,Model.BaseORM):
	allow_sending_180_after_183 = Column('allow_sending_180_after_183',Sql_ast_bool_values)
	max_forwards = Column('max_forwards',Integer)
	unidentified_request_prune_interval = Column('unidentified_request_prune_interval',Integer)
	mwi_tps_queue_high = Column('mwi_tps_queue_high',Integer)
	mwi_tps_queue_low = Column('mwi_tps_queue_low',Integer)
	mwi_disable_initial_unsolicited = Column('mwi_disable_initial_unsolicited',Sql_yesno_values)
	ignore_uri_user_options = Column('ignore_uri_user_options',Sql_yesno_values)
	use_callerid_contact = Column('use_callerid_contact',Sql_ast_bool_values)
	send_contact_status_on_update_registration = Column('send_contact_status_on_update_registration',Sql_ast_bool_values)
	taskprocessor_overload_trigger = Column('taskprocessor_overload_trigger',Sql_pjsip_taskprocessor_overload_trigger_values)
	norefersub = Column('norefersub',Sql_ast_bool_values)
	max_initial_qualify_time = Column('max_initial_qualify_time',Integer)
	keep_alive_interval = Column('keep_alive_interval',Integer)
	contact_expiration_check_interval = Column('contact_expiration_check_interval',Integer)
	disable_multi_domain = Column('disable_multi_domain',Sql_yesno_values)
	unidentified_request_count = Column('unidentified_request_count',Integer)
	unidentified_request_period = Column('unidentified_request_period',Integer)
	user_agent = Column('user_agent',String(255))
	default_outbound_endpoint = Column('default_outbound_endpoint',String(40))
	debug = Column('debug',String(40))
	endpoint_identifier_order = Column('endpoint_identifier_order',String(40))
	default_voicemail_extension = Column('default_voicemail_extension',String(40))
	default_from_user = Column('default_from_user',String(80))
	default_realm = Column('default_realm',String(40))
	regcontext = Column('regcontext',String(80))
	id = Column('id',String(40),nullable=False)
