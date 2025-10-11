from sqlalchemy import Integer,String,Column,DateTime,func,Enum
from sqlalchemy.orm import  relationship
from config.database import Base
import enum

class Role(enum.Enum):
    ADMIN="admin"
    USER="user"
    SELLER="seller"


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,nullable=False,index=True)
    email=Column(String,primary_key=True,index=True)
    hashed_password=Column(String,nullable=False)
    phone_number=Column(String,nullable=False)
    address=Column(String,nullable=False)
    role=Column(Enum(Role),default=Role.USER,nullable=False)
    order=relationship("Order",back_populates="users", cascade="all, delete-orphan")
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now())
    

class RevokedToken(Base):
    __tablename__="revoked_tokens"
    id=Column(Integer,primary_key=True,index=True)
    jti=Column(String(225),unique=True,nullable=False,index=True)
    token_type=Column(String(20),nullable=False) #access or refresh token
    revoked_at=Column(DateTime(timezone=True),server_default=func.now())

