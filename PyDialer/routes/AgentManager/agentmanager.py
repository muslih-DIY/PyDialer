from typing import Optional
from fastapi import APIRouter,Depends,Header,Request,status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy import exc
from sqlalchemy.orm import Session
from pydantic import BaseModel,validator
from PyDialer.exras.UserManager import have_role
from PyDialer.models import User,ps_endpoints,UserEndpoint

router = APIRouter(
    prefix="/AgentManager",
    tags=["AgentManager"],
    #dependencies=[Depends(super_user_information)]
    )


class agent_endpoint_setup(BaseModel):
    user_id:int
    endpoint_id:str

class agent_enpoint(BaseModel):
    user_id:Optional[int] = None
    endpoint_id:Optional[str] = None
    
    @validator('endpoint_id', always=True)
    def check_a_or_b(cls, endpoint_id, values):
        if values.get('user_id') is None and not endpoint_id:
            raise ValueError('Either endpoint_id or user_id is required')
        return endpoint_id

@router.post("/user_endpoint_relation/create", response_class=JSONResponse)
async def update_agent_endpoint(request:Request,agent_endpoint:agent_endpoint_setup):
    "This API connect the user with the pjsip endpoint"
    db:Session = request.db
    user = User.get(db,agent_endpoint.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No user found'
            )     
    ps_end = ps_endpoints.get(db,agent_endpoint.endpoint_id)
    if not ps_end:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='No such Endpoint Found'
            )             

    try:
        user_end = UserEndpoint.create(db=db,user_id=user.id,endpoint_id=ps_end.id)

    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='User already connected with an endpoint'
            )    
    return JSONResponse('Relation Created')


@router.post("/user_endpoint_relation/remove", response_class=JSONResponse)
async def update_agent_endpoint(request:Request,agent_endpoint:agent_enpoint):
    "This API delete the relation between user and endpoint"
    db:Session = request.db
    agent_endpoint_rel = {k:v for k,v in agent_endpoint.dict().items() if v is not None}

    try:
        user_endpoint = UserEndpoint.get_filter_by(**agent_endpoint_rel,db=db).one()
    except exc.NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Details not found')
    except exc.MultipleResultsFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Multiple Endpoint Found , Please pass endpoint details.')

    user_endpoint.delete(db=db)

    return JSONResponse('Relation removed')


