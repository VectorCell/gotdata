from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

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
    app.run(host="0.0.0.0", port=8081)
