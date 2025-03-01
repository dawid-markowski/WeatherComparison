from pydantic import BaseModel

class MeasurementS(BaseModel):
    place: str
    temp_sensor: float
    temp_api: float