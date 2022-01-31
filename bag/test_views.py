from django.test import TestCase

from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404

from products.models import Product, Category
from .views import view_bag, add_to_bag, adjust_bag, remove_from_bag


class TestBagViews(TestCase):
    """
    Test the bag views work correctly
    """
    fixtures = [
        'categories.json',
        'products.json',
    ]
    def test_bag_page_url_works(self):
        """
        Test the url works when loading the page
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='bag/bag.html')

    def test_bag_page_is_accessible_by_name(self):
        """
        test the products page is accessible by name
        """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_view_bag_url(self):
        """
        Test that the view_bag view works correctly
        """
        url = reverse('view_bag')
        self.assertEqual(resolve(url).func, view_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="bag/bag.html")
