from typing import Optional,List
from fastapi import Request,Depends
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy import exc
from PyDialer.depends.db import get_db
from PyDialer.schemas.pjsip import BasicEndpoint,BasicPJModel,BasicPsAuth,BasicPsAOR
from PyDialer import models
from .base_route import router

    
@router.post("/endpoint/create", response_class=JSONResponse)
async def endpoint_create(
    request: Request,endpoint:BasicEndpoint,
    Auth:BasicPsAuth,AOR:BasicPsAOR,db=Depends(get_db)):
    Auth.username = endpoint.display_name or Auth.username  
    ps_auth = models.ps_auth.create(db = db,commit=False,id=f"{endpoint.id}-auth",**Auth.dict())
    ps_aor = models.ps_aors.create(db = db,commit=False,id=endpoint.id,**AOR.dict())
    ps_endpoint = models.ps_endpoint.create(
        db = db,
        commit=True,
        aors=endpoint.id, 
        auth=f"{endpoint.id}-auth",
        ** endpoint.dict())

    return JSONResponse('OK')

@router.post("/endpoint/update/", response_class=JSONResponse)
async def endpoint_update(request: Request,endpoint:BasicEndpoint,db=Depends(get_db)):
    ps_auth = models.ps_auth.get(db = db,id=f"{endpoint.id}-auth")
    ps_aor = models.ps_aors.get(db = db,id=endpoint.id)
    ps_endpoint = models.ps_endpoint.get(db = db,id=endpoint.id)
    if not ps_endpoint:
        raise HTTPException(status_code=200,detail='Details not found')     
    ps_endpoint.update(db=db,**endpoint.dict())       

    return JSONResponse('OK')

@router.post("/endpoint/remove", response_class=JSONResponse)
async def endpoint_remove(request: Request,endpointid:BasicPJModel,db=Depends(get_db)):
    endpoint = models.ps_endpoint.get(db = db,id=endpointid.id)
    endpoint.delete(db = db)
    return JSONResponse('OK')


@router.get("/endpoint/", response_model=List[BasicEndpoint])
async def endpoint_search(request: Request,id:Optional[str]=None,db=Depends(get_db)):
    if not id or id=='all':
        endpoint = models.ps_endpoint.get_all(db = db)        
    else:
        endpoint = [models.ps_endpoint.get(id=id,db = db)]
    if not endpoint:
        raise HTTPException(status_code=200,detail='Details not found')
    return [t.dict() for t in endpoint]