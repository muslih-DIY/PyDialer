
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_systems(mixin.CRUDMixin,Model.BaseORM):
	disable_rport = Column('disable_rport',Sql_ast_bool_values)
	timer_t1 = Column('timer_t1',Integer)
	timer_b = Column('timer_b',Integer)
	compact_headers = Column('compact_headers',Sql_yesno_values)
	threadpool_initial_size = Column('threadpool_initial_size',Integer)
	threadpool_auto_increment = Column('threadpool_auto_increment',Integer)
	threadpool_idle_timeout = Column('threadpool_idle_timeout',Integer)
	threadpool_max_size = Column('threadpool_max_size',Integer)
	disable_tcp_switch = Column('disable_tcp_switch',Sql_yesno_values)
	follow_early_media_fork = Column('follow_early_media_fork',Sql_yesno_values)
	accept_multiple_sdp_answers = Column('accept_multiple_sdp_answers',Sql_yesno_values)
	id = Column('id',String(40),nullable=False)
