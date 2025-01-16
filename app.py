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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 