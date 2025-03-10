from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func

Base = declarative_base()
metadata = Base.metadata

class Measurement(Base):
    __tablename__ = "measurements"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=func.now())
    place = Column(String)
    temp_sensor = Column(Float)
    temp_api = Column(Float)

    def __repr__(self):
        return(f"<Measurement(id={self.id},date={self.date},place={self.place},temp_sensor={self.temp_sensor},temp_api={self.temp_api})>")


