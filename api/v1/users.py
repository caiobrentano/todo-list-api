from flask import abort, jsonify, request

from ..models import db, User
from . import api


@api.route('/users', methods=['GET'])
def list_user():
    users = User.query.all()

    return jsonify({
        'response': [{'username': user.username} for user in users]
    })

@api.route('/users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None:
        abort(400) # missing arguments

    if User.query.filter_by(username=username).first() is not None:
        abort(400) # existing user

    user = User()
    user.username = username
    user.password = password

    db.session.add(user)
    db.session.commit()

    resp = jsonify({'username': user.username})
    resp.status_code = 201

    return resp
