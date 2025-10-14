from fastapi import FastAPI,Request
import uvicorn
from router.Productrouter import router as product_router
from router.Userrouter import router as auth_router
from router.Categoryrouter import router as category_router
from router.Paymentrouter import router as payment_router
from router.Orderrouter import router as order_router
import logging
from middleware.logging_middleware import LoggingMiddleware
from middleware.AuthMiddleware import AuthMiddleware

app=FastAPI( title="E-commerce",
           description="E-commerce backend app",
           version="1.0.0",
           docs_url="/",
           redoc_url="/redoc")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


logger = logging.getLogger(__name__)

app.add_middleware(LoggingMiddleware)

app.include_router(auth_router)
app.add_middleware(AuthMiddleware)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(payment_router)
app.include_router(order_router)


@app.get("/")
def main():
    return {"message":"welcomme to this project"}


if __name__=='__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=5000,reload=True)