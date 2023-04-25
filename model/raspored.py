from . import Base
from model.predmet import Predmet
from model.nastavnik import Nastavnik
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Raspored(Base):
    __tablename__ = "raspored"
    ID_rasporeda = Column(Integer, primary_key=True)
    dan = Column(Date)
    pocetak = Column(DateTime)
    kraj = Column(DateTime)
    
    predmet = relationship("Predmet", back_populates="sati")
    nastavnik = relationship("Nastavnik", back_populates="sati")