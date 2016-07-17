from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
import os

import query_db

app = Flask(__name__)


# Local EDIT

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
# Search results
#

@app.route('/search/<path:query>')
def search(query):
    tokens = query.split('+')
    query_and = ' AND '.join(t for t in tokens)
    query_or = ' OR '.join(t for t in tokens)
    if query_and == query_or:
        results_and = query_db.search_db(' AND '.join(t for t in tokens))
        return render_template('search.html',
                               query_and=query_and,
                               results_and=results_and)
    else:
        results_and = query_db.search_db(' AND '.join(t for t in tokens))
        results_or = query_db.search_db(' OR '.join(t for t in tokens))
        return render_template('search.html',
                               query_and=query_and,
                               results_and=results_and,
                               query_or=query_or,
                               results_or=results_or)

#
# Unit tests
#

@app.route('/unittest')
def unittest():
    print('current working directory:', os.getcwd())
    import subprocess
    command = "python /var/www/FlaskApp/app/tests.py"
    process = subprocess.Popen(command, stdout=None, stderr=subprocess.PIPE, shell=True)
    output = process.communicate()
    return ''.join(o for o in output if isinstance(o, str))

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
        if model == 'characters' and query_db.get_character(id) is not None:
            multiple += [query_db.get_character_dict(id)]
        elif model == 'houses' and query_db.get_house(id) is not None:
            multiple += [query_db.get_house_dict(id)]
        elif model == 'books' and query_db.get_book(id) is not None:
            multiple += [query_db.get_book_dict(id)]
    return jsonify(multiple)

@app.route('/api/<path:model>/<int:id>')
def api_single(model, id):
    if model == 'characters' and query_db.get_character(id) is not None:
        return query_db.get_character_json(id)
    elif model == 'houses' and query_db.get_house(id) is not None:
        return query_db.get_house_json(id)
    elif model == 'books' and query_db.get_book(id) is not None:
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
    else:
        app.run()
