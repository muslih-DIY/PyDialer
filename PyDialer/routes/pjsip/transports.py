
from typing import Optional,List
from fastapi import APIRouter,Request,Form,Depends
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi import status
from fastapi.exceptions import HTTPException
from sqlalchemy import exc
from PyDialer.depends.db import get_db
from PyDialer import models
from .base_route import router
from PyDialer.schemas.pjsip import Transport,BasicPJModel




@router.post("/transport/create", response_class=JSONResponse)
async def transpot_create(request: Request,transport:Transport,db=Depends(get_db)):
    try:

        models.ps_transports.create(
            db = db,
            **transport.dict())
    except exc.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Record already exist'
            )

    return JSONResponse('OK')

@router.post("/transport/update", response_class=JSONResponse)
async def transport_update(request: Request,transport:Transport,db=Depends(get_db)):
    
    trans = models.ps_transports.get(db = db,id=transport.id)
    if not trans:
        raise HTTPException(status_code=200,detail='Details not found')   
    trans.update(db=db,**transport.dict())
    return JSONResponse('OK')

@router.post("/transport/remove", response_class=JSONResponse)
async def transpot_remove(request: Request,transport:BasicPJModel,db=Depends(get_db)):
    transp = models.ps_transports.get(
        db = db,
        id=transport.id)
    transp.delete(db = db)
    return JSONResponse('OK')


@router.get("/transport/{id}", response_model=List[Transport])
async def transpot_search(request: Request,id:Optional[str]=None,db=Depends(get_db)):
    if id=='all':
        transport = models.ps_transports.get_all(db = db)        
    else:
        transport = [models.ps_transports.get(id=id,db = db)]
    if not transport:
        raise HTTPException(status_code=200,detail='Details not found')
    return [t.dict() for t in transport]