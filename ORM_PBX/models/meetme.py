
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class meetme(mixin.CRUDMixin,Model.BaseORM):
	bookid = Column('bookid',Integer,nullable=False)
	starttime = Column('starttime',TIMESTAMP(False))
	endtime = Column('endtime',TIMESTAMP(False))
	maxusers = Column('maxusers',Integer)
	members = Column('members',Integer,nullable=False)
	adminpin = Column('adminpin',String(20))
	opts = Column('opts',String(20))
	adminopts = Column('adminopts',String(20))
	confno = Column('confno',String(80),nullable=False)
	recordingfilename = Column('recordingfilename',String(80))
	recordingformat = Column('recordingformat',String(10))
	pin = Column('pin',String(20))
