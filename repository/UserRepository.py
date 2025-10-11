from typing import List, Optional
from sqlalchemy.orm import Session, lazyload
from fastapi import Depends
from models.Categorymodel import Category
from config.database import get_db
from sqlalchemy.orm import Session, lazyload
from models.Usermodel import  RevokedToken,User



class UserRepository:
    def __init__(self,db:Session):
        self.db=db

    def get_by_email(self,email:str)->Optional[User]:
        return self.db.query(User).filter(User.email==email).first()

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self,user:User)->User:
        user=User(**user)
        self.db.commit(user)
        self.db.refresh(user)
        return user
    def revoke_token(self,jti:str,token_type:str):
        rt=RevokedToken(jti=jti,token_type=token_type)
        self.db.add(rt)
        self.db.commit()
        self.db.refresh(rt)
        return rt

    def is_jti_revoked(self,jti:str)->bool:
        return self.db.query(RevokedToken).filter(RevokedToken.jti==jti).first() is not None

