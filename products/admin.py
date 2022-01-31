from django.contrib import admin
from .models import Product, Category, Review


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

admin.site.register(Review, ReviewAdmin)
