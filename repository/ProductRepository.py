# from typing import List, Optional
# from sqlalchemy.orm import Session, lazyload
# from fastapi import Depends
# from models.Productmodel import Product
# from config.database import get_db



# class Product:
#     def __init__(self,db:Session=Depends(get_db)):
#         self.db=db

#     def createproduct(self,product:Product)->Product:
#         self.db.add(product)
#         self.db.commmit()
#         self.db.refresh()
#         return product

#     def getallproduct
