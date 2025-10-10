
from fastapi import FastAPI,HTTPException,status,APIRouter
from session.orm import Session
from config.database  import get_db
from schemas.Category import CategoryCreate,CategoryResponse,CategoryBase
from service.Categoryservice import Categoryservice
from fastapi import Depends



router=APIRouter(prefix="/category",tags=['Category'])




@app.post("/createcategory",status_code=status.HTTP_201_CREATED,response_model=CategoryRepository)
def createcategory(category:CategoryCreate,db:Session=Depends(get_db)):
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")

    return Categoryservice.createcategory(category,db)
    

@app.get("/getcategory",status_code=status.HTTP_201_CREATED,response_model=List[CategoryResponse])
def getallcategory(category:createCategory,db:Session=Depends(get_db)):
    return Categoryservice.getallcategory(db)

@app.delete("/deletecategory/{category_id}")
def deletecategory(category_id:int, db:Session=Depends(get_db)):
    return Categoryservice.deletecategory(category_id,db)

@app.put("/updatecategory/{category_id}")
def updatedcategory(category_id:int, category:CategoryBase, db:Session=Depends(get_db)):
    return Categoryservice.updatedcategory(category_id, category, db)

@app.put("/getcategorybyId/{category_id}")
def getcategorybyId(category_id:int, db:Session=Depends(get_db)):
    return Categoryservice.getcategorybyId(category_id, db)