from social.database import Base
from pydantic import BaseModel
from typing import List,Optional


class PostBase(BaseModel):
    title:str
    description: Optional[str] = None



class PostCreate(PostBase):
    uid : int

class Post(PostBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):    
    email : str
    class Config:
         orm_mode=True

class UserResp(BaseModel):    
    id : int
    email : str
    class Config:
         orm_mode=True

class UserCreate(UserBase):
    password: str
    class Config:
         orm_mode=True


class User(UserBase):
    id : int
    email : str
    posts : List[Post] = []
    class Config:
         orm_mode=True


  

