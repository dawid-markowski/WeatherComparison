from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine("sqlite+pysqlite:///weater_database.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

def init_db(base_model):
    base_model.metadata.create_all(engine)
    

def get_db():
    db = SessionLocal()
    try:
        yield db  
    finally:
        db.close()  

if __name__ == "__main__":
    print("beton")
    #dodac kod na zapelnienie bazy danych w celach obejrzenia fronta i wytestowania apki bez sensora