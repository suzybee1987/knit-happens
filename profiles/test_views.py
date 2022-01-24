"""
Testing profile page views using Django
"""

from django.test import TestCase
from django.shortcuts import reverse


class TestProfileViews(TestCase):
    """
    Test the profile page loads correctly
    """

    def test_profile_page_url_works(self):
        """ 
        Test the url works when loading the page
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='profiles/profile.html')

    def test_profile_page_is_accessible_by_name(self):
        """
        test the profile page is accessible by name
        """
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
