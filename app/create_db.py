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

        c = Character.query.get(url)
        if not c:
            c = Character(url=url, name=name, culture=culture, born=born,
                          died=died, father=father, mother=mother, spouse=spouse)
        else:
            c.name = name
            c.culture = culture
            c.born = born
            c.died = died
            c.father = father
            c.mother = mother
            c.spouse = spouse            

        print(c)
        db.session.add(c)

        create_rel_allegiances(c, d["allegiances"])
        create_rel_books(c, d["books"])
        create_rel_povbooks(c, d["povBooks"])

"""
Create the allegiances/swornMembers many-to-many 
relationship between characters and houses
"""
def create_rel_allegiances(c, a):
    for house_url in a:
        h = House.query.get(house_url)
        if not h:
            h = House(url=house_url)
        else:
            c.allegiances.append(h)
            
        db.session.add(h)


"""
Create the books/characters many-to-many 
relationship between characters and books
"""
def create_rel_books(c, b):
    for book_url in b:
        b = Book.query.get(book_url)
        if not b:
            b = Book(url=book_url)
        else:
            c.books.append(b)

        db.session.add(b)


"""
Create the povBooks/characters many-to-many 
relationship between characters and books
"""
def create_rel_povbooks(c, b):
    for book_url in b:
        b = Book.query.get(book_url)
        if not b:
            b = Book(url=book_url)
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
        url = d["url"]
        name = d["name"]
        region = d["region"]
        coatOfArms = d["coatOfArms"]
        words = d["words"]
        founded = d["founded"]
        diedOut = d["diedOut"]

        h = House.query.get(url)
        if not h:
            h = House(url=url, name=name, region=region, coatOfArms=coatOfArms,
                      words=words, founded=founded, diedOut=diedOut)
        else:
            h.name = name
            h.region = region
            h.coatOfArms = coatOfArms
            h.words = words
            h.founded = founded
            h.diedOut = diedOut

        print(h)
        db.session.add(h)


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

        b = Book.query.get(url)
        if not b:
            b = Book(url=url, name=name, isbn=isbn, numberOfPages=numberOfPages,
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
        
        print(b)
        db.session.add(b)


"""
Main
"""
if __name__ == "__main__":
    create_db()
