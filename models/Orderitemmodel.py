
from sqlalchemy import Integer,String,Column,DateTime,ForeignKey,Enum
from  sqlalchemy.orm import relationship
from  config.database import Base
import enum
from  sqlalchemy import func


class OrderItem:
    __tablename__='orderitem'

    id=Column(Integer,primary_key=True,nullable=False)
    order_id=Column(Integer,ForeignKey("order.id"),nullable=False)
    product_id=Column(Integer,ForeignKey("product.id"),nullable=False)
    quantity=Column(Integer,nullable=False)
    