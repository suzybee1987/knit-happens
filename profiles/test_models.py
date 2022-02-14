from django.test import TestCase, Client
from django.contrib.auth.models import User


class TestUserProfileModel(TestCase):
    """
    test the user profile model
    """
    @classmethod
    def setUpTestData(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuserprofile", password="abc123def"
        )
        self.client.login(username="testuserprofile", password="abc123def")

    def test_getting_user_profile(self):
        """
        Test retrieving the user profile
        """
        self.client.login(username='testuserprofile', password='abc123def')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_user_profile_string_method_returns_username(self):
        """
        Test the user profile string method returns the username
        """
        expected_output = "testuserprofile"
        self.assertEqual(expected_output, str(self.user))
