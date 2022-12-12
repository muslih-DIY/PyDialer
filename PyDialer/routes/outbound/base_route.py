from fastapi import APIRouter

router = APIRouter(
    prefix="/outbound",
    tags=["outbound"]
    )
