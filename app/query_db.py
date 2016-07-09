from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table

from __init__ import app
from models import db, Character, House, Book


engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
metadata = MetaData(bind=engine)


def get_all_characters():
    return Table('characters', metadata, autoload=True).select(True).execute()

def get_all_houses():
    return Table('houses', metadata, autoload=True).select(True).execute()

