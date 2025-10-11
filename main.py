from fastapi import FastAPI 
import uvicorn
from router.Productrouter import router as product_router
from router.Userrouter import router as auth_router
from router.Categoryrouter import router as category_router
app=FastAPI( title="E-commerce",
           description="E-commerce backend app",
           version="1.0.0",
           docs_url="/",
           redoc_url="/redoc")


app.include_router(category_router)
app.include_router(product_router)
app.include_router(auth_router)


@app.get("/")
def main():
    return {"message":"welcomme to this project"}


if __name__=='__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=5000,reload=True)