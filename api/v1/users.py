from flask import abort, jsonify, request

from ..models import db, User
from . import api

@api.route('/healthcheck', methods = ['GET'])
def healthcheck():
    return 'hello world', 200

@api.route('/users', methods = ['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username = username).first() is not None:
        abort(400) # existing user

    import ipdb; ipdb.set_trace()
    
    user = User(username = username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'username': user.username }), 201
