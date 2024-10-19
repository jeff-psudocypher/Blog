from django.shortcuts import render,redirect
from .models import Blog,Category
# Create your views here.
from django.http import HttpResponse

def post_by_category(request,i):
    posts = Blog.objects.filter (status='Published' , category=i)
    try:
        category = Category.objects.get(id=i)
    except:
        return redirect('home')
    return render(request,'post_by_category.html',{'posts':posts,'category':category})