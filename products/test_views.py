"""
Testing product page views using Django
"""

from django.test import TestCase
from django.shortcuts import reverse
# Create your tests here.


class TestProductViews(TestCase):
    """
    Test the home page loads correctly
    """

    def test_product_page_url_works(self):
        """ 
        Test the url works when loading the page
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='products/products.html')

    def test_product_page_is_accessible_by_name(self):
        """
        test the products page is accessible by name
        """
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
