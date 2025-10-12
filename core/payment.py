import os
import json
from fastapi import FastAPI,response,Request,HTTPException
from dotenv import load_dotenv
from pathlib import Path


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)
app = FastAPI()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")




@app.get("/checkout")
async def create_checkout_session(price:int=10):
    checkout_session=stripe.checkout.Session.create(
        line_items=[
            {
                "price_data":{
                    "currency":"usd",
                    "product_data":{
                        "name":"Fastapi stripe checkout"
                    },
                    "unit_amount":price*100

                    
                },
                "quantity":1

            }
        ],
        metadata={
            "user_id": 3,
            "email": "abc@gmail.com",
            "request_id": 1234567890
        },
         mode="payment",
        success_url=os.getenv("BASE_URL") + "/success/",
        cancel_url=os.getenv("BASE_URL") + "/cancel/",
        customer_email="ping@fastapitutorial.com",

    )

    return responses.RedirectResponse(checkout_session.url, status_code=303)




@app.post("/webbook")
async def stripe_webhook(request:Request):
    