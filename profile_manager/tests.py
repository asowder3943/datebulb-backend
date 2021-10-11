from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestProfileSignals(TestCase):
    def setUp(self):
        # create a client for sending http request to the test server (actually communicates directly with drf)
        c = Client()
        response = c.post('/auth/registration/',
                          {
                              "username": "alice123",
                              "email": "alice123@gmail.com",
                              "password1": "bad_pass_alice12!",
                              "password2": "bad_pass_alice12!"
                          }
                          )
        print(response)
        # creation of new resource should resultin a 201 code
        self.assertEqual(response.status_code, 201)

    def test_profile_signal_accessable(self):
        # select new user from the database table
        test_user = User.objects.get(username='alice123')
        # ensure the default theme preferences have been automatically set for the user profile
        self.assertEqual(test_user.profile.theme_preference, "LT")
