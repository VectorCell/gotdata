import json

from models import db, Character, House, Book


"""
Create the database
"""
def create_db():
    db.drop_all()
    db.create_all()

    create_characters()    
    create_houses()
    create_books()

    db.session.commit()


"""
Create the characters table
"""
def create_characters():
    with open("../anapioficeandfire/characters.json") as char_file:
        characters = json.load(char_file)

    for d in characters:
        url = d["url"]
        name = d["name"]
        culture = d["culture"]
        born = d["born"]
        died = d["died"]
        father = d["father"]
        mother = d["mother"]
        spouse = d["spouse"]

        c = Character(url=url, name=name, culture=culture, born=born,
                      died=died, father=father, mother=mother, spouse=spouse) 
        db.session.add(c)

    db.session.commit()


"""
Create the houses table
"""
def create_houses():
    with open("../anapioficeandfire/houses.json") as house_file:
        houses = json.load(house_file)

    for d in houses:
        url = d["url"]
        name = d["name"]
        region = d["region"]
        coatOfArms = d["coatOfArms"]
        words = d["words"]
        founded = d["founded"]
        diedOut = d["diedOut"]

        h = House(url=url, name=name, region=region, coatOfArms=coatOfArms,
                  words=words, founded=founded, diedOut=diedOut)
        db.session.add(h)

    db.session.commit()


"""
Create the books table
"""
def create_books():
    with open("../anapioficeandfire/books.json") as book_file:
        books = json.load(book_file)

    for d in books:
        url = d["url"]
        name = d["name"]
        isbn = d["isbn"]
        numberOfPages = d["numberOfPages"]
        publisher = d["publisher"]
        country = d["country"]
        mediaType = d["mediaType"]
        released = d["released"]

        b = Book(url=url, name=name, isbn=isbn, numberOfPages=numberOfPages,
                 publisher=publisher, country=country, mediaType=mediaType,
                 released=released)
        db.session.add(b)

    db.session.commit()


"""
Main
"""
if __name__ == "__main__":
    create_db()
