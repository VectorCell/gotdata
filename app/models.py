from __init__ import app
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects import postgresql

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)

class Character(db.Model):
    __tablename__ = "characters"

    # Table attributes
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256))
    name = db.Column(db.String(256))
    gender = db.Column(db.String(256))
    culture = db.Column(db.String(256))
    birth_date = db.Column(db.String(256))
    death_date = db.Column(db.String(256))
    # titles = db.Column(postgresql.ARRAY(db.String))
    # aliases = db.Column(postgresql.ARRAY(db.String))
    father = db.Column(db.String(256))
    mother = db.Column(db.String(256))
    spouse = db.Column(db.String(256))
    # allegiances = db.Column(postgresql.ARRAY(db.String))
    # books = db.Column(postgresql.ARRAY(db.String))
    # pov_books = db.Column(postgresql.ARRAY(db.String))
    # tv_series = db.Column(postgresql.ARRAY(db.String))
    # played_by = db.Column(postgresql.ARRAY(db.String))

    # Foreign keys
    house_id = db.Column(db.Integer, db.ForeignKey("houses.id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    
class House(db.Model):
    __tablename__ = "houses"

    # Table attributes
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256))
    name = db.Column(db.String(256))
    coat_of_arms = db.Column(db.String(256))
    words = db.Column(db.String(256))
    # titles = db.Column(postgresql.ARRAY(db.String))
    # seats = db.Column(postgresql.ARRAY(db.String))
    founded = db.Column(db.String(256))
    founder = db.Column(db.String(256))
    died_out = db.Column(db.String(256))
    # ancestral_weapons = db.Column(postgresql.ARRAY(db.String))
    # cadet_branches = db.Column(postgresql.ARRAY(db.String))
    # sworn_members = db.Column(postgresql.ARRAY(db.String))

    # Foreign keys
    region_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    lord_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    heir_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    overlord_id = db.Column(db.Integer, db.ForeignKey("characters.id"))

class Event(db.Model):
    __tablename__ = "events"

    # Table attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    date = db.Column(db.String(256))
    # result = db.Column(postgresql.ARRAY(String))
    # combatant_1 = db.Column(postgresql.ARRAY(String))
    # combatant_2 = db.Column(postgresql.ARRAY(String))
    # commander_1 = db.Column(postgresql.ARRAY(String))
    # commander_2 = db.Column(postgresql.ARRAY(String))
    # casualties_1 = db.Column(postgresql.ARRAY(String))
    # casualties_2 = db.Column(postgresql.ARRAY(String))

    # Foreign keys
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))

class Location(db.Model):
    __tablename__ = "locations"

    # Table attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    # sub_locations = db.Column(postgresql.ARRAY(db.String))
    seat = db.Column(db.String(256))
    seat_type = db.Column(db.String(256))
    religion = db.Column(db.String(256))
    population = db.Column(db.String(256))
    size = db.Column(db.String(256))
    # events = db.Column(postgresql.ARRAY(db.String))
