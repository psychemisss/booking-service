from fastapi import APIRouter

from backend.api.apps.auth import auth_router
from backend.api.apps.booking import booking_router

api_router = APIRouter()

api_router.include_router(auth_router, prefix='/auth', tags=["auth"])
api_router.include_router(booking_router, prefix='/booking', tags=["booking"])
