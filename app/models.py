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
   
    # Relationships
    # lord = db.relationship("House", uselist=False, backref="lord")

    def __init__(self, url="", name="", gender="", culture="", birth_date="",
                 death_date="", father="", mother="", spouse="", 
                 house_id=None, location_id=None):

        self.url = url
        self.name = name
        self.gender = gender
        self.culture = culture
        self.birth_date = birth_date
        self.death_date = death_date
        self.father = father
        self.mother = mother
        self.spouse = spouse
        self.house_id = house_id
        self.location_id = location_id


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
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
    # lord_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    # heir_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    # overlord_id = db.Column(db.Integer, db.ForeignKey("characters.id"))

    # Relationships
    characters_at = db.relationship("Character", backref="house", 
                                          lazy="dynamic")

    def __init__(self, url="", name="", coat_of_arms="", words="", founded="",
                 founder="", died_out="", location_id=None):

        self.url = url
        self.name = name
        self.coat_of_arms = coat_of_arms
        self.words = words
        self.founded = founded
        self.founder = founder
        self.died_out = died_out
        self.location_id = location_id


# Many-to-many table for events and houses involved
events_houses = db.Table("events_houses",
            db.Column("event_id", db.Integer, db.ForeignKey("events.id")),
            db.Column("house_id", db.Integer, db.ForeignKey("houses.id"))
)


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

    # Relationships
    houses_involved = db.relationship("House", secondary=events_houses,
                                      backref="events")

    def __init__(self, name="", date="", location_id=None):
        self.name = name
        self.date = date
        self.location_id = location_id

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

    # Relationships
    characters_at = db.relationship("Character", backref="location",
                                    lazy="dynamic")
    houses_at = db.relationship("House", backref="location",
                                lazy="dynamic")
    events_at = db.relationship("Event", backref="location",
                                lazy="dynamic")

    def __init__(self, name="", seat="", seat_type="", religion="",
                 population="", size=""):

        self.name = name
        self.seat = seat
        self.seat_type = seat_type
        self.religion = religion
        self.population = population
        self.size = size
