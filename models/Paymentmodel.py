from sqlalchemy import Column,String,Integer,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql import func
import enum

class Payment_method(enum.Enum):
    CREDITCARD="creditcard"
    Paypal='paypal'
    MASTERCARD='mastercard'
    VISA='visa'

class Status(enum.Enum):
    PENDING="pending"
    PAID="paid"
    FAILED='failed'



class Payment(Base):
    __tablename__='payment'
    id=Column(Integer,primary_key,index=True)
    order=relationship("Order",back_populates='payment')
    order_id=Column(Integer,ForeignKey("order.id"))
    payment_method=Column(Enum(Payment_method),server_default=Payment_method.CREDITCARD,nullable=False)
    status=Column(Enum(Status),server_default=Status.PENDING,nullable=False)
    transaction_id=Column(Integer,nullable=False)
    created_at=Column(DateTime(timezone=True), server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now())


