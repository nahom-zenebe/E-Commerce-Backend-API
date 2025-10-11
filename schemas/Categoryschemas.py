from typing import Optional, List
from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
class CategoryCreate(CategoryBase):
    pass   

class CategoryResponse(CategoryBase):
    id: int

    class Config:
        orm_mode=True
