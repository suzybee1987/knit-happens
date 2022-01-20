from django import forms
from .models import Product, Category, Review, Rating

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'has-text-black'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'
