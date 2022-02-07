from django.test import TestCase

from .templatetags.bag_tools import calc_subtotal


class TestTemplateTagsFnWorks(TestCase):
    """
    Test the template tag calc_subtotal function
    """

    def test_calc_subtotal_works(self):
        """
        Test that the calc_subtotal function calculates the subtotal correctly
        """
        self.assertEqual(calc_subtotal(12, 4), 48)
        self.assertEqual(calc_subtotal(10, 3), 30)
        self.assertNotEqual(calc_subtotal(4, 7), 27)
