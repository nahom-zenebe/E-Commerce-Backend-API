from typing import List, Optional
from sqlalchemy.orm import Session, lazyload
from fastapi import Depends
from models.Categorymodel import Category
from config.database import get_db


class CategoryRepository:
    def __init__(self,db:Session=Depends(get_db)):
        self.db=db

    def createCategory(self,category:Category)-> Category:
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)
        return category

    def getallcategory(self)->List[Category]:
        return self.db.query(Category).all()

    def deletecategory(self,category_id:int)->None:
        deletedcategory=self.db.query(Category).filter(Category.id==category_id).first()
        if deletedcategory:
            self.db.delete(deletedcategory)
            self.db.commit()
            self.db.refresh(deletedcategory)
            
    def getcategorybyId(self,category_id:int)->Category:
        return self.db.query(Category).filter(Category.id==category_id).first()


    def updatedcategory(self,category_id:int,category:Category)-> Category:
        updatedcategory=self.db.query(Category).filter(Category.id==category_id)
        if updatedcategory:
            updatedcategory.name=category.name
            updatedcategory.description=category.description
            self.db.commit()
            self.db.refresh(updatedcategory)
            return updatedcategory


