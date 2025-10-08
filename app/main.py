from fastapi import FastAPI 
import uvicorn

app=FastAPI( title="E-commerce",
           description="E-commerce backend app",
           version="1.0.0",
           docs_url="/",
           redoc_url="/redoc")





@app.get("/")
def main():
    return {"message":"welcomme to this project"}


if __name__=='__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=5000,reload=True)