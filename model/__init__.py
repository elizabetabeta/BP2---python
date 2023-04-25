from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("mysql://root:lozinka@localhost:6306/ednevnik", echo=True)
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

Base.metadata.create_all()