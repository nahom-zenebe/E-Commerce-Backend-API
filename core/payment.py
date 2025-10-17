import os
from pathlib import Path
from fastapi import FastAPI, Response, Request, HTTPException
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
import stripe

# Load environment variables
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
BASE_URL = os.getenv("BASE_URL")

# Initialize Stripe
stripe.api_key = STRIPE_SECRET_KEY

app = FastAPI()


@app.get("/checkout")
async def create_checkout_session(price: int = 10):
    """
    Creates a Stripe Checkout session.
    """
    checkout_session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {"name": "FastAPI Stripe Checkout"},
                    "unit_amount": price * 100,  # Stripe expects cents
                },
                "quantity": 1,
            }
        ],
        metadata={
            "user_id": 3,
            "email": "abc@gmail.com",
            "request_id": 1234567890
        },
        mode="payment",
        success_url=f"{BASE_URL}/success/",
        cancel_url=f"{BASE_URL}/cancel/",
        customer_email="ping@fastapitutorial.com",
    )

    return RedirectResponse(checkout_session.url, status_code=303)


@app.post("/webhook")
async def stripe_webhook(request: Request):
    """
    Stripe webhook to handle events like checkout.session.completed
    """
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        # Invalid payload
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Handle the event
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        print(f"Payment successful for session: {session['id']}")
        print(f"Metadata: {session.get('metadata')}")

        # You can save session info to your database here

    return {"status": "success"}
