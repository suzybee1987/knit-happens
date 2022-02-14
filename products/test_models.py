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

    def test_category_friendly_name_str_method(self):
        """
        testing category models friendly name string
        method returns friendly name
        """
        test_case = Category()
        test_case.friendly_name = "Friendly"
        self.assertEqual(test_case.get_friendly_name(), "Friendly")


class TestProductModel(TestCase):
    """
    test product model
    """
    fixtures = [
        'categories.json',
        'products.json',
    ]

    def test_product_string_method_returns_name(self):
        """
        test product model string method
        """
        product = Product.objects.create(name="product_name", price=21.99)
        self.assertEqual(str(product), "product_name")

    def test_product_name_returns_name(self):
        """
        Test that the product name is returned
        """
        product = Product.objects.get(pk=1)
        self.assertEqual(product.name, "'Lambie' Bah Sleep, 200g")
        self.assertNotEqual(product.name, 'Not Bah Sheep')
        self.assertEqual(str(product), product.name)

    def test_product_description_returns_description(self):
        """
        Test that the product description is returned
        """
        product = Product.objects.get(pk=1)
        self.assertEqual(
            product.description, "Variegated yarn made of lambswool in variety of colours, hand wash only"
        )
        self.assertNotEqual(product.description, 'Not made of wool')

    def test_product_has_sizes(self):
        """
        Test whether a product has sizes or not
        """
        product_with_size = Product.objects.get(pk=39)
        product_with_weight = Product.objects.get(pk=5)
        product_no_sizes = Product.objects.get(pk=11)
        self.assertEqual(product_with_size.has_sizes, True)
        self.assertNotEqual(product_with_size.has_sizes, False)
        self.assertEqual(product_no_sizes.has_sizes, False)
        self.assertNotEqual(product_no_sizes.has_sizes, True)
        self.assertNotEqual(product_with_weight.has_sizes, True)

    def test_product_has_weights(self):
        """
        Test whether a product has weights or not
        """
        product_with_weight = Product.objects.get(pk=5)
        product_with_sizes = Product.objects.get(pk=39)
        product_no_sizes_or_weights = Product.objects.get(pk=48)
        self.assertEqual(product_with_weight.has_weights, True)
        self.assertNotEqual(product_with_sizes.has_weights, True)
        self.assertEqual(product_no_sizes_or_weights.has_weights, False)
        self.assertNotEqual(product_no_sizes_or_weights.has_weights, True)
