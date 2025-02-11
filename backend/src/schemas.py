from pydantic import BaseModel

class Measurement(BaseModel):
    place: str
    temp: float