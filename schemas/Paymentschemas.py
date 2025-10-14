from pydantic import BaseModel,Field
from datetime import datetime
from enum import Enum
from pydantic import BaseModel,Field
from  typing import Optional

class Status(str,Enum):
    PENDING="pending"
    PAID="paid"
    FAILED='failed'

class Payment_method(str,Enum):
    CREDITCARD="creditcard"
    Paypal='paypal'
    MASTERCARD='mastercard'
    VISA='visa'

class PaymentBase(BaseModel):
    payment_method:Payment_method
    status:Status
    transaction_id:int


class PaymentCreate(PaymentBase):
    order_id:str

class PaymentResponse(PaymentBase):
    id:str
    created_at:Optional[datetime]=None
    updated_at:Optional[datetime]=None

    class Config:
        orm_mode=True


