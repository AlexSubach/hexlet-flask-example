def validate(user):
    errors = {}
    if not user['nickname']:
        errors['nickname'] = 'Введите никнейм'

    if not user['email']:
        errors['email'] = 'Введите Email'
    return errors
