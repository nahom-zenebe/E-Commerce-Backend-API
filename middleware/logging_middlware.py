import logger 
from fastapi import FastAPI,Request
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self,request:Request,call_next):
        client_ip=request.client.host
        client_method=request.method
        url=request.url.path
        client_agent=request.headers.get("user-agent")
        logger.info(f"IP:{client_ip} Method:{client_method} URL:{url} Agent:{client_agent}")


        response=await call_next(request)
        status_code=response.status_code
        logger.info(f"Status Code:{status_code}")

        return response
