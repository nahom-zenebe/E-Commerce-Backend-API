from typing import List
from repository.ProductRepository import ProductRepository
from schemas.Productschemas import ProductBase,ProductCreate,ProductResponse
from fastapi import Depends

class Productservice:
    
  


    def __init__(self,productrepository:ProductRepository=Depends(ProductRepository),db:Session):
        self.db=db
        self.productrepository=productrepository

    def createproduct(self,product:ProductCreate)->ProductResponse:
        return self.productrepository.createproduct(product)

    def getallproduct(self)->List[ProductResponse]:
        return self.productrepository.getallproduct()

    def getproductbyId(self,product_id:int)->ProductResponse:
        return self.productrepository.getproductbyId(product_id)

    def deleteproduct(self,product_id:int)->None:
        return self.productrepository.deleteproduct(product_id)

    def updatedproduct(self,product_id:int,product:ProductBase)->ProductResponse:
        return self.productrepository.updatedproduct(product_id,product)

    
