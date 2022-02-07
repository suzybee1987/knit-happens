from django.test import TestCase

from django.urls import reverse, resolve
from django.shortcuts import get_object_or_404
from decimal import Decimal
from products.models import Product, Category
from .views import view_bag, add_to_bag, adjust_bag, remove_from_bag


class TestBagViews(TestCase):
    """
    Test the bag views work correctly
    """
    fixtures = [
        'categories.json',
        'products.json',
    ]

    def setUp(self):
        self.category = Category.objects.create(
            name='testingcategory',
            friendly_name='Testing Category'
        )

        self.item = Product.objects.create(
            category = self.category,
            name='testing product',
            description='testing product description',
            price=0.01,
            sku='132456',
        )

        self.quantity = 1

        self.empty_bag = {}

        self.items_in_bag = {'25': 1, '3': 1}

        self.bag_bag = {'404': 1}

    def test_bag_page_url_works(self):
        """
        Test the url works when loading the page
        """
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='bag/bag.html')

    def test_bag_page_is_accessible_by_name(self):
        """
        test the products page is accessible by name
        """
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_view_bag(self):
        """
        Test that the view_bag view works correctly
        """
        link = reverse('view_bag')
        self.assertEqual(resolve(link).func, view_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="bag/bag.html")

    def test_add_to_bag(self):
        """
        Test that the add to bag view works as expected
        """
        link = reverse('add_to_bag', args=['item_id'])
        self.assertEqual(resolve(link).func, add_to_bag)
        response = self.client.get(reverse('view_bag'))
        self.assertEqual(response.status_code, 200)

    def test_add_to_bag_adds_item_to_bag(self):
        """
        Test that the add_to_bag function adds the item to the bag
        """
        product = Product.objects.get(pk=5)
        url = reverse('adjust_bag', args=['itemId'])
        self.assertEqual(resolve(url).func, adjust_bag)
        quantity = 1
        bag = [product.pk]
        self.assertEqual(len(bag), quantity)

    def test_add_to_bag_view(self):
        """
        Test that the add_to_bag view adds the product to the bag
        """
        post_data = {
            'product': Product.objects.get(pk=self.item.id),
            'quantity': self.quantity,
            'bag': self.empty_bag,
            'redirect_url': f'/products/{self.item.id}/'
        }
        response = self.client.post(f'/bag/add/{self.item.id}/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(len(updated_bag), 1)

    def test_add_to_bag_view_updates_item_if_already_present(self):
        """
        Test that the add_to_bag view increases the quantity of
        an item if the item is already present in the shopping bag
        """
        session = self.client.session
        session['bag'] = self.items_in_bag
        session.save()
        post_data = {
            'product': Product.objects.get(pk=25),
            'quantity': 2,
            'redirect_url': '/products/25/'
        }
        response = self.client.post('/bag/add/25/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(updated_bag['25'], 3)


    def test_adjust_bag(self):
        """
        Test that the adjust bag view works as expected to 
        calculate total
        """
        link = reverse('adjust_bag', args=['item_id'])
        self.assertEqual(resolve(link).func, adjust_bag)
        product = Product.objects.get(id=15)
        qty = 5
        bag_total = product.price * qty
        self.assertEqual(bag_total, Decimal('64.95'))
        qty = 2
        bag_total += product.price * qty
        self.assertEqual(bag_total, Decimal('90.93'))

    def test_adjust_bag_view_adds_existing_product(self):
        """
        Test that the add_to_bag view updates the quantity of
        an item if the item is already in the bag
        """
        session = self.client.session
        session['bag'] = self.items_in_bag
        session.save()
        post_data = {
            'bag_item': get_object_or_404(Product, pk=10),
            'quantity': int(self.quantity + 1),
        }
        response = self.client.post('/bag/adjust/10/', post_data)
        self.assertEqual(response.status_code, 302)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(updated_bag['10'], 2)

    def test_remove_from_bag(self):
        """
        Test remove from bag view removes the product from the bag
        """
        link = reverse('remove_from_bag', args=['item_id'])
        self.assertEqual(resolve(link).func, remove_from_bag)

    def test_remove_from_bag_view(self):
        """
        Test that the remove_from_bag view removes an item
        from the bag
        """
        session = self.client.session
        session['bag'] = self.items_in_bag
        session.save()
        response = self.client.post('/bag/remove/25/')
        self.assertEqual(response.status_code, 200)
        updated_bag = self.client.session.get('bag')
        self.assertEqual(len(updated_bag), 1)

    def test_remove_from_bag_error(self):
        """
        Test that the remove from bag view returns an error
        if something goes wrong
        """
        response = self.client.post('/bag/remove/66/')
        self.assertEqual(response.status_code, 500)
