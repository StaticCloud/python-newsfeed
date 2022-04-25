from os import getenv
# allows us to map the models to mysql tables
from sqlalchemy.ext.declarative import declarative_base
# engine manages connection to db
from sqlalchemy import create_engine
# generates temp connections for performing CRUD operations
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# load our .env file if it exists
load_dotenv()

engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()