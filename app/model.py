
from pydantic import BaseModel

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
    url: str
class Statistic(BaseModel):
    cameraid:int
    datestart: str
    dateend: str
