import os
import base64
import tempfile
import unittest
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

    def test_list_users(self):
        import ipdb;ipdb.set_trace()
        # rv = self.app.get('/v1/users')
        pass


    def open_with_auth(self, url, method, username, password):
        return self.client.open(url,
            method=method,
            headers={
                'Authorization': 'Basic ' + base64.b64encode(username + \
                ":" + password)
            }
        )

if __name__ == '__main__':
    unittest.main()
