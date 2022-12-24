
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_aors(mixin.CRUDMixin,Model.BaseORM):
	id = Column('id',String(40),primary_key=True)
	remove_unavailable = Column('remove_unavailable',Sql_ast_bool_values)
	qualify_frequency = Column('qualify_frequency',Integer)
	authenticate_qualify = Column('authenticate_qualify',Sql_yesno_values)
	maximum_expiration = Column('maximum_expiration',Integer)
	support_path = Column('support_path',Sql_yesno_values)
	qualify_timeout = Column('qualify_timeout',FLOAT)
	default_expiration = Column('default_expiration',Integer)
	max_contacts = Column('max_contacts',Integer)
	minimum_expiration = Column('minimum_expiration',Integer)
	remove_existing = Column('remove_existing',Sql_yesno_values)
	contact = Column('contact',String(255))
	mailboxes = Column('mailboxes',String(80))
	outbound_proxy = Column('outbound_proxy',String(40))
	voicemail_extension = Column('voicemail_extension',String(40))
