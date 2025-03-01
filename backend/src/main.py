from fastapi import FastAPI, Depends
import requests, os
from dotenv import load_dotenv
from src.schemas import MeasurementS
from src.db import engine,init_db, get_db
from src.models import Measurement, Base
from sqlalchemy.orm import Session
from sqlalchemy import select
load_dotenv()


#It creates new tables on startup if there are any but doesnt update the exsisting ones
#Alembic should be used for version control and modyfing exsisting ones and adding rest
#works good in testing but its better to use alembic
#init_db(Base)

#get_db in dependency takes care of connecting to database and creating session

app = FastAPI()
#cd into backend#
#uvicorn src.main:app --reload --host 0.0.0.0 --port 8000# run in backend

#@app.get(weather)
#@app.post(weather)
#background task ^

async def get_weather():
    API_KEY = os.environ.get('weather_api_1') or "laalalala"
    weather = requests.get(f"https://api.weatherapi.com/v1/current.json?q=Ozarow%20Mazowiecki&key={API_KEY}")
    weather = weather.json()
    #print(weather)
    place = weather["location"]["name"]
    temp = weather["current"]["temp_c"]

    return {"place":place,"temp":temp}




@app.get("/")
async def root():
    return{"message":"Welcome to weather comparison app"}

@app.post("/post")
async def measurement_Save(meas:MeasurementS, db: Session = Depends(get_db)):
    #pomiar = Measurement(temp_sensor=temp_sensor)
    print(meas.temp_sensor)
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


#Test for artificially added entry in the db
@app.get("/recent_temp")
async def measurement_from_sensor(db: Session = Depends(get_db)):
    statement = select(Measurement) 
    pomiar = db.scalars(statement).first()
    return(pomiar)

