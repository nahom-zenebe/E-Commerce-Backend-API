
from fastapi import FastAPI,HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from config.database  import get_db
from schemas.Orderschemas import OrderCreate,OrderResponse,OrderBase
from service.Orderservice import OrderService
from fastapi import Depends
from typing import List



router=APIRouter(prefix='/orders',tags=['orders'])




@router.post("/createorder",response_model=OrderResponse,status_code=status.HTTP_201_CREATED)
def createorder(order: OrderCreate, db: Session = Depends(get_db)):
    service=OrderService(db)
    try:
        created_order=service.createorder(order)
        return created_order

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/getorder",response_model=List[OrderResponse],status_code=status.HTTP_200_OK)
def getallorder(db:Session=Depends(get_db)):
    service=OrderService(db)
    try:
        orders=service.getallorder()
        return orders

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/deleteorder/{order_id}")
def deleteorder(order_id:int,db:Session=Depends(get_db)):
    service=OrderService(db)

    try:
        service.deleteorder(order_id)
        return {"message": "Order deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    

@router.put("/updateorder/{order_id}", response_model=OrderResponse)
def updatedorder(order_id:int, order:OrderBase, db:Session=Depends(get_db)):
    service=OrderService(db)

    try:
        updated_order=service.updatedorder(order_id, order)
        return updated_order

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/getorderbyId/{order_id}", response_model=OrderResponse)
def getorderbyId(order_id:int, db:Session=Depends(get_db)):
    service=OrderService(db)

    try:
        order=service.getorderbyId(order_id)
        return order

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
