from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add_post/', views.add_post, name='add_post'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete/<slug:slug>/', views.delete_post, name='delete_post'),
]
