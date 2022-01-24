"""
Testing blog page views using Django
"""

from django.test import TestCase
from django.shortcuts import reverse


class TestBlogViews(TestCase):
    """
    Test the blog page loads correctly
    """

    def test_blog_page_url_works(self):
        """ 
        Test the url works when loading the page
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_blog_view_uses_correct_template(self):
        """
        Test the correct template loads on page load
        """
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='blog/blog.html')

    def test_blog_page_is_accessible_by_name(self):
        """
        test the blog page is accessible by name
        """
        response = self.client.get(reverse('blog'))
        self.assertEqual(response.status_code, 200)
