from fastapi import FastAPI 

app=FastAPI( title="E-commerce",
           description="E-commerce backend app",
           version="1.0.0"
           docs_url="/",
           redoc_url="/redoc")





@app.get("/")
def main():
    return {"message":"welcomme to this project"}