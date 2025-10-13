from typing import List
from repository.OrderRepository import OrderRepository
from fastapi import Depends
from schemas.Orderschemas import OrderBase,OrderCreate,OrderResponse
from sqlalchemy.orm import Session


class OrderService:
    def __init__(self,db:Session):
        self.db=db
        self.orderrepository=OrderRepository(self.db)


    def createorder(self,order:OrderCreate)->Order:
        return self.orderrepository.createorder(order)

    def getallorder(self)->List[Order]:
        return self.orderrepository.getallorder()

    def updatedorder(self,order_id:int,order:OrderBase)->Order:
        return self.orderrepository.updatedOrder(order_id,order)

    def deleteorder(self,order_id:int):
        return self.orderrepository.deleteorder(order_id)

    
        