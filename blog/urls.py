# blog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('all_post/', views.all_posts, name='all_posts'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('categories/', views.category_list, name='category_list'),  # Add this line
    path('category/<int:pk>/', views.category_detail, name='category_detail'),  # Add this line
    
]
