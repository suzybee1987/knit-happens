from django.test import TestCase
from .forms import ReviewForm, ProductForm


class TestReviewForm(TestCase):
    """ tests for the review form """

    def test_review_title_is_required(self):
        """
        test to see if review title field is required
        """
        form = ReviewForm({'review_title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review_title',
                      form.errors.keys())
        self.assertEqual(
            form.errors['review_title'][0], 'This field is required.')

    def test_review_field_is_required(self):
        """
        test to see if review field is required
        """
        form = ReviewForm({'review': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('review',
                      form.errors.keys())
        self.assertEqual(
            form.errors['review'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_meta_class(self):
        """
        check the field only displays certain fields
        """
        form = ReviewForm()
        self.assertEqual(form.Meta.fields, ['review_title', 'review'])


class TestProductForm(TestCase):
    """ Tests for product form """

    def test_fields_are_explicit_in_product_form_meta_class(self):
        """
        test to see if review title field is required
        """
        form = ProductForm({'review_title': ''})
        self.assertEqual(form.Meta.fields, [
            'category', 'sku', 'name', 'colour', 'description', 'has_sizes',
            'has_weights', 'price', 'image_url', 'image'])
