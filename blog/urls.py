from django.urls import path
from . import views
# add this line inside the "urlpatterns" list


urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('add/<slug:slug>/', views.add_comment, name='add_comment')
]
