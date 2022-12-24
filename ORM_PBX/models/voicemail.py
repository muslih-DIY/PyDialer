
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class voicemail(mixin.CRUDMixin,Model.BaseORM):
	stamp = Column('stamp',TIMESTAMP(False))
	attach = Column('attach',Sql_yes_no_values)
	deletevoicemail = Column('deletevoicemail',Sql_yes_no_values)
	saycid = Column('saycid',Sql_yes_no_values)
	sendvoicemail = Column('sendvoicemail',Sql_yes_no_values)
	review = Column('review',Sql_yes_no_values)
	tempgreetwarn = Column('tempgreetwarn',Sql_yes_no_values)
	operator = Column('operator',Sql_yes_no_values)
	envelope = Column('envelope',Sql_yes_no_values)
	sayduration = Column('sayduration',Integer)
	forcename = Column('forcename',Sql_yes_no_values)
	forcegreetings = Column('forcegreetings',Sql_yes_no_values)
	maxmsg = Column('maxmsg',Integer)
	volgain = Column('volgain',NUMERIC)
	uniqueid = Column('uniqueid',Integer,nullable=False)
	callback = Column('callback',String(80))
	dialout = Column('dialout',String(80))
	exitcontext = Column('exitcontext',String(80))
	imapport = Column('imapport',String(8))
	imapflags = Column('imapflags',String(80))
	context = Column('context',String(80),nullable=False)
	mailbox = Column('mailbox',String(80),nullable=False)
	password = Column('password',String(80),nullable=False)
	fullname = Column('fullname',String(80))
	alias = Column('alias',String(80))
	email = Column('email',String(80))
	pager = Column('pager',String(80))
	imapuser = Column('imapuser',String(80))
	attachfmt = Column('attachfmt',String(10))
	serveremail = Column('serveremail',String(80))
	language = Column('language',String(20))
	tz = Column('tz',String(30))
	imappassword = Column('imappassword',String(80))
	imapserver = Column('imapserver',String(80))
