from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///weater_database.db", echo=True)



if __name__ == "__main__":
    print("beton")
    #dodac kod na zapelnienie bazy danych w celach obejrzenia fronta i wytestowania apki bez sensora