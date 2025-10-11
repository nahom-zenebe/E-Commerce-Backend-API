from typing import Optional, List
from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class ProductBase(BaseModel):
    name:str
    description:Optional[str]=None
    price:int
    quantity:int
    category_id:int
    created_at:Optional[datetime]=None
    updated_at:Optional[datetime]=None
class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id:int

    class Config:
        orm_mode=True
