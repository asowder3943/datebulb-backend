from rest_framework.test import APITestCase
from django.urls import reverse
# Better print() method
from icecream import ic


# Base Class for the Views Test Cases - declares protected variables accessable by any child case
class ViewTestBase(APITestCase):

    def setUp(self):
        # Define Urls for testing api
        # https://www.django-rest-framework.org/api-guide/routers/#:~:text=The%20example%20above,Name%3A%20%27user-list%27
        self.user_url = reverse('user-list')
        self.group_url = reverse('group-list')

        # Example User data
        self.example_user_data = {
            'email': 'example@gmail.com',
            'username': 'example_username',
            'password': 'example_password'
        }
        return super().setUp()

    # defer to APITestCase destruction
    def tearDown(self):
        return super().tearDown()


class TestUserViewset(ViewTestBase):
    def test_user_list_get_no_auth_blank(self):
        ic("Running user list no auth get case....")
        # should return forbiddden as unauthorized user cannot view other users
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, 403)
