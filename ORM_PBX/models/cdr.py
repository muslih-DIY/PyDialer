
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class cdr(mixin.CRUDMixin,Model.BaseORM):
	sequence = Column('sequence',Integer)
	start = Column('start',TIMESTAMP(False))
	answer = Column('answer',TIMESTAMP(False))
	end = Column('end',TIMESTAMP(False))
	duration = Column('duration',Integer)
	billsec = Column('billsec',Integer)
	dstchannel = Column('dstchannel',String(80))
	lastapp = Column('lastapp',String(80))
	lastdata = Column('lastdata',String(80))
	userfield = Column('userfield',String(256))
	uniqueid = Column('uniqueid',String(150))
	linkedid = Column('linkedid',String(150))
	peeraccount = Column('peeraccount',String(80))
	accountcode = Column('accountcode',String(80))
	disposition = Column('disposition',String(45))
	amaflags = Column('amaflags',String(45))
	src = Column('src',String(80))
	dst = Column('dst',String(80))
	dcontext = Column('dcontext',String(80))
	clid = Column('clid',String(80))
	channel = Column('channel',String(80))
