import django.db.models
from django.shortcuts import render,redirect
from .models import Blog,Category,Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect

def post_by_category(request,i):
    posts = Blog.objects.filter (status='Published' , category=i)
    try:
        category = Category.objects.get(id=i)
    except:
        return redirect('home')
    return render(request,'post_by_category.html',{'posts':posts,'category':category})

def blogs(request,slug):
    single_blog = get_object_or_404(Blog, slug=slug , status='Published')
    if(request.method=='POST'):
        comment=Comment()
        comment.user = request.user
        comment.blog=single_blog
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)



    comments = Comment.objects.filter(blog=single_blog)
    comment_count=comments.count()

        # print(single_blog)
    return render(request,'blogs.html',{'single_blog':single_blog,'comments':comments,'comment_count':comment_count})

def search(request):
    keyword = request.GET.get('keyword')
    print(keyword)
    blogs=Blog.objects.filter(Q(blog_title__icontains=keyword)|Q(short_desc__icontains=keyword)|Q(blog_body__icontains=keyword))
    # print(blogs)
    return render(request,'search.html',{'blogs':blogs,'keyword':keyword})


