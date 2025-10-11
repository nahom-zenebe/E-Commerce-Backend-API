from sqlalchemy import Column,Integer,String,DateTime,func
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql import func



class Category(Base):
    __tablename__="category"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    description=Column(String,nullable=False)
    product=relationship("Product",back_populates="category", cascade="all, delete-orphan")
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now())


