
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *


class ps_auths(mixin.CRUDMixin,Model.BaseORM):
	id = Column('id',String(40),primary_key=True)
	nonce_lifetime = Column('nonce_lifetime',Integer)
	auth_type = Column('auth_type',Sql_pjsip_auth_type_values_v2)
	password = Column('password',String(80))
	realm = Column('realm',String(40))
	username = Column('username',String(40))
	refresh_token = Column('refresh_token',String(255))
	oauth_clientid = Column('oauth_clientid',String(255))
	oauth_secret = Column('oauth_secret',String(255))
	md5_cred = Column('md5_cred',String(40))
