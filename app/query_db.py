from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table

from sqlalchemy_searchable import parse_search_query
from sqlalchemy_searchable import search
from sqlalchemy.orm import sessionmaker

from models import db, Character, House, Book


def search_db(query):
    results = []
    results += search_books(query)
    results += search_houses(query)
    results += search_characters(query)
    return results


def search_books(query):
    results = []
    for item in Book.query.whoosh_search(query).all():
        results += [{'type': 'Book', 'data': item}]
    return results


def search_houses(query):
    results = []
    for item in House.query.whoosh_search(query).all():
        results += [{'type': 'House', 'data': item}]
    return results


def search_characters(query):
    results = []
    for item in Character.query.whoosh_search(query).all():
        results += [{'type': 'Character', 'data': item}]
    return results


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
    d['id'] = id
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
    d['id'] = id
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
