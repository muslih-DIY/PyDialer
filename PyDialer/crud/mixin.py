from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from fastapi.encoders import jsonable_encoder
from sqlalchemy import Column, Integer
from sqlalchemy.orm import Session
from pydantic import BaseModel
from ..depends.db.Model import BaseORM

ModelType = TypeVar("ModelType", bound=BaseORM)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUDMixin(Generic[ModelType]):
    
    __table_args__ = {'extend_existing': True}

    @classmethod
    def create(cls,*args,db : Session,commit=True,**kwargs):
        instance = cls(*args,**kwargs)
        return instance.save(db,commit=commit)

    @classmethod
    def get(cls:BaseORM,db : Session,id)-> Optional[ModelType]:
        return db.query(cls).get(id)

    @classmethod
    def get_all(cls:BaseORM,db : Session)-> List[ModelType]:
        return db.query(cls).all()
        

    @classmethod
    def get_filter_by(cls:BaseORM,db : Session,**kwargs):
        return db.query(cls).filter_by(**kwargs)


    def update(self,db : Session,commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save(db,commit) 

    def save(self,db : Session, commit=True):
        db.add(self)
        if commit:
            db.commit()
        return self

    def delete(self,db : Session, commit=True):
        db.delete(self)
        return commit and db.commit()

    def reload(self,db:Session):
        updated = self.__class__.get(db=db,id=self.id)
        for attr ,value in updated.__dict__.items():
            setattr(self, attr, value)
        return self

    def refresh(self,db : Session):
        db.refresh(self)
        return self

    def dict(self):
        return self.__dict__
