from __init__ import app
from flask_sqlalchemy import SQLAlchemy

# app.config["SQLALCHEMY_DATABASE_URI"] = ("postgresql://ahounsel:mypassword@localhost" 
#                                         "/var/www/FlaskApp/db/test.db")
# db = SQLAlchemy(app)

class Character(db.Model):
    __tablename__ = "characters"

    character_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(256))
    gender = db.Column(db.String(256))
    culture = db.Column(db.String(256))
    birth_date = db.Column(db.String(256))
    death_date = db.Column(db.String(256))
    titles = db.Column(db.String(256))
    aliases = db.Column(db.String(256))
    father = db.Column(db.String(256))
    mother = db.Column(db.String(256))
    spouse = db.Column(db.String(256))
    allegiances = db.Column(db.String(256))
    books = db.Column(db.String(256))
    pov_books = db.Column(db.String(256))
    tv_seasons = db.Column(db.String(256))
    played_by = db.Column(db.String(256))

    def __init__(self, url, gender, culture, birth_date, 
                death_date, titles, aliases, father, 
                mother, spouse, allegiances, books, 
                pov_books, tv_seasons, played_by):

        self.url = url
        self.gender = gender
        self.culture = culture
        self.birth_date = birth_date
        self.death_date = death_date
        self.titles = titles
        self.aliases = alises
        self.father = father
        self.mother = mother
        self.spouse = spouse
        self.allegiances = allegiances
        self.books = books
        self.pov_books = pov_books
        self.tv_seasons = tv_seasons
        self.played_by = played_by
