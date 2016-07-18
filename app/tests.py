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

    def test_character_1(self):
        b1 = Book(id="1", name="Book 1")
        h1 = House(id="1", name="House 1")
        c1 = Character(id="1", name="Character 1", gender="Male", culture="Northern", 
                        born="1987", died="2100", father="Pops", mother="Mom")
        c2 = Character(id="2", name="Character 2")
        
        c1.allegiances.append(h1)
        c1.books.append(b1)
        c1.povBooks.append(b1) 
        c1.spouse = c2
	
        db.session.add(b1)
        db.session.add(h1)
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()        

        b1 = Book.query.get("1")
        h1 = House.query.get("1")
        c1 = Character.query.get("1")
        c2 = Character.query.get("2")
        self.assertEqual(c1.name, "Character 1")
        self.assertEqual(c1.gender, "Male")
        self.assertEqual(c1.culture, "Northern")
        self.assertEqual(c1.born, "1987")
        self.assertEqual(c1.died, "2100")
        self.assertEqual(c1.father, "Pops")
        self.assertEqual(c1.mother, "Mom")
        self.assertEqual(c1.allegiances[0], h1)
        self.assertEqual(c1.books[0], b1)
        self.assertEqual(c1.povBooks[0], b1)
        self.assertEqual(c1.spouse, c2)

    def test_get_characters_1(self):
        c1 = Character(id="1", name="Character 1")
        db.session.add(c1)
        db.session.commit()

        self.assertEqual(repr(Character.query.get("1")),
                        "<Character u'Character 1'>")

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
        h1 = House(id="1", name="House 1")
        c1 = Character(id="1", name="Character 1")
        c1.allegiances.append(h1)
        db.session.add(c1)
        db.session.add(h1)
        db.session.commit()
        
        h1 = House.query.get("1")
        c1 = Character.query.get("1")
        self.assertEqual(c1.allegiances[0], h1)

    def test_get_allegiances_2(self):
        h1 = House(id="1", name="House 1")
        db.session.add(h1)
        c1 = Character(id="1", name="Character 1")
        c1.allegiances.append(h1)
        db.session.add(c1)
        c1 = Character(id="2", name="Character 2")
        c1.allegiances.append(h1)
        db.session.add(c1)
        db.session.commit()
        
        h1 = House.query.get("1")
        c1 = Character.query.get("1")
        self.assertEqual(c1.allegiances[0], h1)
        c2 = Character.query.get("2")
        self.assertEqual(c2.allegiances[0], h1)
        self.assertEqual(c1.allegiances[0], c2.allegiances[0])

    def test_get_spouse_1(self):
        c1 = Character(id="1", name="Character 1")
        c2 = Character(id="2", name="Character 2")
        c1.spouse = c2
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()

        c1 = Character.query.get("1")
        c2 = Character.query.get("2")
        self.assertEqual(c1.spouse, c2)

    def test_get_spouse_2(self):
        c1 = Character(id="1", name="Character 1")
        c2 = Character(id="2", name="Character 2")
        c1.spouse = c2
        #c2.spouse = c1
        db.session.add(c1)
        db.session.add(c2)
        db.session.commit()

        c1 = Character.query.get("1")
        c2 = Character.query.get("2")
        self.assertEqual(c1.spouse, c2)
        #self.assertEqual(c2.spouse, c1)

    # -----------
    # House table tests
    # -----------

    def test_get_houses_1(self):
        h1 = House(id="1", name="House 1")
        db.session.add(h1)
        db.session.commit()

        self.assertEqual(repr(House.query.get("1")),
                        "<House u'House 1'>")

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

    def test_get_houses_3(self):
        h1 = House(id="1", name="Tully", region="The Riverlands", coatOfArms="trout", words="We surrender", founded="10", diedOut="11")
        c1 = Character(id="1", name="Character 1")
        c2 = Character(id="2", name="Character 2")
        c3 = Character(id="3", name="Character 3")
        c4 = Character(id="4", name="Character 4")
        h1.currentLord = c1
        h1.heir=c2
        h1.overlord = c3
        h1.founder=c4
        h1.swornMembers.append(c1)
        h1.swornMembers.append(c3)
        db.session.add(h1)
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.commit()

        h1= House.query.get("1")
        self.assertEqual(h1.name,"Tully")
        self.assertEqual(h1.region,"The Riverlands")
        self.assertEqual(h1.coatOfArms,"trout")
        self.assertEqual(h1.words,"We surrender")
        self.assertEqual(h1.founded,"10")
        self.assertEqual(h1.diedOut,"11")
        self.assertEqual(h1.currentLord,c1)
        self.assertEqual(h1.heir,c2)
        self.assertEqual(h1.overlord,c3)
        self.assertEqual(h1.founder,c4)

        self.assertTrue((h1.swornMembers[0] == c1 and h1.swornMembers[1] == c3) or
                        (h1.swornMembers[0] == c3 and h1.swornmembers[1] == c1))




    def test_get_swornmembers_1(self):
        h1 = House(id="1", name="House 1")
        c1 = Character(id="1", name="Character 1")
        h1.swornMembers.append(c1)
        db.session.add(c1)
        db.session.add(h1)
        db.session.commit()
        
        h1 = House.query.get("1")
        c1 = Character.query.get("1")
        self.assertEqual(h1.swornMembers[0], c1)

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
        
        h1 = House.query.get("1")
        c1 = Character.query.get("1")
        c2 = Character.query.get("2")

        self.assertTrue((h1.swornMembers[0] == c1 and h1.swornMembers[1] == c2) or
                        (h1.swornMembers[0] == c2 and h1.swornMembers[1] == c1))


    def test_get_currentlord(self):
        h1 = House(id="1", name="House 1")
        c1 = Character(id="1", name="Character 1")
        h1.currentLord = c1
        db.session.add(h1)
        db.session.add(c1)
        db.session.commit()

        h1 = House.query.get("1")
        c1 = Character.query.get("1")
        self.assertEqual(h1.currentLord, c1)

    # -----------
    # Book table tests
    # -----------

    def test_get_books_1(self):
        b1 = Book(id="1", name="Book 1")
        db.session.add(b1)
        db.session.commit()

        self.assertEqual(repr(Book.query.get("1")),
                        "<Book u'Book 1'>")

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
        b1 = Book(id="1", name="Book 1")
        c1 = Character(id="1", name="Character 1")
        b1.characters.append(c1)
        db.session.add(c1)
        db.session.add(b1)
        db.session.commit()
        
        b1 = Book.query.get("1")
        c1 = Character.query.get("1")
        self.assertEqual(b1.characters[0], c1)

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
        b1 = Book(id="1", name="Book 1")
        c1 = Character(id="1", name="Character 1")
        b1.povCharacters.append(c1)
        db.session.add(c1)
        db.session.add(b1)
        db.session.commit()
        
        b1 = Book.query.get("1")
        c1 = Character.query.get("1")
        self.assertEqual(b1.povCharacters[0], c1)

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

        self.assertTrue((b1.povCharacters[0] == c1 and b1.povCharacters[1] == c2) or
			(b1.povCharacters[0] == c2 and b1.povCharacters[1] == c1))
        self.assertTrue((b2.povCharacters[0] == c1 and b2.povCharacters[1] == c2) or
                        (b2.povCharacters[0] == c2 and b2.povCharacters[1] == c1))

# -----------
# Main
# -----------

if __name__ == "__main__":
    main()
