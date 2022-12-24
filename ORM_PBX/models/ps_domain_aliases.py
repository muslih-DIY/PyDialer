
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_domain_aliases(mixin.CRUDMixin,Model.BaseORM):
	id = Column('id',String(40),nullable=False)
	domain = Column('domain',String(80))
