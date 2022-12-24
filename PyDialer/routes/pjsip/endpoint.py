from typing import Optional,List,Union
from fastapi import Request,Depends,status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy import exc
from PyDialer.depends.db import get_db
from PyDialer.schemas.pjsip import (
    BasicEndpoint,PjsipBaseSchem,
    BasicPsAuth,BasicPsAOR,BasicUpdateEndpoint)
from PyDialer.models import asterisk
from .base_route import router
from ..user import validate_token

ps_auth_id = lambda id :f"{id}-auth"
    
@router.post("/endpoint/create", response_class=JSONResponse)
async def endpoint_create(
    request: Request,endpoint:BasicEndpoint,
    Auth:BasicPsAuth,AOR:BasicPsAOR):
    db = request.dbs
    user = request.User
    endpoint.callerid = endpoint.callerid or f"'{Auth.username}' <{endpoint.id}>" 
    try:  
        ps_auth = asterisk.ps_auths.create(db = db,commit=False,id=ps_auth_id(endpoint.id),**Auth.dict())
        ps_aor = asterisk.ps_aors.create(db = db,commit=False,id=endpoint.id,**AOR.dict())
        ps_endpoint = asterisk.ps_endpoints.create(
            db = db,
            commit=True,
            aors=endpoint.id, 
            auth=ps_auth_id(endpoint.id),
            ** endpoint.dict())
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Record already exist'
            )

    return JSONResponse('OK')

@router.post("/endpoint/update/", response_class=JSONResponse)
async def endpoint_update(
    request: Request,
    pjsip:PjsipBaseSchem,
    endpoint:Optional[BasicUpdateEndpoint] = None,
    Auth:Optional[BasicPsAuth]= None,
    AOR:Optional[BasicPsAOR]= None,
    db=Depends(get_db)):
    callerid = None
    if Auth:
        ps_auth = asterisk.ps_auths.get(db = db,id=ps_auth_id(pjsip.id))
        if ps_auth:
            ps_auth.update(db=db,commit=False,**Auth.dict())
        if Auth.username:
            callerid = f"'{Auth.username}' <{pjsip.id}>"
    
    if AOR:
        ps_aor = asterisk.ps_aors.get(db = db,id=pjsip.id)
        if ps_aor:
            ps_aor.update(db=db,commit=False,**AOR.dict())

    ps_endpoint = asterisk.ps_endpoints.get(db = db,id=pjsip.id) 
    if not ps_endpoint:
         raise HTTPException(status_code=200,detail='Details not found')
    if callerid :
        ps_endpoint.callerid = callerid
    
    if endpoint:
        ps_endpoint.update(db=db,commit=False,**endpoint.dict())

    db.commit() 

    return JSONResponse('OK')

@router.post("/endpoint/remove", response_class=JSONResponse)
async def endpoint_remove(request: Request,endpointid:PjsipBaseSchem,db=Depends(get_db)):
    endpoint = asterisk.ps_endpoints.get(db = db,id=endpointid.id)
    if not endpoint:
        raise HTTPException(status_code=200,detail='Details not found')
    asterisk.ps_aors.get(db = db,id=endpointid.id).delete(db=db,commit=False)
    asterisk.ps_auths.get(db = db,id=ps_auth_id(endpoint.id)).delete(db=db,commit=False)
    endpoint.delete(db = db)
    return JSONResponse('OK')


@router.get("/endpoint/", response_model=Union[BasicEndpoint,BasicPsAOR,BasicPsAuth])
async def endpoint_search(request: Request,id:Optional[str]='all',db=Depends(get_db)):
    if id=='all':
        endpoint = asterisk.ps_endpoints.get_all(db = db)        
    else:
        endpoint = asterisk.ps_endpoints.get(id=id,db = db)
        endpoint = endpoint and [endpoint] or None
    if not endpoint:
        raise HTTPException(status_code=200,detail='Details not found')
    print(endpoint[0].dict())
    return [t.dict() for t in endpoint]