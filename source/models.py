from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
fom db import Base

class Pokemon(Base):
    __tablename__ ='pokemons'
    ide = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at =Column(DateTime, default=func.now())