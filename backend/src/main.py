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


@app.get("/")
async def root():
    return{"message":"Welcome to weather comparison app"}

#Save sensor and api temperature to db
@app.post("/measurement")
async def measurement_Save(meas:MeasurementS, db: Session = Depends(get_db)):
    API_KEY = os.environ.get('weather_api_1') or "laalalala"
    weather = requests.get(f"https://api.weatherapi.com/v1/current.json?q={meas.place}&key={API_KEY}")#trzeba zrobic tak aby place z sensora bylo wstawione w request
    weather = weather.json()
    #print(weather)
    place_api = weather["location"]["name"]
    temp_api = weather["current"]["temp_c"]
    pomiar = Measurement(place=place_api,temp_sensor=meas.temp_sensor,temp_api=temp_api)
    db.add(pomiar)
    db.commit()

    return{"message":"Measurements added correctly"}


#Access sensor and api temperature
@app.get("/measurement")
async def measurement_from_sensor(db: Session = Depends(get_db)):
    statement = select(Measurement).order_by(Measurement.id.desc())
    pomiar = db.scalars(statement).first()

    return(pomiar)

