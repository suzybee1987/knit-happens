"""
Homepage views using Django
"""
from django.shortcuts import render


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def privacy(request):
    """ A view to return the privacy page """

    return render(request, 'home/privacy.html')


def terms(request):
    """ A view to return the terms and conditions page """

    return render(request, 'home/terms.html')
