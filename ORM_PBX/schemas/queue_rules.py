
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel


class queue_rules(ORMBaseModel):
	rule_name:str 
	time:str 
	min_penalty:str 
	max_penalty:str 
