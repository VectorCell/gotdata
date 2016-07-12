from flask import jsonify
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
    return Character.query.get(str(id))

def get_house(id):
    return House.query.get(str(id))

def get_book(id):
    return Book.query.get(str(id))


def get_character_dict(id):
    d = {}
    char = get_character(id)
    d['id'] = id;
    d['name'] = char.name
    d['gender'] = char.gender
    d['culture'] = char.culture
    d['born'] = char.born
    d['died'] = char.died
    d['spouse'] = char.spouse.split("/").pop() # char.spouse
    d['allegiances'] = [h.id for h in char.allegiances]
    d['books'] = [b.id for b in char.books]
    d['povBooks'] = [b.id for b in char.povBooks]
    return d

def get_house_dict(id):
    d = {}
    house = get_house(id)
    d['id'] = id;
    d['name'] = house.name
    d['region'] = house.region
    d['coatOfArms'] = house.coatOfArms
    d['founded'] = house.founded
    d['diedOut'] = house.diedOut
    d['currentLord'] = house.currentLord.id
    d['heir'] = house.heir.id
    d['overlord'] = house.overlord.id
    d['founder'] = house.founder.id
    d['swornMembers'] = [p.id for p in house.swornMembers]
    return d

def get_book_dict(id):
    d = {}
    book = get_book(id)
    d['id'] = id
    d['name'] = book.name
    d['isbn'] = book.isbn
    d['numberOfPages'] = book.numberOfPages
    d['publisher'] = book.publisher
    d['country'] = book.country
    d['mediaType'] = book.mediaType
    d['released'] = book.released
    return d


def get_character_json(id):
    return jsonify(get_character_dict(id))

def get_house_json(id):
    return jsonify(get_house_dict(id))

def get_book_json(id):
    return jsonify(get_book_dict(id))
