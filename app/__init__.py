from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/character/<int:arg>')
def character(arg):
    character = {
        "name": "Tyrion Lannister",
        "img": "",
        "seasons": 1,
        "house": "Lannister",
        "allegiance": "Nope",
        "alive": True,
        "titles": "None",
        "other_names": "None",
        "actor": "Peter Dinklage",
        "current_location": "King's Landing",
        "locations": "None"
    }
    return render_template('character.html', character=character)

@app.route('/house/<int:arg>')
def house(arg):
    house = {
        "name": "House Tyrell",
        "region": "lol",
        "img": "",
        "words": "I'm a pig",
        "lord": "King Joffrey",
        "heir": "A baby",
        "overlord": "None",
        "weapons": "None",
        "characters": "None",
        "locations": "None"
    }
    return render_template('house.html', house=house)

@app.route('/location/<int:arg>')
def location(arg):
    location = {
        "name": "The Eyrie",
        "img": "",
        "people": "None",
        "ruling_houses": "House Stark",
        "neighbors": "None",
        "conflicts": "???"
    }
    return render_template('location.html', location=location)

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
    app.run(host='0.0.0.0', port=8082)
