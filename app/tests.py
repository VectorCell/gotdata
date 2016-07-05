#!/usr/bin/env python

from unittest import main

from flask import Flask
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy

from models import db, Character, House, Event, Location


class TestGOTData(TestCase):

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


if __name__ == "__main__":
    main()
