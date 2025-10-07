from sqlalchemy import Integer,String,Column,DateTime,func
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
    password_hash=Column(String,nullable=False)
    phone_number=Column(String,nullable=False)
    address=Column(String,nullable=False)
    role=Column(Enum(Role),default=Role.ADMIN,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
    updated_at=Column(DateTime(timezone=True),server_default=func.now())
    