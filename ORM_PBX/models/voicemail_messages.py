
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class voicemail_messages(mixin.CRUDMixin,Model.BaseORM):
	origtime = Column('origtime',Integer)
	duration = Column('duration',Integer)
	recording = Column('recording',BYTEA)
	msgnum = Column('msgnum',Integer,nullable=False)
	flag = Column('flag',String(30))
	category = Column('category',String(30))
	mailboxuser = Column('mailboxuser',String(30))
	mailboxcontext = Column('mailboxcontext',String(30))
	dir = Column('dir',String(255),nullable=False)
	msg_id = Column('msg_id',String(40))
	context = Column('context',String(80))
	macrocontext = Column('macrocontext',String(80))
	callerid = Column('callerid',String(80))
