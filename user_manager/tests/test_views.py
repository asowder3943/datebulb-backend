from rest_framework.test import APITestCase
from django.urls import reverse
from icecream import ic


class ViewTestBase(APITestCase):

    def setUp(self):
        # Define Urls for testing api
        # https://www.django-rest-framework.org/api-guide/routers/#:~:text=The%20example%20above,Name%3A%20%27user-list%27
        self.user_url = reverse('user-list')

        # Example User data
        self.example_user_data = {
            'email': 'example@gmail.com',
            'username': 'example_username',
            'password': 'example_password'
        }
        return super().setUp()

    # defer to APITestCase destruction ggs
    def tearDown(self):
        return super().tearDown()


class TestUserViewset(ViewTestBase):

    """
    User List Test Cases
    """

    def test_user_list_get_no_auth_blank(self):
        ic("Testing UserViewSet: Unauthenticated get request")
        # should return forbiddden as unauthorized user cannot view other users
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, 403)

    # Test Blank get with auth

    # Test post with no auth

    # test post with auth

    """
    User Detail Test Cases
    """

    # Test get no auth

    # Test get with with auth

    # Test get with owner auth

    # Test update no auth

    # Test update with with auth

    # Test update with owner auth

    # Test delete no auth

    # Test delete with with auth

    # Test delete with owner auth
