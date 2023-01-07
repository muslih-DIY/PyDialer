from typing import List,Optional
from fastapi import APIRouter,Request,Depends,status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy import exc
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import joinedload
from PyDialer.schemas.user import (
    UserCreate,Users,UserUpdate,
    GroupsCreate,DBGroup,GroupsUpdate
    )
from PyDialer.schemas.base import Integerid
from PyDialer.models import User,Groups,ps_endpoints
from PyDialer.exras.UserManager import (have_role)

import hashlib

#route
salt = 'Asteriskpystrix'
router = APIRouter(
    prefix="/admin",
    tags=["accounts"],
    #dependencies=[Depends(have_role(['']))]
    )


@router.post('/register', response_class=JSONResponse)
async def user_register(request: Request,user_data:UserCreate):
    try:
        for g_id in user_data.group:
            if not Groups.get(db=request.db,id=g_id):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Group with id  {g_id} is not available .')
        for end_id in user_data.endpoint:
            if not ps_endpoints.get(db=request.db,id=end_id):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Endpoint with id  {end_id} is not available .')            
        user_data.password = hashlib.md5(':'.join([salt,user_data.password]).encode()).hexdigest()
        Userdb = User.create(**user_data.dict(),db=request.dbs)
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This username is not avialiable'
            )
    return JSONResponse('OK')

@router.post('/edituser', response_model=Users)
async def user_edit(request: Request,user_data:UserUpdate):
    try:
        user = User.get(db=request.db,id=user_data.id)
        for g_id in user_data.group:
            if not Groups.get(db=request.db,id=g_id):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Group with id  {g_id} is not available .')
        for end_id in user_data.endpoint:
            if not ps_endpoints.get(db=request.db,id=end_id):
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Endpoint with id  {end_id} is not available .')    
        user.update(db=request.db,**user_data.dict())
    except exc.NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Unknown User')
    return user


@router.get('/users' , response_model=List[Users])
async def users_details(
    request: Request
    ):
    db:Session = request.db
    users:List[User] = db.query(User).options(joinedload(User.endpoint)).all()
    return users

@router.post('/create/groups' , response_model=DBGroup)
async def group_create(
    request: Request,
    groups:GroupsCreate 
    ):
    db:Session = request.db
    try:
        gr = Groups.create(db=db,**groups.dict())
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This Group already available'
            )    
    return gr

@router.post('/update/groups', response_model=DBGroup)
async def user_edit(request: Request,group_data:GroupsUpdate):
    
    group = Groups.get(db=request.db,id=group_data.id)
    if not group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='group is not found')
    group.update(db=request.db,**group_data.dict())
    return group

@router.get('/groups', response_model=List[DBGroup])
async def user_edit(request: Request,groupid:Optional[int]=None):
    try:
        if not groupid :
            group = Groups.get_all(db = request.db)
            return group
        group = Groups.get_filter_by(db=request.db,id=groupid).all()
        return group
    except exc.NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='group is not found')
    
    
@router.post("/remove/group", response_class=JSONResponse)
async def endpoint_remove(request: Request,groupid:Integerid):
    db:Session = request.db
    group = Groups.get(db = db,id=groupid.id)
    if not group:
        raise HTTPException(status_code=200,detail='Details not found')
    group.delete(db = db)
    return JSONResponse('OK')