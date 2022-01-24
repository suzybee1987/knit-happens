from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):
    """ tests for the blog post form """

    def test_title_is_required(self):
        """ test to see if blog post title field is required"""
        form = PostForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title',
                      form.errors.keys())
        self.assertEqual(
            form.errors['title'][0], 'This field is required.')

    def test_content_is_required(self):
        """ test to see if blog post content field is required"""
        form = PostForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('content',
                      form.errors.keys())
        self.assertEqual(
            form.errors['content'][0], 'This field is required.')

    def test_image_field_is_required(self):
        """ test to see if blog post image field is required"""
        form = PostForm({'image': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('image',
                      form.errors.keys())
        self.assertEqual(
            form.errors['image'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_meta_class(self):
        """ 
        check the field only displays certain fields
        """
        form = PostForm()
        self.assertEqual(form.Meta.fields, ['title', 'image', 'content'])


class TestCommentForm(TestCase):
    """ Tests for blog comment form """

    def test_comment_field_is_explicit_in_comment_form_meta_class(self):
        """ test to see if review title field is required"""
        form = CommentForm({'comment': ''})
        self.assertEqual(form.Meta.fields,  ['comment'])
