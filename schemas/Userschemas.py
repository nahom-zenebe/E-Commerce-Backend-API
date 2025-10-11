from Productschemas import ProductResponse
from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import List


class Role(str, Enum):
    ADMIN="admin"
    USER="user"
    SELLER="seller"

class UserBase(BaseModel):
    username: str
    email: str
    phone_number: str
    address: str
    role: Role = Role.USER
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserCreate(UserBase):
    hashed_password: str

class UserResponse(UserBase):
    id: int
    order: List[OrderResponse] = []

    class Config:
        orm_mode=True

class Token(BaseModel):
    access_token:str
    refresh_token:Optional[str]
    token_type:str="bearer"

class TokenPayload(BaseModel):
    sub:Optional[str]=None
    exp:Optional[str]=None
    jti:Optional[str]=None
    token_type:Optional[str]=None
    