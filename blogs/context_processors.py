from .models import Category
from django.shortcuts import render
from misc.models import About,Sociallink

def get_categories(request):
    categories = Category.objects.all()
    return ({'categories':categories})

def get_social_links(request):
    social_links=Sociallink.objects.all()
    return ({'social_links':social_links})
