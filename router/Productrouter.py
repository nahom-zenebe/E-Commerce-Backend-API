from fastapi import FastAPI,HTTPException,status,APIRouter
from session.orm import Session
from config.database import get_db
from schemas.Product import ProductCreate,ProductResponse,ProductBase
from service.Productservice import Productservice
from fastapi import Depends
from typing import List




router=APIRouter(prefix="/product",tags=['product'])





@app.post("/createproduct",response_model=ProductResponse,status_code=status.HTTP_201_CREATED)
def createproduct(product:ProductCreate,db:Session=Depends(get_db)):
    if product is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Productservice.createproduct(product,db)

@app.get("/getallproduct",response_model=List[ProductResponse],status_code=status.HTTP_200_OK)
def getallproduct(db:Session=Depends(get_db)):
    return Productservice.getallproduct(db)

@app.get("/getproductbyId/{product_id}",response_model=ProductResponse,status_code=status.HTTP_200_OK)
def getproductbyId(product_id:int,db:Session=Depends(get_db)):
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Productservice.getproductbyId(product_id,db)

@app.put("/updatedproduct",response_model=ProductResponse)
def updatedproduct(product:ProductBase,product_id:int,db:Session=Depends(get_db)):
    if not product_id or product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Productservice.updatedproduct(product,product_id,db)

@app.delete("/deleteproduct")
def deleteproduct(product_id:int,db:Session=Depends(get_db)):
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return Productservice.deleteproduct(product_id,db)
