import os
import base64
import tempfile
import unittest

from flask import json

from api.app import create_app
from api.models import db, User

class TestAPI(unittest.TestCase):
    default_username = 'steve'
    default_password = 'jobs'

    def setUp(self):
        self.app = create_app()

        self.db_fd, self.app.config['DATABASE'] = tempfile.mkstemp()
        self.app.config['TESTING'] = True

        self.ctx = self.app.app_context()
        self.ctx.push()
        db.drop_all()
        db.create_all()
        u = User(username=self.default_username,
                 password=self.default_password)
        db.session.add(u)
        db.session.commit()

        self.client = self.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(self.app.config['DATABASE'])

    def test_bad_auth(self):
        rv = self.open_with_auth('/v1/users', 'GET', 'abc', 'def')
        self.assertEqual(rv.status_code, 401)

    def test_list_users(self):
        rv = self.open_with_auth('/v1/users', 'GET',
                                 self.default_username,
                                 self.default_password)

        computed = json.loads(rv.data)
        expected = {'response': [{'username': 'steve'}]}

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(computed, expected)

    def test_create_user(self):

        data = json.dumps(dict(username='user01', password='secret'))
        rv = self.open_with_auth('/v1/users', 'POST', self.default_username, self.default_password, data=data)

        computed = json.loads(rv.data)
        expected = {'username': 'user01'}

        self.assertEqual(rv.status_code, 201)
        self.assertEqual(computed, expected)

    def open_with_auth(self, url, method, username, password, data=None):

        auth_string = username + ':' + password

        # encode in utf need for python 3 and greater
        auth_byte = auth_string.encode('utf-8')

        basic = base64.b64encode(auth_byte)

        #decode in utf=8 string for the header
        str_basic = basic.decode('utf-8')

        return self.client.open(url,
            method=method,
            headers={
                'Authorization': 'Basic %s' %str_basic,
                'content-type': 'application/json',
            },
            data=data,
        )

if __name__ == '__main__':
    unittest.main()
