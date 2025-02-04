from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

class Measurement(BaseModel):
    place: str
    temp: float

app = FastAPI()
load_dotenv()

@app.get("/")
async def root():
    return{"message":"Welcome to weather comparison app"}

@app.post("/post")
async def measurement_Save(meas:Measurement):
    print(meas)
    return{"message":"Measurements added correctly"}


@app.get("/get_weather")
async def measurement_from_api():
    API_KEY = os.environ.get('weather_api_1') or "laalalala"
    weather = requests.get(f"https://api.weatherapi.com/v1/current.json?q=Ozarow%20Mazowiecki&key={API_KEY}")
    weather = weather.json()
    place = weather["location"]["name"]
    temp = weather["current"]["temp_c"]

    return {"place":place,"temp":temp}

