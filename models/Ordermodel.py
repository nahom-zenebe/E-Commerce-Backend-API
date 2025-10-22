
from sqlalchemy import Integer,String,Column,DateTime,ForeignKey,Enum
from  sqlalchemy.orm import relationship
from  config.database import Base
import enum
from  sqlalchemy import func




class Status(enum.Enum):
    PENDING="pending"   
    SHIPPED="shipped"
    DElIVERED="delivered"
    CANCELLED="cancelled"
    REFUNDED="refunded"





class Order(Base):
    __tablename__="order"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    product_id=Column(Integer,ForeignKey("product.id"),nullable=False)
    total_amount=Column(Integer, nullable=False)  
    orderitem_id=Column(Integer,ForeignKey("orderitem.id"))
    orderitem=relationship("OrderItem",back_populates="order")
    user=relationship("User",back_populates="order")
    payment=relationship("Payment",back_populates='order',uselist=False)
    status = Column(Enum(Status, name="status_enum"),nullable=False,default=Status.PENDING )
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now())
