from fastapi import FastAPI,HTTPException,status,APIRouter
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.Reviewschemas import ReviewBase,ReviewCreate,ReviewResponse
from service.Reviewservice import Reviewservice
from fastapi import Depends
from typing import List



router=APIRouter(prefix="/review",tags=['review'])



@router.post("/createreview",response_model=ReviewResponse,status_code=status.HTTP_201_CREATED)
def createReview(review:ReviewCreate,db:Session=Depends(get_db)):
    service=Reviewservice(db)

    try:
        created_review=service.createReview(review)
        return created_review

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get('/getallreview',response_model=List[ReviewResponse],status_code=status.HTTP_200_OK)
def getallreview(db:Session=Depends(get_db)):
    service=Reviewservice(db)
    try:
        return service.getallreview()

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/getreviewbyId",response_model=List[ReviewResponse], status_code=status.HTTP_200_OK)
def getreviewbyId(review_id:int, db:Session=Depends(get_db)):
    service=Reviewservice(db)

    try:
        review=service.getallreviewbyId(review_id)
        return review

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.delete("/deletereview", status_code=status.HTTP_204_NO_CONTENT)
def deletereview(review_id:int, db:Session=Depends(get_db)):
    service=Reviewservice(db)

    try:
        service.deletereview(review_id)
        return {"message": "Review deleted successfully"}

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))



@router.put("/updatereview", response_model=ReviewResponse, status_code=status.HTTP_200_OK)
def updatedreview(review_id:int, review:ReviewBase, db:Session=Depends(get_db)):
    service=Reviewservice(db)

    try:
        updated_review=service.updatedreview(review_id, review)
        return updated_review

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

