
from fastapi import FastAPI,HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from config.database  import get_db
from schemas.Categoryschemas import CategoryCreate,CategoryResponse,CategoryBase
from service.Categoryservice import Categoryservice
from fastapi import Depends
from typing import List



router=APIRouter(prefix="/category",tags=['category'])




@router.post("/createcategory",status_code=status.HTTP_201_CREATED,response_model=CategoryResponse)
def createcategory(category:CategoryCreate,db:Session=Depends(get_db)):
    service=Categoryservice(db)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return service.createcategory(category,db)
    

@router.get("/getcategory",status_code=status.HTTP_200_OK,response_model=List[CategoryResponse])
def getallcategory(db:Session=Depends(get_db)):
    service=Categoryservice(db)
    return service.getallcategory(db)

@router.delete("/deletecategory/{category_id}")
def deletecategory(category_id:int, db:Session=Depends(get_db)):
    service=Categoryservice(db)
    if category_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return  service.deletecategory(category_id,db)

@router.put("/updatecategory/{category_id}")
def updatedcategory(category_id:int, category:CategoryBase, db:Session=Depends(get_db)):
    service=Categoryservice(db)
    if category or category_id is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return service.updatedcategory(category_id, category, db)

@router.get("/getcategorybyId/{category_id}")
def getcategorybyId(category_id:int, db:Session=Depends(get_db)):
    service=Categoryservice(db)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return  service.getcategorybyId(category_id, db)