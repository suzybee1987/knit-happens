from django.test import TestCase

from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.conf import settings

from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from products.models import Product, Category


class TestBagViews(TestCase):
    """
    Test the checkout page loads correctly
    """

    fixtures = [
        'categories.json',
        'products.json',
    ]

    def setUp(self):
        self.user = User.objects.create_user(
            username='testingtesting',
            email='testing@testing.com',
            password='ABC123def'
        )

        self.admin = User.objects.create_superuser(
            username='testingsuperuser',
            email='testingsuperuser@testingsuperuser.com',
            password='Test123ing'
        )

        self.category = Category.objects.create(
            name='testingcategory',
            friendly_name='Test Category'
        )

        self.item = Product.objects.create(
            category=self.category,
            name='testingproduct',
            description='testing product description',
            price=0.01,
            sku='123456',
        )

        self.quantity = 1

        self.empty_bag = {}

        self.items_in_bag = {'25': 1, '3': 1}

    def test_cache_checkout_data_view(self):
        """
        Test that the cache_checkout_data view works as expected
        """
        response = self.client.get('/checkout/cache_checkout_data/')
        self.assertEqual(response.status_code, 405)

    def test_checkout_page_url_works(self):
        """
        Test the url works when loading the page
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')

    def test_checkout_page_is_accessible_by_name(self):
        """
        test the products page is accessible by name
        """
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 302)

    def test_get_checkout_view_with_items(self):
        """
        Test get checkout view when items in the bag
        """
        session = self.client.session
        session['bag'] = self.items_in_bag
        session.save()
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)

    def test_empty_bag_error(self):
        """
        Test error msg appears when bag empty
        """
        response = self.client.get('/checkout/')
        message = list(get_messages(response.wsgi_request))
        self.assertEqual(len(message), 1)
        self.assertEqual(message[0].tags, 'error')
        self.assertEqual(
            str(message[0]), "There's nothing in your bag at the moment")

    def test_stripe_key_missing_error(self):
        """
        Test error msg appears when no stripe key
        """
        bag = {'25': 1, '3': 1}
        session = self.client.session
        session['bag'] = bag
        session.save()
        settings.STRIPE_PUBLIC_KEY = ''
        response = self.client.get('/checkout/')
        message = list(get_messages(response.wsgi_request))
        self.assertEqual(len(message), 1)
        self.assertEqual(message[0].tags, 'warning')
        self.assertEqual(
            str(message[0]), 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    def test_autofill_details_if_user_authenticated(self):
        """
        Check if user is authenticated
        then autofill the form with details
        """
        session = self.client.session
        session['bag'] = self.items_in_bag
        session.save()
        self.client.force_login(self.user)
        response = self.client.get('/checkout/')
        user_profile = get_object_or_404(UserProfile, user=self.user)
        user_profile_form = UserProfileForm({
            'default_phone_number': '07777777777',
            'default_street_address11': 'test_street1',
            'default_street_address2': 'test_street2',
            'default_town_or_city': 'test_town',
            'default_county': 'test_county',
            'default_postcode': 'test_postcode',
            'default_country': 'GB'
        },
            instance=user_profile
        )

        self.assertTrue(user_profile_form.is_valid())
        user_profile_form.save()
        order_form = response.context['order_form']
        self.assertGreater(len(order_form.initial), 1)
