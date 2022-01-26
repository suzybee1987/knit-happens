"""
Testing checkout page views using Django
"""

from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.


class TestBagViews(TestCase):
    """
    Test the home page loads correctly
    """

    def test_checkout_page_url_works(self):
        """
        Test the url works when loading the page
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_checkout_page_is_accessible_by_name(self):
        """
        test the products page is accessible by name
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
