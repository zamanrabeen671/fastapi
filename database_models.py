from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
Base = declarative_base()

class Product(Base):
    
    __tablename__ = "prodduct"
    id =  Column(Integer, primary_key=True, index=True) # type: ignore
    name = Column(String) # type: ignore
    description = Column(String) #type: ignore
    price = Column(Float) # type: ignore
    quantity= Column(String) # type: ignore