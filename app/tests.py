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


if __name__ == "__main__":
    main()
