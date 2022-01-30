from django.test import TestCase
from .models import Category, Product


class TestCategoryModel(TestCase):
    """
    test the category model
    """

    def test_category_string_method_returns_name(self):
        """
        test category model string method
        """
        category = Category.objects.create(name="category_name")
        self.assertEqual(str(category), "category_name")


class TestProductModel(TestCase):
    """
    test product model
    """
    def test_product_string_method_returns_name(self):
        """
        test product model string method
        """
        product = Product.objects.create(name="product_name", price=21.99)
        self.assertEqual(str(product), "product_name")
