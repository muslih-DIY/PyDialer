from sqlalchemy import Column,Integer,String,Boolean,ForeignKey
from sqlalchemy.orm import relationship
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.models import User,ps_endpoints
