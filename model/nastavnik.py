from . import Base
from model.raspored import Raspored
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Nastavnik(Base):
    __tablename__ = "nastavnik"
    ID_nastavnika = Column(Integer, primary_key=True)
    ime = Column(String(25))
    prezime = Column(String(25))
    email = Column(String(100))
    titula = Column(String(20))

    sati = relationship("Raspored", back_populates="nastavnici")

