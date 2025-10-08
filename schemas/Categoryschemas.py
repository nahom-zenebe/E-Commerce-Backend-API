from Productschemas import ProductResponse
from typing import Optional
from datetime import datetime
from enum import Enum
from pydantic import BaseModel
from typing import List


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
class CategoryCreate(CategoryBase):
    pass   

class CategoryResponse(CategoryBase):
    id: int
    product: List[ProductResponse] = []

    class Config:
        orm_mode=True
