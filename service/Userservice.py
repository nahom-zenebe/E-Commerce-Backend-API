from typing import List
from repository.UserRepository import UserRepository 
from fastapi import Depends,status,HTTPException
from schemas.Userschemas import UserBase,UserCreate,UserResponse
from core.security import get_password_hash,verify_password,create_jwt_token,decode_jwt_token



class AuthService:
    def __init__(self,db:Session):
        self.db=db
        self.userrepository=UserRepository

    def signup(self,user:UserCreate):
        exisiting=self.userrepository.get_by_email(user.email)
        if exisiting:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered")
        hashed_password=get_password_hash(user.hashed_password)
        user=self.userrepository.create_user(**user)
        return user

    def authenticate(self,user:UserCreate):
        user=self.userrepository.get_by_email(email)
        if not user or not verify_password(user.password,user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        return user

    def create_token_for_user(self,user_id:int):
        access_token, access_payload = create_jwt_token(subject=user_id, token_type="access")
        refresh_token, refresh_payload = create_jwt_token(subject=user_id, token_type="refresh")
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "access_payload": access_payload,
            "refresh_payload": refresh_payload
        }

    def revoke_token_by_jti(self,jti:str,token_type:str):
        return self.userrepository.revoke_token(jti=jti,token_type=token_type)

    def is_token_revoked(self,jti:str)->bool:
        return self.userrepository.is_jti_revoked(jti)

    
    def decode_and_verify(self, token: str, expected_type: str):
        try:
            payload = decode_jwt_token(token)
        except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        if payload.token_type != expected_type:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
        if self.is_token_revoked(payload.jti):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has been revoked")
        return payload




    