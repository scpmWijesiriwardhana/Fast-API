from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# username/password@host:port/database_name
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# to connect to the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# to talk to the database we need session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# to create base class
Base = declarative_base()

# to get the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',              password='chamath123', cursor_factory=RealDictCursor)

#         cursor = conn.cursor()
#         print("Database Connection was successfull")
#         break
#     except Exception as error:
#         print("cnnecting to database failed")
#         print(error)
#         time.sleep(2)