from flask import Flask
from flask import request


app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.headers)
    return 'Hello, World!'


@app.route('/not_found')
def not_found():
    return 'Oops!', 404


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users():
    return 'Users', 302


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'
