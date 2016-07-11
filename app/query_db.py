from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table

from __init__ import app
from models import db, Character, House, Book


engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
metadata = MetaData(bind=engine)


def get_all_characters():
    return Character.query.all()

def get_all_houses():
    return House.query.all()

def get_all_books():
    return Book.query.all()

def get_character(id):
    return Character.query.get(id)

def get_house(id):
    return House.query.get(id)

def get_book(id):
    return Book.query.get(id)
