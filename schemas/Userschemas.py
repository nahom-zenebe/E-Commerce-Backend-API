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
    password: str

class UserResponse(UserBase):
    id: int
    order: List[OrderResponse] = []

    class Config:
        orm_mode=True
