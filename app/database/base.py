import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

load_dotenv()

engine = create_engine(os.getenv("DB_URL", ""))
Session = sessionmaker(bind=engine)
