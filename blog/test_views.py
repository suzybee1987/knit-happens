from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User

from .models import Post


class TestBlogViews(TestCase):
    """
    Test the blog page loads correctly
    """
    @classmethod
    def setUpTestData(self):
        """
        Set up data to run the tests
        """
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuserprofile", password="abc123def"
        )
        self.client.login(username="testuserprofile", password="abc123def")

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

    def test_blog_posts_display(self):
        """
        test blog posts display as expected
        """
        posts = Post.objects.all()
        for post in posts:
            response = self.client.get(reverse('posts'))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, post.id)

    def test_post_string_method_returns_title(self):
        """
        A test to see if the post string method returns the title as expected
        """
        post = Post.objects.create(title="Test Post")
        self.assertEqual(str(post), "Test Post")
