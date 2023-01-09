from flask import Flask
from flask import request, make_response


app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request.headers)
    return 'Hello, World!'


@app.route('/json/')
def json():
    return {'json': 42}


@app.errorhandler(404)
def not_found(error):
    return f'Страница не найдена {error}', 404


@app.get('/users')
def users_get():
    return 'GET /users'


@app.post('/users')
def users():
    return 'Users', 302


@app.route('/courses/<id>')
def courses(id):
    return f'Course id: {id}'


@app.route('/foo')
def foo():
    response = make_response('foo')
    response.headers['alex_master'] = 'hello, alex'
    response.mimetype = 'text/plain'
    response.status_code = 200
    response.set_cookie('foo', 'alex')
    return response
