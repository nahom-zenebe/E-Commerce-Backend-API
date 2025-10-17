from typing import Optional, List
from datetime import datetime
from enum import Enum
from pydantic import BaseModel,Field


class Status(str,Enum):
    PENDING="pending"
    SHIPPED="shipped"
    DElIVERED="delivered"
    CANCELLED="cancelled"
    REFUNDED="refunded"

class OrderBase(BaseModel):
    total_amount:int=Field(...,gt=0)
    status:Status=Status.PENDING


class OrderCreate(OrderBase):
    user_id:str
    product_id:str


class OrderResponse(OrderBase):
    user_id:str
    product_id:str
    created_at:datetime
    updated_at:datetime

    class Config:
        orm_mode=True

    




