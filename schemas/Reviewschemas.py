from pydantic import BaseModel,Field
from datetime import datetime
from enum import Enum
from pydantic import BaseModel,Field




class ReviewBase(BaseModel):
    rating:int=Field(...,gt=0,lt=6)
    comment:str=Field(...,min_length=1)

class ReviewCreate(ReviewBase):
    product_id:str
    user_id:str

class ReviewResponse(ReviewBase):
    created_at:datetime
    updated_at:datetime

    class Config:
        orm_mode=True