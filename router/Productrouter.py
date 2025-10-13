from fastapi import FastAPI,HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.Productschemas import ProductBase,ProductCreate,ProductResponse
from service.Productservice import Productservice
from fastapi import Depends
from typing import List

router=APIRouter(prefix="/product",tags=['product'])

@router.post("/createproduct",response_model=ProductResponse,status_code=status.HTTP_201_CREATED)
def createproduct(product:ProductCreate,db:Session=Depends(get_db)):
    service=Productservice(db)
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return service.createproduct(product,db)

@router.get("/getallproduct",response_model=List[ProductResponse],status_code=status.HTTP_200_OK)
def getallproduct(db:Session=Depends(get_db)):
    service=Productservice(db)
    return service.getallproduct(db)

@router.get("/getproductbyId/{product_id}",response_model=ProductResponse,status_code=status.HTTP_200_OK)
def getproductbyId(product_id:int,db:Session=Depends(get_db)):
    service=Productservice(db)
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return service.getproductbyId(product_id,db)

@router.put("/updatedproduct",response_model=ProductResponse)
def updatedproduct(product:ProductBase,product_id:int,db:Session=Depends(get_db)):
    service=Productservice(db)
    if not product_id or product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return service.updatedproduct(product,product_id,db)

@router.delete("/deleteproduct")
def deleteproduct(product_id:int,db:Session=Depends(get_db)):
    service=Productservice(db)
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return service.deleteproduct(product_id,db)
