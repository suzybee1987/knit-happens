from django.db import models
from profiles.models import UserProfile

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                                  null=True, blank=True, related_name='post')
    updated_on = models.DateTimeField(auto_now=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    #                                  null=True, blank=True, related_name='comment')
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
