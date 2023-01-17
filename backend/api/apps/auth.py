from fastapi import APIRouter
from sqlalchemy import select
from backend.database.models import User
from backend.database.database import engine

auth_router = APIRouter()


@auth_router.get("/status")
async def login() -> dict:
    """
    Simple function
    :return:
    """
    return {"status": "ok"}


@auth_router.get("/all")
async def get_all_users():
    query = select(User)
    connection = engine.connect()
    result = connection.execute(query).fetchall()
    return {"result": result}
