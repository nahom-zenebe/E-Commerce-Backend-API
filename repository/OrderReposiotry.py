from models.Ordermodel import Order
from config.database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session, lazyload






class OrderRepository:
    def __init__(self,db:Session):
        self.db=db

    def createorder(self,order:Order)->Order:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def getallorder(self)->List[Order]:
        return self.db.query(Order).all()


    def deleteorder(self,order_id:int)-> None:
        deleted_order=self.db.query(Order).filter(Order.id==order_id).first()

        if deleted_order:
            self.db.delete(deleted_order)
            self.commit() 
            self.db.refresh(deleted_order)

    def getorderbyId(self,order_id:int)->Order:
        return self.db.query(Order).filter(Order.id==order_id).first() 

    def updatedOrder(self,order_id:int,order:Order)->Order:
        updated_order=self.db.query(Order).filter(Order.id==order_id).first()
        if updated_order:
            updated_order.total_amount=order.total_amount
            updated_order.payment=order.payment
            updated_order.status=order.status
            self.commit()
            self.db.refresh(updated_order)
        return updated_order



            