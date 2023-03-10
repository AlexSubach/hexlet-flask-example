import json

from flask import Flask
from flask import request, render_template, redirect, url_for, flash
from templates.users import support

app = Flask(__name__)
app.secret_key = 'dfdsgfgsdf345676gfknsdrlnq3rythgryt78865eld'


@app.route('/')
def index():
    return render_template('/users/index.html')


@app.errorhandler(404)
def not_found():
    return 'Страница не найдена!', 404


# @app.route('/users')
# def get_users():
#     filtered_user = []
#     term = request.args.get('term', default='')
#     for user in users:
#         if term in user:
#             filtered_user.append(user)
#     return render_template(
#         'users/index.html',
#         users=filtered_user,
#         search=term
#     )


ID: int = 0


# noinspection PyTypeChecker
@app.post('/users')
def users_post():
    global ID
    ID += 1
    user = request.form.to_dict()
    errors = support.validate(user)
    user['id'] = ID
    if errors:
        return render_template('/users/new.html', user=user, errors=errors)
    with open('templates/users/users.json', 'a') as file:
        file.write(json.dumps(user, indent=4))
    flash('User was added successfully')
    return redirect(url_for('user_new'), code=302)


@app.route('/users/new')
def user_new():
    user = {
        'nickname': '',
        'email': '',
        'id': ''
    }
    errors = {}
    return render_template('users/new.html', user=user, errors=errors)

# @app.route('/users/<id>')
# def users(id):
#     return render_template('users/show.html', name=id)
