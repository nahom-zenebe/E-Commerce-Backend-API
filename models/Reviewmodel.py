
from sqlalchemy import Integer,String,Column,DateTime,ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from config.database import Base
import enum
from sqlalchemy import func



class Review(Base):
    __tablename__="Reviews"
    __table_args__=(
        CheckConstraint('rating >=1 AND rating<= 5', name='rating_range'),
    )
    
    id=Column(Integer,primary_key=True,index=True)
    product_id=Column( Integer,ForeignKey("product.id"),nullable=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    rating=Column(Integer,nullable=False)
    comment=Column(String,nullable=True)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now())
