from sqlalchemy import create_engine

engine = create_engine("sqlite+pysqlite:///weater_database.db", echo=True)