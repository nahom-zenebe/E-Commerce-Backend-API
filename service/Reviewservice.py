from typing import List
from repository.ReviewRepository import ReviewRepository  
from fastapi import Depends,status,HTTPException
from schemas.ReviewSchema import ReviewCreate,ReviewResponse,ReviewBase
from sqlalchemy.orm import Session, lazyload


class Reviewservice:
    def __init__(self,db:Session):
        self.db=db
        self.reviewrepository=ReviewRepository(self.db)

    def createReview(self,review:ReviewCreate)->ReviewResponse:
        return self.reviewrepository.creeatereview(review)

    def getallreview(self)->List[ReviewResponse]:
        return self.reviewrepository.getallreview()

    def getallreviewbyId(self,review_id:int)->ReviewResponse:
        return self.reviewrepository.getsinglereviewbyId(review_id)

    def deletereview(self, review_id:int)->None:
        return self.reviewrepository.deletereview(review_id)

    def updatedreview(self,review_id:int,review_id:ReviewBase)->ReviewResponse:
        return self.reviewrepository.updatedreview(review_id,review_id)


