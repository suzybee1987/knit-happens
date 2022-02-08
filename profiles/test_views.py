"""
Testing profile page views using Django
"""

from django.test import TestCase, Client

from django.shortcuts import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import User

from checkout.models import Order


class TestProfileViews(TestCase):
    """
    Test the profile page loads correctly
    """
    def setUp(self):
        self.client = Client()
        User.objects.create_user(
            username="profiletester", email="test@profile.com",
            password="123abcde4"
            )

    def test_profile_page_url_works(self):
        """
        Test the url works when loading the page
        """
        self.client.login(username="profiletester",
                          email="test@profile.com", password="123abcde4")
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_profile_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        self.client.login(username="profiletester",
                          email="test@profile.com", password="123abcde4")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='profiles/profile.html')

    def test_profile_page_is_accessible_by_name(self):
        """
        test the profile page is accessible by name
        """
        self.client.login(username="profiletester",
                          email="test@profile.com", password="123abcde4")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

    def test_profile_for_valid_form(self):
        """
        Test the profile form works if form is valid
        """
        user = User.objects.create_user(
            username="profileuser",
            email="test@profile.com", password="123abcde4"
        )
        self.client.login(
            username=user.username, email=user.email, password="123abcde4")
        user_info = {
            'default_phone_number': '01123456789',
            'default_street_address1': 'testaddress',
            'default_town_or_city': 'testtownorcity',
            'default_postcode': 'zz11zz',
            'default_county': 'testcounty',
            'default_country': 'GB'
        }
        self.client.post('/profile/', user_info)
        response = self.client.post('/profile/', user_info)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(
            str(messages[0]), 'Profile updated successfully')

    def test_order_displays_when_requested(self):
        """
        Test orders displayed on login to profile page
        """
        self.client.login(
            username="profiletester",
            email="test@profile.com", password="123abcde4")
        Order.objects.create(
            order_number='ABC123'
        )
        order_number = 'ABC123'
        response = self.client.get(
            f'/profile/order_history/{order_number}/')
        self.assertTemplateUsed(
            response, template_name="base.html")
