from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):
    """
    tests for the order form
    """

    def test_full_name_is_required(self):
        """
        test to see if full name field is required
        """
        form = OrderForm({
            'full_name': '',
            'email': 'email@email.com',
            'phone_number': '07894561231',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'gb',
            })

        self.assertFalse(form.is_valid())
        self.assertIn('full_name',
                      form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_is_required(self):
        """
        test to see if email field is required
        """
        form = OrderForm({
            'full_name': 'test',
            'email': '',
            'phone_number': '07894561231',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'gb',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email',
                      form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_field_is_required(self):
        """
        test to see if phone number field is required
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'email@email.com',
            'phone_number': '',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': 'gb',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number',
                      form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_country_field_is_required(self):
        """
        test to see if country field is required
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'email@email.com',
            'phone_number': '07894561231',
            'street_address1': 'test',
            'town_or_city': 'test',
            'country': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country',
                      form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')

    def test_town_or_city_field_is_required(self):
        """
        test to see if town_or_city field is required
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'email@email.com',
            'phone_number': '07894561231',
            'street_address1': 'test',
            'town_or_city': '',
            'country': 'gb',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city',
                      form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_street_address1_field_is_required(self):
        """
        test to see if street_address1 field is required
        """
        form = OrderForm({
            'full_name': 'test',
            'email': 'email@email.com',
            'phone_number': '07894561231',
            'street_address1': '',
            'town_or_city': 'test',
            'country': 'gb',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1',
                      form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_fields_are_explicit_in_bag_form_meta_class(self):
        """
        check the field only displays certain fields
        """
        form = OrderForm()
        self.assertEqual(
            form.Meta.fields, ('full_name', 'email',
                               'phone_number', 'street_address1',
                               'street_address2', 'town_or_city', 'postcode',
                               'country', 'county'))
