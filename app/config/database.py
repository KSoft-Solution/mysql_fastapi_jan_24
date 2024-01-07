from sqlalchemy import create_engine,MetaData
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import settings

SQLALCHEMY_DATABASE_URL = f"mysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()
Base = declarative_base()


if not database_exists(engine.url):
    create_database(engine.url)
else:
    # Connect to database if exists, returns connection object.
    e = engine.connect()
    # create a metadata object for table.
    meta = MetaData()
    # This commits the table to database.
    meta.create_all(e)

 # Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()