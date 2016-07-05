#!/usr/bin/env python

from unittest import main

from flask import Flask
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy

from models import db, Character, House, Event, Location


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

    def test_get_characters_one(self):
        a_character = Character(name="A character")
        db.session.add(a_character)
        db.session.commit()
        self.assertEqual(repr(Character.query.all()),
                            "[<Character u'A character'>]")

    def test_get_characters_two(self):
        character_a = Character(name="Character_A")
        character_b = Character(name="Character_B")
        db.session.add(character_a)
        db.session.add(character_b)
        db.session.commit()
        self.assertEqual(repr(Character.query.all()),
                            "[<Character u'Character_A'>,"
                             " <Character u'Character_B'>]")

    def test_get_characters_three(self):
        character_a = Character(name="Character_A")
        character_b = Character(name="Character_B")
        character_c = Character(name="Character_C")
        db.session.add(character_a)
        db.session.add(character_b)
        db.session.add(character_c)
        db.session.commit()
        self.assertEqual(repr(Character.query.all()),
                            "[<Character u'Character_A'>,"
                             " <Character u'Character_B'>,"
                             " <Character u'Character_C'>]")

    # -----------
    # House table tests
    # -----------

    def test_get_houses_one(self):
        a_house = House(name="A house")
        db.session.add(a_house)
        db.session.commit()
        self.assertEqual(repr(House.query.all()),
                            "[<House u'A house'>]")

    def test_get_houses_two(self):
        house_a = House(name="House_A")
        house_b = House(name="House_B")
        db.session.add(house_a)
        db.session.add(house_b)
        db.session.commit()
        self.assertEqual(repr(House.query.all()),
                            "[<House u'House_A'>, <House u'House_B'>]")

    def test_get_house_characters(self):
        a_house = House(name="A house")
        jeff = Character(name="Jeff", house=a_house)
        kyle = Character(name="Kyle", house=a_house)
        db.session.add(a_house)
        db.session.add(jeff)
        db.session.add(kyle)
        db.session.commit()
        self.assertEqual(repr(a_house.characters.all()),
                         "[<Character u'Jeff'>, <Character u'Kyle'>]")

    # -----------
    # Location table tests
    # -----------

    def test_get_locations(self):
        a_location = Location(name="A location")
        db.session.add(a_location)
        db.session.commit()
        self.assertEqual(repr(Location.query.all()),
                            "[<Location u'A location'>]")

    def test_get_location_characters(self):
        a_location = Location(name="A location")
        jeff = Character(name="Jeff", location=a_location)
        kyle = Character(name="Kyle", location=a_location)
        db.session.add(a_location)
        db.session.add(jeff)
        db.session.add(kyle)
        db.session.commit()
        self.assertEqual(repr(a_location.characters.all()),
                         "[<Character u'Jeff'>, <Character u'Kyle'>]")

    def test_get_location_houses(self):
        a_location = Location(name="A location")
        house_a = House(name="House_A", location=a_location)
        house_b = House(name="House_B", location=a_location)
        db.session.add(a_location)
        db.session.add(house_a)
        db.session.add(house_b)
        db.session.commit()
        self.assertEqual(repr(a_location.houses.all()),
                         "[<House u'House_A'>, <House u'House_B'>]")

    def test_get_location_events(self):
        a_location = Location(name="A location")
        event_a = Event(name="Event_A", location=a_location)
        event_b = Event(name="Event_B", location=a_location)
        db.session.add(a_location)
        db.session.add(event_a)
        db.session.add(event_b)
        db.session.commit()
        self.assertEqual(repr(a_location.events.all()),
                        "[<Event u'Event_A'>, <Event u'Event_B'>]") 

    # -----------
    # Event table tests
    # -----------

    def test_get_events_one(self):
        a_event = Event(name="A event")
        db.session.add(a_event)
        db.session.commit()
        self.assertEqual(repr(Event.query.all()),
                            "[<Event u'A event'>]")

    def test_get_events_two(self):
        event_a = Event(name="Event_A")
        event_b = Event(name="Event_B")
        db.session.add(event_a)
        db.session.add(event_b)
        db.session.commit()
        self.assertEqual(repr(Event.query.all()),
                            "[<Event u'Event_A'>,"
                             " <Event u'Event_B'>]")

    def test_get_events_three(self):
        event_a = Event(name="Event_A")
        event_b = Event(name="Event_B")
        event_c = Event(name="Event_C")
        db.session.add(event_a)
        db.session.add(event_b)
        db.session.add(event_c)
        db.session.commit()
        self.assertEqual(repr(Event.query.all()),
                            "[<Event u'Event_A'>,"
                             " <Event u'Event_B'>,"
                             " <Event u'Event_C'>]")

# -----------
# Main
# -----------

if __name__ == "__main__":
    main()
