from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from pydantic.types import conint


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
      orm_mode = True
      
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id : int
    owner: UserOut

    class Config:
      orm_mode = True
       # Pydantic will automatically convert the ORM object to a dictionary, filtering out any additional attributes or methods and only including the model's defined fields.

class Postout(BaseModel):
    Post:  Post
    votes: int

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password : str



class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id : int
    dir : conint(le=1)
    

