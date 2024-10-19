from .models import Category
from django.shortcuts import render

def get_categories(request):
    categories = Category.objects.all()
    return ({'categories':categories})
