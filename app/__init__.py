from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
import os

import query_db

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/characters')
def characters():
    characters = [c for c in query_db.get_all_characters() if c.name]
    return render_template('characters.html', characters=characters)

@app.route('/houses')
def houses():
    houses = [h for h in query_db.get_all_houses()if h.name]
    return render_template('houses.html', houses=houses)

@app.route('/books')
def books():
    books = query_db.get_all_books()
    return render_template('books.html', books=books)

@app.route('/character/<int:arg>')
def character(arg):
    character = query_db.get_character(arg)
    if character is None:
        image = '/img/characters/999.jpg'
    else:
        image = '/img/characters/' + str(character.id) + '.jpg'
    return render_template('character.html', character=character, characterimage=image)

@app.route('/house/<int:arg>')
def house(arg):
    houses = query_db.get_house(arg)
    return render_template('house.html', house=houses)

@app.route('/book/<int:arg>')
def book(arg):
    book = query_db.get_book(arg)
    if book is None:
        image = '/'
    else:
        image = '/img/books/' + str(book.id) + '.jpg'
    return render_template('book.html', book=book, coverimage=image)


#
# API
#

@app.route('/api/<path:model>')
def api_all(model):
    if model == 'characters':
        characters = [query_db.get_character_dict(c.id) for c in query_db.get_all_characters()]
        return jsonify(characters)
    if model == 'houses':
        houses = [query_db.get_house_dict(c.id) for c in query_db.get_all_houses()]
        return jsonify(houses)
    if model == 'books':
        books = [query_db.get_book_dict(c.id) for c in query_db.get_all_books()]
        return jsonify(books)
    else:
        return jsonify({'message': 'error 404 not found'})

@app.route('/api/<path:model>/<string:commadelimited>')
def api_multiple(model, commadelimited):
    multiple = []
    for id in commadelimited.split(','):
        if model == 'character' and query_db.get_character(id) is not None:
            multiple += [query_db.get_character_dict(id)]
        elif model == 'house' and query_db.get_house(id) is not None:
            multiple += [query_db.get_house_dict(id)]
        elif model == 'book' and query_db.get_book(id) is not None:
            multiple += [query_db.get_book_dict(id)]
    return jsonify(multiple)

@app.route('/api/<path:model>/<int:id>')
def api_single(model, id):
    if model == 'character' and query_db.get_character(id) is not None:
        return query_db.get_character_json(id)
    elif model == 'house' and query_db.get_house(id) is not None:
        return query_db.get_house_json(id)
    elif model == 'book' and query_db.get_book(id) is not None:
        return query_db.get_book_json(id)
    else:
        return jsonify({'message': 'error 404 not found'})


#
# Static files
#

@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == "__main__":
    if (os.getuid() == 1003): # ahounsel
        app.run(host='0.0.0.0', port=8081)
    elif (os.getuid() == 1000): # bismith
        app.run(host='0.0.0.0', port=8082)
    elif (os.getuid() == 1001): # holtk
        app.run(host='0.0.0.0', port=8083)
    elif (os.getuid() == 1005): # rkaman
        app.run(host='0.0.0.0', port=8084)
    elif (os.getuid() == 1004): # sh115
        app.run(host='0.0.0.0', port=8085)
    elif (os.getuid() == 1002): # shcott
        app.run(host='0.0.0.0', port=8086)
    elif (os.getuid() == 197609): # shcott's laptop
        app.run(host='0.0.0.0', port=8087)
    else:
        app.run()
