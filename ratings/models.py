from django.db import models

from products.models import Product
from django.contrib.auth.models import User

# Create your models here.

class Ratings(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.PROTECT, related_name="ratings")
    rating_author = models.ForeignKey(
        User, on_delete=models.PROTECT, null=False, blank=False)
    rating = models.FloatField(null=True, default=5, )

class Reviews(models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.PROTECT, related_name="reviews")
    review_author = models.ForeignKey(User, on_delete=models.PROTECT, null=False, blank=False)
    review = models.TextField()
    review_title = models.CharField(max_length=254)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.title

