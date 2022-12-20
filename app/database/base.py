import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DB_URL = os.getenv("DB_URL", "")

Base = declarative_base()

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
