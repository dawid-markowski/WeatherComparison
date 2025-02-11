from fastapi import FastAPI
import requests, os
from dotenv import load_dotenv
from src.schemas import Measurement as MeasurementS
from src.db import engine
from src.models import MeasurementM, Base
load_dotenv()


Base.metadata.create_all(engine)
app = FastAPI()
#cd into backend#
#uvicorn src.main:app --reload --host 0.0.0.0 --port 8000# run in backend




@app.get("/")
async def root():
    return{"message":"Welcome to weather comparison app"}

@app.post("/post")
async def measurement_Save(meas:MeasurementS):
    print(meas)
    return{"message":"Measurements added correctly"}


@app.get("/get_weather")
async def measurement_from_api():
    API_KEY = os.environ.get('weather_api_1') or "laalalala"
    weather = requests.get(f"https://api.weatherapi.com/v1/current.json?q=Ozarow%20Mazowiecki&key={API_KEY}")
    weather = weather.json()
    #print(weather)
    place = weather["location"]["name"]
    temp = weather["current"]["temp_c"]

    return {"place":place,"temp":temp}

