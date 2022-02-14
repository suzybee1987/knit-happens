from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.messages import get_messages

from .models import Category, Product


class TestProductViews(TestCase):

    fixtures = [
        'categories.json',
        'products.json'
    ]

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

    def test_categories(self):
        """
        test categories sort functionality
        """
        product = Product.objects.get(id=1)
        category = Category.objects.get(pk=5)
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(product.category, category)
        self.assertContains(response, product.category)

    def test_sort_functionality(self):
        """
        Test that the sort functionality works
        """
        category_name = 'bamboo'
        sort_array = ['name', 'category']
        for sort in sort_array:
            direction = 'desc'
            current_sorting = f'{sort}_{direction}'
            response = self.client.get(
                f'/products/?category={category_name}'
                f'&sort={sort}&direction={direction}')
            self.assertEqual(current_sorting, f'{sort}_desc')
            self.assertEqual(response.status_code, 200)

    def test_search_functionality(self):
        """
        Test that the search functionality works as expected
        """
        response = self.client.get(
            '/products/?', {'q': 'alpaca'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['search_term'], 'alpaca')

    def test_search_error_messages_output(self):
        """
        Test that the search error message display correctly
        """
        response = self.client.get(
            '/products/?', {'q': ''})
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "You didn't enter any search criteria!")
        self.assertEqual(response.status_code, 302)

    def test_product_detail_page_url_exists(self):
        """
        test product detail page loads via url
        """
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)

    def test_the_product_detail_url_is_accessible_by_name(self):
        """
        test product detail page loads via name
        """
        response = self.client.get(reverse('product_detail', args="1"))
        self.assertEqual(response.status_code, 200)

    def test_product_detail_page_template(self):
        """
        test product detail page loads via template
        """
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
