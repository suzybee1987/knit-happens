from django.contrib import admin
from .models import Product, Category, Review, Rating


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'colour',
        'image'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

# Reviews and ratings


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_title', 'review', 'review_author', 'product')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('score', 'rating_author', 'product')


admin.site.register(Rating, RatingAdmin)
admin.site.register(Review, ReviewAdmin)
