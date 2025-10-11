
from sqlalchemy import Integer,String,Column,DateTime,ForeignKey
from  sqlalchemy.orm import relationship
from  config.database import Base
from sqlalchemy.sql import func



class Product(Base):
    __tablename__="product"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    description=Column(String, nullable=False)
    price=Column(Integer, nullable=False)
    quantity=Column(Integer, nullable=False)
    category_id=Column(Integer,ForeignKey("category.id"))
    created_at=Column(DateTime(timezone=True),server_default=func.now())    
    updated_at=Column(DateTime(timezone=True), server_default=func.now())

