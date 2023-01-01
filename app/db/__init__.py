from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
Session = sessionmaker(bind=engine)
Base = declarative_base()

def init_db(app):
    Base.metadata.create_all(engine)

    # run this whenever a context is destroyed
    app.teardown_appcontext(close_db)

def get_db():
    if 'db' not in g:
        g.db = Session()

    return Session()

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()