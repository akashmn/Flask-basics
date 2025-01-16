from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home page</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'

@app.route('/contact')
def contact():
    return '<h1>Contact Page</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}</h1>'

# @app.route('/user/<id1>/<id2>')
# def addString(id1, id2):
#     return f'<h1>{id1} + {id2} = {id1 + id2}</h1>' // This will concatenate the strings

@app.route('/user/<int:id1>/<int:id2>')
def add(id1, id2):
    return f'<h1>{id1} + {id2} = {id1 + id2}</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 