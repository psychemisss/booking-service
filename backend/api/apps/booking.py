from fastapi import APIRouter
from sqlalchemy import select
from backend.database.models import User, Bookings, Device
from backend.database.database import engine

booking_router = APIRouter()


@booking_router.get("/status")
async def status() -> dict:
    """
    Simple function
    :return:
    """
    return {"status": "ok"}


@booking_router.get("/all")
async def get_all_devices():
    query = select(Device)
    connection = engine.connect()
    result = connection.execute(query).fetchall()
    return {"result": result}


@booking_router.get("/{device_id}")
async def get_device(device_id: int):
    """
    Function for getting specific device by its id
    :param device_id: device id
    """
    query = select(Device).where(Device.id == device_id)
    connection = engine.connect()
    result = connection.execute(query).fetchall()
    return {"result": result}


# @booking_router.get("/create")
# async def create_device(device_name: str, device_type: int):
#     """
#     Function for device creation
#     :param device_name: device name
#     :param device_type: device type
#     """
#     query = Device.insert().values(name=device_name, type=device_type)
#     connection = engine.connect()
#     result = connection.execute(query)
#     return {"result": result}
