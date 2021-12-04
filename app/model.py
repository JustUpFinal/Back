
from pydantic import BaseModel
from typing import Optional

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
class User(BaseModel):
    login : str
    password: str
    

class LoginUser(BaseModel):
        login:str
        password: str
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    login: Optional[str] = None



