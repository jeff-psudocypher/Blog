from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    # category crud
    path('categories/', views.categories, name='categories'),
    path('categories/add', views.add_category, name='add_category'),
    path('categories/edit/<int:pk>', views.edit_category, name='edit_category'),
    path('categories/delete/<int:pk>', views.delete_category, name='delete_category'),
    # blog post crud
    path('posts/', views.posts, name='posts'),
    path('posts/add', views.add_posts, name='add_posts'),
    path('posts/edit/<int:pk>', views.edit_posts, name='edit_posts'),
    path('posts/delete/<int:pk>', views.delete_posts, name='delete_posts'),

    path('users/', views.users, name='users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),

]