from fastapi import APIRouter,HTTPException,status
from app.database import Database
from app.model import CameraNew, Statistic


router = APIRouter( tags=["Camera"])
db =Database

@router.get('/cameras')
async def take_info():
        return await db.take_camera(db)

@router.post ('/newcamera')
async def add_camera(requset: CameraNew):

    await db.add_new_camera(db,requset)
    return { "Camera succeful added"}
@router.get('/infocamera')
async def take_info_setting_camera():
    return await db.take_info_camera(db)
@router.post ('/call')
async def uvel_call_number(addres:str):
    await db.create_call(db,addres)
    return{ "call zapisan"}
@router.get('/call')
async def take_info_calls(request:Statistic):
    return await db.take_calls(db,request)

