from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, Integer
from sqlalchemy.orm import Session
from .Model import BaseORM

class CRUDMixin(object):
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)

    @classmethod
    def create(cls,*args,db : Session,commit=True,**kwargs):
        instance = cls(*args,**kwargs)
        return instance.save(db,commit=commit)

    @classmethod
    def get(cls:BaseORM,db : Session,id):
        return db.query(cls).get(id)
    
    @classmethod
    def get_filter_by(cls:BaseORM,db : Session,**kwargs):
        return db.query(cls).filter_by(**kwargs)

    def update(self,db : Session,commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save(db) or self

    def save(self,db : Session, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self,db : Session, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()