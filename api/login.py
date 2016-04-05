# from flask import Blueprint, g
#
# # from ..models import db, User
# from . import api
#
# login = Blueprint('login', __name__)
# login_auth = HTTPBasicAuth()
#
# @login.route('/token', methods=['POST'])
# @login.login_required
# def token_request():
#     # Note that a colon is appended to the token. When the token is sent in
#     # the Authorization header this will put the token in the username field
#     # and an empty string in the password field.
#     return {'token': g.user.generate_auth_token() + ':'}, 200
