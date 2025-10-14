from typing import List, Optional
from sqlalchemy.orm import Session, lazyload
from fastapi import Depends
from models.Reviewmodel import Review
from config.database import get_db





class ReviewRepository:
    def __init__(self,db:Session):
        self.db=db
    
    def creeatereview(self,review:Review)->Review:
        self.db.add(review)
        self.db.commit()
        self.db.refresh(review)
        return review

    def getallreview(self)->List[Review]:
        return  self.db.query(Review).all()


    def getsinglereviewbyId(self,review_id:int)->Review:
        return  self.db.query(Review).filter(Review.id==review_id).first()


    def deletereview(self,review_id:int)->None:
        deleted_item=self.db.query(Review).filter(Review.id==review_id).first()
        if deleted_item:
            self.db.delete(deleted_item)
            self.db.commit()
            self.db.refresh(deleted_item)
            return deleted_item


    def updatedreview(self,review:Review,review_id:int)->Review:
        updated_item=self.db.query(Review).filter(Review.id==review_id).first()
        if updated_item:
            update_item.rating=review.rating
            update_item.comment=review.comment

            self.db.commit()
            self.db.refresh(updated_item)
            return update_item

