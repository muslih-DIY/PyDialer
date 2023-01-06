from fastapi import APIRouter,Depends,Header,Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from PyDialer.exras.UserManager import have_role



router = APIRouter(
    prefix="/pjsip",
    tags=["pjsip"],
    #dependencies=[Depends(have_role(['admin','super']))]
    )
