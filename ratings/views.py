from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Ratings, Reviews
# from .forms import CommentForm, PostForm


def get_ratings(request):
    ratings = Ratings.objects.all()
    reviews = Reviews.objects.all()

    template = 'ratings/ratings.html'

    context = {
        'ratings': ratings,
        'reviews': reviews,
    }
    
    return render(request, template, context)
