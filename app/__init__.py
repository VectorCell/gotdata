from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
import os

import query_db

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/query=<string:type>', methods=["GET"])
def query(type):
    data = None
    if type == "characters":
        return [c for c in query_db.get_all_characters()]
    elif type == "houses":
        return [c for c in query_db.get_all_houses()]
    return data

@app.route('/characters')
def characters():
    # characters = [c for c in query_db.get_all_characters()]
    characters = query_db.get_all_characters()
    return render_template('characters.html', characters=characters)

@app.route('/houses')
def houses():
    # houses = [c for c in query_db.get_all_houses()]
    houses = query_db.get_all_houses()
    return render_template('houses.html', houses=houses)

@app.route('/books')
def books():
    # books = [c for c in query_db.get_all_books()]
    books = query_db.get_all_books()
    return render_template('books.html', books=books)

@app.route('/character/<int:arg>')
def character(arg):
    character = query_db.get_character(arg)
    # print(character)
    # print("This was a character")
    return render_template('character.html', character=character)

@app.route('/house/<int:arg>')
def house(arg):
    houses = query_db.get_house(arg)
    return render_template('house.html', house=houses[arg])

@app.route('/book/<int:arg>')
def book(arg):
    book = query_db.get_book(arg)
    return render_template('book.html', book=book)

"""
@app.route('/static/houses')
def houses():
    return app.send_static_file('/static/houses.html')

@app.route('/static/characters')
def houses():
    return app.send_static_file('/static/characters.html')


@app.route('/static/locations')
def houses():
    return app.send_static_file('/static/locations.html')

@app.route('/static/events')
def events():
    return app.send_static_file('/static/events.html')
"""

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
