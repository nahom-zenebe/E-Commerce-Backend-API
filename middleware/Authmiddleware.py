from fastapi import FastAPI, Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware



class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request,call_next):
        token=request.headers.get("") 
        if not token:
            raise HTTPException(status_code=401,detail="UnAuthorized")

        response=await call_next(request)
        return response