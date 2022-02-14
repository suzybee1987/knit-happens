"""
Testing home page views using Django
"""

from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.


class TestHomeViews(TestCase):
    """
    Test the home page loads correctly
    """

    def test_home_page_url_works(self):
        """ 
        Test the url works when loading the page
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='home/index.html')

    def test_page_is_accessible_by_name(self):
        """
        test the home page is accessible by name
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_privacy_page_url_works(self):
        """ 
        Test the url works when loading the page
        """
        response = self.client.get('/privacy/')
        self.assertEqual(response.status_code, 200)

    def test_privacy_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get('/privacy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='home/privacy.html')

    def test_privacy_page_is_accessible_by_name(self):
        """
        test the privacy page is accessible by name
        """
        response = self.client.get(reverse('privacy'))
        self.assertEqual(response.status_code, 200)

    def test_tandc_page_url_works(self):
        """ 
        Test the url works when loading the page
        """
        response = self.client.get('/terms/')
        self.assertEqual(response.status_code, 200)

    def test_tandc_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get('/terms/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='home/terms.html')

    def test_tandc_page_is_accessible_by_name(self):
        """
        test the terms and conditions page is accessible by name
        """
        response = self.client.get(reverse('terms'))
        self.assertEqual(response.status_code, 200)
