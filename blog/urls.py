from django.urls import path
from . import views
# add this line inside the "urlpatterns" list


urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_comment/<slug:slug>/', views.add_comment, name='add_comment')
]
