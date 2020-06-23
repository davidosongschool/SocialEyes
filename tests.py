from app import app
import unittest
import os
from flask_pymongo import PyMongo
import app as app_module

app = app_module.app

# Setting up test DB on Mongo and switching CSRF checks off
app.config["TESTING"] = True
app.config["WTF_CSRF_ENABLED"] = False
app.config['MONGO_URI'] = os.environ.get('testDB')

mongo = PyMongo(app)
app_module.mongo = mongo


class AppTestCase(unittest.TestCase):
    """Clean database except admin test login"""

    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            mongo.db.users.delete_many({'username': 'newUser'})
            mongo.db.posts.delete_many({})


class FlaskTestCase(AppTestCase):
    # Ensure that the landing page loads correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/landing', content_type='html/text')
        # Test that the page loads correctly
        self.assertEqual(response.status_code, 200)
        # Test that registration form title is present
        self.assertTrue(b'Join the conversation!' in response.data)

    # Check that registration works correctly and goes to Dashboard
    def test_registration(self):
        tester = app.test_client(self)
        response = tester.post('/register_user', data=dict(username="newUser",
                                                           password="myPass123",
                                                           email='newemail@email.com'), follow_redirects=True)
        # User should be in Dashboard
        self.assertTrue(
            b'This is where your latest post will appear.. Start by posting something!' in response.data)

    # Check that user cannot register with existing email

    def test_existing_email(self):
        tester = app.test_client(self)
        response = tester.post('/register_user', data=dict(username="newUser",
                                                           password="myPass123",
                                                           email='admin@email.com'), follow_redirects=True)
        self.assertTrue(b'Username or Email already exists!' in response.data)

    # Check that login works if creditentials are correct
    def test_login(self):
        tester = app.test_client(self)
        response = tester.post('/login_user', data=dict(username="admin",
                                                        password="myPass123"), follow_redirects=True)
        # User should be in dashboard
        self.assertTrue(
            b'This is where your latest post will appear.. Start by posting something!' in response.data)

    # Check that incorrect credientials gives error
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login_user', data=dict(username="incorrect",
                                                        password="incorrect"), follow_redirects=True)
        self.assertTrue(b'Incorrect Login! Try Again' in response.data)


if __name__ == '__main__':
    app.secret_key = os.environ.get('key')
    unittest.main()
