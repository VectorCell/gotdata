import json

from models import db, Character, House, Book


"""
Create the database
"""
def create_db():
    db.drop_all()
    db.create_all()

    create_characters()    

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
Main
"""
if __name__ == "__main__":
    create_db()
