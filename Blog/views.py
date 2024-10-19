from django.shortcuts import render
from blogs.models import Blog
from misc.models import About
def home(request):
    # categories = Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    about = About.objects.all()
    print(about)
    return render(request,'home.html',{'featured_post':featured_post,'posts':posts,'about':about})