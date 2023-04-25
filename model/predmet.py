from . import Base
from model.raspored import Raspored
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Predmet(Base):
    __tablename__ = "predmet"
    ID_predmeta = Column(Integer, primary_key=True)
    naziv = Column(String(75))
    opis = Column(Text)

    sati = relationship("Raspored", back_populates="predmet")
