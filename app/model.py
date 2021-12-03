
from fastapi.params import Form
from pydantic import BaseModel, validator
from typing import Optional, Text
class FeedPostShow(BaseModel):
    id: int
    id_user: int
    number_like: int
    Text :str
    description: str = None
    url :str = None
class CameraNew(BaseModel):
    addres_name : str
    camera_potok : str
class Statistic(BaseModel):
    addres:str
    startmounth:int
    startyear:int
    endmounth:int
    endyear:int
