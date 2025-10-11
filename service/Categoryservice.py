from typing import List
from repository.CategoryRepository import CategoryRepository
from fastapi import Depends
from schemas.Categoryschemas import CategoryBase,CategoryCreate,CategoryResponse
from sqlalchemy.orm import Session, lazyload

class Categoryservice:

    def __init__(self,db:Session):
        self.db=db
        self.categoryrepository=categoryrepository

    def createcategory(self,category:CategoryCreate)->CategoryResponse:
        return self.categoryrepository.createCategory(category)

    def getallcategory(self):
        return self.categoryrepository.getallcategory()

    def getcategorybyId(self,category_id:int)->CategoryResponse:
        return self.categoryrepository.getcategorybyId(category_id)

    def deletecategory(self, category_id:int)->None:
        return self.categoryrepository.deletecategory(category_id)

    def updatedcategory(self, category_id:int, category:CategoryBase)->CategoryResponse:
        return self.categoryrepository.updatedcategory(category_id,category)
