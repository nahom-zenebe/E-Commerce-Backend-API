
from fastapi import FastAPI,Request,HTTPException,status,APIRouter,BackgroundTasks, Depends
from sqlalchemy.orm import Session
from config.database  import get_db
from schemas.Paymentschemas import PaymentCreate,PaymentResponse,PaymentBase
from service.Paymentservice import PaymentService
from fastapi import Depends
from typing import List



router=APIRouter(prefix='/payments',tags=['payments'])


@router.get("/create/{order_id}")
def createpayment(order_id:int,db:Session=Depends(get_db)):
    service=PaymentService(db)

    try:
        client_secret=service.create_payment_intent(order_id)
        return {"client_secret": client_secret}

    except ValueError as e:
        raise HTTPException(status_code=400,detail=str(e))


@router.post('/webhook')
async def stripe_webhook(request:Request,db:Session=Depends(get_db)):
    payload=await request.body()
    sig_header=request.headers.get("strripe-signature")

    endpoint_secret="this is secret kyu"

    try:
        event=stripe.webbook.construct_event(
            payload,sig_header,endpoint_secret
        )

    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    service = PaymentService(db)
    service.handle_webhook_payment(event)
    return {"status": "success"}

@router.post("/confirm")
async def confirm_payment(payment_data:dict,background_tasks:BackgroundTasks,service=PaymentService=Depends()):
    return await service.confirm_payment(payment_data,background_tasks)
    