from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table

import models

def get_all_characters():
    return models.Character.query.all()

def get_all_houses():
    return models.House.query.all()

def get_all_books():
    return models.Book.query.all()


def get_character(id):
    return models.Character.query.get(str(id))

def get_house(id):
    return models.House.query.get(str(id))

def get_book(id):
    return models.Book.query.get(str(id))


def get_character_dict(id):
    d = {}
    char = get_character(id)
    d['id'] = id;
    d['name'] = char.name
    d['gender'] = char.gender
    d['culture'] = char.culture
    d['born'] = char.born
    d['died'] = char.died
    if char.spouse is not None:
        d['spouse'] = int(char.spouse.id)
    d['allegiances'] = [int(h.id) for h in char.allegiances]
    d['books'] = [int(b.id) for b in char.books]
    d['povBooks'] = [int(b.id) for b in char.povBooks]
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
    if house.currentLord is not None:
        d['currentLord'] = int(house.currentLord.id)
    if house.heir is not None:
        d['heir'] = int(house.heir.id)
    if house.overlord is not None:
        d['overlord'] = int(house.overlord.id)
    if house.founder is not None:
        d['founder'] = int(house.founder.id)
    d['swornMembers'] = [int(p.id) for p in house.swornMembers]
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
