
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class iaxfriends(mixin.CRUDMixin,Model.BaseORM):
	transfer = Column('transfer',Sql_iax_transfer_values)
	jitterbuffer = Column('jitterbuffer',Sql_yes_no_values)
	forcejitterbuffer = Column('forcejitterbuffer',Sql_yes_no_values)
	port = Column('port',Integer)
	sendani = Column('sendani',Sql_yes_no_values)
	regseconds = Column('regseconds',Integer)
	trunk = Column('trunk',Sql_yes_no_values)
	qualifysmoothing = Column('qualifysmoothing',Sql_yes_no_values)
	type = Column('type',Sql_type_values)
	maxauthreq = Column('maxauthreq',Integer)
	requirecalltoken = Column('requirecalltoken',Sql_iax_requirecalltoken_values)
	adsi = Column('adsi',Sql_yes_no_values)
	encryption = Column('encryption',Sql_iax_encryption_values)
	id = Column('id',Integer,nullable=False)
	accountcode = Column('accountcode',String(80))
	mohinterpret = Column('mohinterpret',String(20))
	mohsuggest = Column('mohsuggest',String(20))
	inkeys = Column('inkeys',String(40))
	outkeys = Column('outkeys',String(40))
	language = Column('language',String(10))
	callerid = Column('callerid',String(100))
	cid_number = Column('cid_number',String(40))
	fullname = Column('fullname',String(40))
	auth = Column('auth',String(20))
	disallow = Column('disallow',String(200))
	allow = Column('allow',String(200))
	codecpriority = Column('codecpriority',String(40))
	qualify = Column('qualify',String(10))
	qualifyfreqok = Column('qualifyfreqok',String(10))
	qualifyfreqnotok = Column('qualifyfreqnotok',String(10))
	timezone = Column('timezone',String(20))
	amaflags = Column('amaflags',String(20))
	setvar = Column('setvar',String(200))
	name = Column('name',String(40),nullable=False)
	username = Column('username',String(40))
	mailbox = Column('mailbox',String(40))
	secret = Column('secret',String(40))
	dbsecret = Column('dbsecret',String(40))
	context = Column('context',String(40))
	regcontext = Column('regcontext',String(40))
	host = Column('host',String(40))
	ipaddr = Column('ipaddr',String(40))
	defaultip = Column('defaultip',String(20))
	sourceaddress = Column('sourceaddress',String(20))
	mask = Column('mask',String(20))
	regexten = Column('regexten',String(40))
