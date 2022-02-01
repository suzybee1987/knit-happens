from django.test import TestCase

from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404
from decimal import Decimal
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

    def test_view_bag(self):
        """
        Test that the view_bag view works correctly
        """
        link = reverse('view_bag')
        self.assertEqual(resolve(link).func, view_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="bag/bag.html")

    def test_add_to_bag(self):
        """
        Test that the add to bag view works as expected
        """
        link = reverse('add_to_bag', args=['item_id'])
        self.assertEqual(resolve(link).func, add_to_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_adjust_bag(self):
        """
        Test that the adjust bag view works as expected
        """
        link = reverse('adjust_bag', args=['item_id'])
        self.assertEqual(resolve(link).func, adjust_bag)
        product = Product.objects.get(id=15)
        qty = 5
        bag_total = product.price * qty
        self.assertEqual(bag_total, Decimal('64.95'))
        qty = 2
        bag_total += product.price * qty
        self.assertEqual(bag_total, Decimal('90.93'))

    def test_remove_from_bag(self):
        """
        Test remove from bag view removes the product from the bag
        """
        link = reverse('remove_from_bag', args=['item_id'])
        self.assertEqual(resolve(link).func, remove_from_bag)
