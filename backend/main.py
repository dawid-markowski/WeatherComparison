from fastapi import FastAPI
from pydantic import BaseModel

class Measurement(BaseModel):
    place: str
    temp: float

app = FastAPI()


@app.get("/")
async def root():
    return{"message":"Welcome to weather comparison app"}

@app.post("/post")
async def Measurement_Save(meas:Measurement):
    print(meas)
    return{"message":"Measurements added correctly"}


