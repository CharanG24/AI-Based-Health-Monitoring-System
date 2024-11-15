from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'mysql+pymysql://user:password@localhost/health_db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class PatientData(Base):
    __tablename__ = 'patient_data'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    heart_rate = Column(Float)
    temperature = Column(Float)
    blood_pressure = Column(Float)
    anomaly = Column(Integer)

def init_db():
    Base.metadata.create_all(engine)
