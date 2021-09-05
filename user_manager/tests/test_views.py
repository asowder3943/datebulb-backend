from django.http import response
from user_manager.tests.test_setup import TestSetUp


"""
Authentication should be outsourced and User Models Should be updated before pushing to production

Current Strategy is to use this temporary user model to build new features into the application.

No Further Test Cases should be created until refactor
"""


class TestUserViewset(TestSetUp):

    def test_user_list_get_no_auth_blank(self):
        # should return forbiddden as unauthorized user cannot view other users
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, 403)

    def test_user_list_post_no_auth_blank(self):
        # should return not found as no new user data was provided
        response = self.client.post(self.user_url)
        self.assertEqual(response.status_code, 400)

    # def post_user_list_After_authentication(self):
    #     response = self.client.post(self.user_url, data=self.example_user_data)
    #     self.assertEqual(response.status_code, 200)
    #     print(response.content)


"""

Un-implemented Test Case Parameters

Authorization Status: [AUTHENTICATED, UN-AUTHENTICATED]
Group Privilage: [ADMIN, USER, STAFF]

View: [LIST, EXISTING_DETAIL, NEW_DETAIL]

Method Type: [GET, POST, UPDATE]
Post Data: [NEW_USER, USER_LIST, EXISTING_USER, INVALID_EMAIL, EXISTING_EMAIL, VALID_PASS, INVALID_PASS]

"""
