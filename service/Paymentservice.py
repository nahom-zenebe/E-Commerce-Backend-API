import stripe
from repository.PaymentRepository import PaymentRepository
from core.message import send_payment_email
from sqlalchemy.orm import Session

from fastapi import BackgroundTasks

stripe.api_key="api key"

class PaymentService:
    def __init__(self,db:Session,stripe_client):
        self.paymentrepository=PaymentRepository(self.db)
        self.stripe = stripe_client


    def create_payment_intent(self,order_id:int):
        order=self.paymentrepository.getorderbyId(order_id)

        if not order:
            raise ValueError("Payment already exists for this order")


        intent=stripe.PaymentIntent.create(
            amount=int(order.total_amount*100),
            currency="usd",
            metadata={"order_id":order_id}

        )
        payment=self.paymentrepository.create_payment(
            order_id=order.id,
            stripe_payment_id=intent["id"],
            amount=order.total_amount,
            status="pending"
        )
        return intent.client_secret
    
    def confirm_payment(self,payment_data,background_tasks:BackgroundTasks):
        payment_intent=self.stripe.PaymentIntent.retrieve(payment_data["id"])
        if payment_intent.status=="succeeded":
            payment=self.paymentrepository.get_payment_by_order(payment_data["metadata"]["order_id"])
            payment.status="succeeded"
            self.paymentrepository.db.commit()
            background_tasks.add_task(send_payment_email, payment.user.email, payment.order_id, payment.amount)
            return {"status":"success"}



        
    def handle_webhook_payment(self,stripe_event:dict):
        event_type = stripe_event["type"]
        data = stripe_event["data"]["object"]
        if event_type=="payment_intent.succeeded":
            payment = self.payment_repo.db.query(Payment).filter(
            Payment.stripe_payment_id == data["id"]
            ).first()
            if payment:
                payment.status = "succeeded"
                self.payment_repo.db.commit()
