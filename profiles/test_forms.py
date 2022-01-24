from django.test import TestCase
from .forms import UserProfileForm


class TestProfileForm(TestCase):
    """ tests for the profiles form """
    def test_profile_fields_not_required(self):
        """
        Test that none of the form fields are required
        """
        user_info = {
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_town_or_city': '',
            'default_postcode': '',
            'default_county': '',
            'default_country': ''
        }
        form = UserProfileForm(data=user_info)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)
