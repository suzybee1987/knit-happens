from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    colour = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(null=True, blank=True, default=False)
    has_weights = models.BooleanField(null=True, blank=True, default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=False)


    def __str__(self):
        return self.name

# Reviews and Ratings models 

class Rating(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.PROTECT, related_name="rating")
    rating_author = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    rating = models.FloatField(null=True, default=5)


class Review(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.PROTECT, related_name="reviews")
    review_author = models.ForeignKey(
        User, on_delete=models.PROTECT, null=True, blank=True)
    review = models.TextField(max_length=1000)
    review_title = models.TextField(max_length=254)
    added_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.review_title