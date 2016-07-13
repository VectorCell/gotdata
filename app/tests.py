#!/usr/bin/env python

from unittest import main

from flask import Flask
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy

from models import db, Character, House, Book


class TestGOTData(TestCase):

    # -----------
    # Set up the db
    # -----------

    SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/unittest.db"

    def create_app(self):
        app = Flask(__name__)
        app.config["Testing"] = True
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # -----------
    # Character table tests
    # -----------

    def test_get_character(self):
        a_character = Character(id="1", name="A character")
        db.session.add(a_character)
        db.session.commit()

        self.assertEqual(repr(Character.query.get("1")),
                         "<Character u'A character'>")

    def test_get_allegiances(self):
        a_house = House(id="2", name="A house")
        a_character = Character(id="3", name="A character")
        a_character.allegiances.append(a_house)
        db.session.add(a_character)
        db.session.add(a_house)
        db.session.commit()
        
        h = House.query.get("2")
        c = Character.query.get("3")
        self.assertEqual(c.allegiances[0], h)

    def test_get_spouse(self):
        husband = Character(id="4", name="A character")
        wife = Character(id="5", name="Another character")
        husband.spouse = wife
        db.session.add(husband)
        db.session.add(wife)
        db.session.commit()

        h = Character.query.get("4")
        w = Character.query.get("5")
        self.assertEqual(h.spouse, w)

    # -----------
    # House table tests
    # -----------

    def test_get_house(self):
        a_house = House(id="6", name="A house")
        db.session.add(a_house)
        db.session.commit()

        self.assertEqual(repr(House.query.get("6")),
                         "<House u'A house'>")

    def test_get_swornmembers(self):
        a_house = House(id="7", name="A house")
        a_character = Character(id="8", name="A character")
        a_house.swornMembers.append(a_character)
        db.session.add(a_character)
        db.session.add(a_house)
        db.session.commit()
        
        h = House.query.get("7")
        c = Character.query.get("8")
        self.assertEqual(h.swornMembers[0], c)

    def test_get_currentlord(self):
        a_house = House(id="9", name="A house")
        a_character = Character(id="10", name="A character")
        a_house.currentLord = a_character
        db.session.add(a_house)
        db.session.add(a_character)
        db.session.commit()

        h = House.query.get("9")
        c = Character.query.get("10")
        self.assertEqual(h.currentLord, c)

    # -----------
    # Book table tests
    # -----------

    def test_get_book(self):
        a_book = Book(id="11", name="A book")
        db.session.add(a_book)
        db.session.commit()

        self.assertEqual(repr(Book.query.get("11")),
                         "<Book u'A book'>")

    def test_get_characters(self):
        a_book = Book(id="12", name="A book")
        a_character = Character(id="13", name="A character")
        a_book.characters.append(a_character)
        db.session.add(a_character)
        db.session.add(a_book)
        db.session.commit()
        
        b = Book.query.get("12")
        c = Character.query.get("13")
        self.assertEqual(b.characters[0], c)

    def test_get_povcharacters(self):
        a_book = Book(id="14", name="A book")
        a_character = Character(id="15", name="A character")
        a_book.povCharacters.append(a_character)
        db.session.add(a_character)
        db.session.add(a_book)
        db.session.commit()
        
        b = Book.query.get("14")
        c = Character.query.get("15")
        self.assertEqual(b.povCharacters[0], c)

# -----------
# Main
# -----------

if __name__ == "__main__":
    main()
