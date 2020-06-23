from app import app
import unittest
import os


class FlaskTestCase(unittest.TestCase):

    # Ensure that the landing page loads correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/landing', content_type='html/text')
        # Test that the page loads correctly
        self.assertEqual(response.status_code, 200)
        # Test that registration form title is present
        self.assertTrue(b'Join the conversation!' in response.data)

    # Check that login works if creditentials are correct
    def test_login(self):
        tester = app.test_client(self)
        response = tester.post('/login_user', data=dict(username="dobuzzin",
                                                        password="ilikegolftw"), follow_redirects=True)
        # User should be in dashboard
        self.assertTrue(
            b'This is where your latest post will appear.. Start by posting something!' in response.data)





if __name__ == '__main__':
    app.secret_key = os.environ.get('key')
    unittest.main()
