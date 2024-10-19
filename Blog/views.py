from django.shortcuts import render
from blogs.models import Blog
def home(request):
    # categories = Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    print(posts)
    return render(request,'home.html',{'featured_post':featured_post,'posts':posts})