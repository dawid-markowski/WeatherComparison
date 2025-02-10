from pydantic import BaseModel
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float


class Measurement(BaseModel):
    place: str
    temp: float

Base = declarative_base()

class Measurement_db(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True)
    place = Column(String)
    temp = Column(Float)