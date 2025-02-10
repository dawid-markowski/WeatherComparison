from fastapi import FastAPI
import requests, os
from dotenv import load_dotenv
from backend import models
from backend.db import engine
load_dotenv()


models.Base.metadata.create_all(engine)
app = FastAPI()
#uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000# run in parent dir




@app.get("/")
async def root():
    return{"message":"Welcome to weather comparison app"}

@app.post("/post")
async def measurement_Save(meas:models.Measurement):
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

