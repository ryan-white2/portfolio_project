from flask import Blueprint, jsonify, abort, request
from ..models import User, db
import hashlib
import secrets


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def get_users():
    users = User.query.all()  # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def get_user(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create_user():
    # req body must contain username and password
    checks = ('account_login', 'account_password', 'user_age', 'account_country',
              'user_birthdate', 'account_language', 'account_sex',
              'account_phone', 'account_email', 'account_name')
    for check in checks:
        if check not in request.json:
            return abort(400)

    # req username and password must meet length requirements
    account_login = request.json['account_login']
    account_password = request.json['account_password']
    if len(account_login) < 3 or len(account_password) < 8:
        return abort(400)
    hash_pass = scramble(account_password)

    # construct User
    u = User(
        account_login=account_login,
        account_password=hash_pass,
        user_age=request.json['user_age'],
        account_country=request.json['account_country'],
        user_birthdate=request.json['user_birthdate'],
        account_language=request.json['account_language'],
        account_sex=request.json['account_sex'],
        account_phone=request.json['account_phone'],
        account_email=request.json['account_email'],
        account_name=request.json['account_name']
    )
    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update_user(id: int):
    u = User.query.get_or_404(id)
    if 'account_login' in request.json:
        account_login = request.json['account_login']
        if len(account_login) < 3:
            return abort(400)
        u.account_login = account_login
    if 'account_password' in request.json:
        account_password = request.json['account_password']
        if len(account_password) < 8:
            return abort(400)
        hash_pass = scramble(account_password)
        u.account_password = hash_pass
    if 'account_phone' in request.json:
        account_phone = request.json['account_phone']
        u.account_phone = account_phone
    if 'account_email' in request.json:
        account_email = request.json['account_email']
        u.account_email = account_email
    if 'account_name' in request.json:
        account_name = request.json['account_name']
        u.account_name = account_name
    # update User
    try:
        # db.session.add(u)  # prepare CREATE statement
        db.session.commit()  # execute CREATE statement
        return jsonify(u.serialize())
    except:
        # something went wrong :(
        return jsonify(False)


@ bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
