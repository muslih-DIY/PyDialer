
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_resource_list(mixin.CRUDMixin,Model.BaseORM):
	full_state = Column('full_state',Sql_yesno_values)
	notification_batch_interval = Column('notification_batch_interval',Integer)
	resource_display_name = Column('resource_display_name',Sql_ast_bool_values)
	id = Column('id',String(40),nullable=False)
	list_item = Column('list_item',String(2048))
	event = Column('event',String(40))
