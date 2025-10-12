
import sqlalchemy import Integer,String,Column,DateTime,ForeignKey
import sqlalchemy.orm import relationship
import config.database import Base
import enum
from sqlalchemy import func




class Status(enum.Enum):
    PENDING="pending"   
    SHIPPED="shipped"
    DElIVERED="delivered"
    CANCELLED="cancelled"
    REFUNDED="refunded"





class Order(Base):
    __tablename__="order"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("user.id"),nullable=False)
    product_id=Column(Integer,ForeignKey("product.id"),nullable=False)
    total_amount=Column(Integer, nullable=False)   
    payment=relationship("Payment",back_populates='order',uselist=False)
    payment_id=Column(Integer,ForeignKey("payment.id"),nullable=True)
    status=Column(Enum(Status),server_default=Status.PENDING,nullable=False)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now())
