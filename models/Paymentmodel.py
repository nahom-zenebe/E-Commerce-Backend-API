from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum, text
from sqlalchemy.orm import relationship
from config.database import Base
from sqlalchemy.sql import func
import enum

class Payment_method(enum.Enum):
    CREDITCARD = "creditcard"
    PAYPAL = "paypal"
    MASTERCARD = "mastercard"
    VISA = "visa"

class Status(enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    FAILED = "failed"

class Payment(Base):
    __tablename__ = 'payment'
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    order = relationship("Order", back_populates='payment')
    
    payment_method = Column(
        Enum(Payment_method),
        server_default=text(f"'{Payment_method.CREDITCARD.value}'"),  # Use .value wrapped in text()
        nullable=False
    )
    
    status = Column(
        Enum(Status),
        server_default=text(f"'{Status.PENDING.value}'"),  # Use .value wrapped in text()
        nullable=False
    )
    
    transaction_id = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
