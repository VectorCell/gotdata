from __init__ import app
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://austin:ahh10523@localhost/gotdata"
db = SQLAlchemy(app)


"""
Many-to-many association tables
"""
characters_houses = db.Table("characters_houses",
                             db.Column("character_url", db.String(
                                 512), db.ForeignKey("characters.url")),
                             db.Column("house_url", db.String(512), db.ForeignKey("houses.url")))

characters_books = db.Table("characters_books",
                            db.Column("character_url", db.String(
                                 512), db.ForeignKey("characters.url")),
                            db.Column("book_url", db.String(512), db.ForeignKey("books.url")))


"""
Characters table model
"""
class Character(db.Model):
    __tablename__ = "characters"

    # Table attributes
    url = db.Column(db.String(512), primary_key=True)
    name = db.Column(db.String(512))
    culture = db.Column(db.String(512))
    born = db.Column(db.String(512))
    died = db.Column(db.String(512))
    father = db.Column(db.String(512))
    mother = db.Column(db.String(512))
    spouse = db.Column(db.String(512))

    # Relationships
    allegiances = db.relationship("House", secondary=characters_houses,
                                  back_populates="swornMembers")
    books = db.relationship("Book", secondary=characters_books,
                            back_populates="characters")
    povBooks = db.relationship("Book", secondary=characters_books,
                               back_populates="povCharacters")

    def __init__(self, url="", name="", culture="", born="",
                 died="", father="", mother="", spouse=""):

        self.url = url
        self.name = name
        self.culture = culture
        self.born = born
        self.died = died
        self.father = father
        self.mother = mother
        self.spouse = spouse

    def __repr__(self):
        return "<Character %r>" % self.name


"""
Houses table model
"""
class House(db.Model):
    __tablename__ = "houses"

    # Table attributes
    url = db.Column(db.String(512), primary_key=True)
    name = db.Column(db.String(512))
    region = db.Column(db.String(512))
    coatOfArms = db.Column(db.String(512))
    words = db.Column(db.String(512))
    founded = db.Column(db.String(512))
    diedOut = db.Column(db.String(512))

    # Foreign keys
    currentLord_url = db.Column(db.String(512), db.ForeignKey("characters.url"))
    heir_url = db.Column(db.String(512), db.ForeignKey("characters.url"))
    overlord_url = db.Column(db.String(512), db.ForeignKey("characters.url"))
    founder_url = db.Column(db.String(512), db.ForeignKey("characters.url"))

    # Relationships
    currentLord = db.relationship("Character", uselist=False, foreign_keys="House.currentLord_url")
    heir = db.relationship("Character", uselist=False, foreign_keys="House.heir_url")
    overlord = db.relationship("Character", uselist=False, foreign_keys="House.overlord_url")
    founder = db.relationship("Character", uselist=False, foreign_keys="House.founder_url")
    swornMembers = db.relationship("Character", secondary=characters_houses,
                                   back_populates="allegiances")

    def __init__(self, url="", name="", region="", coatOfArms="",
                 words="", founded="", diedOut=""):

        self.url = url
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
    __tablename__ = "books"

    # Table attributes
    url = db.Column(db.String(512), primary_key=True)
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
    povCharacters = db.relationship("Character", secondary=characters_books,
                                    back_populates="povBooks")

    def __init__(self, url="", name="", isbn="",
                 numberOfPages=0, publisher="", country="",
                 mediaType="", released=""):

        self.url = url
        self.name = name
        self.isbn = isbn
        self.numberOfPages = numberOfPages
        self.publisher = publisher
        self.country = country
        self.mediaType = mediaType
        self.released = released

    def __repr__(self):
        return "<Book %r>" % self.name
