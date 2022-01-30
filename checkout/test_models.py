from django.test import TestCase
from .models import Order
from products.models import Product


class TestOrderModel(TestCase):
    """
    test the order model
    """
    def test_order_string_method_returns_order_number(self):
        """
        test order model string method
        """
        order = Order.objects.create(order_number="123456789")
        self.assertEqual(str(order), "123456789")


class TestOrderLineModel(TestCase):
    """
    test order line model string method
    """
    def test_order_line_string_method_returns_order_number_and_sku(self):
        product = Product.objects.create(sku="bah-woo-mer-2", price=21.99)
        order = Order.objects.create(order_number="123456789")
        correct = "SKU bah-woo-mer-2 on order 123456789"
        self.assertEqual(str(
            f'SKU {product.sku} on order {order.order_number}'), correct)
