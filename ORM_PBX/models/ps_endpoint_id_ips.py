
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_endpoint_id_ips(mixin.CRUDMixin,Model.BaseORM):
	srv_lookups = Column('srv_lookups',Sql_yesno_values)
	id = Column('id',String(40),nullable=False)
	endpoint = Column('endpoint',String(40))
	match = Column('match',String(80))
	match_header = Column('match_header',String(255))
