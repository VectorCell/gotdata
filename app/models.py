from __init__ import app
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.dialects import postgresql

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
db = SQLAlchemy(app)

class Character(db.Model):
    __tablename__ = "characters"

    # Table attributes
    id          = db.Column(db.Integer, primary_key=True)
    url         = db.Column(db.String(256))
    name        = db.Column(db.String(256))
    gender      = db.Column(db.String(256))
    culture     = db.Column(db.String(256))
    birth_date  = db.Column(db.String(256))
    death_date  = db.Column(db.String(256))
    father      = db.Column(db.String(256))
    mother      = db.Column(db.String(256))
    spouse      = db.Column(db.String(256))

    # Foreign keys
    house_id    = db.Column(db.Integer, db.ForeignKey("houses.id"))
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))
 
    # Relationships 
    house       = db.relationship("House", backref=db.backref("characters",
                                                             lazy="dynamic"))
    location    = db.relationship("Location", backref=db.backref("characters",
                                                              lazy="dynamic"))
    
    def __init__(self, url="", name="", gender="", culture="", birth_date="",
                 death_date="", father="", mother="", spouse="", 
                 house=None, location=None):

        self.url = url
        self.name = name
        self.gender = gender
        self.culture = culture
        self.birth_date = birth_date
        self.death_date = death_date
        self.father = father
        self.mother = mother
        self.spouse = spouse
        self.house = house
        self.location = location

    def __repr__(self):
        return "<Character %r>" % self.name

class House(db.Model):
    __tablename__ = "houses"

    # Table attributes
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256))
    name = db.Column(db.String(256))
    coat_of_arms = db.Column(db.String(256))
    words = db.Column(db.String(256))
    founded = db.Column(db.String(256))
    founder = db.Column(db.String(256))
    died_out = db.Column(db.String(256))

    # Foreign keys
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))

    # Relationships
    location = db.relationship("Location", backref=db.backref("houses",
                                                            lazy="dynamic"))

    def __init__(self, url="", name="", coat_of_arms="", words="", founded="",
                 founder="", died_out="", location=None):

        self.url = url
        self.name = name
        self.coat_of_arms = coat_of_arms
        self.words = words
        self.founded = founded
        self.founder = founder
        self.died_out = died_out
        self.location = location

    def __repr__(self):
        return "<House %r>" % self.name

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

    # Foreign keys
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"))

    # Relationships
    location = db.relationship("Location", backref=db.backref("events",
                                                            lazy="dynamic"))

    def __init__(self, name="", date="", location=None):
        self.name = name
        self.date = date
        self.location = location

    def __repr__(self):
        return "<Event %r>" % self.name

class Location(db.Model):
    __tablename__ = "locations"

    # Table attributes
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    seat = db.Column(db.String(256))
    seat_type = db.Column(db.String(256))
    religion = db.Column(db.String(256))
    population = db.Column(db.String(256))
    size = db.Column(db.String(256))

    def __init__(self, name="", seat="", seat_type="", religion="",
                 population="", size=""):

        self.name = name
        self.seat = seat
        self.seat_type = seat_type
        self.religion = religion
        self.population = population
        self.size = size

    def __repr__(self):
        return "<Location %r>" % self.name
