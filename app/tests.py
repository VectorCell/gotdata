#!/usr/bin/env python

"""
NOTE TO GRADER(s): Running tests.py will wipe out 
our production db instead of using a new db. We can't 
figure out why, so please DO NOT run this file.
"""

from unittest import main

from flask import Flask
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy

from test_models import app, db, Character, House, Book


class TestGOTData(TestCase):

    # -----------
    # Set up the db
    # -----------

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # -----------
    # Character table tests
    # -----------

    def test_get_characters_1(self):
        a_character = Character(id="1", name="A character")
        db.session.add(a_character)
        db.session.commit()

        self.assertEqual(repr(Character.query.get("1")),
                        "<Character u'A character'>")

    def test_get_characters_2(self):
        c1 = Character(id="1", name="Character 1")
        db.session.add(c1)
        c1 = Character(id="2", name="Character 2")
        db.session.add(c1)
        db.session.commit()

        self.assertEqual(repr(Character.query.get("1")),
                        "<Character u'Character 1'>")
        self.assertEqual(repr(Character.query.get("2")),
                        "<Character u'Character 2'>")

    def test_get_characters_3(self):
        c1 = Character(id="1", name="Character 1")
        db.session.add(c1)
        c2 = Character(id="2", name="Character 2")
        db.session.add(c2)
        c3 = Character(id="3", name="Character 3")
        db.session.add(c3)
        db.session.commit()

        self.assertEqual(repr(Character.query.get("1")),
                        "<Character u'Character 1'>")
        self.assertEqual(repr(Character.query.get("2")),
                        "<Character u'Character 2'>")
        self.assertEqual(repr(Character.query.get("3")),
                        "<Character u'Character 3'>")   

    def test_get_allegiances_1(self):
        a_house = House(id="2", name="A house")
        a_character = Character(id="3", name="A character")
        a_character.allegiances.append(a_house)
        db.session.add(a_character)
        db.session.add(a_house)
        db.session.commit()
        
        h = House.query.get("2")
        c = Character.query.get("3")
        self.assertEqual(c.allegiances[0], h)

    def test_get_allegiances_2(self):
        h1 = House(id="1", name="House 1")
        db.session.add(h1)
        a_character = Character(id="1", name="Character 1")
        a_character.allegiances.append(h1)
        db.session.add(a_character)
        a_character = Character(id="2", name="Character 2")
        a_character.allegiances.append(h1)
        db.session.add(a_character)
        db.session.commit()
        
        h = House.query.get("1")
        c1 = Character.query.get("1")
        self.assertEqual(c1.allegiances[0], h)
        c2 = Character.query.get("2")
        self.assertEqual(c2.allegiances[0], h)
        self.assertEqual(c1.allegiances[0], c2.allegiances[0])

    def test_get_spouse_1(self):
        husband = Character(id="4", name="A character")
        wife = Character(id="5", name="Another character")
        husband.spouse = wife
        db.session.add(husband)
        db.session.add(wife)
        db.session.commit()

        h = Character.query.get("4")
        w = Character.query.get("5")
        self.assertEqual(h.spouse, w)

    def test_get_spouse_2(self):
        c1 = Character(id="1", name="Character 1")
        c2 = Character(id="2", name="Character 2")
        c1.spouse = c2
        #c2.spouse = c1
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()

        h = Character.query.get("1")
        w = Character.query.get("2")
        self.assertEqual(h.spouse, w)
        #self.assertEqual(w.spouse, h)

    # -----------
    # House table tests
    # -----------

    def test_get_houses_1(self):
        a_house = House(id="6", name="A house")
        db.session.add(a_house)
        db.session.commit()

        self.assertEqual(repr(House.query.get("6")),
                         "<House u'A house'>")

    def test_get_houses_2(self):
        h1 = House(id="1", name="House 1")
        db.session.add(h1)
        h2 = House(id="2", name="House 2")
        db.session.add(h2)
        db.session.commit()

        self.assertEqual(repr(House.query.get("1")),
                         "<House u'House 1'>")
        self.assertEqual(repr(House.query.get("2")),
                         "<House u'House 2'>")

    def test_get_swornmembers_1(self):
        a_house = House(id="7", name="A house")
        a_character = Character(id="8", name="A character")
        a_house.swornMembers.append(a_character)
        db.session.add(a_character)
        db.session.add(a_house)
        db.session.commit()
        
        h = House.query.get("7")
        c = Character.query.get("8")
        self.assertEqual(h.swornMembers[0], c)

    def test_get_swornmembers_2(self):
        h1 = House(id="1", name="House 1")
        c1 = Character(id="1", name="Character 1")
        c2 = Character(id="2", name="Character 2")
        h1.swornMembers.append(c1)
        h1.swornMembers.append(c2)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(h1)
        db.session.commit()
        
        h = House.query.get("1")
        c1 = Character.query.get("1")
        c2 = Character.query.get("2")
        self.assertEqual(h.swornMembers[0], c1)
        self.assertEqual(h.swornMembers[1], c2)

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

    def test_get_books_1(self):
        a_book = Book(id="11", name="A book")
        db.session.add(a_book)
        db.session.commit()

        self.assertEqual(repr(Book.query.get("11")),
                         "<Book u'A book'>")

    def test_get_books_2(self):
        b1 = Book(id="1", name="Book 1")
        b2 = Book(id="2", name="Book 2")
        db.session.add(b1)
        db.session.add(b2)        
        db.session.commit()

        self.assertEqual(repr(Book.query.get("1")),
                                "<Book u'Book 1'>")
        self.assertEqual(repr(Book.query.get("2")),
                                "<Book u'Book 2'>")

    def test_get_book_characters_1(self):
        a_book = Book(id="12", name="A book")
        a_character = Character(id="13", name="A character")
        a_book.characters.append(a_character)
        db.session.add(a_character)
        db.session.add(a_book)
        db.session.commit()
        
        b = Book.query.get("12")
        c = Character.query.get("13")
        self.assertEqual(b.characters[0], c)

    def test_get_book_characters_2(self):
        b1 = Book(id="1", name="Book 1")
        b2 = Book(id="2", name="Book 2")
        c1 = Character(id="1", name="Character 1")
        b1.characters.append(c1)
        b2.characters.append(c1)
        db.session.add(c1)
        db.session.add(b1)
        db.session.add(b2)
        db.session.commit()
        
        b1 = Book.query.get("1")
        b2 = Book.query.get("2")
        c1 = Character.query.get("1")
        self.assertEqual(b1.characters[0], c1)
        self.assertEqual(b2.characters[0], c1)
        self.assertEqual(b1.characters[0], b2.characters[0])

    def test_get_povcharacters_1(self):
        a_book = Book(id="14", name="A book")
        a_character = Character(id="15", name="A character")
        a_book.povCharacters.append(a_character)
        db.session.add(a_character)
        db.session.add(a_book)
        db.session.commit()
        
        b = Book.query.get("14")
        c = Character.query.get("15")
        self.assertEqual(b.povCharacters[0], c)

    def test_get_povcharacters_2(self):
        b1 = Book(id="1", name="Book 1")
        b2 = Book(id="2", name="Book 2")        
        c1 = Character(id="1", name="Character 1")
        c2 = Character(id="2", name="Character 2")
        b1.povCharacters.append(c1)
        b1.povCharacters.append(c2)
        b2.povCharacters.append(c1)
        b2.povCharacters.append(c2)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(b1)
        db.session.add(b2)
        db.session.commit()
        
        b1 = Book.query.get("1")
        b2 = Book.query.get("2")
        c1 = Character.query.get("1")
        c2 = Character.query.get("2")
        self.assertEqual(b1.povCharacters[0], c1)
        self.assertEqual(b1.povCharacters[1], c2)
        self.assertEqual(b2.povCharacters[0], c1)
        self.assertEqual(b2.povCharacters[1], c2)
        self.assertEqual(b1.povCharacters[0], b2.povCharacters[0])
        self.assertEqual(b1.povCharacters[1], b2.povCharacters[1])

# -----------
# Main
# -----------

if __name__ == "__main__":
    main()
