from fastapi import APIRouter,Depends,Header,Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from PyDialer.exras.UserManager import super_user_information



router = APIRouter(
    prefix="/pjsip",
    tags=["pjsip"],
    #dependencies=[Depends(super_user_information)]
    )
