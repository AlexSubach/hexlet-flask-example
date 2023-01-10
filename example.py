from flask import Flask
from flask import request, make_response, render_template


app = Flask(__name__)
users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/')
def hello_world():
    print(request.headers)
    return 'Hello, World!'


@app.errorhandler(404)
def not_found(error):
    return 'Страница не найдена!', 404


@app.route('/users/')
def get_users():
    filtered_user = []
    term = request.args.get('term', default=None)
    for user in users:
        if term in user:
            filtered_user.append(user)
    return render_template(
        'users/index.html',
        users=filtered_user,
        search=term
    )


# @app.route('/users/<id>')
# def users(id):
#     return render_template('users/show.html', name=id)
