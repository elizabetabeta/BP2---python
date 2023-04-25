from . import Base
from model.razred import Ucenik
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Izostanak(Base):
    __tablename__ = "izostanak"
    ID_izostanka = Column(Integer, primary_key=True)
    datum = Column(Date)
    opis = Column(Text)
    opravdano = Column(Boolean)
    
    ucenik = relationship("Ucenik", back_populates="izostanci")