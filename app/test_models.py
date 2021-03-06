from flask import Flask
from flask_sqlalchemy import SQLAlchemy

SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/default.db"
SQLALCHEMY_BINDS = {
    "test": "postgresql://austin:ahh10523@localhost/test",
}

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

"""
Many-to-many association tables
"""
characters_houses = db.Table("characters_houses",
                             db.Column("character_id", db.String(
                                 512), db.ForeignKey("characters.id")),
                             db.Column("house_id", db.String(
                                 512), db.ForeignKey("houses.id")),
                             info={"bind_key": "test"})

characters_books = db.Table("characters_books",
                            db.Column("character_id", db.String(
                                      512), db.ForeignKey("characters.id")),
                            db.Column("book_id", db.String(
                                512), db.ForeignKey("books.id")),
                            info={"bind_key": "test"})

characters_povbooks = db.Table("characters_povbooks",
                               db.Column("character_id", db.String(
                                         512), db.ForeignKey("characters.id")),
                               db.Column("book_id", db.String(
                                   512), db.ForeignKey("books.id")),
                               info={"bind_key": "test"})


"""
Characters table model
"""


class Character(db.Model):
    __bind_key__ = "test"
    __tablename__ = "characters"

    # Table attributes
    id = db.Column(db.String(512), primary_key=True)
    name = db.Column(db.String(512))
    gender = db.Column(db.String(512))
    culture = db.Column(db.String(512))
    born = db.Column(db.String(512))
    died = db.Column(db.String(512))
    father = db.Column(db.String(512))
    mother = db.Column(db.String(512))

    # Foreign keys
    spouse_id = db.Column(db.String(512), db.ForeignKey("characters.id"))

    # Relationships
    spouse = db.relationship("Character", remote_side=[id])
    allegiances = db.relationship("House", secondary=characters_houses,
                                  back_populates="swornMembers")
    books = db.relationship("Book", secondary=characters_books,
                            back_populates="characters")
    povBooks = db.relationship("Book", secondary=characters_povbooks,
                               back_populates="povCharacters")

    def __init__(self, id="", name="", gender="", culture="",
                 born="", died="", father="", mother=""):

        self.id = id
        self.name = name
        self.gender = gender
        self.culture = culture
        self.born = born
        self.died = died
        self.father = father
        self.mother = mother

    def __repr__(self):
        return "<Character %r>" % self.name


"""
Houses table model
"""


class House(db.Model):
    __bind_key__ = "test"
    __tablename__ = "houses"

    # Table attributes
    id = db.Column(db.String(512), primary_key=True)
    name = db.Column(db.String(512))
    region = db.Column(db.String(512))
    coatOfArms = db.Column(db.String(512))
    words = db.Column(db.String(512))
    founded = db.Column(db.String(512))
    diedOut = db.Column(db.String(512))

    # Foreign keys
    currentLord_id = db.Column(db.String(512), db.ForeignKey("characters.id"))
    heir_id = db.Column(db.String(512), db.ForeignKey("characters.id"))
    overlord_id = db.Column(db.String(512), db.ForeignKey("characters.id"))
    founder_id = db.Column(db.String(512), db.ForeignKey("characters.id"))

    # Relationships
    currentLord = db.relationship("Character", uselist=False,
                                  foreign_keys="House.currentLord_id")
    heir = db.relationship("Character", uselist=False,
                           foreign_keys="House.heir_id")
    overlord = db.relationship("Character", uselist=False,
                               foreign_keys="House.overlord_id")
    founder = db.relationship("Character", uselist=False,
                              foreign_keys="House.founder_id")
    swornMembers = db.relationship("Character", secondary=characters_houses,
                                   back_populates="allegiances")

    def __init__(self, id="", name="", region="", coatOfArms="",
                 words="", founded="", diedOut=""):

        self.id = id
        self.name = name
        self.region = region
        self.coatOfArms = coatOfArms
        self.words = words
        self.founded = founded
        self.diedOut = diedOut

    def __repr__(self):
        return "<House %r>" % self.name


"""
Books table model
"""


class Book(db.Model):
    __bind_key__ = "test"
    __tablename__ = "books"

    # Table attributes
    id = db.Column(db.String(512), primary_key=True)
    name = db.Column(db.String(512))
    isbn = db.Column(db.String(512))
    numberOfPages = db.Column(db.Integer)
    publisher = db.Column(db.String(512))
    country = db.Column(db.String(512))
    mediaType = db.Column(db.String(512))
    released = db.Column(db.String(512))

    # Relationships
    characters = db.relationship("Character", secondary=characters_books,
                                 back_populates="books")
    povCharacters = db.relationship("Character", secondary=characters_povbooks,
                                    back_populates="povBooks")

    def __init__(self, id="", name="", isbn="",
                 numberOfPages=0, publisher="", country="",
                 mediaType="", released=""):

        self.id = id
        self.name = name
        self.isbn = isbn
        self.numberOfPages = numberOfPages
        self.publisher = publisher
        self.country = country
        self.mediaType = mediaType
        self.released = released

    def __repr__(self):
        return "<Book %r>" % self.name
