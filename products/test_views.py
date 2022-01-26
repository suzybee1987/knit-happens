from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User

from .models import Category, Product


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

    def test_products(self):
        """
        test products display
        """
        products = Product.objects.all()
        for product in products:
            response = self.client.get(reverse('products'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, product.pk)

    def test_categories(self):
        """
        test categories sort functionality
        """
        product = Product.objects.get(id=25)
        category = Category.objects.get(pk=8)
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product.category, category)
        self.assertContains(response, product.category)

    # def test_product_details_page_shows_details(self):
    #     """
    #     test products display on individual product detail page
    #     """
    #     product = Product.objects.get(id=25)
    #     response = self.client.get(reverse('products'))
    #     self.assertContains(response, product.name)

    # def test_product_details_page_url(self):
    #     """
    #     test products urls on individual product detail pages
    #     """
    #     response = self.client.get('/products/25/')
    #     self.assertEqual(response.status_code, 200)
