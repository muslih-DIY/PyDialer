
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_asterisk_publications(mixin.CRUDMixin,Model.BaseORM):
	device_state = Column('device_state',Sql_yesno_values)
	mailbox_state = Column('mailbox_state',Sql_yesno_values)
	mailboxstate_publish = Column('mailboxstate_publish',String(40))
	id = Column('id',String(40),nullable=False)
	device_state_filter = Column('device_state_filter',String(256))
	mailbox_state_filter = Column('mailbox_state_filter',String(256))
	devicestate_publish = Column('devicestate_publish',String(40))
