import psycopg2
import os

con = psycopg2.connect(**{
    'dbname': 'test_ast_rdb',
    'user': 'AsteriskPBX',
    'password': 'PyPbX-secret',
    'host': 'DB-PYPBX'
    }
)

schama_base = """
from enum import Enum
from sqlalchemy.dialects.postgresql import ENUM

enumvalue = lambda obj: [e.value for e in obj]

"""
model_base = """
from sqlalchemy import (
	Column,Integer,BigInteger,
	TIMESTAMP,String,FLOAT,TEXT,
	NUMERIC,UniqueConstraint,LargeBinary
	)
from PyDialer.crud import mixin
from PyDialer.depends.db import Model
from PyDialer.schemas.asterisk_enum import *

"""

pydentic_base = """
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from . import asterisk_enum as asnum
from .base import ORMBaseModel

"""
form_base = """

"""

base_pydentic_class = "ORMBaseModel"

base_model_class = "mixin.CRUDMixin,Model.BaseORM"
sql_tables = "select table_name from information_schema.tables where table_schema='public';"
sql_table_columns ="select column_name , is_nullable ,udt_name,character_maximum_length,data_type='USER-DEFINED'  from information_schema.columns where table_name ="
sql_distinct_user_defined = "select distinct udt_name from information_schema.columns where data_type='USER-DEFINED' and table_name ="
sql_usertype ="""SELECT pg_catalog.format_type(t.oid, NULL) AS "Name",
pg_catalog.array_to_string(
ARRAY(SELECT e.enumlabel FROM pg_catalog.pg_enum e WHERE e.enumtypid = t.oid ORDER BY e.enumsortorder),'|') AS "Elements"
FROM pg_catalog.pg_type t
LEFT JOIN pg_catalog.pg_namespace n ON n.oid = t.typnamespace
WHERE (t.typrelid = 0 OR (SELECT c.relkind = 'c' FROM pg_catalog.pg_class c WHERE c.oid = t.typrelid))
AND NOT EXISTS(SELECT 1 FROM pg_catalog.pg_type el WHERE el.oid = t.typelem AND el.typarray = t.oid)
AND n.nspname <> 'pg_catalog'
AND n.nspname <> 'information_schema'
AND pg_catalog.pg_type_is_visible(t.oid)
ORDER BY 1, 2"""  

def typemap(c_type,size,usertype,nullable,c,t):
    
    if c_type=='int4':return 'Integer,nullable=False' if nullable=='NO' else 'Integer'
    if c_type=='int8':return 'BigInteger,nullable=False' if nullable=='NO' else 'BigInteger'
    if c_type=='bytea':return 'LargeBinary,nullable=False' if nullable=='NO' else 'BYTEA'
    if c_type=='float8':return 'FLOAT,nullable=False' if nullable=='NO' else 'FLOAT'
    if c_type=='varchar': return f'String({size}),nullable=False' if nullable=='NO' else f'String({size})'
    if c_type=='text': return f'TEXT,nullable=False' if nullable=='NO' else f'TEXT'
    if c_type=='numeric': return f'NUMERIC,nullable=False' if nullable=='NO' else f'NUMERIC'
    if c_type=='timestamp': return f'TIMESTAMP(False),nullable=False' if nullable=='NO' else f'TIMESTAMP(False)'
    if usertype:return f"Sql_{c_type},nullable=False" if nullable=='NO' else f"Sql_{c_type}"
    print(c_type,size,usertype,nullable,c,t)
    print("unknown type")

def form_type(c_type,size,usertype,nullable,c,t,enum):

    required = lambda nullable: 'required' if nullable=='NO' else ''
    options = lambda v : '\n'.join([f'<option value="{name}">{name}</option>' for name in v[1].split('|')])
    label_input = lambda c,n,t :f"""
<div>
<label for="{c}">{c}:</label>
<input type="{t}" id="{c}" name="{c}" {required(n)}>
</div>
"""


    if c_type in ('int4','int8','float8','numeric'):return label_input(c,nullable,'number') 

    if c_type in ('varchar','text','bytea'):return label_input(c,nullable,'text')
    if c_type in ('timestamp'):return label_input(c,nullable,'datetime-local')
    if c_type in ('date'):return label_input(c,nullable,'date')

    if usertype:
        return  f"""
<div>
<label for="{c}">{c}:</label>
  <select d="{c}" name="{c}" {required(nullable)}>
    {options(enum)}
  </select>
</div>
"""        
        #return  f"\t{c}:asnum.{c_type} \n" if nullable=='NO' else f"\t{c}:Optional[asnum.{c_type}] = asnum.{c_type}.\n"

    print(c_type,size,usertype,nullable,c,t)
    print("unknown type")    

def pydentic_model(c_type,size,usertype,nullable,c,t):
    if c_type in ('int4','int8'):return  f"\t{c}:int \n" if nullable=='NO' else f"\t{c}:Optional[int] = None\n"
    if c_type=='bytea':return  f"\t{c}:str \n" if nullable=='NO' else f"\t{c}:Optional[str] = None\n"
    if c_type in ('float8','numeric'):return  f"\t{c}:float \n" if nullable=='NO' else f"\t{c}:Optional[float] = None\n"
    if c_type in ('varchar','text'): return  f"\t{c}:str \n" if nullable=='NO' else f"\t{c}:Optional[str] = None\n"
    if c_type in('timestamp','date'): return  f"\t{c}:datetime \n" if nullable=='NO' else f"\t{c}:Optional[datetime] = None\n"
    if usertype:return  f"\t{c}:asnum.{c_type} \n" if nullable=='NO' else f"\t{c}:Optional[asnum.{c_type}] = asnum.{c_type}.\n"

    print(c_type,size,usertype,nullable,c,t)
    print("unknown type")    
    

with con.cursor() as cur:   
    cur.execute(sql_tables)
    tables = [c[0] for c in cur.fetchall()]
    cur.execute(sql_usertype)
    usertype_list = cur.fetchall()

    with open(os.path.join('models',f"__init__.py"),'w') as initf:
        for t in tables:
            initf.writelines(f"\nfrom .{t} import {t}")
            cur.execute(sql_table_columns+f"'{t}'")
            with open(os.path.join('models',f"{t}.py"),'w') as f:
                f.writelines(model_base)
                f.writelines(f"\nclass {t}({base_model_class}):\n")
                for r in cur.fetchall():
                    c,nullable,c_type,size,usertype = r
                    f.writelines(f"\t{c} = Column('{c}',{typemap(c_type,size,usertype,nullable,c,t)})\n")
        
    with open(os.path.join('schemas',f"__init__.py"),'w') as initf:
        for t in tables:
            initf.writelines(f"\nfrom .{t} import {t}")
            cur.execute(sql_table_columns+f"'{t}'")
            with open(os.path.join('schemas',f"{t}.py"),'w') as f:
                f.writelines(pydentic_base)
                f.writelines(f"\nclass {t}({base_pydentic_class}):\n")
                data = cur.fetchall()
                data.sort(key=lambda s : s[1])
                for r in data:
                    c,nullable,c_type,size,usertype = r
                    f.writelines(pydentic_model(c_type,size,usertype,nullable,c,t))
        
                       
    with open(os.path.join('forms',f"__init__.html"),'w') as initf:
        for t in tables:
            initf.writelines(f"\n {t}.html")
            cur.execute(sql_table_columns+f"'{t}'")
            with open(os.path.join('forms',f"{t}.html"),'w') as f:
                data = cur.fetchall()
                data.sort(key=lambda s : s[1])
                for r in data:
                    c,nullable,c_type,size,usertype = r
                    f.writelines(form_type(c_type,size,usertype,nullable,c,t,enum=usertype_list[usertype]))
    
    with open(os.path.join('enum_schema',"schemas.py"),'w') as f:
        f.writelines(schama_base)
        
        for tp,values in usertype_list:
            f.writelines(f"\nclass {tp}(str,Enum):\n")
            for val in values.split('|'):
                f.writelines(f"\t{val}:str = '{val}'\n")
            f.writelines(f"""\nSql_{tp} = ENUM(\n\t{tp},\n\tname='{tp}',\n\tcreate_type=True,\n\tvalues_callable=enumvalue\n)\n""")
    
    with open(os.path.join('migration',"downgrade.py"),'w') as f:
        for tp,values in usertype_list:
            f.writelines(f"""\nop.execute("DROP TYPE  IF EXISTS {tp}")""")
            
con.commit()
con.close()