from django.contrib import admin
from . import views
from django.urls import path
urlpatterns=[
path('<int:i>/',views.post_by_category,name='post_by_category')
]