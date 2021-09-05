from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from icecream import ic


class ModelTestBase(APITestCase):

    def setUp(self):
        return super().setUp()

    def tearDown(self):
        return super().tearDown()


class TestUserModel(ModelTestBase):
    def test_create_example_user(self):
        ic("Testing User model: Creation of example user")
        example_user = User.objects.create(
            username="authenticated_user")
        example_user.set_password("auth_password")
        example_user.save()
        self.assertEqual(User.objects.first(), example_user)

    # Test Faulty Password error

    # Test Faulty User Group Error

    # Test Existing Email Error

    # Test Existing username Error

    # Test Password Change Error
