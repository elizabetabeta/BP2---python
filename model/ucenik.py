from . import Base
from model.razred import Razred
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Ucenik(Base):
    __tablename__ = "ucenik"
    ID_ucenika = Column(Integer, primary_key=True)
    ime = Column(String(50))
    prezime = Column(String(50))
    
    razred = relationship("Razred", back_populates="ucenici")
    izostanak = relationship("Izostanak", back_populates="ucenici")