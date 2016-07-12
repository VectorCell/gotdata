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
        id = d["url"].split("/").pop()
        name = d["name"]
        gender = d["gender"]
        culture = d["culture"]
        born = d["born"]
        died = d["died"]
        father = d["father"]
        mother = d["mother"]

        c = Character.query.get(id)
        if not c:
            c = Character(id=id, name=name, gender=gender, culture=culture, born=born,
                          died=died, father=father, mother=mother)
        else:
            c.name = name
            c.gender = gender
            c.culture = culture
            c.born = born
            c.died = died
            c.father = father
            c.mother = mother

        create_rel_spouse(c, d["spouse"])
        create_rel_allegiances(c, d["allegiances"])
        create_rel_books(c, d["books"])
        create_rel_povbooks(c, d["povBooks"])

        db.session.add(c)
        print(c)


"""
Create the spouse one-to-one 
relationship between two characters
"""
def create_rel_spouse(c, character_url):
    if character_url == "":
        return

    character_id = character_url.split("/").pop()
    s = Character.query.get(character_id)
    if not s:
        s = Character(id=character_id)
    c.spouse = s

    db.session.add(s)


"""
Create the allegiances/swornMembers many-to-many 
relationship between characters and houses
"""
def create_rel_allegiances(c, a):
    for house_url in a:
        house_id = house_url.split("/").pop()
        h = House.query.get(house_id)
        if not h:
            h = House(id=house_id)
        else:
            c.allegiances.append(h)
            
        db.session.add(h)


"""
Create the books/characters many-to-many 
relationship between characters and books
"""
def create_rel_books(c, b):
    for book_url in b:
        book_id = book_url.split("/").pop()
        b = Book.query.get(book_id)
        if not b:
            b = Book(id=book_id)
        else:
            c.books.append(b)

        db.session.add(b)


"""
Create the povBooks/povCharacters many-to-many 
relationship between characters and books
"""
def create_rel_povbooks(c, b):
    for book_url in b:
        book_id = book_url.split("/").pop()
        b = Book.query.get(book_id)
        if not b:
            b = Book(id=book_id)
        else:
            c.povBooks.append(b)

        db.session.add(b)


"""
Create the houses table
"""
def create_houses():
    with open("../anapioficeandfire/houses.json") as house_file:
        houses = json.load(house_file)

    for d in houses:
        id = d["url"].split("/").pop()
        name = d["name"]
        region = d["region"]
        coatOfArms = d["coatOfArms"]
        words = d["words"]
        founded = d["founded"]
        diedOut = d["diedOut"]

        h = House.query.get(id)
        if not h:
            h = House(id=id, name=name, region=region, coatOfArms=coatOfArms,
                      words=words, founded=founded, diedOut=diedOut)
        else:
            h.name = name
            h.region = region
            h.coatOfArms = coatOfArms
            h.words = words
            h.founded = founded
            h.diedOut = diedOut

        create_rel_currentlord(h, d["currentLord"])
        create_rel_heir(h, d["heir"])
        create_rel_overlord(h, d["overlord"])
        create_rel_founder(h, d["founder"])

        db.session.add(h)
        print(h)


"""
Create the currentLord one-to-one 
relationship between a house and 
a character
"""
def create_rel_currentlord(h, character_url):
    if character_url == "":
        return

    character_id = character_url.split("/").pop()
    c = Character.query.get(character_id)
    if not c:
        c = Character(id=character_id)
    h.currentLord = c

    db.session.add(c)


"""
Create the heir one-to-one 
relationship between a house and 
a character
"""
def create_rel_heir(h, character_url):
    if character_url == "":
        return

    character_id = character_url.split("/").pop()
    c = Character.query.get(character_id)
    if not c:
        c = Character(id=character_id)
    h.heir = c

    db.session.add(c)


"""
Create the overlord one-to-one 
relationship between a house and 
a character
"""
def create_rel_overlord(h, character_url):
    if character_url == "":
        return

    character_id = character_url.split("/").pop()
    c = Character.query.get(character_id)
    if not c:
        c = Character(id=character_id)
    h.overlord = c

    db.session.add(c)


"""
Create the founder one-to-one 
relationship between a house and 
a character
"""
def create_rel_founder(h, character_url):
    if character_url == "":
        return

    character_id = character_url.split("/").pop()
    c = Character.query.get(character_id)
    if not c:
        c = Character(id=character_id)
    h.founder = c

    db.session.add(c)


"""
Create the books table
"""
def create_books():
    with open("../anapioficeandfire/books.json") as book_file:
        books = json.load(book_file)

    for d in books:
        id = d["url"].split("/").pop()
        name = d["name"]
        isbn = d["isbn"]
        numberOfPages = d["numberOfPages"]
        publisher = d["publisher"]
        country = d["country"]
        mediaType = d["mediaType"]
        released = d["released"].split("T")[0]

        b = Book.query.get(id)
        if not b:
            b = Book(id=id, name=name, isbn=isbn, numberOfPages=numberOfPages,
                     publisher=publisher, country=country, mediaType=mediaType,
                     released=released)
        else:
            b.name = name
            b.isbn = isbn
            b.numberOfPages = numberOfPages
            b.publisher = publisher
            b.country = country
            b.mediaType = mediaType
            b.released = released
        
        db.session.add(b)
        print(b)


"""
Main
"""
if __name__ == "__main__":
    create_db()
