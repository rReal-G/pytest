# from typing import Counter
# from sqlalchemy import Column, Integer, Float, String, null
# from sqlalchemy.orm import DeclarativeBase

# from test2 import Product


# class Base(DeclarativeBase):
#     pass

# class ProductORM(Base):
#     __tablename__ = 'products'
#     prodId = Column(Integer, primary_key=True, nullable=False)
#     prodName = Column(String(6), unique=True)
#     price = Column(Float)
#     #stock = Column(Integer)


# orm_instance = ProductORM(prodId=1, prodName='top g', price=555)
# print(repr(orm_instance))
# pydantic_instance = Product.model_validate(orm_instance, from_attributes=True)
# print(repr(pydantic_instance))
# print(repr(pydantic_instance.model_dump_json()))
# print(pydantic_instance.model_dump()['prodName'])