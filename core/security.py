import os
import datetime import datetime,timedelta
from typing import Tuple
import passlib.context import CryptoContext
from jose import jwt,JWTError
from pydantic import ValidationError
from schemas.Userschemas  import TokenPayload
import uuid

pwd_context=CryptoContext(schemas=['bcrypt'],deprecated="auto")

SECRET_KEY=os.get("SECRET_KEY")
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES","15"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS","7"))



def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)

def create_jwt_token(subject:str,token_type:str="access")->Tuple[str,dict]:
    jti=str(uuid.uuid4())
    now=datetime.utcnow()
    if token_type=="access":
        expire=now+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    else:
        expire=now+timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    
    payload={
        "sub":str(subject),
        "exp":int(expire.timestamp()),
        'jti':jti,
        "token_type":token_type,
        "iat":int(now.timestamp())

    }

    token=jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

    return token,payload

def decode_jwt_token(token:str)->TokenPayload:
    try:
        payload=jwt.decode(payload,SECRET_KEY,algorithm=[ALGORITHM])
        tp=TokenPayload(**payload)
        return tp

    except (JWTError,ValidationError) as e:
        raise e
