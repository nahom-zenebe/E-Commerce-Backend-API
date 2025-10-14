from typing import List, Optional
from sqlalchemy.orm import Session, lazyload
from fastapi import Depends
from models.Paymentmodel import Payment
from config.database import get_db



class PaymentRepository:
    def __init__(self,db:Session):
        self.db=db

    
    def create_payment(self,order_id:int,stripe_payment_id:str,amount:float,status:str)->Payment:
        payment=Payment(
            order_id=order_id,
            stripe_payment_id=stripe_payment_id,
            amount=amount,
            status=status

        )
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment


    def get_payment_by_order(self,order_id:int)->Payment:
        return self.db.query(Payment).filter(Payment.order_id==order_id)
        