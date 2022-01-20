from django.contrib import admin

from .models import Reviews, Ratings
# Register your models here.

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'review', 'review_author', 'product')


class RatingsAdmin(admin.ModelAdmin):
    list_display = ('rating', 'rating_author', 'product')