from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetUp(APITestCase):
    def setUp(self):

        # https://www.django-rest-framework.org/api-guide/routers/#:~:text=The%20example%20above,Name%3A%20%27user-list%27
        self.user_url = reverse('user-list')
        self.group_url = reverse('group-list')

        example_user_data = {
            'email': 'example@gmail.com',
            'username': 'example_username',
            'password': 'example_password'
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()
