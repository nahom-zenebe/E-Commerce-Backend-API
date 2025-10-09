from typing import List, Optional
from sqlalchemy.orm import Session, lazyload
from fastapi import Depends
from models.Productmodel import Product
from config.database import get_db



class Product:
    def __init__(self,db:Session=Depends(get_db)):
        self.db=db

    def createproduct(self,product:Product)->Product:
        self.db.add(product)
        self.db.commmit()
        self.db.refresh()
        return product

    def getallproduct(self)->List[Product]:
        return self.db(Category).all()

    def getproductbyId(self,product_id:int)->Product:
        return self.db(Product).filter(Product.id==product_id).first()

    def deleteprodcut(self,product_id:int)->None:
        deletedproduct=self.db(Product).filter(Product.id==product_id).first()
        if deletedproduct:
            self.db.delete(deletedproduct)
            self.db.commit()
            self.db.refresh(deletedproduct)

    def updatedproduct(self,product_id:int,product:Product)->Product:
        updatedproduct=self.db(Product).filter(Product.id==product_id)

        if updatedproduct:
            updatedproduct.name=product.name
            updatedproduct.description=product.description
            updatedproduct.price=product.price
            updatedproduct.quantity=product.quantity
            self.db.commit()
            self.db.refresh(updatedproduct)
            return updatedproduct

