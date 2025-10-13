import stripe
from repository.PaymentRepository import PaymentRepository
from repository.OrderRepository import OrderRepository
from sqlalchemy.orm import Session



stripe.api_key="api key"

class PaymentService:
    def __init__(self,db:Session):
        self.paymentrepository=PaymentRepository(self.db)


    def create_payment_intent(self,order_id:int):
        order=self.OrderRepository.getorderbyId(order_id)

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

    def handle_webhook_payment(self,stripe_event:dict):
        event_type = stripe_event["type"]
        data = stripe_event["data"]["object"]
        if event_type="payment_intent.succeeded":
            payment = self.payment_repo.db.query(Payment).filter(
            Payment.stripe_payment_id == data["id"]
            ).first()
            if payment:
                payment.status = "succeeded"
                self.payment_repo.db.commit()
